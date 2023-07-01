import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='screenshot')
        panel = wx.Panel(self)
        screenshot_button = wx.Button(panel, label='take screenshot')
        screenshot_button.Bind(wx.EVT_BUTTON, self.on_take_screenshot)
        print_button = wx.Button(panel, label='print screenshot')
        print_button.Bind(wx.EVT_BUTTON, self.on_print_screenshot)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(screenshot_button, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(print_button, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(sizer)

    def on_take_screenshot(self, event):
        rect = self.GetRect()
        dc_screen = wx.ScreenDC()
        bmp = wx.EmptyBitmap(rect.width, rect.height)
        mem_dc = wx.MemoryDC()
        mem_dc.SelectObject(bmp)
        mem_dc.Blit(
            0, 0, rect.width, rect.height,
            dc_screen, rect.x, rect.y
        )
        mem_dc.SelectObject(wx.NullBitmap)
        img = bmp.ConvertToImage()
        filename = '1.png'
        img.SaveFile(filename, wx.BITMAP_TYPE_PNG)

    def on_print_screenshot(self, event):
        pass
app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
