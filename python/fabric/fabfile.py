from __future__ import print_function
import inspect
import importlib
import fabric.api as api
from fabric.context_managers import env
import config

env.hosts = config.hosts
env.passwords = config.passwords

class Helper:
    @staticmethod    
    def getFunctions(module):
        if isinstance(module, basestring):
            module = importlib.import_module(module)
            return inspect.getmembers(module, inspect.isfunction)
    @staticmethod
    def getFunctionNames(module):
        return [func[0] for func in Helper.getFunctions(module)]

    @staticmethod
    def getArgs(function):
        return inspect.getargspec(function)

def runremote(cmd=""):
    with api.hide('running', 'warnings'), api.settings(warn_only=True):
        return api.run(cmd)

def runlocal(cmd=""):
    with api.hide('running', 'warnings'), api.settings(warn_only=True):
        return api.local(cmd)

def ssh():
    runremote("/bin/bash")
    
def update():
    runremote("apt-get update")
    
def upgrade():
    runremote("apt-get upgrade -y")

def autoremove():
    runremote("apt-get autoremove -y")

def update_upgrade():
    update()
    upgrade()
    autoremove()

def upload(src, des):
    api.put(src, des)
    
def download(src, des):
    api.get(src, des)
    
def download_config(configs, filename="config.zip"):
    if isinstance(configs, basestring):
        configs = configs.split(";")
    paths = []
    for config in configs:
        paths += config.LIST_OF_CONFIGS[config]["path"]
    runremote("zip -r temp.zip " + " ".join(paths))
    download("/root/temp.zip", filename)
    runremote("rm temp.zip")
    return
    
def download_all_config(filename="all_config.zip"):
    download_config(config.LIST_OF_CONFIGS.keys(), filename)

def deploy():
    """Deploy application in remote server"""
    for command in config.LIST_OF_COMMANDS:
        with api.cd(command["path"]):
            runremote(command["command"])
            
def help():
    for func in Helper.getFunctions(__name__):
        print(func[0], end="")
        args = Helper.getArgs(func[1])[0]
        if len(args) > 0:
            print("(", end="")
        for arg in args:
            end = ", " if arg!=args[-1] else ")"
            print(arg, end=end)
        if func[1].__doc__:
            print(" : ", end="")
            print(func[1].__doc__, end="")
        print()

