import shutil
import os
import datetime

def backup_files(source , destination):
    today = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_files_name = os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_files_name.replace(".tar.gz", ""), 'gztar', source)

source = "C:\\Users\\visha\\OneDrive\\Desktop\\python-workshop-practice"
destination = "C:\\Users\\visha\\OneDrive\\Desktop\\python-workshop-practice\\backups"
backup_files(source, destination)