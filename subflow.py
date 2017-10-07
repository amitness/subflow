import sublime
import sublime_plugin
import subprocess


class SubFlowCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for region in self.view.sel():
            line = self.view.line(region)
            cont = self.view.substr(line)

            if (len(cont) < 1):
                pass
            else:
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
