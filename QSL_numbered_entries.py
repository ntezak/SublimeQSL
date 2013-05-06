import sublime_plugin
import sublime
import re

row_header_pattern = re.compile('^\-\[([A-Za-z][A-Za-z0-9]*)_.*\] .*')
col_header_pattern = re.compile('^\<(\d+)\> .*')


class QslGridRowCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        if len(self.view.sel()) == 1:
            region = self.view.sel()[0]
            line = self.view.line(region)
            (a, b) = line.a, line.b

            gridvarname = 'gridvarname'
            # found_var = False

            m = row_header_pattern.match(self.view.substr(line))
            if m:
                gridvarname = m.group(1)
            self.view.sel().clear()
            self.view.sel().add(sublime.Region(b, b))
            self.view.run_command('insert_snippet',
                                  {"contents":
                                  "\n-[" + gridvarname + "_$1] $0"})


class QslGridColCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        if len(self.view.sel()) == 1:
            region = self.view.sel()[0]
            line = self.view.line(region)
            (a, b) = line.a, line.b

            m = col_header_pattern.match(self.view.substr(line))
            if m:
                colnumber = int(m.group(1))
                self.view.sel().clear()
                self.view.sel().add(sublime.Region(b, b))
                self.view.run_command('insert_snippet',
                                      {"contents": "\n<" +
                                      str(colnumber + 1)
                                      + "> $0"})
