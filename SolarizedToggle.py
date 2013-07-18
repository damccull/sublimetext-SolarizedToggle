import sublime
import sublime_plugin

class SolarizedToggle(object):
    def do_setup(self):
        # Setup our settings objects and settings files
        self.global_settings_file = 'Preferences.sublime-settings'
        self.global_settings = sublime.load_settings(self.global_settings_file)
        self.plugin_settings_file = 'SolarizedToggle.sublime-settings'
        self.plugin_settings = sublime.load_settings(self.plugin_settings_file)

    def update_mode(self):
        # Get current mode from plugin_settings
        self.current_mode = self.plugin_settings.get("solarized_toggle_mode")

        # Update current mode based on current mode
        if (self.current_mode == "dark"):
            new_mode = "light"
        elif (self.current_mode == "light"):
            new_mode = "dark"
        else: # If no current mode exists (if first run), set it to light
            self.current_mode = "light"
            new_mode = "light"
        # Set the mode in the plugin_settings, then save to settings file
        self.plugin_settings.set("solarized_toggle_mode", new_mode)
        sublime.save_settings(self.plugin_settings_file)

    def set_color_scheme(self):
        # Get the color schemes we want to switch between from the plugin_settings
        light_scheme = self.plugin_settings.get("color_scheme_light")
        dark_scheme = self.plugin_settings.get("color_scheme_dark")
        # Decide on which scheme to use based on current mode
        new_scheme = light_scheme if self.current_mode == "dark" else dark_scheme

        # Set the color scheme in global_settings and save the global settings file
        self.global_settings.set("color_scheme", new_scheme)
        sublime.save_settings(self.global_settings_file)

    def set_theme(self):
        # First get status of theme switching setting from plugin_settings
        themes_enabled = self.plugin_settings.get("enable_theme_switching")

        if (themes_enabled): # If switching is enabled...
            # Get the two themes to toggle between from plugin_settings
            light_theme = self.plugin_settings.get("theme_light")
            dark_theme = self.plugin_settings.get("theme_dark")
            # Decide on which theme to use based on current mode
            new_theme = light_theme if self.current_mode == "dark" else dark_theme

            # Set the theme in global_settings and save to global settings file
            self.global_settings.set("theme", new_theme)
            sublime.save_settings(self.global_settings_file)

class SolarizedToggleCommand(sublime_plugin.ApplicationCommand):
    def run(self, **args): # Called every time hotkey pressed
        # Toggle the current mode
        _toggler.update_mode()
        # Set the new theme
        _toggler.set_theme()
        # Set the new color scheme
        _toggler.set_color_scheme()

def plugin_loaded(): # Called automatically in ST3 only.
    # Run initial setup
    _toggler.do_setup()

# Create a SolarizedToggle object
_toggler = SolarizedToggle()
# Assume plugin is running on ST2
_st_version = 2

# This technique copied from wbond's Package Control
if int(sublime.version()) > 3000:
    # If we're running on ST3, set the verson to that
    _st_version = 3

if _st_version == 2:
    # If this is ST2, manually invoke plugin_loaded to do initial setup
    plugin_loaded()
