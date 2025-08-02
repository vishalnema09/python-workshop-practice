import os
import datetime
def run_command (command):
    print(os.system(command))

# run_command("df -h")
# run_command("uptime")
# run_command("free -h")
# run_command("top -b -n 1 | head -n 10")


def show_date():
    return datetime.datetime.today()


today = show_date()
print(today)
