import re
import os
from tkinter import Tk


class ResolutionManager:

    pattern1 = r'(?<=\t\".{8}defaultres\"\t\t\")[0-9]*'
    pattern2 = r'(?<=\t\".{8}defaultresheight\"\t\t\")[0-9]*'
    desiredWidth = '1280'
    desiredHeight = '1024'
    pathToConfig = r'D:\Steam\steamapps\common\Underlords\game\dac\cfg\video.txt'

    def changeResolution(self) -> None:
        with open(self.pathToConfig, 'r+') as config:
            file = config.read()
            file = re.sub(self.pattern1, self.desiredWidth, file)
            file = re.sub(self.pattern2, self.desiredHeight, file)
            config.seek(0)
            config.write(file)
            config.truncate()

    def changeParameters(self) -> None:
        root = Tk()
        self.desiredWidth = str(root.winfo_screenwidth())
        self.desiredHeight = str(root.winfo_screenheight())


if __name__ == '__main__':
    pathToGame = r'D:\Steam\steamapps\common\Underlords\game\bin\win64\underlords.exe'
    manager = ResolutionManager()
    manager.changeParameters()
    manager.changeResolution()
    os.startfile(pathToGame)