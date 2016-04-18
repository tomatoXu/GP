#coding:utf-8
from download import download
import wx
import Image
import ImageEnhance

class UI(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(740, 640))
#menubar
        menubar = wx.MenuBar()  
        file = wx.Menu()  
        edit = wx.Menu()  
        help = wx.Menu()  
        file.Append(101, '&open', 'open a picture')  
        file.Append(102, '&save', 'save the picture')  
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
        searchtext = wx.TextCtrl(searchbar, -1, 'search', pos = (20,5), size = (300, 40))
        searchtext.SetInsertionPoint(0)
        
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
        pic_1.AddSimpleTool(221, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_2.AddSimpleTool(212, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_2.AddSimpleTool(222, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
	pic_3.AddSimpleTool(213, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_3.AddSimpleTool(223, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
	pic_4.AddSimpleTool(214, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_4.AddSimpleTool(224, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
	pic_5.AddSimpleTool(215, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_5.AddSimpleTool(225, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
	pic_6.AddSimpleTool(216, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')
        pic_6.AddSimpleTool(226, wx.Image('view.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '', '')

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

        wx.EVT_TOOL(self, 1, self.OnHome)
        wx.EVT_TOOL(self, 2, self.OnMine)
        wx.EVT_TOOL(self, 3, self.OnQuit)
        wx.EVT_TOOL(self, 4, self.OnSearch)
        
        wx.EVT_TOOL(self, 211, self.OnPic)
        wx.EVT_TOOL(self, 212, self.OnPic)
        wx.EVT_TOOL(self, 213, self.OnPic)
        wx.EVT_TOOL(self, 214, self.OnPic)
        wx.EVT_TOOL(self, 215, self.OnPic)
        wx.EVT_TOOL(self, 216, self.OnPic)
	wx.EVT_TOOL(self, 221, self.OnDow)
        wx.EVT_TOOL(self, 222, self.OnDow)
        wx.EVT_TOOL(self, 223, self.OnDow)
        wx.EVT_TOOL(self, 224, self.OnDow)
        wx.EVT_TOOL(self, 225, self.OnDow)
        wx.EVT_TOOL(self, 226, self.OnDow)
	

        self.SetSizer(vbox)
        self.statusbar = self.CreateStatusBar()       
        self.Centre()

#响应函数
    def OnHome(self, event):
        self.statusbar.SetStatusText('Home Command')
        im = Image.open("home.png")
        out = im.resize((40,40))
        out.save("home.png")
        self.Refresh()
    def OnMine(self, event):
        self.statusbar.SetStatusText('Mine Command')
    def OnSearch(self, event):
        self.statusbar.SetStatusText('Please wait')
 	dl = download()
        a = dl.urlencode('a')
        b = dl.get_linklist(a)
        dl.downImageViaMutiThread(b)
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
	self.statusbar.SetStatusText('search done')
    def OnOpen(self, event):
        self.statusbar.SetStatusText('Open Command')
    def OnSave(self, event):
        self.statusbar.SetStatusText('Save Command')
    def OnQuit(self, event):
        self.Close()
    def OnPic(self, event):
        id = event.GetId()
        self.statusbar.SetStatusText('Show pic')
        pic_frame = pic_show(None, -1, 'pic', id)
        pic_frame.Center()
        pic_frame.Show(True)
    def OnDow(self, event):
	self.statusbar.SetStatusText('Download Command')

class pic_show(wx.Frame):
    def __init__(self, parent, ID, title, id):
        wx.Frame.__init__(self, parent, id, 'show pic',
                size=(1920, 1080))
        pic_show_box = wx.BoxSizer(wx.VERTICAL)         
        funcbar = wx.ToolBar(self, -1, style = wx.TB_HORIZONTAL | wx.NO_BORDER)
        funcbar.AddSimpleTool(3001, wx.Image('suoxiao.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'small', 'Small') 
        funcbar.AddSimpleTool(3002, wx.Image('fangda.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'big', 'Big')
        funcbar.AddSimpleTool(3003, wx.Image('liangdu.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'bright', 'Bright')
        funcbar.AddSimpleTool(3004, wx.Image('duibidu.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'contrast', 'Contrast')
	funcbar.AddSimpleTool(3005, wx.Image('save.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'save', 'Save')
        funcbar.Realize()
        
        #print self.tag
        image = wx.Image("/home/allen/GP/src/r" + str(id - 200) + ".jpg",wx.BITMAP_TYPE_ANY)
        self.size = image.GetSize()
        self.tag = id
        self.bright = 1.0
        self.contrast = 1.0
        temp = image.ConvertToBitmap()        

        self.panel = wx.Panel(self, -1)
        '''
        self.button = wx.Button(self.panel, -1, "suoxiao", pos=(10, 500))
        self.Bind(wx.EVT_BUTTON, self.OnSmall, self.button)
        self.button = wx.Button(self.panel, -1, "fangda", pos=(110, 500))
        self.Bind(wx.EVT_BUTTON, self.OnBig, self.button)
        self.button = wx.Button(self.panel, -1, "liangdu", pos=(210, 500))
        self.Bind(wx.EVT_BUTTON, self.OnBright, self.button)
        self.button = wx.Button(self.panel, -1, "duibidu", pos=(310, 500))
        self.Bind(wx.EVT_BUTTON, self.OnContrast, self.button)
        '''
	im = Image.open("/home/allen/GP/src/r" + str(id - 200) + ".jpg")
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (400 - (im.size[0]/2), 200 - (im.size[1]/2)), size = (1920, 1080))      
        pic_show_box.Add(self.panel, 0, wx.EXPAND)
        pic_show_box.Add(funcbar, 0, wx.EXPAND)
        self.SetSizer(pic_show_box)
        
        wx.EVT_TOOL(self, 3001, self.OnSmall)
        wx.EVT_TOOL(self, 3002, self.OnBig)
        wx.EVT_TOOL(self, 3003, self.OnBright)
        wx.EVT_TOOL(self, 3004, self.OnContrast)
	wx.EVT_TOOL(self, 3005, self.OnSave)
    
    def PreDeal(self, size, bright, contrast):
        im = Image.open("/home/allen/GP/src/r" + str(self.tag - 200) + ".jpg")
        out = im.resize((size[0], size[1]))
        out.save("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        enhancer1 = ImageEnhance.Brightness(out)
        enhancer1.enhance(bright).save("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        print bright
        temp = Image.open("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        enhancer2 = ImageEnhance.Contrast(temp)
        enhancer1.enhance(contrast).save("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
	image = wx.Image("bg.jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
        im = Image.open("bg.jpg")
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (0, 0), size = (800,400))
        
    def OnSmall(self, event):
        #print self.tag
        self.PreDeal(self.size, self.bright, self.contrast)
        
        im = Image.open("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        #print im.size
        if im.size[0] > 320:
            self.size[0] = self.size[0] - 64
            self.size[1] = self.size[1] - 32
            out = im.resize((self.size[0], self.size[1]))
        else:
            out = im        
        out.save("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        image = wx.Image("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
	im = Image.open("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (400 - (im.size[0]/2), 200 - (im.size[1]/2)), size = (800,400))
        self.panel.Refresh()
        print self.size

    def OnBig(self, event):
        self.PreDeal(self.size, self.bright, self.contrast)
        im = Image.open("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        if im.size[0] < 1280:
            self.size[0] = self.size[0] + 64
            self.size[1] = self.size[1] + 32
            out = im.resize((self.size[0], self.size[1]))
        else:
            out = im
        out.save("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        image = wx.Image("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
	im = Image.open("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (400 - (im.size[0]/2), 200 - (im.size[1]/2)), size = (800,400))
        self.panel.Refresh()
        print self.size
        
    def OnBright(self, event):
        self.PreDeal(self.size, self.bright, self.contrast)
        self.bright = self.bright + 1.0       
        im = Image.open("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        enhancer = ImageEnhance.Brightness(im)
        if self.bright > 8.0:
            self.bright = self.bright - 8.0
        factor = self.bright / 4.0
        enhancer.enhance(factor).save("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        image = wx.Image("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
	im = Image.open("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (400 - (im.size[0]/2), 200 - (im.size[1]/2)), size = (800,400))
        self.panel.Refresh()
        
    def OnContrast(self, event):
        self.PreDeal(self.size, self.bright, self.contrast)
        self.contrast = self.contrast + 1.0
        im = Image.open("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        enhancer = ImageEnhance.Contrast(im)
        if self.contrast > 8.0:
            self.contrast = self.bright - 8.0
        factor = self.contrast / 4.0
        enhancer.enhance(factor).save("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        image = wx.Image("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg",wx.BITMAP_TYPE_ANY)
        temp = image.ConvertToBitmap()
	im = Image.open("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
        wx.StaticBitmap(parent = self.panel, bitmap = temp, pos = (400 - (im.size[0]/2), 200 - (im.size[1]/2)), size = (800,400))
        self.panel.Refresh()

    def OnSave(self, event):
	im = Image.open("/home/allen/GP/src/rr" + str(self.tag - 200) + ".jpg")
	im.save('/home/allen/GP/save/'+'name'+'.jpg')
	print 'save'


class MyApp(wx.App):
    def OnInit(self):
        frame = UI(None, -1, 'Background')
        frame.SetIcon(wx.Icon('logo.ico', wx.BITMAP_TYPE_ICO))
        frame.Center()
        frame.Show(True)
        return True
app = MyApp(0)
app.MainLoop()
