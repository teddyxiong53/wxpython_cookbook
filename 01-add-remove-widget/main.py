import wx
class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.number_of_buttons = 0
        self.frame = parent
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        control_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.widget_sizer = wx.BoxSizer(wx.VERTICAL)

        self.add_button = wx.Button(self, label='add')
        self.add_button.Bind(wx.EVT_BUTTON, self.on_add_widget)
        control_sizer.Add(self.add_button, 0, wx.CENTER | wx.ALL, 5)

        self.remove_button = wx.Button(self, label='remove')
        self.remove_button.Bind(wx.EVT_BUTTON, self.on_remove_widget)
        control_sizer.Add(self.remove_button, 0, wx.CENTER|wx.ALL, 5)

        self.main_sizer.Add(control_sizer, 0, wx.CENTER)
        self.main_sizer.Add(self.widget_sizer, 0, wx.CENTER|wx.ALL, 10)

        self.SetSizer(self.main_sizer)

    def on_add_widget(self, event):
        self.number_of_buttons += 1
        label = f'Button {self.number_of_buttons}'
        name = f'button{self.number_of_buttons}'
        new_button = wx.Button(self, label=label, name=name)
        self.widget_sizer.Add(new_button, 0, wx.ALL, 5)
        self.frame.sizer.Layout()
        self.frame.Fit()

    def on_remove_widget(self, event):
        if self.widget_sizer.GetChildren():
            self.widget_sizer.Hide(self.number_of_buttons-1)
            self.widget_sizer.Remove(self.number_of_buttons-1)
            self.number_of_buttons -= 1
            self.frame.sizer.Layout()
            self.frame.Fit()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='add remove control')
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        panel = MyPanel(self)
        self.sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()
        self.Show()

app = wx.App()
frame = MyFrame()
app.MainLoop()
