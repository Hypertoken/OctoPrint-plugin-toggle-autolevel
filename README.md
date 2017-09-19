# OctoPrint-plugin-toggle-autolevel
An OctoPrint plugin to allow G29 commands (auto-leveling) to be commented out.

## Suitability
Although this plugin was created specifically for the Robo C2/R2 printers, it will work as well with other brands/models.

### Caveat
If you're *not* running **roboOctoPrint** (**roboOS**), then you'll want to substitute below during the installation instructions. Instead of changing to the `cd ~/oprint/lib/python2.7/site-packages/octoprint/plugins` folder, use the usual `~/.octoprint/plugins` folder.

## Overview
Many people are happy with an autoleveling routine at the startup of each print job. There are times, though, where you'd instead like to manually level the printer and stop doing autoleveling all the time since it can cause more troubles.

## Problem

Once you've made that commitment, however, you then might need to go back, edit your slicer's startup GCODE and re-slice all of your STL files to remove that G29 autoleveling command from those GCODE files. But that's a hassle. Which files have it and which files don't?

## Solution

This plugin should alleviate that by making OctoPrint just comment out the G29 command when it sees it (simple enough). And it's also easy to toggle autoleveling back on by using *Settings -> Plugin Manager -> Toggle Autolevel -> Disable* then restart OctoPrint.

## Installation
The installation should be straightforward enough since it's a single Python script:

1. Turn on the printer
2. In a terminal prompt on your workstation, remote into your printer by using `ssh` or `putty` as either version below (use your own printer's serial number as the hostname):
	* $ `ssh pi@charming-pascal.local` # pw = raspberry
	* $ `ssh pi@printer-ip-address`
3. $&nbsp;`cd ~/oprint/lib/python2.7/site-packages/octoprint/plugins` # If not on the Robo C2/R2, see caveat above
4. $&nbsp;`curl -o ToggleAutolevel.py https://raw.githubusercontent.com/OutsourcedGuru/OctoPrint-plugin-toggle-autolevel/master/ToggleAutolevel.py`
5. $ `exit`
6. In your workstation's browser, visit the OctoPrint interface, for example: `http://charming-pascal.local`
7. *System -> Restart OctoPrint*
8. *Settings -> Plugin Manager* and verify that *Toggle Autolevel* is now listed
9. Save
10. In the *Printer Terminal* section, click its header to open it up and enter a `G29` code, looking for a commented-out `;G29` to be sent to the printer
11. You'd confirmed that the plugin is now installed and enabled

![toggleautolevel-in-action](https://user-images.githubusercontent.com/15971213/30572061-5d52981e-9ca0-11e7-8d27-eea280d6af3a.png)

## Removing the plugin
Removing the plugin is also easy. Under *Settings -> Plugin Manager -> Toggle Autolevel*, click the *Disable* icon and allow OctoPrint to restart. Remote into your Robo printer as you did before with `ssh` and enter the following command to remove the Python script: $&nbsp;`rm ~/oprint/lib/python2.7/site-packages/octoprint/plugins/ToggleAutolevel.py`. Finally, restart OctoPrint again and verify that it's now missing from the list of plugins.

### Non-Robo version

For those *not* on a Robo printer, run the following command instead to delete the Python script: $&nbsp;`rm ~/.octoprint/plugins/ToggleAutolevel.py`.