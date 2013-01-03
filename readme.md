# One Click Deploy

## Introduction

This is a tool meant to help FRC teams easily download their C++ code from their repository, 
compile it, and deploy it to the robot. This tool is meant to assist those who don't know
much about using WindRiver/mucking around with IP Addresses.

Warning: This is in alpha stage, and hasn't been throughly tested yet. Use with caution.

### Features

-   Automatically download the latest version of your code from an SVN repository, compile
    it, and deploy it to the robot
-   Can reset your IP addresses so you can reconnect back to the internet.

### Limitations

-   Works only in Windows
-   Only works with C++ code
-   WindRiver must be installed on the computer the program is running in
-   Currently can only download code from SVN repositories.
-   Your source code must contain a file called `.wrmakefile` in order for it to be
    compilable.


## Usage

### Gui

For a simplified guide, see <easy_instructions.docx>.

You must open the gui in admistrative mode (right-click the program, and click 
"**Run as administator**"). 

There are two tabs: "**Options**" and "**Go!**". The options pane has the following options, and
must be configured before running the program.

**Team Number:**
:   Your team number
    
**Robot Network Name:**
:   The SSID of the router attached to the robot
    
**Source Code Url:**
:   The location of your source code repository (SVN repos only). For example,
    
        <http://my-team-name.googlecoe.com/svn/trunk/2012_code>
    
**Source Code Revision:**
:   The revision of your source code to download. Specify "LATEST" to download the latest
    revision
    
**WindRiver Install Dir:**
:   The folder WindRiver is installed in.
    
**Wireless Adapter:**
:   Your wireless adapter, if you want to connect to the robot wirelessly. Leave as 'None' if you
    want the program to leave it alone.
    
**Ethernet Adapter:**
:   The same thing, except for Ethernet.
    
Don't forget to hit "**Apply**" to set the options.

* * *

Under the "**Go!**" tab, you have three options.

**DEPLOY:**

1.  Downloads the code specified at "Source Code Revision" to the current working directory 
    inside a folder called "source". If the folder already exists, this step is skipped.
2.  Compiles the code
3.  Sets the adapters specified in the options tab to connect to your robot. This will
    disable access to the internet.
4.  Connects to the robot
5.  Deploys the code via FTP. You will need to reboot the robot at this step.
       
**Download Code From Repository:**

1.  Downloads the code specified at "Source Code Revision" to the current working directory
    inside a folder called "source". If the folder already exists, it is deleted and
    overwritten.
    
**Restore Internet:**

1.  Resets your adapters so you can connect to the internet.
    
### Command Line

The command line interface currently does not work for the exe, but does work for the python
files. This is less polished then the gui interface, and may have bugs or errors. You can find
more information by typing the below in the command line:

    python one-click-deploy.pyw --help


## Misc

Author: 
:   Michael Lee

Version: 
:   January 2, 2012 (version 4)

License: 
:   MIT License

Repository: 
:   http://github.com/Michael0x2a/one-click-deploy
