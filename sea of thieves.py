import random, time
from threading import Timer
import json
from cryptography.fernet import Fernet

achievementList = dict(cheater=False)
settingList = dict(autosaveStatus=False)
reputationData = dict(goldReputation = 0, soulsReputation = 0, merchantReputation = 0, callReputation = 0, reaperReputation = 0, servantReputation = 0, guardianReputation = 0)
key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)
with open('filekey.key', 'rb') as filekey:
   key = filekey.read()
fernet = Fernet(key)

print("Welcome to the Sea of Thieves!")
time.sleep(1)
print("This game is a piracy simulator where you collect treasure and gain reputation with the local trading companies. ")
print("This is the main menu! What do you wish to do, captain? ")
while True:
    menuOption = input("Your options are that of an options menu, start the game, and leave the game. Enter O for options, S to start the game, and E to leave the game. ")
    menuOption = menuOption.upper()
    if menuOption == "WWSSADADBA":
        print("That's the Konami Code, captain.")
        print("Achievement Unlocked! 'Cheater!'")
        achievementList["cheater"] = True
        menuOption = input("Well done on that achievement, captain, but you need to select something to do. Your options are the same as above. ")
        continue
    elif menuOption == "S":
        print("Understood, captain! There are two modes from here. You can play the Maiden Voyage, and learn the ropes, or you can start the game in Adventure Mode! ")
        modeSelection = input("Enter A for Adventure Mode, or enter M for the Maiden Voyage. ")
        saveChoice = input("Is this a new save or do you wish to load data? Enter N for new data, or L to load data. ")
        saveChoice = saveChoice.upper()
        if saveChoice == "L":
            successCheck=0
            with open("achievements.txt") as achievements:
                data = achievements.read()
                achievementList = json.loads(data)
                with open("settings.txt") as settings:
                    data = settings.read()
                    settingList = json.loads(data)
                    with open("save.txt") as save:
                        data = save.read()
                        reputationData = json.loads(data)
                        successCheck=1
            if successCheck == 1:
                print("Load Successful! ")
            elif successCheck == 0:
                print("Load Failed! ")
        modeSelection = modeSelection.upper()
        if modeSelection == "M":
            #go to maiden voyage
            pass
        if modeSelection == "A":
            #go to adventure mode
            pass
    elif menuOption == "O":
        print("Welcome to the options menu! ")
        print("Autosave - A")
        print("Exit - EXIT")
        optionChoice = input("Enter what option you wish to modify. ")
        optionChoice = optionChoice.upper()
        if optionChoice == "A":
            while True:
                print("Autosave Status =", settingList["autosaveStatus"])
                autosaveToggle = input("Do you wish to toggle this option? (Y/N)")
                autosaveToggle = autosaveToggle.upper()
                if autosaveToggle == "Y":
                    if settingList["autosaveStatus"] == False:
                        settingList["autosaveStatus"] = True
                        break
                    elif settingList["autosaveStatus"] == True:
                        settingList["autosaveStatus"] = False
                        break
                    else:
                        print("My apologies, but I cannot understand that. ")
                        continue
                elif autosaveToggle == "N":
                    print("Understood. Returning you to the options menu. ")
                    break
            continue
        elif optionChoice == "EXIT":
            print("Returning to main menu... ")
            continue
        else:
            print("I cannot understand that, captain. Returning you to the main menu. ")
            continue
    elif menuOption == "E":
        while True:
            exitOption = input("'Yer sure, captain? Any unsaved data will be lost! (Y/N)")
            exitOption = exitOption.upper()
            if exitOption == "Y":
                encryptSuccess = 0
                print("See ya soon, captain! ")
                with open("achievements.txt", "w") as achievements:
                    achievements.write(json.dumps(achievementList))
                with open("settings.txt", "w") as settings:
                    settings.write(json.dumps(settingList))
                with open("save.txt", "w") as save:
                    save.write(json.dumps(reputationData))
                with open("achievements.txt", "rb") as file:
                    original = file.read()
                    encrypted = fernet.encrypt(original)
                    with open("achievements.txt", "wb") as encryptedFile:
                        encryptedFile.write(encrypted)
                        encryptSuccess = 1
                        with open("settings.txt", "rb") as file:
                            original = file.read()
                            encrypted = fernet.encrypt(original)
                            with open("settings.txt", "wb") as encryptedFile:
                                encryptedFile.write(encrypted)
                                
                if encryptSuccess == 1:
                    print("File Encryption Successful")
                elif encryptSuccess != 1:
                    print("File Encryption Failed!")
                exit()
            elif exitOption == "N":
                print("Understood, captain! Returning you to the main menu! ")
                break
            else:
                print("I can't understand you, captain. Say that again, will you? ")
                continue
        continue
    else:
        print("Captain, that isn't an option! Can you please repeat that? ")
        continue
