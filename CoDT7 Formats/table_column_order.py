import sublime, sublime_plugin

DEBUG_ON = False

def debug(*args):
    if not DEBUG_ON:
        return
    print(*args)

# these match the order of their corresponding syntax files
# From Packages/CoDT7 Formats/SoundAliasTable.sublime-syntax
sound_alias_order = {
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
sound_reverb_order = {
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
sound_t5alias_order = {
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
sound_t5reverb_order = {
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
sound_ambient_order = {
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
sound_test_order = {
    'name': 0,
    'test_filename': 1,
    'test_level': 2,
    'test_type': 3,
    'test_global_id': 4,
    'test_secondary_id': 5
}

def is_commented(line):
    line = line.strip()
    if len(line) == 0:
        return False
    return line[0] == '#'

def is_empty(line):
    line = line.strip()
    return len(line) == 0

# <get_column_names> gets a list of column names for the table and
# also returns the index of the line from which the names were read
def get_column_names(view):
    line = view.line(0)
    pos = line.size() + 1
    line_index = 0
    # skip commented/empty lines
    while is_commented(view.substr(line)) or is_empty(view.substr(line)):
        line = view.line(pos)
        pos += line.size() + 1
        line_index += 1

    return view.substr(line).strip(',').split(','), line_index

# <get_new_order_mapping> creates a map between the current position
# of a table's columns and the position they should be moved to
# the key is the current position, the value is the new position
# param <list_order> - the file's column order
# param <dict_correct_order> - the expected column order
def get_new_order_mapping(list_order, dict_correct_order):
    order_mapping = {}
    for i in range(len(list_order)):
        name = list_order[i].lower().strip()
        # get correct position for column
        index = dict_correct_order.get(name)
        if index is not None:
            # column is in correct position
            if i == index:
                continue
            # mismatch is already recorded and adding a
            # reciprocal mapping would do the swap twice
            # resulting in no change

            # if the correct column index is already a
            # key in the mapping table, it need not be
            # a value in the table, as there would be
            # a double swap resulting in no change.
            # for example, c1 -> c2, c2 -> c1. c1 is
            # searched in the table keys and because
            # there is already c1 -> c2, c1 will not
            # be added as a value for c2.
            if index in order_mapping:
                # in the special case where index is already
                # a key in the table, but it maps to the
                # reserved value -1, indicating column
                # <index> is currently an unknown column,
                # e.g. column 2 in the alias table, which
                # should be 'storage', is currently an
                # unknown column in this example index = 2,
                # and i would be the column position where
                # 'storage' was in this file, say position 5.
                # Then i would be 5 and column 5 would be the
                # 'storage' column. Then, column 2 (index)
                # would be remapped to column 5 (i) and
                # column 5 would be given the value reserved
                # for unknowns -1. This way, columns 2 and 5
                # would swap, putting 'storage' in column 2
                # as required, and column 5 is now marked as
                # the unknown column. Then, if the true column
                # 5 is encountered later in this loop, for
                # example at i = 10, meaning column 10 is the
                # 'filespecrelease' column which should be at
                # column 5, then in that event, index = 5, and
                # i = 10, and so 5 will be remapped from -1 to
                # 10, thus moving column 10 to column 5, and
                # putting the unknown column in 10. This will
                # continue until the unknown column is finally
                # at a column that is completely missing from
                # the file, and it will be left as -1, which is
                # handled later where the column is moved to the
                # end of the file, and the old position is made
                # empty.
                if order_mapping[index] == -1:
                    order_mapping[index] = i
                    order_mapping[i] = -1
                continue
            # record mismatch, mapping the current position to the
            # correct position
            order_mapping[i] = index
        # unknown column name, give a reserved value of -1
        else:
            order_mapping[i] = -1

    return order_mapping

# <compare_column_order> checks that the two column orders given match each other
# param <list_order>         - list of column names of the actual file
# param <dict_correct_order> - table of column names to positions describing the correct order
# <list_order> only needs to match <dict_correct_order> for its own length; it does not need
# to have every column that <dict_correct_order> has
def compare_column_order(list_order, dict_correct_order):
    # loop through the file's column names
    for i in range(min(len(list_order), len(dict_correct_order))):
        name = list_order[i].strip().lower()
        index = dict_correct_order.get(name)
        if index is not None:
            # the columns names are not at matching positions
            if index != i:
                debug('column mismatch:',
                      list_order[i].strip(),
                      list_order[index]
                        if index < len(list_order)
                        else '<missing column>')
                return False
        # the column name is not recognized
        else:
            # No mismatch but there is a column with an unknown name
            debug('unknown column name:',
                  list_order[i].strip())
            return False

    return True

def compare_alias_column_order(list_order):
    return compare_column_order(list_order, sound_alias_order)

def compare_reverb_column_order(list_order):
    return compare_column_order(list_order, sound_reverb_order)

def compare_t5alias_column_order(list_order):
    return compare_column_order(list_order, sound_t5alias_order)

def compare_t5reverb_column_order(list_order):
    return compare_column_order(list_order, sound_t5reverb_order)

def compare_ambient_column_order(list_order):
    return compare_column_order(list_order, sound_ambient_order)

def compare_test_column_order(list_order):
    return compare_column_order(list_order, sound_test_order)

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
# param <list_order>  - list of column name strings from file's header row
# param <dict_correct_order> - table mapping column names to their expected positions
def reorder_columns_for_line(view,
                             edit,
                             line,
                             is_header,
                             dict_order_map,
                             list_order,
                             dict_correct_order):
    # get string from the region covering the line
    str_line = view.substr(line)

    # line is empty, return 1 to advance the newline
    if len(str_line) == 0:
        debug('Nothing to be done for empty row')
        return 1

    # line is commented with a '#'
    if is_commented(str_line):
        debug('Nothing to be done for commented row')
        return (len(str_line) + 1)

    debug('Row before reordering:', str_line)
    debug('Row length before reordering:', len(str_line))

    # get array of the comma-separated values in the row
    column_values = str_line.split(',')

    # get number of columns
    n_cols = len(column_values)

    # columns might be missing, get the required padding amount
    padding = len(dict_correct_order) - n_cols

    # pad the list if needed
    if padding > 0:
        debug('Padding row with', padding, 'columns')
        column_values += [''] * padding

    # keep track of columns which are not recognized by the syntax
    # as they are handled differently
    unknown_columns = []

    # get the expected column names as a list in the expected order
    column_names = sorted(list(dict_correct_order.keys()),
                          key=lambda x:dict_correct_order[x])

    # loop through the old-new map for the column positions
    for old_index, new_index in sorted(list(dict_order_map.items()),
                                       key=lambda x:x, reverse=True):
        # new positional value of -1 means it's an unknown column
        if new_index == -1:
            unknown_columns.append(old_index)
            continue

        # swap the columns in the list
        debug('Swapping columns', old_index, 'and', new_index)
        column_values[old_index], column_values[new_index] = \
        column_values[new_index], column_values[old_index]

    # handle the unknown columns
    for index in unknown_columns:
        # get the string in this column
        val = column_values[index]
        # no other column to swap with so replace with an
        # empty column
        column_values[index] = ''
        # append the unknown column to the end of the row
        debug('Appending unexpected column value \'',
              column_values[index],
              '\' to end of row')
        column_values.append(val)

    # fill in missing column names in header
    if is_header:
        debug('Adding missing column names in header')
        is_capitalized = column_values[0][0].isupper()
        for i in range(min(len(column_names), len(column_values))):
            if column_values[i].strip() == '':
                if is_capitalized:
                    column_values[i] = column_names[i][0].upper() \
                                       + column_names[i][1:]
                else:
                    column_values[i] = column_names[i]

    # get new string from column list
    str_reordered_line = ','.join(column_values)

    debug('Row after reordering:', str_reordered_line)
    debug('Row length after reordering:', len(str_reordered_line))

    # replace line in buffer
    view.replace(edit, line, str_reordered_line)

    # return the new length to advance by
    return (len(str_reordered_line) + 1)

# <reorder_columns> will edit the current file to match the column order
# of its syntax definition
# param <dict_correct_order> is a table of column names to indices
# which describes the column order that the table should be in
def reorder_columns(view, edit, dict_correct_order):
    # get the comma-separated values in the header row where the column names
    # are given
    # <list_order> is a list of the column name strings
    # <header_line_index> is the line index of the header row (first line = index 0)
    list_order, header_line_index = get_column_names(view)
    # <get_new_order_mapping> finds the columns that are in the wrong place
    # and creates a map between the current index of a column and the index
    # it should be at when it is reordered
    # <dict_order_map> is a table of column indices; the keys of the table
    # are the old column indices and their corresponding value is the column
    # index they should be moved to; for exaample, for dict_order_map[0] = 1,
    # column 0 should be swapped with column 1
    dict_order_map = get_new_order_mapping(list_order, dict_correct_order)
    debug(dict_order_map)

    # the columns are reordered line by line; <pos> gives the position
    # of the next line to be edited, as line lengths can change if some
    # columns are mising and needed to be added
    pos = 0

    # <i> tracks the line index, used for comparing with the line index of
    # the header row to check if the header row is currently being processed;
    # the comparison line_inedx == i is passed as tha <is_header> param
    i = 0

    # view.size() is called every time as the file length can change as each
    # line is edited
    while pos < view.size():
        line = view.line(pos)
        # <reorder_columns_for_line> will move columns in the line to the index
        # the syntax expects them to be at.
        # <advance> gives the length of the line after it is changed
        debug('calling reorder_columns_for_line() at position',
              pos, 'on line', i)
        advance = reorder_columns_for_line(view,
                                           edit,
                                           line,
                                           header_line_index == i,
                                           dict_order_map,
                                           list_order,
                                           dict_correct_order)
        # advance position to start of next line
        pos += advance
        i += 1

def reorder_alias_columns(view, edit):
    reorder_columns(view, edit, sound_alias_order)

def reorder_reverb_columns(view, edit):
    reorder_columns(view, edit, sound_reverb_order)

def reorder_t5alias_columns(view, edit):
    reorder_columns(view, edit, sound_t5alias_order)

def reorder_t5reverb_columns(view, edit):
    reorder_columns(view, edit, sound_t5reverb_order)

def reorder_ambient_columns(view, edit):
    reorder_columns(view, edit, sound_ambient_order)

def reorder_test_columns(view, edit):
    reorder_columns(view, edit, sound_test_order)

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
        if not scope in column_reorder_funcs:
            return
        # run the appropriate cb
        column_reorder_funcs[scope](self.view, edit)

COLUMN_CHECK_SETTINGS_KEY = 'check_syntax_column_order'
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
    if not scope in column_order_compare_funcs:
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
    # <column_names> is a list of the column name strings
    # <line_index> is the line index of the header row (first line = index 0)
    column_names, line_index = get_column_names(view)

    # run sanity cb
    # if returns True, columns are in same order as syntax expects, nothing to do
    if column_order_compare_funcs[scope](column_names):
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
