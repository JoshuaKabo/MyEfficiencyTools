import os, sys, Helpers

def removeOldGodotPath():
    orig_path = os.environ["PATH"]
    updated_path = ""

    for path in os.environ["PATH"].split(os.pathsep):
        if "Godot" in path:
            updated_path = os.environ["PATH"].replace(path + os.pathsep, "")

    print(updated_path)

def updateGodotPath():

    # if not already, get admin privileges
    Helpers.acquire_admin_privileges()

    # go to c/users/ to inspect the folders there
    os.chdir("C:/Users/")
    userfolders = os.listdir()

    # select the folder for joshk / jk
    for folder in userfolders:
        if folder[0] == "j":
            os.chdir(folder)
            break

    os.chdir("dev/Tools/Godot/Godot_Mono")

    # collect the files at the Godot_Mono folder
    godotfiles = os.listdir()
    desiredfile = ""

    # grab the exe desired (assumes the name is not altered so it will end in "_win64.exe")
    for file_entry in godotfiles:
        if file_entry.endswith("_win64.exe"):
            desiredfile = file_entry
            break

    godotpath = r"" + os.getcwd() + "\\" + desiredfile

    print("Latest Godot path: " + godotpath)

    os.environ["PATH"] += os.pathsep + godotpath
    print("PATH has been updated!")
    input("Press enter to exit...")

    

    # os.environ["Godot"] = godotpath

    # print(godotpath)
    # print(os.pathsep)



def runGodot():
    os.system(os.environ["Godot"])

# app_path = os.path.join(root_path, 'other', 'dir', 'to', 'app')
# print(os.environ["PATH"])

# updateGodotPath()
    


# if is_admin():
#     print("The script is run with admin privileges.")
# else:
#     print("The script is not run with admin privileges.")
print(Helpers.is_admin())
Helpers.acquire_admin_privileges()
print(Helpers.is_admin())