import sublime, sublime_plugin

from . import codt7_table

DEBUG = False

if DEBUG:
    def debug(*args):
        print(*args)
else:
    def debug(*args):
        return

# these match the order of their corresponding syntax files
# From Packages/CoDT7 Formats/SoundAliasTable.sublime-syntax
sound_alias_fields = {
    'name': 0,
    'behavior': 1,
    'storage': 2,
    'filespec': 3,
    'filespecsustain': 4,
    'filespecrelease': 5,
    'template': 6,
    'loadspec': 7,
    'secondary': 8,
    'sustainalias': 9,
    'releasealias': 10,
    'bus': 11,
    'volumegroup': 12,
    'duckgroup': 13,
    'duck': 14,
    'reverbsend': 15,
    'centersend': 16,
    'volmin': 17,
    'volmax': 18,
    'distmin': 19,
    'distmaxdry': 20,
    'distmaxwet': 21,
    'drymincurve': 22,
    'drymaxcurve': 23,
    'wetmincurve': 24,
    'wetmaxcurve': 25,
    'limitcount': 26,
    'limittype': 27,
    'entitylimitcount': 28,
    'entitylimittype': 29,
    'pitchmin': 30,
    'pitchmax': 31,
    'prioritymin': 32,
    'prioritymax': 33,
    'prioritythresholdmin': 34,
    'prioritythresholdmax': 35,
    'amplitudepriority': 36,
    'pantype': 37,
    'pan': 38,
    'futz': 39,
    'looping': 40,
    'randomizetype': 41,
    'probability': 42,
    'startdelay': 43,
    'envelopmin': 44,
    'envelopmax': 45,
    'enveloppercent': 46,
    'occlusionlevel': 47,
    'isbig': 48,
    'distancelpf': 49,
    'fluxtype': 50,
    'fluxtime': 51,
    'subtitle': 52,
    'doppler': 53,
    'contexttype': 54,
    'contextvalue': 55,
    'contexttype1': 56,
    'contextvalue1': 57,
    'contexttype2': 58,
    'contextvalue2': 59,
    'contexttype3': 60,
    'contextvalue3': 61,
    'timescale': 62,
    'ismusic': 63,
    'iscinematic': 64,
    'fadein': 65,
    'fadeout': 66,
    'pauseable': 67,
    'stoponentdeath': 68,
    'compression': 69,
    'stoponplay': 70,
    'dopplerscale': 71,
    'futzpatch': 72,
    'voicelimit': 73,
    'ignoremaxdist': 74,
    'neverplaytwice': 75,
    'continuouspan': 76,
    'filesource': 77,
    'filesourcesustain': 78,
    'filesourcerelease': 79,
    'filetarget': 80,
    'filetargetsustain': 81,
    'filetargetrelease': 82,
    'platform': 83,
    'language': 84,
    'outputdevices': 85,
    'platformmask': 86,
    'wiiumono': 87,
    'stopalias': 88,
    'distancelpfmin': 89,
    'distancelpfmax': 90,
    'facialanimationname': 91,
    'restartcontextloops': 92,
    'silentincpz': 93,
    'contextfailsafe': 94,
    'gpad': 95,
    'gpadonly': 96,
    'mutevoice': 97,
    'mutemusic': 98,
    'rowsourcefilename': 99,
    'rowsourceshortname': 100,
    'rowsourcelinenumber': 101
}
# From Packages/CoDT7 Formats/SoundReverbTable.sublime-syntax
sound_reverb_fields = {
    'name': 0,
    'loadspec': 1,
    'masterreturn': 2,
    'earlyinputlpf': 3,
    'earlyfeedback': 4,
    'earlysmear': 5,
    'earlybasedelayms': 6,
    'earlypredelayms': 7,
    'earlyreturn': 8,
    'nearinputlpf': 9,
    'nearfeedback': 10,
    'nearreturn': 11,
    'nearlowdamp': 12,
    'nearhighdamp': 13,
    'neardecaytime': 14,
    'nearsmear': 15,
    'nearpredelayms': 16,
    'farinputlpf': 17,
    'farfeedback': 18,
    'farreturn': 19,
    'farlowdamp': 20,
    'farhighdamp': 21,
    'fardecaytime': 22,
    'farsmear': 23,
    'farpredelayms': 24
}
# From Packages/CoDT7 Formats/SoundT5AliasTable.sublime-syntax
sound_t5alias_fields = {
    'name': 0,
    'file': 1,
    'template': 2,
    'loadspec': 3,
    'secondary': 4,
    'group': 5,
    'vol_min': 6,
    'vol_max': 7,
    'team_vol_mod': 8,
    'dist_min': 9,
    'dist_max': 10,
    'dist_reverb_max': 11,
    'volume_falloff_curve': 12,
    'reverb_falloff_curve': 13,
    'volume_min_falloff_curve': 14,
    'reverb_min_falloff_curve': 15,
    'limit_count': 16,
    'limit_type': 17,
    'entity_limit_count': 18,
    'entity_limit_type': 19,
    'pitch_min': 20,
    'pitch_max': 21,
    'team_pitch_mod': 22,
    'min_priority': 23,
    'max_priority': 24,
    'min_priority_threshold': 25,
    'max_priority_threshold': 26,
    'spatialized': 27,
    'type': 28,
    'loop': 29,
    'randomize_type': 30,
    'probability': 31,
    'start_delay': 32,
    'reverb_send': 33,
    'duck': 34,
    'pan': 35,
    'center_send': 36,
    'envelop_min': 37,
    'envelop_max': 38,
    'envelop_percentage': 39,
    'occlusion_level': 40,
    'occlusion_wet_dry': 41,
    'is_big': 42,
    'distance_lpf': 43,
    'move_type': 44,
    'move_time': 45,
    'real_delay': 46,
    'subtitle': 47,
    'mature': 48,
    'doppler': 49,
    'futz': 50,
    'context_type': 51,
    'context_value': 52,
    'compression': 53,
    'timescale': 54,
    'music': 55,
    'fade_in': 56,
    'fade_out': 57,
    'pc_format': 58,
    'pause': 59,
    'stop_on_death': 60,
    'bus': 61,
    'snapshot': 62,
    'voice_limit': 63,
    'file_xenon': 64,
    'file_size_xenon': 65,
    'file_ps3': 66,
    'file_size_ps3': 67,
    'file_pc': 68,
    'file_size_pc': 69,
    'file_wii': 70,
    'file_size_wii': 71,
    'source_csv': 72,
    'language': 73
}
# From Packages/CoDT7 Formats/SoundT5ReverbTable.sublime-syntax
sound_t5reverb_fields = {
    'name': 0,
    'room': 1,
    'roomhf': 2,
    'roomrollofffactor': 3,
    'decaytime': 4,
    'decayhfratio': 5,
    'reflections': 6,
    'reflectionsdelay': 7,
    'reverb': 8,
    'reverbdelay': 9,
    'diffusion': 10,
    'density': 11,
    'hfreference': 12
}
# From Packages/CoDT7 Formats/SoundAmbientTable.sublime-syntax
sound_ambient_fields = {
    'name': 0,
    'loadspec': 1,
    'defaultroom': 2,
    'reverb': 3,
    'nearverb': 4,
    'farverb': 5,
    'reverbdrylevel': 6,
    'reverbwetlevel': 7,
    'entitycontexttype0': 8,
    'entitycontextvalue0': 9,
    'entitycontexttype1': 10,
    'entitycontextvalue1': 11,
    'entitycontexttype2': 12,
    'entitycontextvalue2': 13,
    'globalcontexttype': 14,
    'globalcontextvalue': 15,
    'loop': 16,
    'duck': 17
}
# From Packages/CoDT7 Formats/SoundTestTable.sublime-syntax
sound_test_fields = {
    'name': 0,
    'test_filename': 1,
    'test_level': 2,
    'test_type': 3,
    'test_global_id': 4,
    'test_secondary_id': 5
}

