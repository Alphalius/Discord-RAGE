# Imports the needed libaries
import pyautogui
import webbrowser
import time

# Asks the user for the inputs
message = input("Enter the message to spam: ")
repeats = int(input("Enter the amount of times it needs to be send: "))
delay = int(input("Enter the delay in ms: "))

# Asks the user if Discord is loaded
isLoaded = input("Press enter if Discord is loaded")

# Shows the user it will start in 5 seconds
print("Five seconds until the rage starts")

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