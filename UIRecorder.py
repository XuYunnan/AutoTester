# -*-coding:utf-8 -*-  
import pythoncom  
import pyHook
import os
import threading
import time

class UIRecorder(object):
    """
    UI控制的记录与重放
    """
    def __init__(self, outputDir="", windowsName=""):
        super(UIRecorder, self).__init__()
        self.outputDir = outputDir             # 记录文件夹的位置
        self.windowsName = windowsName         # 游戏窗口的名字
        self.hm = pyHook.HookManager()         # hook manager

        if not outputDir:
            print "need outputDir..."
            return

        if not os.path.isdir(outputDir):
            os.mkdir(outputDir)
        
        self.outputFile = open(outputDir + "/out.txt", "w")


    def startRecord(self):
        self.hm.KeyDown = self.onKeyboardEvent
        self.hm.MouseAll = self.onMouseEvent
        self.hm.HookKeyboard()
        self.hm.HookMouse()
        threading.Thread(target = pythoncom.PumpMessages)
        # pythoncom.PumpMessages()
    
    def stopRecord(self):
        self.hm.UnhookKeyboard()
        self.hm.UnhookMouse()
    
    def onKeyboardEvent(self, event):
        print event.MessageName
    
    def onMouseEvent(self, event):
        f = self.outputFile
        print >> f, "MessageName:",event.MessageName  
        print >> f, "Message:", event.Message  
        print >> f, "Time:", event.Time  
        print >> f, "Window:", event.Window  
        print >> f, "WindowName:", event.WindowName  
        print >> f, "Position:", event.Position  
        print >> f, "Injected:", event.Injected  
        print >> f, "---"  

