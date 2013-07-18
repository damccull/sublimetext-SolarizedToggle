import sublime
import sublime_plugin

class SolarizedToggle(object):
    def do_setup(self):
        self.global_settings_file = 'Preferences.sublime-settings'
        self.global_settings = sublime.load_settings(self.global_settings_file)
        self.plugin_settings_file = 'SolarizedToggle.sublime-settings'
        self.plugin_settings = sublime.load_settings(self.plugin_settings_file)

    def update_mode(self):
        self.current_mode = self.plugin_settings.get("solarized_toggle_mode")
        if (self.current_mode == "dark"):
            new_mode = "light"
        elif (self.current_mode == "light"):
            new_mode = "dark"
        else:
            self.current_mode = "light"
            new_mode = "dark"
        self.plugin_settings.set("solarized_toggle_mode", new_mode)
        sublime.save_settings(self.plugin_settings_file)

    def set_color_scheme(self):
        light_scheme = self.plugin_settings.get("color_scheme_light")
        dark_scheme = self.plugin_settings.get("color_scheme_dark")
        new_scheme = light_scheme if self.current_mode == "dark" else dark_scheme

        self.global_settings.set("color_scheme", new_scheme)
        sublime.save_settings(self.global_settings_file)

    def set_theme(self):
        light_theme = self.plugin_settings.get("theme_light")
        dark_theme = self.plugin_settings.get("theme_dark")
        if (light_theme is not None and dark_theme is not None):
            new_theme = light_theme if self.current_mode == "dark" else dark_theme

            self.global_settings.set("theme", new_theme)
            sublime.save_settings(self.global_settings_file)

class SolarizedToggleCommand(sublime_plugin.ApplicationCommand):
    def run(self, **args):
        _toggler.update_mode()
        _toggler.set_theme()
        _toggler.set_color_scheme()

def plugin_loaded():
    _toggler.do_setup()


_toggler = SolarizedToggle()
_st_version = 2

# This technique copied from wbond's Package Control
if int(sublime.version()) > 3000:
    _st_version = 3

if _st_version == 2:
    plugin_loaded()
