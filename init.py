import os
from subprocess import Popen,PIPE

class Init:
    def __init__(self, backend, base):

        os.system('chmod u+x initialize.sh')
        os.system('sh initialize.sh ' + backend + ' ' + base)
