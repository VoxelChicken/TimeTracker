#!/usr/bin/python
import TimeTracker, os, atexit


def run(script: str):
    """
    Runs any script.
    """
    if not os.path.exists(script):
        error_msg = "The script file (path to script) does not exist. Please create a new script with the name '" + script + "' or maybe check if there's no typo in the code referring to the name of the script!"
        exit(error_msg)

    os.system(script)


tc = TimeTracker.TimeTracker(program_to_check="godot-bin", program_to_run="org.godotengine.Godot", target_file="seconds-data")

run("./run_program.sh")

atexit.register(tc.save_usage_time, end_program=True)