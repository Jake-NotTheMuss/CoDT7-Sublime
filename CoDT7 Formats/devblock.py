# This file is part of the T7-Sublime project.
# T7-Sublime is an enhanced syntax-highlighting package for (almost) all Call of Duty Black Ops III developer file formats.

import sublime, sublime_plugin

def devblocks_in_region(view, region, start_tok, end_tok):
    devblock_regions = []
    base = region.begin()
    str_region = view.substr(region)

    offs = str_region.find(start_tok)
    while offs != -1:
        end = str_region.find(end_tok, offs + 2)
        if end != -1:
            end += 2
            devblock_regions.append(sublime.Region(base + offs, base + end))
        else:
            break
        offs = str_region.find(start_tok, end)

    return devblock_regions

def build_devblock_data(view, pt):
    shell_vars = view.meta_info("shellVariables", pt)
    if not shell_vars:
        return []

    # transform the list of dicts into a single dict
    all_vars = {}
    for v in shell_vars:
        if 'name' in v and 'value' in v:
            all_vars[v['name']] = v['value']

    devblocks = []

    # transform the dict into a single array of valid devblocks
    start = all_vars.setdefault("TM_DEVBLOCK_START")
    end = all_vars.setdefault("TM_DEVBLOCK_END")
    disable_indent = all_vars.setdefault("TM_DEVBLOCK_DISABLE_INDENT")

    if start and end:
        devblocks.append((start, end, disable_indent == 'yes'))
        devblocks.append((start.strip(), end.strip(), disable_indent == 'yes'))

    return devblocks

class ToggleDevblockCommand(sublime_plugin.TextCommand):
    def remove_devblock(self, view, edit, devblock_data, region):
        (start, end, disable_indent) = devblock_data[0]

        # get devblocks in selection
        # we can't extract scope since devblocks only have meta scope
        # so widen the search to fit possible start/end tokens bordering the
        # selection to ensure proper removal
        search_region = sublime.Region(
            max(region.begin() - len(start), 0),
            min(region.end() + len(end), view.size()))
        devblocks = devblocks_in_region(view, search_region, start, end)

        for d in devblocks:
            start_region = sublime.Region(d.begin(), d.begin() + len(start))
            end_region = sublime.Region(d.end() - len(end), d.end())

            if view.substr(start_region) == start and view.substr(end_region == end):
                # It's faster to erase the start region first
                view.erase(edit, start_region)

                # shift the region by the size of the start token
                end_region = sublime.Region(
                    end_region.begin() - start_region.size(),
                    end_region.end() - start_region.size())

                view.erase(edit, end_region)
                return True

        return False

    def devblock_region(self, view, edit, devblock_data, region):
        (start, end, disable_indent) = devblock_data

        if region.empty():
            # Silly buggers to ensure the cursor doesn't end up after the end
            # token
            view.replace(edit, sublime.Region(region.end()), 'x')
            view.insert(edit, region.end() + 1, end)
            view.replace(edit, sublime.Region(region.end(), region.end() + 1), '')
            view.insert(edit, region.begin(), start)
        else:
            view.insert(edit, region.end(), end)
            view.insert(edit, region.begin(), start)

    def add_devblock(self, view, edit, devblock_data, region):
        devblocks = devblock_data

        if len(devblocks) == 0:
            return

        self.devblock_region(view, edit, devblocks[0], region)

    def run(self, edit):
        for region in self.view.sel():
            # get devblock tokens for the beginning of the selection
            # region.begin() gives the character index of the first
            # character in the selection. This is used to specify
            # the scope in which to look to get the tokens, since
            # different scopes/languages can and do define different
            # comment tokens
            devblock_data = build_devblock_data(self.view, region.begin())
            # region.end() gives the character index of the 
            # first character after the end of the selection.
            # if it is equal to view.size(), then the selection
            # spans to the end of the file.
            # If it spans to the end of the file, we don't want
            # to get the tokens for the scope at that point, since
            # there would be no scope outside the file
            # If calling 'build_devblock_data' again, this time passing
            # the end index of the selection, gives a different result
            # then that given by passing the start index, then the selection
            # is not sensible for this operation since it spans over multiple
            # languages/scopes.
            if (region.end() != self.view.size() and
                    build_devblock_data(self.view, region.end()) != devblock_data):
                # region spans languages, nothing we can do
                continue

            if self.remove_devblock(self.view, edit, devblock_data, region):
                continue

            self.add_devblock(self.view, edit, devblock_data, region)
