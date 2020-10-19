# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import octoprint.plugin
import board
import digitalio



class EmergencyStopFT232HPlugin(octoprint.plugin.StartupPlugin,
                                octoprint.plugin.SettingsPlugin,
                                octoprint.plugin.TemplatePlugin):

    def on_after_startup(self):
        self._logger.info("Emergency Stop - FT232H is running")
        if (self.estopCommand != "M112"):
		    self._logger.warn("WARNING! EMERGENCY STOP COMMAND HAS BEEN CHANGED FROM DEFAULT \"M112\" TO \"" + self.emergencyGCODE + "\"")
    def get_settings_defaults(self):
		return dict(
			emergencyGCODE="M112",
			stop_button=D5
		)
    def get_template_configs(self):
		return [
			dict(type="settings", name="Emergency Stop - FT232H", template="emergencystopft232h_settings.jinja2", custom_bindings=False)
			]

    def read_button(self):
        button = digitalio.DigitalInOut(board.+self.stop_button)
        button.direction = digitalio.Direction.INPUT
        return[button.value]




	# Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			simpleemergencystop=dict(
				displayName="Emergency Stop - FT232H",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="bepstein111",
				repo="OctoPrint-Emergency Stop - FT232H",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/bepstein111/OctoPrint-EmergencyStop-FT232H/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Emergency Stop - FT232H"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Allows one to use a button connected to a FT232H board as an E-Stop"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = EmergencyStopFT232HPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}



