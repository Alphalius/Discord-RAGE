# Imports the needed libaries
import os
import pyautogui
import webbrowser
import time
from pystyle import Colors, Colorate, Center

# Changes the window title
os.system("title Discord RAGE")

# Prints the title
image = ("""          
          
          ▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄     ██▀███   ▄▄▄        ▄████ ▓█████ 
          ▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌   ▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▓█   ▀ 
          ░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▒███   
          ░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ 
          ░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓    ░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒
           ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒    ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░
           ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒      ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░  ░ ░  ░
           ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░      ░░   ░   ░   ▒   ░ ░   ░    ░   
             ░     ░        ░  ░ ░          ░ ░     ░        ░          ░           ░  ░      ░    ░  ░
           ░                   ░                           ░                                           
          
          """)

print(image)

# Asks the user for the inputs
int(input(Center.XCenter("Enter the message to spam: ")))
int(input(Center.XCenter("Enter the amount of times it needs to be send: ")))
int(input(Center.XCenter("Enter the delay amount in MS: ")))

# Asks the user if Discord is loaded
isLoaded = input("Press enter if Discord is loaded")

# Sleeps for 5 seconds
time.sleep(5)

# Spams in Discord
for i in range (0,repeats):
    if message != "":
         pyautogui.typewrite(message)
         pyautogui.press("enter")
    else:
         pyautogui.hotkey('ctrl', 'v')
         pyautogui.press("enter")
    time.sleep(delay/1000)

# Shows the user it's finished
print("Done\n")
