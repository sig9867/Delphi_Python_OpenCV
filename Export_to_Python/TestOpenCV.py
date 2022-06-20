from delphifmx import *
from main import MainForm

def main():
    Application.Initialize()
    Application.Title = 'OpenCV'
    Application.MainForm = MainForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
