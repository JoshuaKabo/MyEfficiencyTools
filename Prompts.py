possibleActions = "etc"
possibleYesNoSelection = "yn"
dividerSize = 80


# prompts include lowercasing for good measure
def runPrompt(possibleResponses, PromptPrint, *promptArgs):

    # convert to string if in list form
    if(not isinstance(possibleResponses, str)):
        possibleResponses = "".join(possibleResponses)

    possibleResponses = possibleResponses.lower()

    response = '~'

    while(response not in possibleResponses):
        response = PromptPrint(*promptArgs)
        response = response.lower()
    return response

def runPromptNoResponseLimit(PromptPrint, *promptArgs):
    response = '~'
    response = PromptPrint(*promptArgs)
    response = response.lower()
    return response

def promptActionList():
    printDiv('-')
    print("e to edit this script")
    print("t to open notes")
    print("c to exit")
    printDiv('-')
    return input("Select an action: ")

def printDiv(divChar = '-'):
    div = ""
    for i in range(0, dividerSize):
        div+=divChar
    print(div)

# y/n prompt is just a subset of the listed prompt
def runYesNoPrompt(PromptPrint, *promptArgs):
    response = runPrompt(possibleYesNoSelection, PromptPrint, *promptArgs).lower()
    return response == 'y'

def promptGenericList(list):
    printDiv('*')
    for item in list:
     print(item)
    printDiv('*')
    return input("Make a selection: ")

def promptDelete(toDelete):
    printDiv('*')
    return input(("Delete %s. Are you sure? y/n: " % toDelete))


# promptDrive returns the name and letter chosen
def promptDrive(usableDrives, drivePrompts):
    # get the desired deletion from user
    driveLetter = runPrompt(usableDrives, promptGenericList, drivePrompts)
    
    selectionName = ""
    
    # get the name from the selection for warning prompt:
    for i in range(len(drivePrompts)):
        if(drivePrompts[i][0].lower() == driveLetter.lower()):
            selectionName = drivePrompts[i]
            break
        
    return driveLetter, selectionName