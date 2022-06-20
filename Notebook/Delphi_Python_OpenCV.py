#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
from delphifmx import *


# In[2]:


import time
class TWidth:
    def __init__(self, rate=0.2, f='{:03.1f} [ms]'):
        self.rate = rate
        self.tw = 0.0
        self.f = f
        
    def start(self):
        self.t0 = time.time()
    
    def get(self):
        self.tw = self.tw * (1.0 - self.rate) + (time.time() - self.t0) * self.rate
        return self.f.format(self.tw * 1000)


# In[3]:


import cv2
class CVBase(cv2.VideoCapture):
    def __init__(self, device=None, original='origin.png', arranged='arranged.png'):
        super().__init__(device)
        self.original = original
        self.arranged = arranged

    def step(self):
        pass

    def close(self):
        self.release()
    
    def save(self, org_img, arg_img):
        cv2.imwrite(self.original, org_img)
        cv2.imwrite(self.arranged, arg_img)


# In[4]:


import numpy as np

class OpiticalFlow(CVBase):

    def __init__(self, device):
        super().__init__(device)
        #
        ret, frame = self.read()
        self.prvs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.hsv = np.zeros_like(frame)
        self.hsv[...,1] = 255
    
    def step(self):
        ret, frame = self.read()
        if not ret:
            return
        next = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(self.prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
        self.hsv[...,0] = ang * 180 / np.pi / 2
        self.hsv[...,2] = cv2.normalize(mag, None , 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(self.hsv, cv2.COLOR_HSV2BGR)
        self.save(frame, bgr)
        self.prvs = next


# ORBは、主にSIFTとSURFが特許取得済みのアルゴリズムであるために考案されました。ただし、ORBは無料で使用できます。
# 
# https://ichi.pro/orb-no-gaiyo-oriented-fast-and-rotated-brief-72709114183887

# In[5]:


class ORB(CVBase):

    def __init__(self, device):
        super().__init__(device)

    def step(self):
        ret, img = self.read()
        if not ret: return
        orb = cv2.ORB_create()
        kps = orb.detect(img)
        result = cv2.drawKeypoints(img, kps, None, -1, cv2.DrawMatchesFlags_DEFAULT)
        self.save(img, result)


# In[6]:


class MainForm(Form):

    def __init__(self, owner):
        self.ImageRaw = None
        self.ImageArranged = None
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
        self.TextRaw = None
        self.ShadowEffect1 = None
        self.TextArranged = None
        self.ShadowEffect2 = None
        filepath = '../Export_to_Python/' + "main.pyfmx"
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath('__file__')), filepath))
        self.movie = 'vtest.avi'
        self.cv = None
        self.select_cv()
        # 
        self.Timer1.Interval = 50
        self.tw = TWidth(rate=1.0)

    def FormClose(self, Sender, Action):
        self.cv.close()
        os.remove(self.cv.original)
        os.remove(self.cv.arranged)
        
    def Timer1Timer(self, Sender):
        self.tw.start()
        self.cv.step()
        self.ImageRaw.Bitmap.LoadFromFile(self.cv.original)
        self.ImageArranged.Bitmap.LoadFromFile(self.cv.arranged)
        self.Caption = 'OpenCV を検討する: ' + self.tw.get()

    def MenuOpenClick(self, Sender):
        if self.OpenDialog1.Execute():
            self.MenuIMovie.IsChecked = True
            self.movie = self.OpenDialog1.FileName
            self.select_cv()
    
    def MenuExitClick(self, Sender):
        self.close()

    def Menu_SelectorClick(self, Sender):
        Sender.IsChecked = True
        self.select_cv()

    def select_cv(self):
        self.Timer1.Enabled = False
        if self.cv:
            self.cv.close()
            del self.cv
        dev = self.select_device()
        if self.MenuOpticalFlow.IsChecked:
            self.cv = OpiticalFlow(dev)
            #self.cv.step()
        else:
            self.cv = ORB(dev)
        self.TextArranged.Text = self.MenuOpticalFlow.Text if self.MenuOpticalFlow.IsChecked else self.MenuORB.Text
        self.Timer1.Enabled = True
    
    def select_device(self):
        self.TextRaw.Text = self.MenuUsbWeb.Text if self.MenuUsbWeb.IsChecked else self.movie
        return 0 if self.MenuUsbWeb.IsChecked else self.movie

# In[7]:


def main():
    Application.Initialize()
    Application.Title = 'OpenCV'
    Application.MainForm = MainForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()


# In[8]:


if __name__ == '__main__':
    main()


# In[ ]:




