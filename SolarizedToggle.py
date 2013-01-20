import sublime, sublime_plugin

class SolarizedToggle(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		schemeDay = args["color_sceme_day"]
		schemeNight = args["color_sceme_night"]

		current_scheme = self.view.settings().get("color_scheme")

		new_scheme = schemeDay if current_scheme == schemeNight else schemeNight
		self.view.settings().set("color_scheme",new_scheme)