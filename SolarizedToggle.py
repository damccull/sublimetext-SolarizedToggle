import sublime
import sublime_plugin
import os.path


class SolarizedToggle(object):
    def do_setup(self):
        self.global_settings_file = 'Preferences.sublime-settings'
        self.global_settings = sublime.load_settings(self.global_settings_file)
        self.plugin_settings_file = 'SolarizedToggle.sublime-settings'
        self.plugin_settings = sublime.load_settings(self.plugin_settings_file)

    def set_color_scheme(self):
        current_scheme = self.global_settings.get("color_scheme")
        light_scheme = self.plugin_settings.get("color_scheme_light")
        dark_scheme = self.plugin_settings.get("color_scheme_dark")
        new_scheme = light_scheme if current_scheme == dark_scheme else dark_scheme

        self.global_settings.set("color_scheme", new_scheme)
        sublime.save_settings(self.global_settings_file)

_toggler = SolarizedToggle()

class SolarizedToggleCommand(sublime_plugin.ApplicationCommand):
    def run(self, **args):
        _toggler.set_color_scheme()

def plugin_loaded():
    _toggler.do_setup()
