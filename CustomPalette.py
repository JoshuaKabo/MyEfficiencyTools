from subprocess import Popen, PIPE, CalledProcessError
import sys, os, time, string, pyautogui, shutil, stat, win32api, pickle, Prompts

def handleActionList():
    actionToTake = Prompts.runPrompt(Prompts.possibleActions, Prompts.promptActionList)
    
    match actionToTake:
        case 'e': # edit this script
            os.system("code-insiders C:\\MyStuff\\MyEfficiencyTools")
        case 't': # open notes
            os.system("code-insiders C:\\Users\\joshk\\MyNotes")
        case 'c': # close
            sys.exit()
        case _: # default - close
            sys.exit()
    sys.exit()

# pickles userprefs for between session use
def saveUserPrefs():
    with open("userpref.pkl", "wb") as up_file:
        pickle.dump
    pass

# use pickled userprefs for 
def loadUserPrefs():
    pass
        
def main():
    pyautogui.PAUSE = 0.03
    handleActionList()
    
if __name__ == "__main__":
    main()
    
