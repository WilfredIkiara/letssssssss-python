#the program below is a sheduled bak up to the file google iside 2024 code
#the program is scheduled to back up the file at 18:55 every day till the program is terminated
#do not run the program to savee cpu powre
#if ran use ctrl + c to end the program in the terminal


import os
import shutil
import datetime
import schedule
import time

source_dir = "/home/gh0st/Desktop/code/2024 code/google"
destination_dir ="/home/gh0st/Desktop/backups"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest,str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"folder copied to :{dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in : {dest_dir}")

schedule.every().day.at("18:55").do(lambda:copy_folder_to_directory(source_dir, destination_dir)) #lambda is used to call a function that you wanna pass other arguments to
#schedule helps the computer schedule tasks at a time of choosing for however long the programmers sets the schedule
#copy_folder_to_directory(source_dir, destination_dir)


while True:
    schedule.run_pending()
    time.sleep(60)

