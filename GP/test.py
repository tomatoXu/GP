#coding:utf-8
import wx

class test(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(800, 600))
        menubar = wx.MenuBar()  
        file = wx.Menu()  
        edit = wx.Menu()
        help = wx.Menu() 
        file.Append(101, '&打开', '打开图片')
        file.AppendSeparator() 
        quit = wx.MenuItem(file, 105, '&Quit\tCtrl+Q', 'Quit the Application')  
        file.AppendItem(quit)
        edit.Append(201, 'check item1', '', wx.ITEM_CHECK)  
        edit.Append(202, 'check item2', kind= wx.ITEM_CHECK)  
        submenu = wx.Menu()  
        submenu.Append(301, 'radio item1', kind=wx.ITEM_RADIO)  
        submenu.Append(302, 'radio item2', kind=wx.ITEM_RADIO)  
        submenu.Append(303, 'radio item3', kind= wx.ITEM_RADIO)  
        edit.AppendMenu(203, 'submenu', submenu) 
        menubar.Append(file, '&文件')  
        menubar.Append(edit, '&编辑')
        menubar.Append(help, '&help')
        self.SetMenuBar(menubar)
        self.Center() 
        
class MyApp(wx.App):
    def OnInit(self):
        frame = test(None, -1, '壁纸')
        frame.SetIcon(wx.Icon('logo.ico', wx.BITMAP_TYPE_ICO))
        frame.Center()
        frame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()