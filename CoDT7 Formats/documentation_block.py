# This file is part of the T7-Sublime project.
# T7-Sublime is an enhanced syntax-highlighting package for (almost) all Call of Duty Black Ops III developer file formats.

import sublime, sublime_plugin

def build_documentation_block_data(view, pt):
    shell_vars = view.meta_info("shellVariables", pt)
    if not shell_vars:
        return []

    # transform the list of dicts into a single dict
    all_vars = {}
    for v in shell_vars:
        if 'name' in v and 'value' in v:
            all_vars[v['name']] = v['value']

    block_comments = []

    # transform the dict into a single array of valid comment blocks
    start = all_vars.setdefault("TM_DOCUMENTATION_START")
    end = all_vars.setdefault("TM_DOCUMENTATION_END")
    disable_indent = all_vars.setdefault("TM_DOCUMENTATION_DISABLE_INDENT")

    if start and end:
        block_comments.append((start, end, disable_indent == 'yes'))
        block_comments.append((start.strip(), end.strip(), disable_indent == 'yes'))

    return block_comments

class ToggleDocumentationCommand(sublime_plugin.TextCommand):
    def remove_documentation_block(self, view, edit, documentation_block_data, region):
        documentation_blocks = documentation_block_data

        # Call extract_scope from the midpoint of the region, as calling it
        # from the start can give false results if the block comment begin/end
        # markers are assigned their own scope, as is done in HTML.
        whole_region = view.extract_scope(region.begin() + region.size() / 2)

        for d in documentation_blocks:
            (start, end, disable_indent) = d
            start_region = sublime.Region(whole_region.begin(), whole_region.begin() + len(start))
            end_region = sublime.Region(whole_region.end() - len(end), whole_region.end())

            if view.substr(start_region) == start and view.substr(end_region) == end:
                # It's faster to erase the start region first
                view.erase(edit, start_region)

                end_region = sublime.Region(
                    end_region.begin() - start_region.size(),
                    end_region.end() - start_region.size())

                view.erase(edit, end_region)
                return True

        return False

    def documentation_block_region(self, view, edit, documentation_block_data, region):
        (start, end, disable_indent) = documentation_block_data

        if region.empty():
            # Silly buggers to ensure the cursor doesn't end up after the end
            # comment token
            view.replace(edit, sublime.Region(region.end()), 'x')
            view.insert(edit, region.end() + 1, end)
            view.replace(edit, sublime.Region(region.end(), region.end() + 1), '')
            view.insert(edit, region.begin(), start)
        else:
            view.insert(edit, region.end(), end)
            view.insert(edit, region.begin(), start)

    def add_documentation_block(self, view, edit, documentation_block_data, region):
        (documentation_blocks) = documentation_block_data

        if len(documentation_blocks) == 0:
            return

        # add the documentation block
        self.documentation_block_region(view, edit, documentation_blocks[0], region)

    def run(self, edit):
        for region in self.view.sel():
            documentation_block_data = build_documentation_block_data(self.view, region.begin())
            if (region.end() != self.view.size() and
                build_documentation_block_data(self.view, region.end()) != documentation_block_data):
                # region spans languages, nothing we can do
                continue

            if self.remove_documentation_block(self.view, edit, documentation_block_data, region):
                continue

            self.add_documentation_block(self.view, edit, documentation_block_data, region)
