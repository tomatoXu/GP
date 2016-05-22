#coding:utf-8
#!/usr/bin/python
from download import download
import wx
import os
import math
import Image
import ImageEnhance
import ImageFilter
import re
global word
word = ""
global cur
cur = 1
global dir
dir = "/home/allen/GP/save/"
global max_page
max_page = 0

class UI(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(740, 640))
#menubar
        menubar = wx.MenuBar()  
        file = wx.Menu()  
        edit = wx.Menu()  
        help = wx.Menu()  
        file.Append(101, '&open', 'open a picture')  
        help.Append(102, '&help', 'development information')  
        file.AppendSeparator()  
        quit = wx.MenuItem(file, 105, '&Quit\tCtrl+Q', 'Quit the Application')  
        quit.SetBitmap(wx.Image ('stock_exit.png',  wx.BITMAP_TYPE_PNG).ConvertToBitmap())  
        file.AppendItem(quit)  
        edit.Append(201, 'check item1', '', wx.ITEM_CHECK)  
        edit.Append(202, 'check item2', kind= wx.ITEM_CHECK)  
        submenu = wx.Menu()  
        submenu.Append(301, 'radio item1', kind=wx.ITEM_RADIO)  
        submenu.Append(302, 'radio item2', kind=wx.ITEM_RADIO)  
        submenu.Append(303, 'radio item3', kind= wx.ITEM_RADIO)  
        edit.AppendMenu(203, 'submenu', submenu)  
        menubar.Append(file, '&file')  
        menubar.Append(edit, '&edit')  
        menubar.Append(help, '&help')
        self.SetMenuBar(menubar)
        self.Center()          
        wx.EVT_MENU(self, 105, self.OnQuit)
	wx.EVT_MENU(self, 102, self.OnHelp)
