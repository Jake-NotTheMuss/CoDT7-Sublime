import sublime, sublime_plugin
import os

def get_documentation_comment_tokens(view, pt):
    shell_vars = view.meta_info("shellVariables", pt)
    if not shell_vars:
        return []

    # transform the list of dicts into a single dict
    all_vars = {}
    for v in shell_vars:
        if 'name' in v and 'value' in v:
            all_vars[v['name']] = v['value']

    # transform the dict into a single array of valid comment blocks
    start = all_vars.setdefault("TM_DOCUMENTATION_START")
    end = all_vars.setdefault("TM_DOCUMENTATION_END")

    return start, end

def get_module_name(view):
    module_name = view.file_name()
    if module_name is None:
        return ''
    else:
        module_name = os.path.splitext(os.path.basename(module_name))[0]

        # skip leading '_'
        module_name = module_name.lstrip('_')

        # is this a shared script, e.g. *_shared.gsc
        endpos = module_name.find('_shared')
        if endpos != -1:
            module_name = module_name[:endpos]
            if len(module_name) >= 3:
                return module_name.capitalize()
            else:
                return module_name.upper()

        # name is too short
        if len(module_name) <= 2:
            return ''
        
        # get gamemode prefix from name
        gamemode = module_name[:2]

        # Zombies
        if gamemode == 'zm':
            gamemode = 'Zombie'
        # Multiplayer
        elif gamemode == 'mp':
            gamemode = 'Multiplayer'
        # Campaign
        elif gamemode == 'cp':
            gamemode = 'Campaign'
        # Don't put gamemode
        else:
            gamemode = ''

        # get last underscore, this ensures on map scripts
        # the mapname is skipped, e.g. in 'zm_zod_train',
        # 'zod' is not included in the module name
        nextstartpos = module_name.rfind('_')
        if nextstartpos != -1:
            module_name = module_name[nextstartpos + 1:]

        # At this point, a file such as 'zm_zod_train.gsc'
        # will give a module_name of 'Train'
        module_name = module_name.capitalize()
        # Don't put module name if in struct.gsc
        if module_name == 'Struct':
            return ''
        # Don't add gamemode if module is utility
        if module_name != 'Utility' and module_name != 'Struct' and gamemode:
            module_name = gamemode + ' ' + module_name

        return module_name

class InsertGscDocumentationTemplateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view

        pt = view.sel()[0].begin()

        start_token, end_token = get_documentation_comment_tokens(view, pt)

        if not start_token or not end_token:
            return

        def score(scopes):
            return view.score_selector(pt, scopes)

        if not score('entity.name.function.codt7.gsc'):
            return

        symbol_region = view.expand_by_class(pt,
                        sublime.CLASS_WORD_START | sublime.CLASS_WORD_END)

        symbol_name = view.substr(symbol_region)

        module_name = get_module_name(view)

        # get the string containing the param list (...)
        scope = 'meta.function.parameters.codt7.gsc'

        # Note that a simple string.find(')') will not always work
        # since a param list can contain additional parens in the
        # middle, e.g. some_func( array = array(), array1 )

        # advance to start of param list
        while not score(scope):
            pt += 1

        # don't need the initial open paren
        pt_begin = pt + 1

        # advance to end of param list
        while score(scope):
            pt += 1

        # don't need the last close paren
        pt_end = pt - 1

        # get param list as region and string
        paramlist_region = sublime.Region(pt_begin, pt_end)
        str_paramlist = view.substr(paramlist_region)

        # some commas might be separating arguments in function calls
        # or vectors so just change those commas to another character
        # so they don't get counted in string.split()
        pt = str_paramlist.find(',')
        while pt != -1:
            if view.score_selector(pt_begin + pt,
            'meta.function.parameters meta.group meta.group'):
                # replace the comma with a different character
                # so it doesn't get counted in split()
                str_paramlist = str_paramlist[0:pt] + '|' + str_paramlist[pt + 1:]
            pt = str_paramlist.find(',', pt + 1)

        # convert to list of param names
        if len(str_paramlist.strip()) == 0:
            paramlist = []
        else:
            paramlist = [s.strip() for s in str_paramlist.split(',')]

        # complete list of lines to insert in the documentation block
        doc_lines = []

        # string containing the name line (Name: some_func...)
        doc_name_line = '"Name: %s(' % (symbol_name)
        # list of lines for each argument (MandatoryArg: <name> ...)
        man_arg_lines = []
        # optional args are listed after the mandatory ones
        opt_arg_lines = []
        man_arg = 'MandatoryArg'
        opt_arg = 'OptionalArg'

        # process the list of param names in place
        # put lt-gt's around mandatory args and
        # square brackets around optional args
        for i in range(len(paramlist)):
            str_param = paramlist[i]
            # equals sign means arg is default-initialized
            # and is treated as optional in the documentation
            # block
            eq_sign_pos = str_param.find('=')
            b_default_initialized = eq_sign_pos != -1
            # get rid of the default value in the param
            if b_default_initialized:
                str_param = '[' + str_param[0:eq_sign_pos].strip() + ']'
                full_arg_line = '"%s: %s : "' % (opt_arg, str_param)
                opt_arg_lines.append(full_arg_line)
                doc_name_line = doc_name_line + ' %s ,' % (str_param)
            else:
                str_param = '<' + str_param + '>'
                full_arg_line = '"%s: %s : "' % (man_arg, str_param)
                man_arg_lines.append(full_arg_line)
                doc_name_line = doc_name_line + ' %s ,' % (str_param)

        # remove extra comma at the end of the list
        if doc_name_line[-1] == ',':
            doc_name_line = doc_name_line[0:-1]
        # complete list
        doc_name_line = doc_name_line + ')"'

        # Name line
        doc_lines.append(doc_name_line)
        # Summary line
        doc_lines.append('"Summary: "')
        # Module line
        if module_name:
            doc_lines.append('"Module: %s"' % (module_name))
        # CallOn line
        doc_lines.append('"CallOn: "')
        # Mandatory args
        doc_lines += man_arg_lines
        # Optional args
        doc_lines += opt_arg_lines
        # Example line
        doc_lines.append('"Example: "')
        # SPMP line
        doc_lines.append('"SPMP: "')

        pt = symbol_region.begin() - 1
        # backtrack to before the function declaration
        while score('meta.function'):
            pt -= 1

        while not score('comment.block.documentation'):
            pt -= 1
            # stop if encountering any construct before a
            # documentation block
            if not score('meta.assumed-macro') and score('meta'):
                break

        str_new_comment = '\n'.join(doc_lines)

        if score('comment.block.documentation'):
            pt -= len(end_token)
            # in case of empty comment, add a character
            # so that extract_scope() can work on a point
            # that has just 'comment' but not 'punctuation'
            # scope
            view.insert(edit, pt, 'x')
            old_comment_region = view.extract_scope(pt)
        else:
            prev_line = view.line(view.line(symbol_region.begin()).begin() - 1)
            str_line = view.substr(prev_line).strip()
            seen_declaration_keyword = False
            pt = symbol_region.begin() - 1
            default_pt = view.line(pt).begin() - 1
            search_range = 20
            while search_range > 0:
                if score('keyword.declaration'):
                    pt = view.line(pt).begin() - 1
                    break
                pt -= 1
                search_range -= 1

            if search_range == 0:
                pt = default_pt

            old_comment_region = sublime.Region(pt)

            # if not replacing an existing comment, add a leading newline
            start_token = '\n' + start_token

        str_new_comment = start_token + '\n' + str_new_comment + '\n' + end_token

        view.replace(edit, old_comment_region, str_new_comment)
