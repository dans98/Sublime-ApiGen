import sublime, sublime_plugin, glob, os, subprocess

__ApiGenActive__ = False

class ApiGenShowConsoleCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.window().run_command("show_panel", {"panel": 'console'})
        print('\n\n#################################### ApiGen ####################################')

class ApiGenSelfupdateCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        global __ApiGenActive__
        __ApiGenActive__ = True        
        self.view.run_command('api_gen_show_console') 
        commandArgs = []
        self.view.run_command('api_gen_run', {"command": "selfupdate", "args": commandArgs})

    def is_enabled(self):
        global __ApiGenActive__
        return not __ApiGenActive__

class ApiGenVersionCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        global __ApiGenActive__
        __ApiGenActive__ = True  
        self.view.run_command('api_gen_show_console') 
        commandArgs = []
        self.view.run_command('api_gen_run', {"command": "-v", "args": commandArgs}) 

    def is_enabled(self):
        global __ApiGenActive__
        return not __ApiGenActive__

class ApiGenGenerateCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        global __ApiGenActive__
        fileName = 'apigen.neon'

        path = self.view.file_name()
        if path == None:
            return

        __ApiGenActive__ = True  
        self.view.run_command('api_gen_show_console') 
        
        config = self.getneonfile(path, fileName)

        if config != '':
            print('Processing will proceed using ' + config)
            commandArgs = ['--config', config]
            self.view.run_command('api_gen_run', {"command": "generate", "args": commandArgs}) 

        else:
            # a config file was not found
            print( fileName + ' could not be found!')
            __ApiGenActive__ = False

    def getneonfile(self, start, filename):
        neon = ''
        lastPass = start
        thisPass = os.path.dirname(start)

        while lastPass != thisPass :
            os.chdir(thisPass)

            for file in glob.glob(filename):

                neon = thisPass + os.sep + file 
                if neon != '':
                    break

            if neon != '':
                break
            lastPass = thisPass
            thisPass = os.path.dirname(thisPass)

        return neon

    def is_enabled(self):
        global __ApiGenActive__
        return not __ApiGenActive__

class ApiGenRunCommand(sublime_plugin.TextCommand):

    def run(self, edit, command, args):
        self.command = command
        self.args = args
        sublime.set_timeout_async(self.runApiGen, 0)

    def runApiGen(self):
        global __ApiGenActive__
        proc = ''
        settings = sublime.load_settings("ApiGen.sublime-settings")
        php = settings.get('phpBin', 'php')
        phar = settings.get('pharPath', 'apigen.phar')
        cmd = [php, phar, self.command]
        cmd.extend(self.args)

        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, startupinfo=startupinfo)
        else:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)

        while proc.poll() is None:
            try:
                data = proc.stdout.readline().decode(encoding='UTF-8')
                print(data, end="")
            except:
                __ApiGenActive__ = False
                return

        __ApiGenActive__ = False
        return
