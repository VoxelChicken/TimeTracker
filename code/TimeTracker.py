import os


def modify_file(target_file, data):
    """
    Modifies the target file and changes its contents.
    """
    file = open(target_file, "w")
    file.write(data)


class TimeTracker:
    """
    This class is there to easily write a TimeTracker (or modify it, since it exists anyway).
    """

    def __init__(self, program_to_check: str, program_to_run: str):
        self.error_msg = ""
        self.program_to_check = program_to_check

        modify_file("program_to_check", program_to_check)
        modify_file("program_to_run", program_to_run)

    def save_usage_time(self, time_before_start: float, time_at_start, time_at_end: float, target_file):
        """
        This function stores the time at the start and end of the program and then calculates the amount of time spent in it.
        That then gets added to the current amount that is already stored in the file.
        """
        if not os.path.exists(target_file):
            cmd = "touch " + target_file
            os.system(cmd)

        time_used = time_at_end - time_at_start

        file = open(target_file, "w")
        file.write(str(time_used + time_before_start))
