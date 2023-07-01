import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
        sizer = wx.BoxSizer(wx.VERTICAL)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        for i in range(4):
            label = f'Button{i}'
            btn = wx.Button(self, label=label)
            sizer.Add(btn, 0, wx.ALL, 5)

        h_sizer.Add((1,1), 1, wx.EXPAND)
        h_sizer.Add(sizer, 0, wx.TOP, 100)
        h_sizer.Add((1,1), 0, wx.ALL, 75)
        self.SetSizer(h_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.on_erase_background)

    def on_erase_background(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap('big_cat.jpg')
        dc.DrawBitmap(bmp, 0 , 0)

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='bg pic')
        panel = MyPanel(self)
        self.Centre()
app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
