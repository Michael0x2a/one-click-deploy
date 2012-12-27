#!/usr/bin/env python

import wx

class DeployTab(wx.Panel):
    def __init__(self, parent):
        super(DeployTab, self).__init__(parent, id=wx.ID_ANY)
        
        self.sizer = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        deploy = wx.Button(
            self, 
            label="DEPLOY")
            #size=(250, 100))
        self.sizer.Add(deploy, proportion=2, flag=wx.EXPAND|wx.ALL, border=5)
        
        download = wx.Button(
            self,
            label="Download Code\n(will overwrite existing code)")
        self.sizer.Add(download, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        
        restore = wx.Button(
            self,
            label="Restore Internet")
        self.sizer.Add(restore, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        
        self.SetSizer(self.sizer)
        self.Layout()
        
class ConfigTab(wx.Panel):
    # For now, copy.
    def __init__(self, parent):
        super(ConfigTab, self).__init__(parent, id=wx.ID_ANY)
        
        self.sizer = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        deploy = wx.Button(
            self, 
            label="test")
        self.sizer.Add(deploy, proportion=2, flag=wx.EXPAND|wx.ALL, border=5)
        
        download = wx.Button(
            self,
            label="test")
        self.sizer.Add(download, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        
        restore = wx.Button(
            self,
            label="test")
        self.sizer.Add(restore, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        
        self.SetSizer(self.sizer)
        self.Layout()
        
class NotebookTabs(wx.Notebook):
    def __init__(self, parent):
        super(NotebookTabs, self).__init__(parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)
        
        self.deploy_tab = DeployTab(self)
        self.AddPage(self.deploy_tab, "Go!")
        
        self.options_tab = ConfigTab(self)
        self.AddPage(self.options_tab, "Options")
    

class MainWindow(wx.Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.setup_ui()
        self.setup_sizers()
        
    def setup_ui(self):
        self.menubar = wx.MenuBar()
        
        file_menu = wx.Menu()
        f_quit = file_menu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.Bind(wx.EVT_MENU, self.on_quit, f_quit)
        
        self.menubar.Append(file_menu, '&File')
        
        help_menu = wx.Menu()
        f_about = help_menu.Append(100, 'About', 'About this program')
        f_help = help_menu.Append(101, 'Help', 'How to use this program')
        self.menubar.Append(help_menu, '&Help')
        
        self.SetMenuBar(self.menubar)
        
        self.SetSize((300, 250))
        self.SetTitle('One Click Deploy')
        self.Centre()
        self.Show(True)
        
    def setup_sizers(self):
        self.panel = wx.Panel(self)
        self.notebook = NotebookTabs(self.panel)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.panel.SetSizer(self.sizer)
        self.Layout()
        
    def on_quit(self, event):
        self.Close()
        
def main():
    app = wx.App()
    MainWindow(None)
    app.MainLoop()
    
if __name__ == '__main__':
    main()