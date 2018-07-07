import wx

class Main(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        self.text = wx.TextCtrl(self, wx.NewId(), style=wx.TE_RICH)
        self.check = wx.CheckBox(self, wx.NewId(), 'Make text red if 0')
        self.check.Bind(wx.EVT_CHECKBOX, self.onCheck)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text, 0)
        sizer.Add(self.check, 0)
        self.SetSizerAndFit(sizer)
        self.Show()

    def onCheck(self, evt):
        value = self.text.GetValue()
        if self.check.IsChecked() and value == '0':
            self.text.SetForegroundColour(wx.RED)
        else:
            self.text.SetForegroundColour(wx.BLACK)

app = wx.App(0)
Main(None, -1, 'Checkbox')
app.MainLoop()
