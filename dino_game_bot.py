import pyautogui , webbrowser, selenium
from splinter import Browser
def jump():
    pyautogui.typewrite(" ")
    return
def isObstacleClose():
    xPos = browser.evaluate_script('Runner.instance_.horizon.obstacles[0].xPos')
    if(xPos < 105):
        return True
    else:
        return False

browser = Browser('chrome')
browser.visit('chrome://dino')
jump()
foundX = False
while foundX != True:
    try:
        xpos = browser.evaluate_script('Runner.instance_.horizon.obstacles[0].xPos')
        foundX = True;
    except selenium.common.exceptions.WebDriverException:
        pass
print(xpos)
while True:
    if (isObstacleClose()):
        if(browser.evaluate_script('Runner.instance_.horizon.obstacles[0].yPos') != 50):
            jump()
    


