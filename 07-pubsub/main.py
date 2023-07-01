import wx
from wx.lib.pubsub import pub

class OtherFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'second frame')
        panel = wx.Panel(self)
        msg = 'send a msg to main frame'
        cmd = wx.StaticText(panel, label=msg)
        self.msg_txt = wx.TextCtrl(panel, value='')
        close_btn = wx.Button(panel, label='send and close')
        close_btn.Bind(wx.EVT_BUTTON, self.on_send_and_close)

        sizer = wx.BoxSizer(wx.VERTICAL)
        flags = wx.ALL | wx.CENTER
        sizer.Add(cmd, 0, flags, 5)
        sizer.Add(self.msg_txt, 0, flags, 5)
        sizer.Add(close_btn, 0, flags, 5)
        panel.SetSizer(sizer)

    def on_send_and_close(self, event):
        msg = self.msg_txt.GetValue()
        pub.sendMessage('panel_listener', message=msg)
        pub.sendMessage('panel_listener', message='test2', arg2='2nd arg')
        self.Close()


class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        pub.subscribe(self.my_listener, "panel_listener")
        btn = wx.Button(self, label='open frame')
        btn.Bind(wx.EVT_BUTTON, self.on_open_frame)

    def my_listener(self, message, arg2=None):
        print(f'receive msg:{message}')
        if arg2:
            print(f'arg2:{arg2}')

    def on_open_frame(self, event):
        frame = OtherFrame()
        frame.Show()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='pubsub test', size=(500,400))
        panel = MyPanel(self)
        self.Show()


app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
