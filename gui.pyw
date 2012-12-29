#!/usr/bin/env python

import urllib2
import os.path
import sys

import core
import compile
import options
import repo
import deploy

import one_click_deploy as meta

import wx

class DeployTab(wx.Panel):
    def __init__(self, parent):
        super(DeployTab, self).__init__(parent, id=wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.create_elements()
        self.create_bindings()
        self.create_layout()
        
    def create_elements(self):
        self.deploy_button = wx.Button(
            self,
            wx.ID_ANY,
            label="DEPLOY")
        self.download_button = wx.Button(
            self,
            wx.ID_ANY,
            label="Download Code From Repository\n(will overwrite existing code)")
        self.restore_button = wx.Button(
            self,
            wx.ID_ANY,
            label="Restore Internet")
            
    def create_bindings(self):
        self.Bind(
            wx.EVT_BUTTON,
            self.deploy_func,
            self.deploy_button)
        self.Bind(
            wx.EVT_BUTTON,
            self.download_func,
            self.download_button)
        self.Bind(
            wx.EVT_BUTTON,
            self.restore_func,
            self.restore_button)
            
    def create_layout(self):
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(
            self.deploy_button,
            proportion=2, 
            flag=wx.EXPAND|wx.ALL, 
            border=2)
        self.sizer.Add(
            self.download_button, 
            proportion=1, 
            flag=wx.EXPAND|wx.ALL, 
            border=2)
        self.sizer.Add(
            self.restore_button, 
            proportion=1, 
            flag=wx.EXPAND|wx.ALL, 
            border=2)
            
        self.SetSizer(self.sizer)
        self.sizer.Fit(self)
        
    def deploy_func(self, event):
        op = self.get_options()
        if op is None:
            event.Skip()
            return
        if not core.does_code_exist(op):
            self.deploy_button.SetLabel('Downloading code, please wait...')
            try:
                success = self.download_code(op)
                downloaded = True
                if not success:
                    self.deploy_button.SetLabel('DEPLOY')
                    return                
            except urllib2.URLError:
                self.display_error('Please restore access to the internet first.')
                self.deploy_button.SetLabel('DEPLOY')
                return
        else:
            downloaded = False
        
        self.deploy_button.SetLabel('Connecting to robot, please wait...')
        try:
            core.connect_to_robot(op)
        except deploy.ConnectionError as e:
            self.display_error(str(e))
            self.deploy_button.SetLabel('DEPLOY')
            return
        except deploy.NetworkConnectionError as e:
            self.display_error(str(e))
        
        self.deploy_button.SetLabel('Compiling code, please wait. This may take a while.\n')
        try:
            core.compile_code(op)
        except compile.CompilationError as e:
            self.display_error(str(e))
            return
        except compile.MissingWrmakefile as e:
            self.display_error(str(e))
            return
        finally:
            self.deploy_button.SetLabel('DEPLOY')
            
        self.deploy_button.SetLabel('Deploying code, please wait...')
        try:
            core.deploy_code(op)
        except deploy.ConnectionError as e:
            self.display_error(str(e))
            return
        finally:
            self.deploy_button.SetLabel('DEPLOY')
            
        if downloaded:
            self.display_success('Successfully downloaded, compiled, and deployed code')
        else:
            self.display_success('Successfully compiled and deployed code')
        pass
    
    def download_func(self, event):
        op = self.get_options()
        if op is None:
            event.Skip()
            return
        self.download_button.SetLabel('Downloading code, please wait...')
        try:
            is_success = self.download_code(op)
            if is_success:
                self.display_success('Successfully downloaded code from the repo')
        except urllib2.URLError:
            self.display_error('Please restore access to the internet first.')
        finally:
            self.download_button.SetLabel('Download Code From Repository\n(will overwrite existing code)')
            
    def restore_func(self, event):
        op = self.get_options()
        if op is None:
            event.Skip()
            return
        self.restore_button.SetLabel('Restoring internet, please wait...')
        if op.wireless_mac_address.lower() == 'none':
            self.display_error('Please select an adapter from the options tab')
            self.restore_button.SetLabel('Restore Internet')
            return
        try:
            core.restore_internet(op)
            self.display_success('Successfully restored access to the internet')
        except deploy.ConnectionError as e:
            self.display_error(str(e))
        finally:
            self.restore_button.SetLabel('Restore Internet')
        
    def get_options(self):
        try:
            op = core.get_options()
        except options.ConfigurationMissing:
            self.display_error('Please set the options in the "Options" tab first')
            return None
        return op
        
    def download_code(self, op):
        try:
            core.download_code(op)
            return True
        except repo.InvalidRevision:
            self.display_error('Please set a valid revision number (or type "latest" to download the latest revision) in the options tab.')
            return False
        except repo.InvalidUrl as e:
            self.display_error(str(e))
        except repo.InaccessibleUrl as e:
            self.display_error(str(e))
        finally:
            pass
        
        
    def display_success(self, message, title='Success!'):
        dialog = wx.MessageBox(
            message,
            title,
            wx.OK|wx.ICON_EXCLAMATION)
    
    def display_error(self, message, title='Error'):
        dialog = wx.MessageBox(
            message,
            title,
            wx.OK|wx.ICON_ERROR)
            
class OptionsTab(wx.Panel):
    def __init__(self, parent):
        super(OptionsTab, self).__init__(parent, id=wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.create_elements()
        self.bind_elements()
        self.create_layout()
        
    def create_elements(self):
        if not core.does_options_exist():
            core.create_default_options()
            wx.MessageBox(
                'Be sure to configure the settings in the "Options" tab before running anything!',
                'Alert!',
                wx.OK|wx.ICON_EXCLAMATION)
        op = core.get_options()
        
        self.team_number_static = wx.StaticText(self, wx.ID_ANY, "Team Number")
        self.team_number_text = wx.TextCtrl(self, wx.ID_ANY, op.team_number)
        
        self.robot_network_static = wx.StaticText(self, wx.ID_ANY, "Robot Network Name")
        self.robot_network_text = wx.TextCtrl(self, wx.ID_ANY, op.robot_network_name)
        
        self.source_static = wx.StaticText(self, wx.ID_ANY, "Source Code Url")
        self.source_text = wx.TextCtrl(self, wx.ID_ANY, op.repo_target_url)
        
        self.revision_static = wx.StaticText(self, wx.ID_ANY, "Source Code Revision")
        self.revision_text = wx.TextCtrl(self, wx.ID_ANY, op.repo_target_revision)
        
        self.install_dir_static = wx.StaticText(self, wx.ID_ANY, "WindRiver Install Dir")
        self.install_dir_text = wx.TextCtrl(self, wx.ID_ANY, op.windriver_install_dir)
        
        (e_default, ethernet), (w_default, wireless) = self.get_adapter_choices(op)
        self.wireless_adapter_static = wx.StaticText(self, wx.ID_ANY, "Wireless Adapter")
        self.wireless_adapter_choice = wx.ComboBox(
            self, 
            wx.ID_ANY, 
            value=w_default,
            choices=wireless, 
            style=wx.CB_DROPDOWN | wx.CB_DROPDOWN)
        
        self.ethernet_adapter_static = wx.StaticText(self, wx.ID_ANY, "Ethernet Adapter")
        self.ethernet_adapter_choice = wx.ComboBox(
            self, 
            wx.ID_ANY, 
            value=e_default, 
            choices=ethernet, 
            style=wx.CB_DROPDOWN | wx.CB_DROPDOWN)
        
        self.apply_button = wx.Button(self, id=wx.ID_ANY, label="Apply")
        
    def bind_elements(self):
        self.Bind(
            wx.EVT_BUTTON,
            self.apply_func,
            self.apply_button)
            
    def create_layout(self):
        self.sizer = wx.FlexGridSizer(8, 2, 0, 0)
        self.sizer.Add(
            self.team_number_static, 
            proportion=0, 
            flag=0, 
            border=2)
        self.sizer.Add(
            self.team_number_text, 
            proportion=0, 
            flag=wx.EXPAND, 
            border=2)
        
        self.sizer.Add(
            self.robot_network_static, 
            proportion=0, 
            flag=0, 
            border=2)
        self.sizer.Add(
            self.robot_network_text, 
            proportion=0, 
            flag=wx.EXPAND, 
            border=2)
            
        self.sizer.Add(
            self.source_static, 
            proportion=0, 
            flag=0, 
            border=2)
        self.sizer.Add(
            self.source_text, 
            proportion=0, 
            flag=wx.EXPAND, 
            border=2)
            
        self.sizer.Add(
            self.revision_static, 
            proportion=0, 
            flag=0, 
            border=2)
        self.sizer.Add(
            self.revision_text, 
            proportion=0, 
            flag=wx.EXPAND, 
            border=2)    
            
        self.sizer.Add(
            self.install_dir_static, 
            proportion=0, 
            flag=wx.EXPAND, 
            border=2)
        self.sizer.Add(
            self.install_dir_text, 
            proportion=0, 
            flag=wx.EXPAND, 
            border=2)
            
        self.sizer.Add(
            self.wireless_adapter_static, 
            proportion=0, 
            flag=0, 
            border=2)
        self.sizer.Add(
            self.wireless_adapter_choice, 
            proportion=0, 
            flag=wx.EXPAND, 
            border=2)
            
        self.sizer.Add(
            self.ethernet_adapter_static, 
            proportion=0, 
            flag=0, 
            border=2)
        self.sizer.Add(
            self.ethernet_adapter_choice, 
            proportion=0, 
            flag=wx.EXPAND, 
            border=2)
            
        self.sizer.Add(
            self.apply_button, 
            proportion=0, 
            flag=wx.EXPAND|wx.ALIGN_RIGHT, 
            border=2)
        
        self.sizer.AddGrowableCol(1)
        self.SetSizer(self.sizer)
        self.sizer.Fit(self)
        
    def get_adapter_choices(self, op):
        con = core.get_connection_options()
        ethernet = con['ethernet']
        wireless = con['wireless']
        ethernet_out = ['None']
        wireless_out = ['None']
        ethernet_default = 'None'
        wireless_default = 'None'
        for name, mac in ethernet.items():
            label = '{0} ({1})'.format(name, mac)
            ethernet_out.append(label)
            norm = op.ethernet_mac_address
            dash = norm.replace(':', '-')
            if (norm in mac) or (dash in mac):
                ethernet_default = label
        for name, mac in wireless.items():
            label = '{0} ({1})'.format(name, mac)
            wireless_out.append(label)
            norm = op.wireless_mac_address
            dash = norm.replace(':', '-')
            if (norm in mac) or (dash in mac):
                wireless_default = label
                
        if op.ethernet_mac_address.lower() == 'None':
            ethernet_default = 'None'
        if op.wireless_mac_address.lower() == 'None':
            wireless_default = 'None'
            
        return (ethernet_default, ethernet_out), (wireless_default, wireless_out)
        
    def apply_func(self, event):
        def get_mac(string):
            if string.lower() == 'none':
                return 'None'
            else:
                return string[-18: -1]

        op = options.Options()
        op['team_number'] = self.team_number_text.GetValue()
        op['robot_network_name'] = self.robot_network_text.GetValue()
        op['repo_target_url'] = self.source_text.GetValue()
        op['repo_target_revision'] = self.revision_text.GetValue()
        op['windriver_install_dir'] = self.install_dir_text.GetValue()
        op['wind_base'] = os.path.join(op['windriver_install_dir'], 'vxworks-6.3')
        op['wireless_mac_address'] = get_mac(self.wireless_adapter_choice.GetValue())
        op['ethernet_mac_address'] = get_mac(self.ethernet_adapter_choice.GetValue())
        
        core.save_options(op)
        
        wx.MessageBox(
            'Options successfully applied!',
            'Success!',
            wx.OK|wx.ICON_EXCLAMATION)
            
        
        
class NotebookTabs(wx.Notebook):
    def __init__(self, parent):
        super(NotebookTabs, self).__init__(parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)
        
        self.deploy_tab = DeployTab(self)
        self.AddPage(self.deploy_tab, "Go!")
        
        self.options_tab = OptionsTab(self)
        self.AddPage(self.options_tab, "Options")
        

class MainWindow(wx.Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        
        self.SetTitle('One Click Deploy')
        self.icon = wx.Icon(r'resources/icon.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        
        self.setup_ui()
        self.setup_sizers()
        
        self.SetSize((500, 300))
        self.Centre()
        self.Show(True)
        
        if not core.is_admin():
            wx.MessageBox(
                'Please right-click this program and select "Run As Administrator". This program needs admin rights in order to function properly.',
                'Error',
                wx.OK|wx.ICON_ERROR)
            self.Close()
            sys.exit(0)                 
        
    def setup_ui(self):
        self.menubar = wx.MenuBar()
        
        file_menu = wx.Menu()
        f_quit = file_menu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.Bind(wx.EVT_MENU, self.on_quit, f_quit)
        
        self.menubar.Append(file_menu, '&File')
        
        about_menu = wx.Menu()
        f_about = about_menu.Append(100, 'About', 'About this program')
        self.Bind(wx.EVT_MENU, self.about_func, id=100)
        self.menubar.Append(about_menu, '&About')
        
        self.SetMenuBar(self.menubar)
        
    def setup_sizers(self):
        self.panel = wx.Panel(self)
        self.notebook = NotebookTabs(self.panel)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.panel.SetSizer(self.sizer)
        self.sizer.Fit(self)
        self.Layout()
        
    def on_quit(self, event):
        self.Close()
        
    def about_func(self, event):
        info = wx.AboutDialogInfo()
        info.SetName(meta.__prog__)
        info.SetVersion(meta.__version__)
        info.SetDescription(meta.__doc__)
        info.SetLicense(meta.__license__)
        info.AddDeveloper(meta.__author__)
        
        wx.AboutBox(info)
        
        
def main():
    app = wx.App()
    MainWindow(None)
    app.MainLoop()
    
if __name__ == '__main__':
    main()