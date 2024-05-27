#python3 get_game_data.py data target
#the code should run and rename all files or something like tht
#the code below is a basis of how to manipulate files in the os using python
#the code should start by "python3 get_game_data.py data target", where data is passed as the argument, target
#the files should be on saved on a new file called targets....it renames

import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"
GAME_CODE_EXTENSION = ".go"
GAME_COMPILE_COMMAND =["go", "build"]


def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source):
        #the os.walk wil walk through the path ....helps to recursively  look through files 
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)

        break#so as to run the for loop once
    return game_paths

def get_name_from_paths(paths, to_strip):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)

    return new_names
        

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def copy_and_ovewrite(source, dest):
    #copys everything including other directories in the directory
    if os.path.exists(dest):
        shutil.rmtree(dest)#a recursive delete
    shutil.copytree(source, dest) # copys tthe directory

def make_json_meta_data_file(path, game_dirs):
    data = {
        "gameNames" : game_dirs,
        "numberOfGames": len(game_dirs)
    }

    with open(path, "w") as f:#context manager
        json.dump(data, f)# with to prevent memory leaks where an error occurs befoore we close the file

def compile_game_code(path):
    code_file_name = None
    
    for root, dirs,files in os.walk(path):#determines the name of the code file
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                code_file_name = file
                break
        break#to run the loop once ...only gets the first file with .go
    
    if code_file_name is None:
        return
    
    command = GAME_COMPILE_COMMAND + [code_file_name]
    run_command(command , path)

def run_command (command, path):
    cwd = os.getcwd()
    os.chdir(path)

    result = run(command, stdout=PIPE, stdin=PIPE, universal_newlines = True)
    #pipe makes a bridge between our python code and the process that we are using to run the command 
    #coommunication
    #the command is not a python built command
    print("compile result", result)

    os.chdir(cwd)


def main(source, target):
    cwd = os.getcwd()#current working directory
    source_path = os.path.join(cwd, source) #when creating the path based on the operating system you are working on
    #using a manual written file system "is/considereed/bad/practice" since it might fail"
    #he source directory fetched in the above is "~/Desktop/code/2024 code/lets python/projects/script$ "
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    new_game_dirs = get_name_from_paths(game_paths, "_game")# removes the "_game"....part on the names of the folders 
    
    create_dir(target_path)
    
    for src, dest in zip(game_paths, new_game_dirs):
        dest_path = os.path.join(target_path, dest)
        copy_and_ovewrite(src, dest_path)
        compile_game_code(dest_path)

    json_path = os.path.join(target_path, "metadata.json")
    make_json_meta_data_file(json_path, new_game_dirs)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("you must pass a source and target directory - only.")
    
    source, target = args[1:]
    main(source, target)