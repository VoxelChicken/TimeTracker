#!/usr/bin/python
import TimeTracker, time, atexit, os


def run(script: str):
    """
    Runs any script.
    """
    if not os.path.exists(script):
        error_msg = "The script file (path to script) does not exist. Please create a new script with the name '" + script + "' or maybe check if there's no typo in the code referring to the name of the script!"
        exit(error_msg)

    os.system(script)


tc = TimeTracker.TimeTracker(program_to_check="godot-bin", program_to_run="org.godotengine.Godot")

TIME_SPENT_PRIOR = float(open("seconds-data", "r").readline())
TIME_AT_START = time.time()

run("./run_program.sh")

TIME_AT_END = time.time()

atexit.register(tc.save_usage_time, time_before_start=TIME_SPENT_PRIOR, time_at_start=TIME_AT_START, time_at_end=TIME_AT_END, target_file="seconds-data")
