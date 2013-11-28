#Solarized Toggle

##Important Note!
Recently Package Control upgraded its control channel with the release of the new version. Using the old schema, Solarized Toggle was only compatible with ST2. I've updated the schema, but the kicker is that your plugin may not manually update. If it does not, simply uninstall the current version you have, and reinstall it from Package Control. Sorry for the inconvenience!

##Introduction
Solarized Toggle is a very simple plugin originally written to allow users of [Sublime Text 2][st2] and [Sublime Text 3][st3] to easily switch between light and dark versions of the Solarized color scheme.

Now any color scheme included with Sublime Text or installed separately can be used with a change to the plugin's settings file. The font settings can also be toggled between the differnt modes. You can also choose to use the built in theme switcher to toggle between two different themes at the same time.

Why use this plugin? Instead of having to manually click Preferences->Color Scheme->Some Colors, you can simply press F12 (CMD+F12 on OSX) in order to toggle between two themes. If you enable the theme switcher, you can also easily toggle between themes that compliment your color schemes.

Contribute to this code:
* Fork the project, write a patch, submit a pull request.
* Reporting issues or request features in the Issues tab.

##Installation
This plugin can be installed by using the [Package Control][packagecontrol] plugin, or manually.

###Package Control \(preferred\)
1. Install the [Package Control][packagecontrol] plugin if you haven't already.
2. Simply press CTRL-SHIFT-P from inside Sublime Text, then type PCI, and press enter. This will open the package installation browser.
3. Type 'Solarized Toggle' then press enter.

###Manual Installation
1. Download the [current version][currentVersion] of the plugin.

####Sublime Text 2
1. In Sublime Text 2, click Preferences->Browse Packages.
2. Unzip the file you downloaded into that directory.
3. Rename the folder you just unzipped to 'Solarized Toggle'.

####Sublime Text 3
1. In Sublime Text 3, click Preferences->Browse Packages.
2. Go up one level, then open the Installed Packages folder.
3. Copy the zip file you downloaded here, and rename it to 'Solarized Toggle.sublime-package'.


Congratulations. The plugin is now installed. Test it by pressing F12 a few times.

##Notes
* This plugin will overwrite the following settings in your Preferences.sublime-settings (USER) file:
  * color_scheme
  * font\_face, font\_size, font\_options, (if font switching is enabled)
  * theme (if theme switching is enabled)
* There is an issue with the theme switcher for both versions of Sublime Text where the window sometimes does not update the entire theme, leaving some artifacts of the previous theme behind. I currently believe this to be a limitation of Sublime Text itself. To fix the issue, simply resize or minimize/restore your window. This will cause the window to redraw itself with the new theme.

[st2]: http://www.sublimetext.com/ "Sublime Text 2"
[st3]: http://www.sublimetext.com/3 "Sublime Text 3"
[packagecontrol]: http://wbond.net/sublime_packages/package_control "Package Control"
[currentVersion]: https://github.com/damccull/sublimetext-SolarizedToggle/archive/1.4.7.zip "Current Version"
