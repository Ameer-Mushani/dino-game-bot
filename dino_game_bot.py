import pyautogui, selenium
from splinter import Browser
def jump():
    pyautogui.typewrite(" ")
def isObstacleClose():
    xPos = browser.evaluate_script('Runner.instance_.horizon.obstacles[0].xPos')
    if(xPos < 120):
        return True
    else:
        return False
undefinedX = True
groundY = 23
trexX = 93
trexWidth = 44
browser = Browser('chrome')
browser.visit('chrome://dino')
jump()
while True:
    if browser.evaluate_script('Runner.instance_.crashed'):
        while True:
            print ("dead")
    if undefinedX:
        try:
            xpos = browser.evaluate_script('Runner.instance_.horizon.obstacles[0].xPos')
            undefinedX = False;
        except selenium.common.exceptions.WebDriverException:
            pass
    else:
        if browser.evaluate_script('Runner.instance_.crashed'):
            undefinedX = True
            jump()
        else:
            if (isObstacleClose()):
                if(browser.evaluate_script('Runner.instance_.horizon.obstacles[0].yPos') > 50):
                    jump()
                    while browser.evaluate_script('Runner.instance_.tRex.jumping'):
                        print(browser.evaluate_script('Runner.instance_.horizon.obstacles[0].xPos') + browser.evaluate_script('Runner.instance_.horizon.obstacles[0].width'))
                        print(browser.evaluate_script('Runner.instance_.horizon.obstacles[0].xPos'))
                        
                        if(browser.evaluate_script('Runner.instance_.horizon.obstacles[0].xPos') + browser.evaluate_script('Runner.instance_.horizon.obstacles[0].width') < trexX - trexWidth):
                            pyautogui.keyDown('down')
                    pyautogui.keyUp('down')
##                    if(browser.evaluate_script('Runner.instance_.horizon.obstacles[0]
##                    print(browser.evaluate_script('Runner.instance_.horizon.obstacles[0].yPos'))
