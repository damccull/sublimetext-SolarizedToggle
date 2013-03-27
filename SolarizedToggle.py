import sublime, sublime_plugin

class SolarizedToggle(sublime_plugin.ApplicationCommand):
	def run(self, **args):
		settingsFile = "Preferences.sublime-settings"
		schemeDay = args["color_sceme_day"]
		schemeNight = args["color_sceme_night"]

		settings = sublime.load_settings(settingsFile)
		current_scheme = settings.get("color_scheme")
		print("Current_scheme:" + str(current_scheme))
		new_scheme = schemeDay if current_scheme == schemeNight else schemeNight

		settings.set("color_scheme",new_scheme)
		sublime.save_settings(settingsFile)