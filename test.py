import wx

app = wx.App()
frame = wx.Frame(None, title='GridBagSizer Example')

panel = wx.Panel(frame)
gbSizer = wx.GridBagSizer(10, 10)

btn1 = wx.Button(panel, label='Button 1')
gbSizer.Add(btn1, pos=(0, 0), flag=wx.EXPAND|wx.ALL, border=5)

btn2 = wx.Button(panel, label='Button 2')
gbSizer.Add(btn2, pos=(1, 0), flag=wx.EXPAND|wx.ALL, border=5)

btn3 = wx.Button(panel, label='Button 3')
gbSizer.Add(btn3, pos=(2, 0), flag=wx.EXPAND|wx.ALL, border=5)

btn4 = wx.Button(panel, label='Button 4')
gbSizer.Add(btn4, pos=(3, 0), flag=wx.EXPAND|wx.ALL, border=5)

btn5 = wx.Button(panel, label='Button 5')
gbSizer.Add(btn5, pos=(4, 0), flag=wx.EXPAND|wx.ALL, border=5)

gbSizer.AddGrowableRow(4)  # 将第 4 行设置为可伸缩的行

panel.SetSizer(gbSizer)
gbSizer.Fit(panel)

frame.Show()
app.MainLoop()