def is_commented(line):
    line = line.lstrip()
    if not line:
        return False
    return line[0] == '#'

def is_empty(line):
    return not line.strip()

# <get_field_names> gets a list of column names for the table and
# also returns the index of the line from which the names were read
def get_field_names(view):
    line = view.line(0)
    pos = line.size() + 1
    line_index = 0
    # skip commented/empty lines
    while is_commented(view.substr(line)) or is_empty(view.substr(line)):
        line = view.line(pos)
        pos += line.size() + 1
        line_index += 1

    return view.substr(line).split(','), line_index

# returns information about missing/unexpected fields in a file
# param <field_names>        - the list of field names from the file
# param <expected_fields> - a dict of expected field names to their
#                              expected column position
# return <missing_fields>    - list of indices of fields which are
#                              expected but missing
# return <unexpected_fields> - list of indices of unexpected fields
def get_field_information(field_names, expected_fields):
    # get a dictionary from field_names
    # and look for any unexpected fields
    dict_field_names = {}
    unexpected_fields = {}
    for i in range(len(field_names)):
        name = field_names[i].strip().lower()
        dict_field_names[name] = i
        expected_index = expected_fields.get(name)
        if expected_index is None:
            unexpected_fields[i] = True

    missing_fields = {}

    for name in expected_fields:
        exists = dict_field_names.get(name) is not None
        if not exists:
            missing_fields[expected_fields[name]] = True

    return missing_fields, unexpected_fields

