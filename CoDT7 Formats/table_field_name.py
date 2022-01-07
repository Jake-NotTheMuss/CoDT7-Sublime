import sublime, sublime_plugin

def get_field_name(scope, separator):
    ret = ''
    for s in scope.split(separator):
        # capitalize() leaves letters after the first lowercase,
        # but we want to preserve case for those letters
        s = s[0].upper() + s[1:]
        ret = ret + ' ' + s

    return ret

# <symbol_at_point> returns the string in the column
# that is scoped under param <scope>
def symbol_at_point(view, pt, scope):
    pt_end = pt - 1

    while view.score_selector(pt_end, scope):
        pt_end -= 1

    pt_start = pt_end + 1
    pt_end = pt + 1

    while view.score_selector(pt_end, scope):
        pt_end += 1

    return view.substr(sublime.Region(pt_start, pt_end))

def _popup_css():
    return """
        body {
            white-space: nowrap;
        }
        h1 {
            font-size: 1.1rem;
            font-weight: bold;
            text-align: center;
            margin: 0 0 0.5em 0;
        }
        p {
            font-size: 1.05rem;
            text-align: center;
            margin: 0;
            color: color(var(--foreground) a(0.7));
            font-style: italic;
        }
    """

class ShowTableColumnName(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
        if not view.settings().get('show_definitions'):
            return

        ShowTableColumnName.default_on_hover(view, point, hover_zone)

    def default_on_hover(view, point, hover_zone):
        if view.is_auto_complete_visible():
            return

        if hover_zone != sublime.HOVER_TEXT:
            return

        if view.substr(point).isspace():
            return

        def score(scopes):
            return view.score_selector(point, scopes)

        if not score('text.codt7.table'):
            return
        # look for 'meta.column.<something>.codt7'
        # but not 'meta.column.codt7'
        if not score('meta.column') or score('meta.column.codt7'):
            return

        # get the sound parameter name from the meta scope
        scope = view.scope_name(point)
        start = scope.find('meta.column.')
        col_scope = scope[start:scope.find(' ', start)]

        value = symbol_at_point(view, point, col_scope)

        start += 12
        end = scope.find('.', start)
        parameter_name = scope[start:end]
        parameter_name = get_field_name(parameter_name, "-")

        header = """
            <h1>%s</h1>
            <p>%s</p>
        """ % (parameter_name, value)

        body = """
            <body id=show-parameter>
                <style>
                    body {
                        font-family: system;
                    }
                    %s
                </style>
                %s
            </body>
        """ % (_popup_css(), header)

        view.show_popup(
            body,
            flags=sublime.HIDE_ON_MOUSE_MOVE_AWAY,
            location=point,
            max_width=1024)
