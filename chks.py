import subprocess
import os
import json

class checks:
    def __init__(self, path):
        self.path = path
        try:
            with open(path, 'r') as file:
                self.data = json.load(file)
        except:
            del self
            print("Error loading the JSON file")
            
    def chkFileExists():
        return os.path.exists(path)

    def checkDjangoVersion():
    #Checks Django Version
        getVersion =  subprocess.Popen("django-admin --version", shell=True, stdout=subprocess.PIPE).stdout
        djVer =  getVersion.read()
        djVerStr = djVer.decode()
        djVerStr = djVerStr[0:-1]
        if(djVerStr == "4.1.2"):
            return True
        else:
            return False
    
    def chkKeys(self):
        for it in self.data.keys():
            if(validString(it) == False):
                return False
            
        return True

    def chkValues(data):
        for it in data.values():
            if (type(it) == dict or type(it) == list):
                return False
        
        return True

    def chkPythonVer:
    # Checks Python version
        getVersion =  subprocess.Popen("python3 --version", shell=True, stdout=subprocess.PIPE).stdout
        pyVer =  getVersion.read()
        pyVerStr = pyVer.decode()[7:-1]
        print(pyVerStr)
    
    def chkPipVer:
        #Checks Pip version
        getVersion =  subprocess.Popen("pip --version", shell=True, stdout=subprocess.PIPE).stdout
        pyPipVer =  getVersion.read()
        pyPipVerStr = pyPipVer.decode()
        pyPipVerStr.split(" ")[1]
        print(pyPipVerStr.split(" ")[1])


     
            
        
        