#toolbar
        vbox = wx.BoxSizer(wx.VERTICAL)
        toolbox = wx.BoxSizer(wx.HORIZONTAL)

	mainbox = wx.BoxSizer(wx.HORIZONTAL)
        toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER)
        toolbar.AddSimpleTool(1, wx.Image('home.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'home', 'Home')
        toolbar.AddSimpleTool(2, wx.Image('mine.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'mine', 'Mine')
        toolbar.AddSeparator()
        toolbar.AddSimpleTool(3, wx.Image('exit.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'exit', 'Exit')
        toolbar.AddSeparator()
        toolbar.AddSimpleTool(4, wx.Image('search.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'search', 'Search')         
        toolbar.Realize()
        toolbox.Add( toolbar, 0, wx.EXPAND)
        
        searchbar = wx.Panel(self, -1)
        self.searchtext = wx.TextCtrl(searchbar, -1, 'search', pos = (20,5), size = (300, 40))
        self.searchtext.SetInsertionPoint(0)
        
        bn_button = wx.ToolBar(self, -1, style = wx.TB_HORIZONTAL | wx.NO_BORDER)
        bn_button.AddSimpleTool(5, wx.Image('back.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'back', 'Back') 
        bn_button.AddSimpleTool(6, wx.Image('next.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'next', 'Next')
        bn_button.Realize()
        toolbox.Add(searchbar, 0, wx.EXPAND)            
        toolbox.Add(bn_button, 0, wx.EXPAND)
        
        typebox = wx.BoxSizer(wx.VERTICAL)
        typebar = wx.ToolBar(self, -1, style = wx.TB_VERTICAL | wx.NO_BORDER)
        typebar.AddSimpleTool(11, wx.Image('11.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'view', 'view')
        typebar.AddSimpleTool(12, wx.Image('12.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'cartoon', 'cartoon')
        typebar.AddSimpleTool(13, wx.Image('13.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'pet', 'pet')
        typebar.AddSimpleTool(14, wx.Image('14.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'car', 'car')
        typebar.AddSimpleTool(15, wx.Image('15.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'game', 'game')
        typebar.AddSimpleTool(16, wx.Image('16.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'film', 'film')
        typebar.Realize()
        typebox.Add(typebar, 0, wx.EXPAND)

        picbox = wx.BoxSizer(wx.VERTICAL)
        picbox_1 = wx.BoxSizer(wx.HORIZONTAL)
        picbox_2 = wx.BoxSizer(wx.HORIZONTAL)
        picbox_3 = wx.BoxSizer(wx.HORIZONTAL)
        
	picbox_11 = wx.BoxSizer(wx.VERTICAL)
	picbox_12 = wx.BoxSizer(wx.VERTICAL)
	picbox_21 = wx.BoxSizer(wx.VERTICAL)
	picbox_22 = wx.BoxSizer(wx.VERTICAL)
	picbox_31 = wx.BoxSizer(wx.VERTICAL)
	picbox_32 = wx.BoxSizer(wx.VERTICAL)


        pic_1 = wx.ToolBar(self, -1, style = wx.TB_HORIZONTAL | wx.NO_BORDER)
        pic_2 = wx.ToolBar(self, -1, style = wx.TB_HORIZONTAL | wx.NO_BORDER)
        pic_3 = wx.ToolBar(self, -1, style = wx.TB_HORIZONTAL | wx.NO_BORDER)
        pic_4 = wx.ToolBar(self, -1, style = wx.TB_HORIZONTAL | wx.NO_BORDER)
	pic_5 = wx.ToolBar(self, -1, style = wx.TB_HORIZONTAL | wx.NO_BORDER)
	pic_6 = wx.ToolBar(self, -1, style = wx.TB_HORIZONTAL | wx.NO_BORDER)

	
	self.pic_panel_1 = wx.Panel(self, -1)
	im = wx.Image('/home/allen/GP/src/r11.png',wx.BITMAP_TYPE_ANY)
	temp = im.ConvertToBitmap()
	wx.StaticBitmap(parent = self.pic_panel_1, bitmap = temp, pos=(0,0), size = (330,140))
	picbox_11.Add(self.pic_panel_1, 0, wx.EXPAND)

	self.pic_panel_2 = wx.Panel(self, -1)
        im = wx.Image('/home/allen/GP/src/r12.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_2, bitmap = temp, pos=(0,0), size = (300,140))
        picbox_12.Add(self.pic_panel_2, 0, wx.EXPAND)
 
	self.pic_panel_3 = wx.Panel(self, -1)
        im = wx.Image('/home/allen/GP/src/r13.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_3, bitmap = temp, pos=(0,0), size = (330,140))
        picbox_21.Add(self.pic_panel_3, 0, wx.EXPAND)

	self.pic_panel_4 = wx.Panel(self, -1)
        im = wx.Image('/home/allen/GP/src/r14.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_4, bitmap = temp, pos=(0,0), size = (300,140))
        picbox_22.Add(self.pic_panel_4, 0, wx.EXPAND)

	self.pic_panel_5 = wx.Panel(self, -1)
        im = wx.Image('/home/allen/GP/src/r15.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_5, bitmap = temp, pos=(0,0), size = (330,140))
        picbox_31.Add(self.pic_panel_5, 0, wx.EXPAND)

	self.pic_panel_6 = wx.Panel(self, -1)
        im = wx.Image('/home/allen/GP/src/r16.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_6, bitmap = temp, pos=(0,0), size = (300,140))
        picbox_32.Add(self.pic_panel_6, 0, wx.EXPAND)

        pic_1.AddSimpleTool(211, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_1.AddSimpleTool(221, wx.Image('download.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_2.AddSimpleTool(212, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_2.AddSimpleTool(222, wx.Image('download.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
	pic_3.AddSimpleTool(213, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_3.AddSimpleTool(223, wx.Image('download.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
	pic_4.AddSimpleTool(214, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_4.AddSimpleTool(224, wx.Image('download.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
	pic_5.AddSimpleTool(215, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_5.AddSimpleTool(225, wx.Image('download.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
	pic_6.AddSimpleTool(216, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_6.AddSimpleTool(226, wx.Image('download.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')

        pic_1.Realize()
        pic_2.Realize()
        pic_3.Realize()
	pic_4.Realize()
	pic_5.Realize()
	pic_6.Realize()        

        picbox_11.Add(pic_1, 0, wx.EXPAND)
        picbox_12.Add(pic_2, 0, wx.EXPAND)
	picbox_21.Add(pic_3, 0, wx.EXPAND)
        picbox_22.Add(pic_4, 0, wx.EXPAND)
	picbox_31.Add(pic_5, 0, wx.EXPAND)
        picbox_32.Add(pic_6, 0, wx.EXPAND)

	picbox_1.Add(picbox_11, 0 , wx.EXPAND)
	picbox_1.Add(picbox_12, 0 , wx.EXPAND)
	picbox_2.Add(picbox_21, 0 , wx.EXPAND)
	picbox_2.Add(picbox_22, 0 , wx.EXPAND)
	picbox_3.Add(picbox_31, 0 , wx.EXPAND)
	picbox_3.Add(picbox_32, 0 , wx.EXPAND)

        picbox.Add(picbox_1, 1, wx.EXPAND)
        picbox.Add(picbox_2, 1, wx.EXPAND)
        picbox.Add(picbox_3, 1, wx.EXPAND)
        
        mainbox.Add(typebox, 0, wx.EXPAND)
        mainbox.Add(picbox, 0, wx.EXPAND)
        vbox.Add(toolbox, 0, wx.EXPAND)
        vbox.Add(mainbox, -1, wx.EXPAND)

	wx.EVT_TOOL(self, 101, self.OnOpen)
        wx.EVT_TOOL(self, 1, self.OnHome)
        wx.EVT_TOOL(self, 2, self.OnMine)
        wx.EVT_TOOL(self, 3, self.OnQuit)
        wx.EVT_TOOL(self, 4, self.OnSearch)
        wx.EVT_TOOL(self, 5, self.OnBack)
	wx.EVT_TOOL(self, 6, self.OnNext)

        wx.EVT_TOOL(self, 211, self.OnPic)
        wx.EVT_TOOL(self, 212, self.OnPic)
        wx.EVT_TOOL(self, 213, self.OnPic)
        wx.EVT_TOOL(self, 214, self.OnPic)
        wx.EVT_TOOL(self, 215, self.OnPic)
        wx.EVT_TOOL(self, 216, self.OnPic)
	wx.EVT_TOOL(self, 221, self.OnSet)
        wx.EVT_TOOL(self, 222, self.OnSet)
        wx.EVT_TOOL(self, 223, self.OnSet)
        wx.EVT_TOOL(self, 224, self.OnSet)
        wx.EVT_TOOL(self, 225, self.OnSet)
        wx.EVT_TOOL(self, 226, self.OnSet)

	wx.EVT_TOOL(self, 11, self.OnKey)
	wx.EVT_TOOL(self, 12, self.OnKey)
	wx.EVT_TOOL(self, 13, self.OnKey)
	wx.EVT_TOOL(self, 14, self.OnKey)
	wx.EVT_TOOL(self, 15, self.OnKey)
	wx.EVT_TOOL(self, 16, self.OnKey)
	

        self.SetSizer(vbox)
        self.statusbar = self.CreateStatusBar()       
        self.Centre()

#响应函数
    def OnHome(self, event):
        self.statusbar.SetStatusText('Home Command')
        global cur
        global max_page
        global word
        cur = 1
        word = unicode("高清", "utf-8")
        self.statusbar.SetStatusText('Please wait')
        dl = download()
        a = dl.urlencode(word)
        b = dl.get_linklist(a, 0)
        c = dl.getnum()
        max_page = int(math.ceil(dl.getnum() / 6.0))
        print dl.getnum(),max_page
        dl.downImageViaMutiThread(b, 0)
        im = wx.Image('/home/allen/GP/src/r11.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_1, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_1.Refresh()
        im = wx.Image('/home/allen/GP/src/r12.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_2, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_2.Refresh()
        im = wx.Image('/home/allen/GP/src/r13.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_3, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_3.Refresh()
        im = wx.Image('/home/allen/GP/src/r14.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_4, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_4.Refresh()
        im = wx.Image('/home/allen/GP/src/r15.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_5, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_5.Refresh()
        im = wx.Image('/home/allen/GP/src/r16.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_6, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_6.Refresh()
        path = '/home/allen/GP/src'
        filelist = os.listdir(path)
        for file in filelist:
                if (not re.match(r'r[1-3][1-6].[jpg,png]',file)):
                        os.remove(path +'/'+file)
        self.statusbar.SetStatusText('search done')

    def OnMine(self, event):
        self.statusbar.SetStatusText('Mine Command')

    def OnSearch(self, event):
	global cur
	global max_page
	global word
	cur = 1
	key = self.searchtext.GetValue()
	print key
	word = key
        self.statusbar.SetStatusText('Please wait')
 	dl = download()
        a = dl.urlencode(key)
        b = dl.get_linklist(a, 0)
	c = dl.getnum()
	if (c == 0):
		dlg = wx.MessageDialog(None, "无搜索结果", "无结果", wx.ID_OK)
        	if dlg.ShowModal() == wx.ID_OK:
        		dlg.Destroy()
		return
	max_page = int(math.ceil(dl.getnum() / 6.0))
        print dl.getnum(),max_page
        dl.downImageViaMutiThread(b, 0)
	im = wx.Image('/home/allen/GP/src/r11.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_1, bitmap = temp, pos=(0,0), size = (300,140))
	self.pic_panel_1.Refresh()
	im = wx.Image('/home/allen/GP/src/r12.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_2, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_2.Refresh()
	im = wx.Image('/home/allen/GP/src/r13.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_3, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_3.Refresh()
	im = wx.Image('/home/allen/GP/src/r14.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_4, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_4.Refresh()
	im = wx.Image('/home/allen/GP/src/r15.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_5, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_5.Refresh()
	im = wx.Image('/home/allen/GP/src/r16.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_6, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_6.Refresh()
	path = '/home/allen/GP/src'
	filelist = os.listdir(path)
	for file in filelist:
        	if (not re.match(r'r[1-3][1-6].[jpg,png]',file)):
                	os.remove(path +'/'+file)
	self.statusbar.SetStatusText('search done')

    def OnOpen(self, event):
        self.statusbar.SetStatusText('Open Command')
	dlg = wx.FileDialog(self, "Open a picture", os.getcwd(), style = wx.OPEN, wildcard = "*.*")
	if dlg.ShowModal() == wx.ID_OK:
		im = Image.open(dlg.GetPath())
		im.save("/home/allen/GP/src/r10.jpg")
	        pic_frame = pic_show(None, -1, 'pic', 210)
        	pic_frame.Center()
        	pic_frame.Show(True)
	
	dlg.Destroy()

    def OnQuit(self, event):
        self.Close()

    def OnHelp(self, event):
	dlg = wx.MessageDialog(None, u"开发者：徐寅",u"开发者",wx.OK)
	if dlg.ShowModal() == wx.ID_OK:
		dlg.Destroy()
	dlg.Destroy()

    def OnBack(self,event):
	global cur
	if (cur == 1):
		self.statusbar.SetStatusText('It\'s already the first page')
	else:
		cur = cur - 1
		im = wx.Image('/home/allen/GP/src/r'+str(cur)+'1.png',wx.BITMAP_TYPE_ANY)
        	temp = im.ConvertToBitmap()
        	wx.StaticBitmap(parent = self.pic_panel_1, bitmap = temp, pos=(0,0), size = (300,140))
        	self.pic_panel_1.Refresh()
        	im = wx.Image('/home/allen/GP/src/r'+str(cur)+'2.png',wx.BITMAP_TYPE_ANY)
        	temp = im.ConvertToBitmap()
        	wx.StaticBitmap(parent = self.pic_panel_2, bitmap = temp, pos=(0,0), size = (300,140))
        	self.pic_panel_2.Refresh()
        	im = wx.Image('/home/allen/GP/src/r'+str(cur)+'3.png',wx.BITMAP_TYPE_ANY)
        	temp = im.ConvertToBitmap()
        	wx.StaticBitmap(parent = self.pic_panel_3, bitmap = temp, pos=(0,0), size = (300,140))
        	self.pic_panel_3.Refresh()
        	im = wx.Image('/home/allen/GP/src/r'+str(cur)+'4.png',wx.BITMAP_TYPE_ANY)
        	temp = im.ConvertToBitmap()
        	wx.StaticBitmap(parent = self.pic_panel_4, bitmap = temp, pos=(0,0), size = (300,140))
        	self.pic_panel_4.Refresh()
        	im = wx.Image('/home/allen/GP/src/r'+str(cur)+'5.png',wx.BITMAP_TYPE_ANY)
        	temp = im.ConvertToBitmap()
        	wx.StaticBitmap(parent = self.pic_panel_5, bitmap = temp, pos=(0,0), size = (300,140))
        	self.pic_panel_5.Refresh()
        	im = wx.Image('/home/allen/GP/src/r'+str(cur)+'6.png',wx.BITMAP_TYPE_ANY)
        	temp = im.ConvertToBitmap()
        	wx.StaticBitmap(parent = self.pic_panel_6, bitmap = temp, pos=(0,0), size = (300,140))
        	self.pic_panel_6.Refresh()
        	self.statusbar.SetStatusText('page ' + str(cur))

    def OnNext(self, event):
	global cur
	global max_page
	global word
	filename = r'/home/allen/GP/src/r'+str(cur+1)+'1.png'
        if (cur == max_page):
                self.statusbar.SetStatusText('It\'s already the last page')
		return
	elif (not os.path.exists(filename)):
		print 'aaaa'
		dl = download()
		a = dl.urlencode(word)
        	b = dl.get_linklist(a, cur/3)
        	c = dl.getnum()
        	dl.downImageViaMutiThread(b, cur/3)
        cur = cur + 1
	if (os.path.exists(r'/home/allen/GP/src/r'+str(cur)+'1.png')):
        	im = wx.Image('/home/allen/GP/src/r'+str(cur)+'1.png',wx.BITMAP_TYPE_ANY)
        	temp = im.ConvertToBitmap()
        	wx.StaticBitmap(parent = self.pic_panel_1, bitmap = temp, pos=(0,0), size = (300,140))
        	self.pic_panel_1.Refresh()
	if (os.path.exists(r'/home/allen/GP/src/r'+str(cur)+'2.png')):
        	im = wx.Image('/home/allen/GP/src/r'+str(cur)+'2.png',wx.BITMAP_TYPE_ANY)
        	temp = im.ConvertToBitmap()
        	wx.StaticBitmap(parent = self.pic_panel_2, bitmap = temp, pos=(0,0), size = (300,140))
        	self.pic_panel_2.Refresh()
        if (os.path.exists(r'/home/allen/GP/src/r'+str(cur)+'3.png')):
		im = wx.Image('/home/allen/GP/src/r'+str(cur)+'3.png',wx.BITMAP_TYPE_ANY)
        	temp = im.ConvertToBitmap()
        	wx.StaticBitmap(parent = self.pic_panel_3, bitmap = temp, pos=(0,0), size = (300,140))
        	self.pic_panel_3.Refresh()
        if (os.path.exists(r'/home/allen/GP/src/r'+str(cur)+'4.png')):
		im = wx.Image('/home/allen/GP/src/r'+str(cur)+'4.png',wx.BITMAP_TYPE_ANY)
        	temp = im.ConvertToBitmap()
        	wx.StaticBitmap(parent = self.pic_panel_4, bitmap = temp, pos=(0,0), size = (300,140))
        	self.pic_panel_4.Refresh()
        if (os.path.exists(r'/home/allen/GP/src/r'+str(cur)+'5.png')):
		im = wx.Image('/home/allen/GP/src/r'+str(cur)+'5.png',wx.BITMAP_TYPE_ANY)
        	temp = im.ConvertToBitmap()
        	wx.StaticBitmap(parent = self.pic_panel_5, bitmap = temp, pos=(0,0), size = (300,140))
        	self.pic_panel_5.Refresh()
	if (os.path.exists(r'/home/allen/GP/src/r'+str(cur)+'6.png')):
        	im = wx.Image('/home/allen/GP/src/r'+str(cur)+'6.png',wx.BITMAP_TYPE_ANY)
        	temp = im.ConvertToBitmap()
        	wx.StaticBitmap(parent = self.pic_panel_6, bitmap = temp, pos=(0,0), size = (300,140))
        	self.pic_panel_6.Refresh()
        self.statusbar.SetStatusText('page ' + str(cur))

    def OnPic(self, event):
        id = event.GetId()
        self.statusbar.SetStatusText('Show pic')
        pic_frame = pic_show(None, -1, 'pic', id)
        pic_frame.Center()
        pic_frame.Show(True)

    def OnSet(self, event):
	global cur
	self.statusbar.SetStatusText('Set Command')
	dlg = wx.MessageDialog(None, "设置壁纸成功", "设置成功", wx.OK)
        im = Image.open("/home/allen/GP/src/r" + str(cur) + str(event.GetId() - 220) + ".jpg")
        im.save("/home/allen/图片/" + 'name' + '.jpg')
        if dlg.ShowModal() == wx.ID_OK:
        	dlg.Destroy()


    def OnKey(self, event):
	global word
	global cur
	cur = 1
	id = event.GetId()
	print id
        values = {
		11:"风景",
		12:"动漫",
		13:"宠物",
		14:"汽车",
		15:"游戏",
		16:"影视",
	}
	key = values.get(id, "推荐")
        print key
	key = unicode(key, "utf-8")
	word = key
        self.statusbar.SetStatusText('Please wait')
        dl = download()
        a = dl.urlencode(key)
        b = dl.get_linklist(a, 0)
	max_page = int(math.ceil(dl.getnum() / 6.0))
	print dl.getnum(),max_page
        dl.downImageViaMutiThread(b, 0)
        im = wx.Image('/home/allen/GP/src/r11.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_1, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_1.Refresh()
        im = wx.Image('/home/allen/GP/src/r12.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_2, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_2.Refresh()
        im = wx.Image('/home/allen/GP/src/r13.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_3, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_3.Refresh()
        im = wx.Image('/home/allen/GP/src/r14.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_4, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_4.Refresh()
        im = wx.Image('/home/allen/GP/src/r15.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_5, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_5.Refresh()
        im = wx.Image('/home/allen/GP/src/r16.png',wx.BITMAP_TYPE_ANY)
        temp = im.ConvertToBitmap()
        wx.StaticBitmap(parent = self.pic_panel_6, bitmap = temp, pos=(0,0), size = (300,140))
        self.pic_panel_6.Refresh()
	path = '/home/allen/GP/src'
	filelist = os.listdir(path)
	for file in filelist:
        	if (not re.match(r'r[1-3][1-6].[jpg,png]',file)):
                	os.remove(path +'/'+file)
        self.statusbar.SetStatusText('search done')


class pic_show(wx.Frame):
    def __init__(self, parent, ID, title, id):
        wx.Frame.__init__(self, parent, id, 'show pic',
                size=(1200, 600))
        pic_show_box = wx.BoxSizer(wx.VERTICAL)         
        funcbar = wx.ToolBar(self, -1, style = wx.TB_HORIZONTAL | wx.NO_BORDER)
        funcbar.AddSimpleTool(3001, wx.Image('suoxiao.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'small', 'Small') 
        funcbar.AddSimpleTool(3002, wx.Image('fangda.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'big', 'Big')
        funcbar.AddSimpleTool(3003, wx.Image('liangdu.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'bright', 'Bright')
        funcbar.AddSimpleTool(3004, wx.Image('duibidu.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'contrast', 'Contrast')
	funcbar.AddSimpleTool(3005, wx.Image('save.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'save', 'Save')
	funcbar.AddSimpleTool(3006, wx.Image('set.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'set', 'Set')
        funcbar.AddSimpleTool(3007, wx.Image('contour.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'contour', 'Contour')
	funcbar.AddSimpleTool(3008, wx.Image('emboss.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'emboss', 'Emboss')
	funcbar.AddSimpleTool(3009, wx.Image('edge.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'edge', 'Edge')
	funcbar.AddSimpleTool(3010, wx.Image('water.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'watermark', 'Watermark')
	funcbar.Realize()
        
        #print self.tag
	global cur
        image = wx.Image("/home/allen/GP/src/r" + str(cur) + str(id - 210) + ".jpg",wx.BITMAP_TYPE_ANY)
        self.size = image.GetSize()
        self.tag = id
        self.bright = 1.0
        self.contrast = 1.0
	self.contour = 0
	self.emboss = 0
	self.edge = 0
        temp = image.ConvertToBitmap()        

        self.panel = wx.Panel(self, -1)
	im = Image.open("/home/allen/GP/src/r" + str(cur) + str(id - 210) + ".jpg")
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (600 - (im.size[0]/2), 300 - (im.size[1]/2)), size = (im.size[0],im.size[1]))      
        pic_show_box.Add(self.panel, 0, wx.EXPAND)
        pic_show_box.Add(funcbar, 0, wx.EXPAND)
        self.SetSizer(pic_show_box)
	
	im = Image.open("/home/allen/GP/src/r" + str(cur) + str(self.tag - 210) + ".jpg")
        out = im.resize((self.size[0], self.size[1]))
        out.save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        
        wx.EVT_TOOL(self, 3001, self.OnSmall)
        wx.EVT_TOOL(self, 3002, self.OnBig)
        wx.EVT_TOOL(self, 3003, self.OnBright)
        wx.EVT_TOOL(self, 3004, self.OnContrast)
	wx.EVT_TOOL(self, 3005, self.OnSave)
	wx.EVT_TOOL(self, 3006, self.OnSet)
	wx.EVT_TOOL(self, 3007, self.OnContour)
	wx.EVT_TOOL(self, 3008, self.OnEmboss)
	wx.EVT_TOOL(self, 3009, self.OnEdge)
	wx.EVT_TOOL(self, 3010, self.OnWatermark)    

    def PreDeal(self, size, bright, contrast, contour, emboss, edge):
	global cur
	im = Image.open("/home/allen/GP/src/r" + str(cur) + str(self.tag - 210) + ".jpg")
        out = im.resize((size[0], size[1]))
        out.save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        enhancer1 = ImageEnhance.Brightness(out)
        enhancer1.enhance(bright).save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        temp = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        enhancer2 = ImageEnhance.Contrast(temp)
        enhancer1.enhance(contrast).save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
	im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
	if contour == 1:
		im = im.filter(ImageFilter.CONTOUR)
	if emboss == 1:
		im = im.filter(ImageFilter.EMBOSS)
	if edge == 1:
		im = im.filter(ImageFilter.FIND_EDGES)
	im.save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")	
	image = wx.Image("bg.jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
        im = Image.open("bg.jpg")
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (0, 0), size = (1200,600))
        
    def OnSmall(self, event):
        #print self.tag
	global cur
        self.PreDeal(self.size, self.bright, self.contrast, self.contour, self.emboss, self.edge)
        
        im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        #print im.size
        if im.size[0] > 320:
            self.size[0] = self.size[0] - 64
            self.size[1] = self.size[1] - 32
            out = im.resize((self.size[0], self.size[1]))
        else:
            out = im        
        out.save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        image = wx.Image("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
	im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (600 - (im.size[0]/2), 300 - (im.size[1]/2)), size = (im.size[0],im.size[1]))
        self.panel.Refresh()
        print self.size

    def OnBig(self, event):
	global cur
        self.PreDeal(self.size, self.bright, self.contrast, self.contour, self.emboss, self.edge)
        im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        if im.size[0] < 1280:
            self.size[0] = self.size[0] + 64
            self.size[1] = self.size[1] + 32
            out = im.resize((self.size[0], self.size[1]))
        else:
            out = im
        out.save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        image = wx.Image("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
	im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (600 - (im.size[0]/2), 300 - (im.size[1]/2)), size = (im.size[0],im.size[1]))
        self.panel.Refresh()
        print self.size
        
    def OnBright(self, event):
	global cur
        self.PreDeal(self.size, self.bright, self.contrast, self.contour, self.emboss, self.edge)
        self.bright = self.bright + 1.0       
        im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        enhancer = ImageEnhance.Brightness(im)
        if self.bright > 8.0:
            self.bright = self.bright - 8.0
        factor = self.bright / 4.0
        enhancer.enhance(factor).save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        image = wx.Image("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
	im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (600 - (im.size[0]/2), 300 - (im.size[1]/2)), size = (im.size[0],im.size[1]))
        self.panel.Refresh()
        
    def OnContrast(self, event):
	global cur
        self.PreDeal(self.size, self.bright, self.contrast, self.contour, self.emboss, self.edge)
        self.contrast = self.contrast + 1.0
        im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        enhancer = ImageEnhance.Contrast(im)
        if self.contrast > 8.0:
            self.contrast = self.bright - 8.0
        factor = self.contrast / 4.0
        enhancer.enhance(factor).save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        image = wx.Image("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
	im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (600 - (im.size[0]/2), 300 - (im.size[1]/2)), size = (im.size[0],im.size[1]))
        self.panel.Refresh()

    def OnSave(self, event):
	global dir
	global cur
	dlg = wx.TextEntryDialog(self, "保存路径：" + dir + "请输入保存图片名称", "保存确认","")
	if dlg.ShowModal() == wx.ID_OK:
		name = dlg.GetValue()
		if os.path.exists(dir + name +".jpg"):
			warning = wx.MessageDialog(None, dir + name + u".jpg 已存在是否覆盖", "warning", wx.YES_NO)
			if warning.ShowModal() == wx.ID_YES:
				im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
		                im.save(dir + name + '.jpg')
				warning.Destroy()
			elif warning.ShowModal() == wx.ID_NO:
				warning.Destroy()
		else:
			im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
                        im.save(dir + name + '.jpg')
	dlg.Destroy()

    def OnSet(self, event):
        global cur
        dlg = wx.MessageDialog(None, "设置壁纸成功", "设置成功", wx.OK)
        im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        im.save("/home/allen/图片/" + 'name' + '.jpg')
        if dlg.ShowModal() == wx.ID_OK:
                dlg.Destroy()

    def OnContour(self, event):
        global cur
	if self.contour == 0:
		self.contour =1
        	self.PreDeal(self.size, self.bright, self.contrast, self.contour, self.emboss, self.edge)
        	im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
		imfilter = im.filter(ImageFilter.CONTOUR)
		imfilter.save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
	else:
		self.contour = 0
		self.PreDeal(self.size, self.bright, self.contrast, self.contour, self.emboss, self.edge)
		im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
	image = wx.Image("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
	wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (600 - (im.size[0]/2), 300 - (im.size[1]/2)), size = (im.size[0],im.size[1]))
        self.panel.Refresh()

    def OnEmboss(self, event):
        global cur
        if self.emboss == 0:
                self.emboss =1
                self.PreDeal(self.size, self.bright, self.contrast, self.contour, self.emboss, self.edge)
                im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
                imfilter = im.filter(ImageFilter.EMBOSS)
                imfilter.save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        else:
                self.emboss = 0
                self.PreDeal(self.size, self.bright, self.contrast, self.contour, self.emboss, self.edge)
                im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        image = wx.Image("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (600 - (im.size[0]/2), 300 - (im.size[1]/2)), size = (im.size[0],im.size[1]))
        self.panel.Refresh()
	

    def OnEdge(self, event):
        global cur
        if self.edge == 0:
                self.edge =1
                self.PreDeal(self.size, self.bright, self.contrast, self.contour, self.emboss, self.edge)
                im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
                imfilter = im.filter(ImageFilter.FIND_EDGES)
                imfilter.save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        else:
                self.edge = 0
                self.PreDeal(self.size, self.bright, self.contrast, self.contour, self.emboss, self.edge)
                im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        image = wx.Image("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (600 - (im.size[0]/2), 300 - (im.size[1]/2)), size = (im.size[0],im.size[1]))
        self.panel.Refresh()
    
    def OnWatermark(self, event):
        global cur
	POSITION = ('LEFTTOP','RIGHTTOP','CENTER','LEFTBOTTOM','RIGHTBOTTOM')
        #self.PreDeal(self.size, self.bright, self.contrast, self.contour, self.emboss, self.edge)
	dlg = wx.FileDialog(self, "Open a picture", os.getcwd(), style = wx.OPEN, wildcard = "*.*")
        if dlg.ShowModal() == wx.ID_OK:
                markimage = dlg.GetPath()
		print markimage
		pos_dlg = wx.TextEntryDialog(self,"1:左上 2：右上 3：中间 4：左下 5：右下","位置选择","")
        	if pos_dlg.ShowModal() == wx.ID_OK:
			tmp = pos_dlg.GetValue()
			if tmp == '1':
				position = POSITION[0]
			elif tmp == '2':
				position = POSITION[1]
                	elif tmp == '3':
                        	position = POSITION[2]
                	elif tmp == '4':
                        	position = POSITION[3]
                	elif tmp == '5':
                        	position = POSITION[4]
			else:
				warning = wx.MessageDialog(None, u"无效参数", "warning", wx.OK)
				if warning.ShowModal() == wx.ID_OK:
					warning.Destroy()
					dlg.Destroy
					return
		pos_dlg.Destroy()
		im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
	       	mark = Image.open(markimage)
		if mark.mode != 'RGBA':
			mark = mark.convert('RGBA')
		else:
        		mark = mark.copy()
        	alpha = mark.split()[3]
		print alpha
        	alpha = ImageEnhance.Brightness(alpha).enhance(0.9)
        	mark.putalpha(alpha)
        	if im.mode != 'RGBA':
                	im = im.convert('RGBA')
        	layer = Image.new('RGBA', im.size, (0,0,0,0))
        	if position == 'title':
                	for y in range(0, im.size[1], mark.size[1]):
                        	for x in range(0, im.size[0], mark.size[0]):
                                	layer.paste(mark, (x, y))
        	elif position == 'scale':
                	ratio = min(
                	float(im.size[0]) / mark.size[0], float(im.size[1]) / mark.size[1])
                	w = int(mark.size[0] * ratio)
                	h = int(mark.size[1] * ratio)
                	mark = mark.resize((w, h))
                	layer.paste(mark, ((im.size[0] - w) / 2, (im.size[1] - h) / 2))
        	elif position == POSITION[0]:
                	position = (10,10)
                	layer.paste(mark, position)
        	elif position == POSITION[1]:
                	position = (im.size[0] - mark.size[0]-10, 10)
                	layer.paste(mark, position)
        	elif position == POSITION[2]:
                	position = ((im.size[0] - mark.size[0])/2,(im.size[1] - mark.size[1])/2)
                	layer.paste(mark, position)
        	elif position == POSITION[3]:
                	position = (10,im.size[1] - mark.size[1]-10,)
                	layer.paste(mark, position)
        	else:
                	position = (im.size[0] - mark.size[0]-10, im.size[1] - mark.size[1]-10,)
                	layer.paste(mark, position)
        	Image.composite(layer, im, layer).save("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
        dlg.Destroy()
	im = Image.open("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg")
	image = wx.Image("/home/allen/GP/src/rr" + str(cur) + str(self.tag - 210) + ".jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (600 - (im.size[0]/2), 300 - (im.size[1]/2)), size = (im.size[0],im.size[1]))
        self.panel.Refresh()		

class MyApp(wx.App):
    def OnInit(self):
        frame = UI(None, -1, 'Background')
        frame.SetIcon(wx.Icon('logo.ico', wx.BITMAP_TYPE_ICO))
        frame.Center()
        frame.Show(True)
        return True
app = MyApp(0)
app.MainLoop()
