import sublime, glob, os, subprocess

settings = sublime.load_settings("ApiGen.sublime-settings")

active = False

def canRun():
    global active
    return not active

def activate():
    global active
    active = True

def deactivate():
    global active
    active = False

def getConfigFile(start):
    global settings

    config = ''
    lastPass = start
    thisPass = os.path.dirname(start)
    filename = settings.get('configFileName', 'apigen.neon')

    while lastPass != thisPass :
        os.chdir(thisPass)

        for file in glob.glob(filename):

            config = thisPass + os.sep + file 
            if config != '':
                break

        if config != '':
            break
        lastPass = thisPass
        thisPass = os.path.dirname(thisPass)

    return config

def runApiGen(args):
	global settings

	php = settings.get('phpBin', 'php')
	phar = settings.get('pharPath', 'apigen.phar')
	cmd = [php, phar]
	cmd.extend(args)
	proc = ''

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
			deactivate()
			return

	deactivate()