# <get_sort_order> creates a map between the current position
# of a table's columns and the position they should be moved to
# the key is the current position, the value is the new position
# param <field_names> - the file's column order
# param <expected_fields> - the expected column order
def get_sort_order(field_names, expected_fields, missing_fields, unexpected_fields):
    num_missing_fields = len(missing_fields)
    num_unexpected_fields = len(unexpected_fields)
    num_fields = len(field_names)
    num_expected_fields = len(expected_fields)

    expected_len = num_expected_fields + num_unexpected_fields
    padding_amount = expected_len - num_fields

    sort_order = [None] * expected_len

    missing_counter = 0
    unexpected_counter = 1

    for i in range(expected_len):
        if missing_fields.get(i) == True:
            sort_order[i] = num_fields + missing_counter
            missing_counter += 1

        if i >= num_fields:
            continue

        if unexpected_fields.get(i) == True:
            sort_order[expected_len - unexpected_counter] = i
            unexpected_counter += 1
            continue

        name = field_names[i].strip().lower()
        index = expected_fields.get(name)
        if index is not None:
            sort_order[index] = i
        else:
            print("Error generating sort order for table in table_column_order.py")
            return []


    return sort_order

# <compare_column_order> checks that the two column orders given match each other
# param <field_names>         - list of column names of the actual file
# param <expected_fields> - table of column names to positions describing the correct order
# <field_names> only needs to match <expected_fields> for its own length; it does not need
# to have every column that <expected_fields> has
def compare_column_order(field_names, expected_fields):
    # loop through the file's column names
    for i in range(min(len(field_names), len(expected_fields))):
        name = field_names[i].strip().lower()
        index = expected_fields.get(name)
        if index is not None:
            # the columns names are not at matching positions
            if index != i:
                debug('column mismatch:',
                      field_names[i].strip(),
                      field_names[index]
                        if index < len(field_names)
                        else '<missing column>')
                return True
        # the column name is not recognized
        else:
            # No mismatch but there is a column with an unknown name
            debug('unknown column name:',
                  field_names[i].strip())
            return True

    return False

def compare_alias_column_order(field_names):
    return compare_column_order(field_names, sound_alias_fields)

def compare_reverb_column_order(field_names):
    return compare_column_order(field_names, sound_reverb_fields)

def compare_t5alias_column_order(field_names):
    return compare_column_order(field_names, sound_t5alias_fields)

def compare_t5reverb_column_order(field_names):
    return compare_column_order(field_names, sound_t5reverb_fields)

def compare_ambient_column_order(field_names):
    return compare_column_order(field_names, sound_ambient_fields)

