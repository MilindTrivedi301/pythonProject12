class Browser:

    def __init__(self, browser):
        self.browser = browser

    def openBrowser(self, browser="chrome"):
        print("Write the code to open the Browser -> " + self.browser)
        print("Write the code to open the Browser -> " + browser)

#b = Browser()                  #it will take chrome
b = Browser("Firefox")
b.openBrowser()