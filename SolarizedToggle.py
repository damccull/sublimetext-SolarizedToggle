import sublime
import sublime_plugin


class SolarizedToggle(sublime_plugin.ApplicationCommand):
    def flip(self, args, settings, what):
        current = settings.get(what)
        light = args["{}_light".format(what)]
        dark = args["{}_dark".format(what)]
        if current == dark:
            new = light
        else:
            new = dark
        settings.set(what, new)
        return None

    def run(self, **args):
        settings = sublime.load_settings("Preferences.sublime-settings")
        self.flip(args, settings, 'color_scheme')
        if args["flip_theme"]:
            self.flip(args, settings, 'theme')
        sublime.save_settings(settings)
