# coding=utf-8

import octoprint.plugin
__plugin_pythoncompat__ = ">=2.7,<4"
class ToggleAutolevelPlugin(octoprint.plugin.OctoPrintPlugin):
	def rewrite_g29(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
		if gcode and gcode == "G29":
			cmd = ";G29"
		return cmd,

	def sent_g29(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
		if gcode and gcode == ";G29":
			self._logger.info("Just commented G29: {cmd}".format(**locals()))

__plugin_name__ = "Toggle Autolevel"
def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = ToggleAutolevelPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.comm.protocol.gcode.queuing": __plugin_implementation__.rewrite_g29,
		"octoprint.comm.protocol.gcode.sent": __plugin_implementation__.sent_g29
	}

