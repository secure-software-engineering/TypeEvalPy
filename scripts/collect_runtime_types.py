import io
import json
import pdb


class Debugger(pdb.Pdb):
    def __init__(self, *args, **kwargs):
        self.identifiers = {}
        super().__init__(stdin=io.StringIO(), stdout=io.StringIO(), *args, **kwargs)

    def user_line(self, frame):
        # Ignore internal Python identifiers
        valid_identifiers = {
            k: v for k, v in frame.f_locals.items() if not k.startswith("__")
        }

        # Collect local variable identifiers and their types
        for identifier, value in valid_identifiers.items():
            # Define the scope
            if frame.f_code.co_name == "<module>":
                scope = "global"
            else:
                scope = frame.f_code.co_name  # function name

            # Add line number, scope, and identifier to the identifiers
            self.identifiers[f"{frame.f_lineno}:{scope}:{identifier}"] = type(
                value
            ).__name__

        self.do_next(None)  # Continue execution


# Run the debugger
debugger = Debugger()
debugger.run(open("test.py").read())

# Print the collected identifiers and their types
print(json.dumps(debugger.identifiers, indent=4))
