import os
from delphifmx import *

class MainForm(Form):

    def __init__(self, owner):
        self.ImageRaw = None
        self.TextRaw = None
        self.ShadowEffect1 = None
        self.ImageArranged = None
        self.TextArranged = None
        self.ShadowEffect2 = None
        self.StyleBook1 = None
        self.Timer1 = None
        self.MainMenu1 = None
        self.MenuItem1 = None
        self.MenuOpen = None
        self.Menu_Seperator = None
        self.MenuExit = None
        self.MenuItem2 = None
        self.MenuIMovie = None
        self.MenuUsbWeb = None
        self.MenuItem3 = None
        self.MenuOpticalFlow = None
        self.MenuORB = None
        self.Splitter1 = None
        self.OpenDialog1 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.pyfmx"))

    def FormClose(self, Sender, Action):
        pass

    def Timer1Timer(self, Sender):
        pass

    def MenuOpenClick(self, Sender):
        pass

    def MenuExitClick(self, Sender):
        pass

    def Menu_SelectorClick(self, Sender):
        pass