import os
import shutil
import errno
from rich.console import Console
from rich.progress import track
import random
import time
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
console = Console()
console.print("Welcome to Versort! \nVersatile, Fast and fun!", style="bold green")
def get_file_info(sortdir):
    files_info = []
    for root, dirs, files in os.walk(sortdir):
        for file in files:
            file_path = os.path.join(root, file)
            name = os.path.splitext(file)[0]
            ext = os.path.splitext(file)[1]
            size = os.path.getsize(file_path)
            if ext != "":

                  files_info.append({
                    "name": name,
                   "type": ext,
                    "size": size,
                    "path": file_path
                })
            else:
                files_info.append({
                    "name" : name,
                    "type" : "No Extension",
                    "size" : size,
                    "path" : file_path
                })
    return files_info
def move_file(targets, targetpath):
    success_msgs = []
    fail_msgs = []
    for target in track(targets, description="Moving files..."):
        filename = os.path.basename(target)
        try:
            shutil.move(target, os.path.join(targetpath, filename))
            success_msgs.append(f"File {filename} was moved successfully.")
        except OSError as e:
            if e.errno == errno.EACCES:
                fail_msgs.append(f"Permission denied. File {filename} could not be moved.")
    console.print("Processing logs...", style="bold blue")
    for msg in success_msgs:
        console.print(msg, style="green")
    for msg in fail_msgs:
        console.print(msg, style="red")
def copy_file(targets, targetpath):
    success_msgs = []
    fail_msgs = []
    for target in track(targets, description="Copying files..."):
        filename = os.path.basename(target)
        try:
            shutil.copy2(target, os.path.join(targetpath, filename))
            success_msgs.append(f"File {filename} was copied successfully.")
        except OSError as e:
            if e.errno == errno.EACCES:
                fail_msgs.append(f"Permission denied. File {filename} could not be copied.")
    console.print("Processing Logs...", style="bold blue")
    for msg in success_msgs:
        console.print(msg, style="green")
    for msg in fail_msgs:
        console.print(msg, style="red")
def delete_file(targets):
    success_msgs = []
    fail_msgs = []
    for target in track(targets, description="Deleting files..."):
        filename = os.path.basename(target)
        try:
            os.remove(target)
            success_msgs.append(f"File {filename} was deleted successfully.")
        except OSError as e:
            if e.errno == errno.EACCES:
                fail_msgs.append(f"Permission denied. File {filename} could not be deleted.")
    console.print("Processing Logs...", style="bold blue")
    for msg in success_msgs:
        console.print(msg, style="green")
    for msg in fail_msgs:
        console.print(msg, style="red")
