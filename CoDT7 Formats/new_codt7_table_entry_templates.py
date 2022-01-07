import sublime, sublime_plugin

DEBUG = False

if DEBUG:
    def debug(*args):
        print(*args)
else:
    def debug(*args):
        return

def replace_rows_with_template(view, edit, template):
    # list of cols from template string
    template_cols = template.split(',')
    # number of columns in template string
    n_template_cols = len(template_cols)
    # list of new selections to add afterward
    new_selections = []
    for region in view.sel():
        # absolute position of cursor at this selection
        cursor_pos = region.begin()
        new_selections.append(cursor_pos)
        # region covering the entire line
        line_region = view.line(cursor_pos)
        # number of characters in line before editing
        original_line_size = line_region.size()
        # relative position of cursor in this line
        line_pos = cursor_pos - line_region.begin()
        debug('Inserting template into selection',
              region,
              'at position',
              line_pos,
              'in line')
        # string of characters in the line
        str_line = view.substr(line_region)
        # list of column values in the line
        row_cols = str_line.split(',')
        # original number of columns before editing
        # used for debugging
        n_cols_before = len(row_cols)
        # number of columns before the cursor position
        # in the line
        n_leading_cols = str_line.count(',', 0, line_pos) + 1
        # cursor might be past the number of expected
        # columns
        if n_leading_cols >= n_template_cols:
            debug('Selection was beyond expected number of columns:',
                  region,
                  'Skipping selection')
            continue
        # new list of columns with the template inserted
        new_row_cols = row_cols[0:n_leading_cols] + template_cols[n_leading_cols:]
        # string of characters in edited line
        str_new_row = ','.join(new_row_cols)
        # number of characters in line after editing
        new_line_size = len(str_new_row)
        debug('Number of characters in line changed from',
              original_line_size,
              'to',
              new_line_size)
        # make the changes in the buffer
        view.replace(edit, line_region, str_new_row)

    # clear selections and add back the same selections
    # but each only spanning a single position.
    view.sel().clear()
    for new_sel in new_selections:
        view.sel().add(sublime.Region(new_sel))

class NewSoundAliasEntryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        template = 'NAME,,loaded,filespec.wav,,,TEMPLATE_NAME,,,,,BUS_FX,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
        replace_rows_with_template(self.view, edit, template)

class NewSoundReverbEntryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        template = 'NAME,,,,,,,,,,,,,,,,,,,,,,,,\n'
        replace_rows_with_template(self.view, edit, template)

class NewSoundT5AliasEntryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        template = 'NAME,,TEMPLATE_NAME,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
        replace_rows_with_template(self.view, edit, template)

class NewSoundT5ReverbEntryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        template = ',,,,,,,,,,,,'
        replace_rows_with_template(self.view, edit, template)

class NewSoundAmbientEntryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        template = ',,,,,,,,,,,,,,,,,'
        replace_rows_with_template(self.view, edit, template)
