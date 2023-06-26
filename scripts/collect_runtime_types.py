import io
import json
import pdb

_in = io.StringIO("step")
_out = io.StringIO()


class Debugger(pdb.Pdb):
    def __init__(self, *args, **kwargs):
        self.identifiers = {}
        self.all_identifiers = None
        super().__init__(*args, **kwargs)
        # super().__init__(stdin=_in, stdout=_out, *args, **kwargs)

    def user_line(self, frame):
        # Ignore internal Python identifiers
        valid_identifiers = {
            k: v
            for k, v in frame.f_locals.items()
            if (
                not k.startswith("__")
                and k
                not in [
                    "io",
                    "json",
                    "pdb",
                    "_in",
                    "_out",
                    "Debugger",
                    "debugger",
                    "cmd",
                    "globals",
                    "locals",
                ]
            )
        }
        # Collect local variable identifiers and their types
        for identifier, value in valid_identifiers.items():
            # Define the scope
            if frame.f_code.co_name == "<module>":
                scope = "global"
            else:
                scope = frame.f_code.co_name  # function name

            # Add line number, scope, and identifier to the identifiers

            if f"{frame.f_lineno-1}" not in self.identifiers:
                self.identifiers[frame.f_lineno - 1] = {}

            if identifier not in self.identifiers[frame.f_lineno - 1]:
                self.identifiers[frame.f_lineno - 1][identifier] = {
                    "identifier": identifier,
                    "context": scope,
                    "type": [type(value).__name__],
                }
            else:
                print("###############################")
                self.identifiers[frame.f_lineno - 1][identifier]["type"].append(
                    type(value).__name__
                )

        # self.do_step(None)  # Continue execution
        # self.onecmd("step")
        # _in.write("")


# Run the debugger
debugger = Debugger()
debugger.run(open("test.py").read())

# Print the collected identifiers and their types
print(json.dumps(debugger.identifiers, indent=4, sort_keys=1))
