import sublime, sublime_plugin

def get_field_name(scope, separator):
    ret = ''
    for s in scope.split(separator):
        # capitalize() leaves letters after the first lowercase,
        # but we want to preserve case for those letters
        s = s[0].upper() + s[1:]
        ret = ret + ' ' + s

    return ret

def symbol_at_point(view, pt):
    symbol = view.substr(view.expand_by_class(pt, sublime.CLASS_WORD_START | sublime.CLASS_WORD_END, ","))
    return symbol.strip(',')

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

class ShowSoundParameters(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
        if not view.settings().get('show_definitions'):
            return

        ShowSoundParameters.default_on_hover(view, point, hover_zone)

    def default_on_hover(view, point, hover_zone):
        if view.is_auto_complete_visible():
            return

        if hover_zone != sublime.HOVER_TEXT:
            return

        def score(scopes):
            return view.score_selector(point, scopes)

        if not score('text.codt7.table.sound'):
            return
        if not score('meta'):
            return
        if score('meta.header') or score('comment'):
            return

        c = view.substr(point)

        # get the sound parameter name from the meta scope
        scope = view.scope_name(point)
        start = scope.find('meta.')
        if start == -1:
            return
        start += 5
        end = scope.find('.', start)
        parameter_name = scope[start:end]
        parameter_name = get_field_name(parameter_name, "-")

        if c.isspace():
            value = ''
        else:
            value = symbol_at_point(view, point)

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
