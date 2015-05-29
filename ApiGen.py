import sys, os
import sublime, sublime_plugin
import ApiGen.ApiGenHelper as ag

class ApiGenShowConsoleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().run_command("show_panel", {"panel": 'console'})
        print('\n\n#################################### ApiGen ####################################')

class ApiGenBaseClass(sublime_plugin.TextCommand):
    def is_enabled(self):
        return ag.canRun()

class ApiGenSelfupdateCommand(ApiGenBaseClass):
    def run(self, edit):       
        self.view.run_command('api_gen_show_console') 
        ag.activate()
        args = ['selfupdate']
        sublime.set_timeout_async(lambda : ag.runApiGen(args), 0)

class ApiGenVersionCommand(ApiGenBaseClass):
    def run(self, edit):
        self.view.run_command('api_gen_show_console') 
        ag.activate()
        args = ['-v']
        sublime.set_timeout_async(lambda : ag.runApiGen(args), 0)

class ApiGenGenerateCommand(ApiGenBaseClass):
    def run(self, edit):
        path = self.view.file_name()
        if path == None:
            return

        ag.activate()
        self.view.run_command('api_gen_show_console') 
        config = ag.getConfigFile(path)

        if config != '':
            print('Processing will proceed using ' + config) 
            args = ['generate', '--config', config]
            sublime.set_timeout_async(lambda : ag.runApiGen(args), 0)
        else:
            print('No config file could not be found!')
            ag.deactivate()
