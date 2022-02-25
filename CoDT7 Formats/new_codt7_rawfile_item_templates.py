# This file is part of the T7-Sublime project.
# T7-Sublime is an enhanced syntax-highlighting package for (almost) all Call of Duty Black Ops III developer file formats.

import sublime, sublime_plugin

class NewStringDefinitionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #language_idents = self.view.find_by_selector('constant.language.language-identifier.codt7.localizedstrings')

        pt = self.view.sel()[0].begin()

        if self.view.score_selector(pt, 'text.codt7.localizedstrings') == 0:
            return

        the_language = None

        # get the language for this file
        while pt >= 0 and self.view.score_selector(pt, 'constant.language.language-identifier') == 0:
            if self.view.score_selector(pt, 'constant.language.language-identifier'):
                language_ident = self.view.expand_by_class(pt,
                        sublime.CLASS_WORD_START | sublime.CLASS_WORD_END)
                the_language = self.view.substr(language_ident)
                break
            pt -= 1

        # No language identifiers found, default to english
        if the_language is None:
            the_language = 'LANG_ENGLISH'

        # 20 character indent
        padding = '                    '
        
        # language identifier may be 20 or more characters long
        i = len(the_language)
        while i >= 20:
            padding += ' '
            i -= 1

        # dummy name for the string alias
        placeholder_name = 'STRINGALIAS'

        # the part of the template before the string alias
        template_begin  = 'REFERENCE           '
        # the second line of the string definition: <LANG_ID><WS-padding><quotes>
        template_end = the_language + padding[len(the_language):] + '""'

        # list of new selections for each inserted placeholder alias
        new_selections = []
        
        for region in self.view.sel():
            # Replace whole lines
            region = self.view.line(region.begin())
            region_start = region.begin()

            # This is for replacing existing string defs
            # if selection is on alias line, include the next translation line
            if self.view.score_selector(region_start, 'meta.string-reference'):
                pt = region.end() + 1
                limit = self.view.size()
                while pt < limit:
                    if self.view.score_selector(pt, 'meta.string-implementation'):
                        break

                    pt = self.view.line(pt).end() + 1

                if pt >= limit:
                    pt = region.end()
                else:
                    pt = self.view.line(pt).end()

                region = sublime.Region(region_start, pt)
            # if selection is on translation line, include the previous alias line
            elif self.view.score_selector(region_start, 'meta.string-implementation'):
                pt = region_start - 1

                while pt >= 0:
                    if self.view.score_selector(pt, 'meta.string-reference'):
                        break

                    pt = self.view.line(pt).begin() - 1

                if pt < 0:
                    pt = region_start
                else:
                    pt = self.view.line(pt).begin()

                region = sublime.Region(pt, region.end())

            # The above won't handle situations where the selection is in between
            # an alias line and a translation line, e.g.:
            #
            # REFERENCE     ALIAS
            #
            # <selection>
            #
            # LANG_ENGLISH "English translation"

            region_start = region.begin()

            # get offset for where new selction will start
            new_selection_offs = len(template_begin)

            template = template_begin + placeholder_name + '\n' + template_end

            self.view.replace(edit, region, template)

            new_selections.append(sublime.Region(region_start + new_selection_offs,
                                                 region_start + new_selection_offs + len(placeholder_name)))

        self.view.sel().clear()

        # add new selections
        for new_sel in new_selections:
            self.view.sel().add(new_sel)
