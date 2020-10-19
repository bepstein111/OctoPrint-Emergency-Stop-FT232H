# OctoPrint-Emergency-Stop-FT232H

I'm attempting to make a Emergency Stop plugin that works with the FT232H module, specifically the Blinka V2 (USB-C version) sold by Adafruit, which is the one I happen to have on hand. The aim of the project is to enable OctoPrint users who aren't using Raspberry Pi's to use any button lying around as an Emergency Stop button. I have very little knowledge of how to create a plugin, and this is certainly not in a working state, let along finished. Right now, help/education about mistakes I've made or some pointers about how to actually trigger the GCode would be much appreciated!

Thanks for taking the time to take a look at my little project.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/bepstein111/OctoPrint-Emergency-Stop-FT232H/archive/master.zip

LINUX ONLY AT THE MOMENT

You're also going to need to follow the instructions at this link [here](https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h?view=all) in order to get dependencies set up correctly.

## Configuration

- Option to change GCode Command triggered (M112 by default)
- Ability to pick any available GPIO pin.