import os, Prompts

language_options = ["Mono", "GDScipt"]
language_option_selections = ["m", "g"]


# Note:
# At first I thought I should update path each time, but now I've realized it makes way more sense to just rename the Godot exe to Godot.exe and make a text file to keep track of the version number.
# cli_entry is a flag to indicate if this is being called directly from the command line or from internally. This dictates console output and exit behavior.
def fixGodotName(cli_entry = False):

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

    versioninfo = ""

    # rename exes, careful not to double rename
    for file_entry in godotfiles:
        if file_entry == "Godot.exe" or file_entry == "Godot_console.exe"  or file_entry == "GodotVersion.txt"  or file_entry == "GodotSharp":
            # don't rename when naming is already correct
            continue
        if (file_entry.endswith("_console.exe") and (not "Godot_console.exe" in file_entry)):
            # rename the console, as it'll catch .exe too
            os.rename(file_entry, "Godot_console.exe")
        elif (file_entry.endswith(".exe") and (not "Godot.exe" in file_entry)):
            # save full name of the exe, eg Godot_v4.2.1-stable_mono_win64
            versioninfo = file_entry
            os.rename(file_entry, "Godot.exe")

    # if the rename wasn't a dupe, write out version info
    if len(versioninfo) > 0:
        with open("GodotVersion.txt", "w") as file:
            file.write(versioninfo)
            
    godotpath = r"" + os.getcwd() + "\\" + "Godot.exe"

    if cli_entry:
        print("Latest Godot path: " + godotpath)
        input("Press enter to exit...")

def runGodot():
    lang_choice = Prompts.runPromptNoResponseLimit(promptGenericList(language_options)
    match lang_choice:
        case 'm':
            os.environ["GODOT"] = "C:/Users/joshk/dev/Tools/Godot/Godot_Mono/Godot.exe"
        case 'g':
            os.environ["GODOT"] = "C:/Users/joshk/dev/Tools/Godot/Godot_GDScript/Godot.exe"
        case _:
            os.environ["GODOT"] = "C:/Users/joshk/dev/Tools/Godot/Godot_Mono/Godot.exe"
    fixGodotName(cli_entry=False)
    os.system(os.environ["GODOT"])