def compare_test_column_order(field_names):
    return compare_column_order(field_names, sound_test_fields)

column_order_compare_funcs = {
    'text.codt7.table.sound.alias': compare_alias_column_order,
    'text.codt7.table.sound.reverb': compare_reverb_column_order,
    'text.codt7.table.sound.t5alias': compare_t5alias_column_order,
    'text.codt7.table.sound.t5reverb': compare_t5reverb_column_order,
    'text.codt7.table.sound.ambient': compare_ambient_column_order,
    'text.codt7.table.sound.test': compare_test_column_order
}

# <reorder_columns_for_line> will sort the columns of the line given
# based on a desired order given by param <dict_order_map>
# param <view>        - handle to current view
# param <edit>        - handle to buffer used by view
# param <line>        - region covering the line
# param <is_header>   - whether the line is the header row of the table
# param <dict_order_map>   - table mapping current column positions to their new positions
# param <field_names>  - list of column name strings from file's header row
# param <expected_fields> - table mapping column names to their expected positions
def reorder_columns_for_line(view,
                             edit,
                             line,
                             is_header,
                             n_unexpected_fields,
                             sort_order,
                             field_names,
                             expected_fields):
    # get string from the region covering the line
    str_line = view.substr(line)

    # line is empty, return 1 to advance the newline
    if not str_line.strip():
        debug('Nothing to be done for empty row')
        return (len(str_line) + 1)

    # line is commented with a '#'
    if is_commented(str_line):
        debug('Nothing to be done for commented row')
        return (len(str_line) + 1)

    debug('Row before reordering:', str_line)
    debug('Row length before reordering:', len(str_line))

    # get array of the comma-separated values in the row
    field_values = str_line.split(',')

    # get number of columns
    n_fields = len(field_values)

    # columns might be missing, get the required padding amount
    padding = len(expected_fields) + n_unexpected_fields - n_fields

    # pad the list if needed
    if padding > 0:
        debug('Padding row with', padding, 'columns')
        field_values += [''] * padding
 
    new_field_values = [None] * len(field_values)

    for i in range(len(sort_order)):
        old_index = sort_order[i]
        new_field_values[i] = field_values[old_index]

    field_values = new_field_values

    #fill in missing column names in header
    if is_header:
        debug('Adding missing field names in header')
        casing_type = codt7_table.get_casing_type(field_values)
        if codt7_table.cased_field_names_supported():
            for i in range(min(len(expected_fields), len(field_values))):
                if not field_values[i].strip():
                    new_value = codt7_table.get_field_name_with_casing_type(i, casing_type)
                    field_values[i] = new_value
        else:
            # get the field names as a list in the expected order
            field_names = sorted(list(expected_fields.keys()),
                                 key=lambda x:expected_fields[x])
            is_capitalized = casing_type == codt7_table.CASE_CAPITALIZED \
                             or casing_type == codt7_table.CASE_CAMEL_UPPER
            for i in range(min(len(expected_fields), len(field_values))):
                if not field_values[i].strip():
                    if is_capitalized:
                        field_values[i] = field_names[i][0].upper() \
                                           + field_names[i][1:]
                    else:
                        field_values[i] = field_names[i]

    # get new string from column list
    str_reordered_line = ','.join(field_values)

    debug('Row after reordering:', str_reordered_line)
    debug('Row length after reordering:', len(str_reordered_line))

    # replace line in buffer
    view.replace(edit, line, str_reordered_line)

    # return the new length to advance by
    return (len(str_reordered_line) + 1)

