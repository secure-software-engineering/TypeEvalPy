import io
import os
import tarfile
import tokenize
from io import BytesIO


def _strip_comments(source):
    """Replace comment text with bare '#', preserving line numbers and structure."""
    lines = source.splitlines(keepends=True)
    try:
        tokens = tokenize.generate_tokens(io.StringIO(source).readline)
        for tok_type, _, tok_start, _, _ in tokens:
            if tok_type == tokenize.COMMENT:
                row, col = tok_start
                line = lines[row - 1]
                # Keep everything before the '#', replace comment with bare '#',
                # then re-attach the original line ending so line count is unchanged.
                stripped = line.rstrip("\r\n")
                ending = line[len(stripped):]
                lines[row - 1] = line[:col] + "#" + ending
    except tokenize.TokenError:
        pass  # Return best-effort result on malformed source
    return "".join(lines)


class FileHandler:
    def copy_files_to_container(self, container, src, dst):
        # Build tar of micro-benchmark folder, excluding ground truth JSON files
        # (data leakage prevention) and stripping Python comments while keeping
        # line numbers intact (ground truth is line-number based).
        temp_path = "/tmp/temp.tar"
        with tarfile.open(temp_path, "w:gz") as tar:
            base_folder = "micro-benchmark"
            for dirpath, dirnames, filenames in os.walk(src):
                rel = os.path.relpath(dirpath, src)
                arcdir = base_folder if rel == "." else os.path.join(base_folder, rel)
                tar.add(dirpath, arcname=arcdir, recursive=False)

                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    arcname = os.path.join(arcdir, filename)

                    if filename.endswith(".json"):
                        continue  # Skip ground truth files

                    if filename.endswith(".py"):
                        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                            source = f.read()
                        data = _strip_comments(source).encode("utf-8")
                        info = tar.gettarinfo(filepath, arcname=arcname)
                        info.size = len(data)
                        tar.addfile(info, BytesIO(data))
                    else:
                        tar.add(filepath, arcname=arcname)

        with open(temp_path, "rb") as file:
            data = file.read()
            container.put_archive(dst, data)

    def copy_files_from_container(self, container, src, dst):
        command_to_run = ["chmod", "-R", "777", src]
        _, response = container.exec_run(" ".join(command_to_run), stream=True)
        stream, _ = container.get_archive(src)
        stream_bytes = b"".join(stream)
        stream_bytes_io = BytesIO(stream_bytes)

        tar = tarfile.open(fileobj=stream_bytes_io)
        tar.extractall(path=dst)
        tar.close()

    def list_python_files(self, directory):
        python_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    python_files.append(
                        os.path.relpath(os.path.join(root, file), directory)
                    )
        return python_files
