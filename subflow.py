import sublime
import sublime_plugin
import subprocess


class SubFlowCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for region in self.view.sel():
            line = self.view.line(region)
            cont = self.view.substr(line)

        if (len(cont) < 2):
            pass
        else:
            lang = "in " + self.get_syntax()
            cont = cont + lang
            print(cont)
            p = subprocess.Popen("howdoi " + cont,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 shell=True)
            output, errors = p.communicate()

            # Decode binary data for python 3
            output = output.decode('utf-8')

            # Remove CR for windows.
            if sublime.platform() == 'windows':
                output = output.replace('\r', '')

            self.view.replace(edit, line, output)

    def get_syntax(self):
        syntax_file = self.view.settings().get('syntax')
        start = syntax_file.rfind('/')
        if start == -1:
            start = 0

        end = syntax_file.rfind('.')
        if end == -1:
            end = len(syntax_file)

        return syntax_file[start+1:end].lower()