# <reorder_columns> will edit the current file to match the column order
# of its syntax definition
# param <expected_fields> is a table of column names to indices
# which describes the column order that the table should be in
def reorder_columns(view, edit, expected_fields):
    # get the comma-separated values in the header row where the column names
    # are given
    # <field_names> is a list of the column name strings
    # <header_line_index> is the line index of the header row (first line = index 0)
    field_names, header_line_index = get_field_names(view)
    # <get_sort_order> finds the columns that are in the wrong place
    # and creates a map between the current index of a column and the index
    # it should be at when it is reordered
    # <dict_order_map> is a table of column indices; the keys of the table
    # are the old column indices and their corresponding value is the column
    # index they should be moved to; for exaample, for dict_order_map[0] = 1,
    # column 0 should be swapped with column 1
    #debug(dict_order)
    missing_fields, unexpected_fields = get_field_information(field_names, expected_fields)
    sort_order = get_sort_order(field_names, expected_fields, missing_fields, unexpected_fields)
    n_unexpected_fields = len(unexpected_fields)
    if sort_order is None or len(sort_order) != len(expected_fields) + n_unexpected_fields:
        debug('ERROR: Bad sort order')
        return

    debug('Sorting list:', sort_order)

    # the columns are reordered line by line; <pos> gives the position
    # of the next line to be edited, as line lengths can change if some
    # columns are mising and needed to be added
    pos = 0

    # <i> tracks the line index, used for comparing with the line index of
    # the header row to check if the header row is currently being processed;
    # the comparison line_inedx == i is passed as tha <is_header> param
    i = 0

    # previous line used to compare with current line for
    prev_line = sublime.Region(-1)

    # view.size() is called every time as the file length can change as each
    # line is edited
    while pos < view.size():
        line = view.line(pos)

        # ensure position was advanced to the next line
        if line.begin() == prev_line.begin():
            debug('Error calculating line advance amount on line',
                  i + 1)
            break

        debug('calling reorder_columns_for_line() at position',
              pos,
              'on line',
              i + 1)
        # <reorder_columns_for_line> will move columns in the line to the index
        # the syntax expects them to be at.
        # <advance> gives the length of the line after it is changed
        advance = reorder_columns_for_line(view,
                                           edit,
                                           line,
                                           header_line_index == i,
                                           n_unexpected_fields,
                                           sort_order,
                                           field_names,
                                           expected_fields)
        # advance position to start of next line
        pos += advance
        i += 1
        prev_line = line

def reorder_alias_columns(view, edit):
    reorder_columns(view, edit, sound_alias_fields)

def reorder_reverb_columns(view, edit):
    reorder_columns(view, edit, sound_reverb_fields)

def reorder_t5alias_columns(view, edit):
    reorder_columns(view, edit, sound_t5alias_fields)

def reorder_t5reverb_columns(view, edit):
    reorder_columns(view, edit, sound_t5reverb_fields)

def reorder_ambient_columns(view, edit):
    reorder_columns(view, edit, sound_ambient_fields)

def reorder_test_columns(view, edit):
    reorder_columns(view, edit, sound_test_fields)

# table of syntax-specific callbacks to reorder the columns of a table
# key is the base scope of the syntax, i.e. text.codt7.table.sound.<type>
column_reorder_funcs = {
    'text.codt7.table.sound.alias': reorder_alias_columns,
    'text.codt7.table.sound.reverb': reorder_reverb_columns,
    'text.codt7.table.sound.t5alias': reorder_t5alias_columns,
    'text.codt7.table.sound.t5reverb': reorder_t5reverb_columns,
    'text.codt7.table.sound.ambient': reorder_ambient_columns,
    'text.codt7.table.sound.test': reorder_test_columns
}

# Text command for reordering columns in a sound table to match the order
# in its corresponding syntax definition
# example: some sound table with first 4 columns 'name,storage,filespec,behavior'
# will get reordered to 'name,bahevior,storage,filespec' which matches the syntax
class OrderCodt7TableColumnsToSyntaxCommand(sublime_plugin.TextCommand):
    # param <scope> indexes the appropriate callback for the type of
    # sound table that is loaded, e.g. alias, reverb, ambient, etc.
    def run(self, edit, scope):
        reorder_func = column_reorder_funcs.get(scope)
        if reorder_func is None:
            return
        codt7_table.set_field_name_list_for_scope(scope)
        # run the appropriate cb
        reorder_func(self.view, edit)

