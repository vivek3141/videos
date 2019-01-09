import inspect
import streamer_ai


file = str(input("Enter File Name:"))

with open(f"{file}.sh", "w") as f:
    f.write("")

with open(f"{file}.sh", "a+") as f:
    f.write("#!/usr/bin/env bash\n")
    for name, obj in inspect.getmodule(streamer_ai, inspect.isclass):
        f.write(f"python3 extract_scene.py mean_squared_error.py {name}\n")


