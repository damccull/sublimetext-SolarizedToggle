import sublime
import sublime_plugin
import os.path


class SolarizedToggle(sublime_plugin.ApplicationCommand):

    def set_color_scheme(self, scheme_type, settings):
        default_light = "Packages/Color Scheme - Default/Solarized (Light).tmTheme"
        default_dark = "Packages/Color Scheme - Default/Solarized (Dark).tmTheme"
        color_scheme_light = "Packages/Solarized Color Scheme/Solarized (light).tmTheme"
        color_scheme_dark = "Packages/Solarized Color Scheme/Solarized (dark).tmTheme"

        current_scheme = settings.get("color_scheme")
        new_scheme = "light" if "dark" in current_scheme.lower() else "dark"

        if scheme_type == "color":
            if new_scheme == "light":
                settings.set("color_scheme", color_scheme_light)
            else:
                settings.set("color_scheme", color_scheme_dark)
        else:
            if new_scheme == "light":
                settings.set("color_scheme", default_light)
            else:
                settings.set("color_scheme", default_dark)

    def run(self, **args):
        settingsFile = "Preferences.sublime-settings"
        settings = sublime.load_settings(settingsFile)

        sublime2_path = sublime.packages_path() + "/Solarized Color Scheme"
        sublime3_path = (sublime.installed_packages_path() +
                            "/Solarized Color Scheme.sublime-package")

        if os.path.exists(sublime2_path) or os.path.exists(sublime3_path):
            self.set_color_scheme("color", settings)
        else:
            self.set_color_scheme("default", settings)

        sublime.save_settings(settingsFile)