while True:
    console.print("Please type a directory (or type 'exit' to quit)", style="bold blue")
    sortdir = input()
    if sortdir.lower() == "exit":
        console.print("Thank you for using Versort! ☺\n", style="bold green")
        console.print("  ⣠⣤⣶⣶⣦⣄⡀  ⠀⢀⣤⣴⣶⣶⣤  ", style="bold red")
        console.print(" ⣼⣿⣿⣿⣿⣿⣿⣷⣤⣾⣿⣿⣿⣿⣿⣿⣧  ", style="bold red")
        console.print(" ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  ", style="bold red")
        console.print(" ⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏  ", style="bold red")
        console.print("  ⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀   ", style="bold red")
        console.print(" ⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀    ", style="bold red")
        console.print(" ⠀⠀⠀⠀⠀⠉⢿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀      ", style="bold red")
        console.print(" ⠀⠀⠀⠀⠀⠀⠀⠙⠻⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ", style="bold red")
        break
    if not os.path.exists(sortdir):
        console.print("Directory does not exist. Try again.", style="green")
        continue
    sortfinder = get_file_info(sortdir)
    console.print("\nhere are the files in the directory: \n", style="bold blue underline")
    for info in sortfinder:
        console.print(f"{info['name']} : {info['type']}", style="bold cyan")
        console.print("----------------------------------------------------------", style="bold blue")
    print("\n")
    console.print("What do you want to do? ", style="bold green underline")
    console.print("\n 1- Manage all files \n 2- First letter sorting \n 3- File type sorting \n 4- File size sorting \n 5- Locate a file \n 6- Gather duplicates \n \n Type 'exit' to quit.\n ", style ="green")
    console.print(" Type 'G' for a surprise...", style="italic purple")
    choice = input(": ")
    if choice.lower() == "exit":
        console.print("Thank you for using Versort! ☺\n", style="bold green")
        console.print(" ⠀⣠⣤⣶⣶⣦⣄⡀  ⠀⢀⣤⣴⣶⣶⣤   ", style="bold red")
        console.print(" ⣼⣿⣿⣿⣿⣿⣿⣷⣤⣾⣿⣿⣿⣿⣿⣿⣧  ", style="bold red")
        console.print(" ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  ", style="bold red")
        console.print(" ⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏  ", style="bold red")
        console.print("  ⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀   ", style="bold red")
        console.print(" ⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀    ", style="bold red")
        console.print(" ⠀⠀⠀⠀⠀⠉⢿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀      ", style="bold red")
        console.print(" ⠀⠀⠀⠀⠀⠀⠀⠙⠻⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ", style="bold red")
        break
    if choice == "1":
        targets = []
        print("\n")
        for info in sortfinder:
            console.print(f"{info['name']} : {info['type']}", style="bold yellow")
            targets.append(info['path'])
        console.print("\n1- Move files \n2- Copy files \n3- Delete files", style="bold green")
        console.print("\nType 'n' to go back", style="italic red")
        input1 = input(": ").lower()
        if input1 == "n":
            continue
        elif input1 == "1":
            console.print("Please select the target directory to move the file(s) to", style="bold green")
            console.print("Note: One of the duplicate file pair get deleted once moved or copied to the same directory.",style="red italic")
            targetpath = input(": ")
            if not os.path.exists(targetpath):
                console.print("Target Directory does not exist. Try again.", style="green")
                continue
            move_file(targets, targetpath)
        elif input1 == "2":
            console.print("Please select the target directory to copy the file(s) to", style="bold green")
            console.print("Note: One of the duplicate file pair get deleted once moved or copied to the same directory.",style="red italic")
            targetpath = input(": ")
            if not os.path.exists(targetpath):
                console.print("Target Directory does not exit. Try again.", style="green")
                continue
            copy_file(targets, targetpath)
        elif input1 == "3":
            delete_file(targets)
    elif choice == "2":
        console.print("Enter the first letter to sort by.", style="bold green")
        console.print("\nType 'n' to go back.", style="italic red")
        first_letter = input(": ")
        if first_letter.lower() == "n":
            continue
        targets = []
        for info in sortfinder:
            if info['name'].startswith(first_letter.upper()) or info['name'].startswith(first_letter.lower()):
                console.print(f"{info['name']} : {info['type']}", style="bold yellow")
                targets.append(info['path'])
        file_count = len(targets)
        if file_count == 0:
            console.print("No files were found with that first letter.", style="bold red")
            continue
        random1 = 0
        while random1 < 1:
            console.print("1- Move files \n2- Copy files \n3- Delete files\n", style="bold green")
            xx = input(": ")
            if xx == "1":
                console.print("Please select the target directory to move the files to.", style="bold green")
                console.print("Note: One of the duplicate file pair get deleted once moved or copied to the same directory.",style="red italic")
                targetpath = input(": ")
                if not os.path.exists(targetpath):
                    console.print("Target Directory does not exist. Try again.", style="green")
                    continue
                move_file(targets, targetpath)
                random1 += 1
            elif xx == "2":
                console.print("Please select the target directory to copy the files to.", style="bold green")
                console.print("Note: One of the duplicate file pair get deleted once moved or copied to the same directory.",style="red italic")
                targetpath = input(": ")
                if not os.path.exists(targetpath):
                    console.print("Target Directory does not exist. Try again", style="green")
                    continue
                copy_file(targets, targetpath)
                random1 += 1
            elif xx == "3":
                delete_file(targets)
                random1 += 1
            else:
                console.print("Invalid choice please try again.", style="italic blue")
    elif choice == "3":
        console.print("Enter the file type to sort by (.txt, .jpg, etc.) \n", style="bold green")
        console.print("\nType 'n' to go back", style="italic red")
        file_type = input()
        if file_type.lower() == "n":
            continue
        targets = []
        for info in sortfinder:
            if info['type'] == file_type.lower():
                console.print(f"{info['name']} : {info['type']}", style="bold yellow")
                targets.append(info['path'])
        file_count = len(targets)
        if file_count == 0:
            console.print("No files were found with that file type.", style="bold red")
            continue
        random2 = 0
        while random2 < 1:
            console.print("1- Move files \n2- Copy files \n3- Delete files", style="bold green")
            xx = input(": ")
            if xx == "1":
                console.print("Please select the target direcory to move the files to.", style="bold green")
                console.print("Note: One of the duplicate file pair get deleted once moved or copied to the same directory.",style="red italic")
                targetpath = input(": ")
                if not os.path.exists(targetpath):
                    console.print("Target Directory does not exist. Try again.", style="green")
                    continue
                move_file(targets, targetpath)
                random2 += 1
            elif xx == "2":
                console.print("Please select the target directory to copy the files to.", style="bold green")
                console.print("Note: One of the duplicate file pair get deleted once moved or copied to the same directory.",style="red italic")
                targetpath = input(": ")
                if not os.path.exists(targetpath):
                    console.print("Target Directory does not exist. Try again.", style="green")
                    continue
                copy_file(targets, targetpath)
                random2 += 1
            elif xx == "3":
                delete_file(targets)
                random2 += 1
            else:
                console.print("Invalid choice please try again.", style="italic blue")
    elif choice == "4":
        print("\n")
        console.print("1. Greater than limit. \n2. Less than limit\n", style="green")
        console.print("\nType 'n' to go back.", style="italic red")
        xxx = input(": ")
        if xxx.lower() == 'n':
            continue
        console.print("Enter the file size limit in Megabytes: ", style="green")
        size_limit0 = float(input())
        size_limit = size_limit0 * 1000000
        targets = []
        if xxx == "1":
            for info in sortfinder:
                if float(info['size']) >= size_limit:
                    console.print(f"{info['name']} : {info['type']}", style="bold yellow")
                    targets.append(info['path'])
        elif xxx == "2":
            for info in sortfinder:
                if int(info['size']) <= size_limit:
                    console.print(f"{info['name']} : {info['type']}", style="bold yellow")
                    targets.append(info['path'])
        else:
            console.print("Invalid choice please try again.", style="italic blue")
            continue
        file_count = len(targets)
        if file_count == 0:
            console.print("No files were found with that size limit.", style="bold red")
            continue
        random = 0
        while random < 1:
            console.print("1- Move files \n2- Copy files \n3- Delete files", style="bold green")
            xx = input(": ")
            if xx == "1":
                console.print("Please select the target directory to move the files to.", style="bold green")
                console.print("Note: One of the duplicate file pair get deleted once moved or copied to the same directory.",style="red italic")
                targetpath = input(": ")
                if not os.path.exists(targetpath):
                    console.print("Target Directory does not exist. Try again.", style="green")
                    continue
                move_file(targets, targetpath)
                random += 1
            elif xx == "2":
                console.print("Please select the target directory to copy the files to.", style="bold green")
                console.print("Note: One of the duplicate file pair get deleted once moved or copied to the same directory.",style="red italic")
                targetpath = input(": ")
                if not os.path.exists(targetpath):
                    console.print("Target Directory does not exist. Try again", style="green")
                    continue
                copy_file(targets, targetpath)
                random += 1
            elif xx == "3":
                delete_file(targets)
                random += 1
            else:
                console.print("Invalid choice please try again.", style="italic blue")
    elif choice == "5":
        console.print("Enter the name of the file to locate as shown in the list.", style="bold yellow")
        console.print("\nType 'n' to go back", style="italic red")
        file_name = input(": ")
        if file_name.lower() == "n":
            continue
        found = False
        storedfound = []
        for info in sortfinder:
            w = info['name']
            if str(w).lower() == file_name.lower():
                console.print("File(s) found at: ", info['path'], style ="bold green")
                storedfound.append(info['path'])
                found = True
        if found:
            console.print("Would you like to move, copy or delete the file(s)? (1, 2, 3)", style="bold yellow")
            console.print("Type 'n' to go back.", style="italic red")
            choice1 = input().lower()
            if choice1 == "1":
                console.print("Please select the target directory to move the file(s) to.", style="bold green")
                console.print("Note: One of the duplicate file pair get deleted once moved or copied to the same directory.",style="red italic")
                targetpath = input(": ")
                if not os.path.exists(targetpath):
                    console.print("Target Directory does not exist. Try again.", style="green")
                    continue
                move_file(storedfound, targetpath)
            elif choice1 == "2":
                console.print("Please select the target directory to copy the file(s) to")
                console.print("Note: One of the duplicate file pair get deleted once moved or copied to the same directory.",style="red italic")
                targetpath = input(": ")
                if not os.path.exists(targetpath):
                    console.print("Target Directory does not exist. Try again.", style="green")
                    continue
                copy_file(storedfound, targetpath)
            elif choice1 == "3":
                delete_file(storedfound)
            elif choice1 == "n":
                continue
        if not found:
             console.print("File not found.", style="bold red")
    elif choice == "6":
         seen = set()
         duplicates = {}
         for info in sortfinder:
             key = (info['name'], info['type'])
             if key in seen:
                 if key not in duplicates:
                     duplicates[key] = []
                     file_name = key[0]
                     for info in sortfinder:
                         w = info['name']
                         if (info['name'].lower(), info['type']) == (file_name.lower(), key[1]):
                             duplicates[key].append(info['path'])
             else:
                 seen.add(key)
         if duplicates:
                 for key, paths in duplicates.items():
                      console.print(f"Duplicate file: {key[0]} ({key[1]})", style="bold red")
                      targets = []
                      random3 = 0
                      for path in paths:
                             console.print("  ", path, style="red italic")
                             targets.append(path)
                      while random3 < 1:
                             console.print("Would you like to move, copy or delete these files? (1,2,3)", style="bold yellow")
                             console.print("Type 'n' to go back.", style="italic red")
                             answer = input().lower()
                             if answer == "n":
                                random3 +=1
                                continue
                             elif answer == "1":
                                 console.print("Please select the target directory to move or copy files to.", style="bold green")
                                 console.print("Note: One of the duplicate file pair get deleted once moved or copied to the same directory.",style="red italic")
                                 console.print("Type 'n' to skip.", style="italic red")
                                 targetpath = input(": ")
                                 if targetpath.lower() == "n":
                                     continue
                                 if not os.path.exists(targetpath):
                                     console.print("Target Directory does not exist. Try again.", style="green")
                                     continue
                                 move_file(targets, targetpath)
                                 random3 += 1
                             elif answer == "2":
                                 console.print("Please select the target directory to move or copy files to.", style="bold green")
                                 console.print("Note: One of the duplicate file pair get deleted once moved or copied to the same directory.",style="red italic")
                                 console.print("Type 'n' to skip.", style="italic red")
                                 targetpath = input(": ")
                                 if targetpath.lower() == "n":
                                     continue
                                 if not os.path.exists(targetpath):
                                      console.print("Target Directory does not exist. Try again", style="green")
                                      continue
                                 copy_file(targets, targetpath)
                                 random3 += 1
                             elif answer == "3":
                                 console.print("Warning! This will delete all duplicates and their originals permanently!", style="bold red")
                                 console.print("Do you wish to proceed? (y/n)", style="bold green")
                                 choice2 = input(": ").lower()
                                 if choice2 == "y":
                                     delete_file(targets)
                                     random3 += 1
                             elif answer == "n":
                                 continue
                             else:
                                  console.print("No duplicate files were found.", style="bold yellow")
                                  random += 1
    elif choice.lower() == "g":
        console.print("\n옻 SORT IT! 옻\n", style="bold purple underline")
        console.print("Would you like to play in the current directory?", style="green bold")
        console.print("Y/N", style="yellow bold")
        console.print("Type 'x' to go back", style="red italic")
        choice3 = input(": ")
        if choice3.lower() == "n":
            console.print("Please type a directory (or type 'exit' to quit)")
            choice4 = input(": ").lower()
            if choice4 == "exit":
                continue
            if not os.path.exists(choice4):
                console.print("Directory does not exist. Try again", style="green")
                continue
            sortdir = choice4
        if choice3.lower() == "x":
            continue
        hidelocation0 = os.walk(sortdir)
        hidelocations = []
        for root, dirs, files in hidelocation0:
            for d in dirs:
                full_path = os.path.join(root, d)
                hidelocations.append(full_path)
            break
        virus_names = [f"virus{i}.txt" for i in range(1,6)]
        current_location = os.path.dirname(os.path.abspath(__file__))
        targets = []
        for virus in virus_names:
            virus_path = os.path.join(current_location, virus)
            with open(virus, 'w') as f:
                f.write("I am an evil virus! >:3")
            targets.append(virus_path)
        if not hidelocations:
            console.print("No directories found to hide viruses in!", style="bold yellow")
            continue
        random.shuffle(hidelocations)
        hidelocations = hidelocations[:5]
        hint = []
        if len(targets) > len(hidelocations):
                console.print("There must be at least 5 sub directories in your selection! ", style="bold yellow")
                break
        for i in range(min(5, len(hidelocations))):
            target = targets[i]
            dest_folder = hidelocations[i]
            dest_path = os.path.join(dest_folder, os.path.basename(target))
            hint0 = os.path.basename(dest_folder)
            hint.append(hint0)
            try:
                shutil.move(target, dest_path)
            except OSError as e:
                if e.errno == errno.EACCES:
                    console.print(f"Couldn't move {target} due to a lack of permissions in the directory.", style="red")
            retrieved_dir = os.path.join(current_location, "Retrieved")
            os.makedirs(retrieved_dir, exist_ok=True)
        console.print("Virus files hidden in your directory! Can you find them?", style="bold violet")
        time.sleep(0.65)
        console.print("Once you find a virus, copy it to the 'Retrieved' folder in the program directory!", style="bold blue")
        time.sleep(0.5)
        console.print("you could open Versort in another tab and use the file finder....", style="italic blue")
        time.sleep(0.4)
        console.print("Type 'help' for a hint :P or 'n' to continue")
        choice5 = input(": ").lower()
        if choice5 == "help":
            console.print(f"This might help...{hint}", style="purple italic")
        console.print("Type 'done' to verify the files when you're done or 'exit' to go back", style="bold green")
        choice6 = input(": ").lower()
        if choice6 == "exit":
            continue
        found_viruses = []
        todelete = []
        for virus in virus_names:
            virus_path = os.path.join(retrieved_dir, virus)
            if os.path.exists(virus_path):
                found_viruses.append(virus)
                todelete.append(virus_path)
        if len(found_viruses) == 5:
            console.print("\nYou have eliminated all the viruses! YOU'VE WON WOHOOOOOO! (^▿^) \n", style="purple bold")
            console.print("don't mine me I'll just clean up...", style="italic blue")
            time.sleep(0.75)
            delete_file(todelete)
            continue
        elif found_viruses:
            console.print(f"\nYou found {len(found_viruses)}/5 viruses, That's good enough! ;D\n", style="bold blue")
            time.sleep(0.75)
            console.print("don't mind me I'll just clean up...", style="italic blue")
            time.sleep(0.65)
            delete_file(todelete)
            continue
        else:
            console.print("\nNo viruses found... Better luck next time.. (⌣̩̩́_⌣̩̩̀)\n", style="bold red")

            continue
