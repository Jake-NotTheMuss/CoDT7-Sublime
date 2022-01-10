import sublime, sublime_plugin
import os

# Common settings to set for syntaxes of particular scopes
common_settings = {
    'text.codt7': { 'word_wrap': False },
    'source.codt7': {},
    'text.codt7.table': { 'show_definitions': True },
    'text.codt7.table.sound': { 'check_syntax_column_order': True }
}

# Syntax specific settings, listed in the order they were added to the package
# Settings here can override the same settings from the common_settings dict
codt7_syntax_settings = {
    # GSC
    'source.codt7.gsc': {},
    # ZONE SOURCE
    'text.codt7.table.zone.source': {},
    # ZONE DEPS
    'text.codt7.table.zone.deps': {},
    # LOCALIZED STRINGS
    'text.codt7.localizedstrings': {},
    # FX
    'source.codt7.fx': {},
    # VISION
    'text.codt7.vision': {},
    # XASSET
    'text.codt7.xasset': {},
    # SOUND ALIAS
    'text.codt7.table.sound.alias': {},
    # SOUND REVERB
    'text.codt7.table.sound.reverb': {},
    # SOUND T5 ALIAS
    'text.codt7.table.sound.t5alias': {},
    # SOUND T5 REVERB
    'text.codt7.table.sound.t5reverb': {},
    # SOUND AMBIENT
    'text.codt7.table.sound.ambient': {},
    # MAP FILE
    'source.codt7.map': {},
    # LENSFLARE
    'source.codt7.lensflare': {},
    # ANIMTREE
    'source.codt7.animtree': {},
    # ANIM SELECTOR TABLE
    'text.codt7.table.anim.selector': {},
    # ANIM MAPPING TABLE
    'text.codt7.table.anim.mapping': {},
    # PLAYER ANIM SCRIPT
    'source.codt7.playeranimscript': {},
    # TECH SET DEF
    'source.codt7.techsetdef': {}
}

# sublime api returns a list of syntaxes from a scope
# but only 1 syntax should match the scope, so this
# function returns just the one match or None
def get_syntax_from_scope(scope):
    for syntax in sublime.list_syntaxes():
        if syntax.scope == scope:
            return syntax
    return None

def get_settings_file_name_from_scope(scope):
    syntax = get_syntax_from_scope(scope)
    assert syntax is not None
    syntax_name = os.path.splitext(os.path.basename(syntax.path))[0]
    return syntax_name + '.sublime-settings'

# some codt7 files are of existing grammars
# but have unrecognized extensions, e.g.
# xcam_export, mus, ai_bt which are all JSON
def add_codt7_extensions_in_settings():
    new_extensions = {
        'source.json': ['xcam_export', 'szc', 'ctx', 'duk', 'ai_bt', 'ai_bsm', 'ai_asm', 'mus']
    }
    for scope in new_extensions:
        settings_name = get_settings_file_name_from_scope(scope)
        settings = sublime.load_settings(settings_name)
        current_extensions = settings.get('extensions')
        if current_extensions is None:
            current_extensions = []
        current_extensions += new_extensions.get(scope)
        current_extensions = list(set(current_extensions))
        settings.set('extensions', current_extensions)
        sublime.save_settings(settings_name)

class InitializeCodt7SyntaxSettingsCommand(sublime_plugin.WindowCommand):
    def run(self):
        for scope in codt7_syntax_settings:
            # get any common settings to load first
            syntax_settings = {}
            for base_scope in common_settings:
                # scope root match
                settings_to_add = common_settings.get(base_scope)
                assert isinstance(settings_to_add, dict)
                if base_scope in scope:
                    # merge settings
                    syntax_settings.update(settings_to_add)

            # merge syntax specific settings
            syntax_specific_settings = codt7_syntax_settings.get(scope)
            syntax_settings.update(syntax_specific_settings)

            # No settings to initialize
            if len(syntax_settings) == 0:
                continue

            # get settings file name from scope
            settings_name = get_settings_file_name_from_scope(scope)

            # load existing settings
            settings = sublime.load_settings(settings_name)

            # override settings
            for key in syntax_settings:
                settings.set(key, syntax_settings.get(key))

            # flush settings
            sublime.save_settings(settings_name)

        add_codt7_extensions_in_settings()
