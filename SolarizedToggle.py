import sublime
import sublime_plugin


class SolarizedToggle(object):
    def plugin_loaded_setup(self):
        self.global_settings = sublime.load_settings('Preferences.sublime-settings')
        self.plugin_settings_file = 'SolarizedToggle.sublime-settings'
        self.plugin_settings = sublime.load_settings(self.plugin_settings_file)
        self.state = self.plugin_settings.get('current_state')

    def _set(self, setting, state):
        new = self.plugin_settings.get("{}_{}".format(setting, state))
        self.global_settings.set(setting, new)

    def _flip_state(self):
        if self.state == 'dark':
            self.state = 'light'
        else:
            self.state = 'dark'
        self.plugin_settings.set('current_state', self.state)
        sublime.save_settings(self.plugin_settings_file)

    def flip(self):
        self._flip_state()
        self._set('color_scheme', self.state)
        if self.plugin_settings.get("flip_theme"):
            self._set('theme', self.state)
        self.update_view()

    def update_view(self, view=None):
        desired_scheme = (self.plugin_settings
                          .get("color_scheme_{}"
                          .format(self.state)))
        (sublime.active_window().active_view()
         .settings().set('color_scheme', desired_scheme))


class SolarizedToggleListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        _flipper.update_view(view)


class SolarizedToggleCommand(sublime_plugin.ApplicationCommand):
    def run(self, **args):
        _flipper.flip()


_flipper = SolarizedToggle()


def plugin_loaded():
    _flipper.plugin_loaded_setup()