COLUMN_CHECK_SETTINGS_KEY =           'check_syntax_column_order'
COLUMN_CHECK_BLACKLIST_SETTINGS_KEY = 'disable_syntax_column_order_check_files'

def column_checking_disabled_in_settings(settings_base_name,
                                         loaded_file_name,
                                         settings_key):
    settings_name = settings_base_name + '.sublime-settings'
    settings = sublime.load_settings(settings_name)
    skip_check = settings.get(settings_key) == False
    if skip_check:
        return True

    file_list = settings.get(COLUMN_CHECK_BLACKLIST_SETTINGS_KEY)
    if file_list is not None:
        return loaded_file_name in file_list
    else:
        return False

def disable_column_checking_in_settings(settings_base_name,
                                        settings_key):
    settings_name = settings_base_name + '.sublime-settings'
    settings = sublime.load_settings(settings_name)
    settings.set(settings_key, False)
    sublime.save_settings(settings_name)

def disable_file_column_checking_in_settings(file_name_list,
                                       settings_base_name,
                                       settings_key):
    settings_name = settings_base_name + '.sublime-settings'
    settings = sublime.load_settings(settings_name)
    file_list = settings.get(settings_key)
    if file_list is None:
        file_list = []
    file_list += file_name_list
    settings.set(settings_key, file_list)
    sublime.save_settings(settings_name)

# check_column_order performs a sanity check on the table column order
# param <scope> is the base scope of the syntax of the table being checked
def check_column_order(view, scope):
    # check that there is a sanity check cb for this syntax
    compare_func = column_order_compare_funcs.get(scope)
    if compare_func is None:
        return

    # settings can suppress these checks
    syntax_settings_base_name = view.syntax().name.replace(' ', '')
    if column_checking_disabled_in_settings(syntax_settings_base_name,
                                            view.file_name(),
                                            COLUMN_CHECK_SETTINGS_KEY):
        view.settings().set('syntax', 'Packages/Text/Plain text.tmLanguage')
        return

    # get the comma-separated values in the header row where the column names
    # are given
    # <field_names> is a list of the column name strings
    # <line_index> is the line index of the header row (first line = index 0)
    field_names, line_index = get_field_names(view)

    # run sanity cb
    # if returns True, columns are in same order as syntax expects, nothing to do
    if not compare_func(field_names):
        return

    # give option to reformat table or unassign the syntax
    response = sublime.yes_no_cancel_dialog(
        'This table has a different column ordering than the syntax definition expects.' \
        ' Would you like to reformat the table so it is highlighted correctly?',
        'Reformat Table',
        'Never Ask Again')

    if response == sublime.DIALOG_YES:
        view.run_command('order_codt7_table_columns_to_syntax', {'scope': scope})
    else:
        # switch to plain text syntax for the file
        view.settings().set('syntax', 'Packages/Text/Plain text.tmLanguage')
        # if 'never ask again' option was chosen
        if response == sublime.DIALOG_NO:
            # table type taken from the scope name for message box string
            table_type = scope[len('text.codt7.table.sound.'):]
            # ask to disable checking for all tables of this type
            # or just this file
            response_2 = sublime.yes_no_cancel_dialog(
                'Disable for this specific file or all tables of this type?',
                'All %s Tables' % (table_type.capitalize()),
                'Only This File')
            if response_2 == sublime.DIALOG_CANCEL:
                return
            elif response_2 == sublime.DIALOG_YES:
                disable_column_checking_in_settings(
                                        syntax_settings_base_name,
                                        COLUMN_CHECK_SETTINGS_KEY)
            elif response_2 == sublime.DIALOG_NO:
                file_name = view.file_name()
                if file_name is not None:
                    disable_file_column_checking_in_settings([file_name],
                                        syntax_settings_base_name,
                                        COLUMN_CHECK_BLACKLIST_SETTINGS_KEY)

# Event listeners for checking table sanity when the sound table syntax
# is assigned
class CheckCodt7TableColumnOrderCommand(sublime_plugin.EventListener):
    # callback for when file is loaded
    def on_load(self, view):
        check_column_order(view, view.syntax().scope)
