# T7-Sublime

T7-Sublime is an enhanced syntax-highlighting package for (almost) all Call of Duty Black Ops III developer file formats.

## About

The Call of Duty developers included in the Black Ops III mod tools documentation a Sublime package for the GSC scripting language. The package provides some basic syntax highlighting as well as auto-completions for many of the Black Ops III engine functions. However, since the package is partial and does not remotely exhaust the set of possible features that could be provided for the GSC language (as well as the lack of any support for other Call of Duty developer file formats), this project was created to provide a level of support that more closely resembles complete.

The key improvements in this package compared to the developer package follow:
1. The syntax highlighting is more detailed.
2. More auto-completions are supported for a multitude of contexts.
3. Syntaxes other than GSC are also supported.

## Supported Grammars

- GSC
- Zone Source
- Localized Strings
- FX
- Vision
- Sound Alias Table
- Sound Reverb Table
- Sound Ambient Table
- Animtree
- Anim Selector Table
- Anim Mapping Table
- Player Anim Script
- Tech Set Def

## Installation

If you want to make changes to these packages and test them locally, fork this repository and then symlink the changed packages into your *Packages* folder.

### OS X

```bash
$ git clone https://github.com/Jake-NotTheMuss/CoDT7-Sublime.git
$ ln -s `pwd`/CoDT7\ Formats ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
```

### Linux

```bash
$ git clone https://github.com/Jake-NotTheMuss/CoDT7-Sublime.git
$ ln -s `pwd`/CoDT7\ Formats ~/.config/sublime-text-3/Packages/
```

### Windows

On Windows, you can use directory junctions instead of symlinks (symlinks require administrative rights; directory junctions don't):

```powershell
# Using PowerShell
PS> git clone https://github.com/Jake-NotTheMuss/CoDT7-Sublime.git
PS> cmd /c mklink /J "$env:APPDATA/Sublime Text 3/Packages/CoDT7 Formats" (convert-path "./CoDT7 Formats")
```

## Initialization

Once the package is installed, the user can initialize some default syntax settings that will be used by various modules in the package. This can be done by selecting File > CoDT7 > Initialize Settings in the menu bar. This will invoke a command defined in the module initialize_settings.py and as a result, various syntax-specific settings files will be generated in the User directory of the application's data folder.

---