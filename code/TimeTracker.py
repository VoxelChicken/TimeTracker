import os, time, sys


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

    def __init__(self, program_to_check: str, program_to_run: str, target_file: str):
        self.error_msg = ""
        self.program_to_check = program_to_check

        modify_file("program_to_check", program_to_check)
        modify_file("program_to_run", program_to_run)

        self.target_file = target_file

        self.time_at_start = time.time()
        self.time_already_used_prior = float(open(self.target_file, "r").readline())

    def get_time_run_until_now(self):
        """
        This method gets the current time spent in the program. Since the program then does NOT close automatically, you can use it without worry.
        :return: float
        """
        current_time = time.time()
        time_run_until_now = current_time - self.time_at_start

        return current_time

    def save_usage_time(self, end_program: bool):
        """
        This function stores the time at the start and end of the program and then calculates the amount of time spent in it.
        That then gets added to the current amount that is already stored in the file.
        """
        if not os.path.exists(self.target_file):
            cmd = "touch " + self.target_file
            os.system(cmd)

        time_used_until_now = self.get_time_run_until_now() - self.time_at_start

        file = open(self.target_file, "w")
        file.write(str(time_used_until_now + self.time_already_used_prior))

        if end_program:
            sys.exit("Program stopped via the TimeTracker class method 'save_usage_time'.")
