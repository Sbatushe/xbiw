# xbps-install wrapper that doesn't care about case sensitive or package versions
# Written by Sbatushe

import sys
import os
import subprocess
import re

#setup your superuser value
superuser = "sudo"
#superuser = "doas"

if (len(sys.argv)>1):

    #grub xbps-query output
    rv = subprocess.Popen(["xbps-query","-Rs",sys.argv[1]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    stdout = rv.communicate()
    if stdout != "":
    
        #scan xbps-query output
        pkglist = []
        results = re.split(r'\\n',str(stdout))
        for row in results:
            element = re.split(r' ',row)
            if len(element)>1:
                pkglist.append(element[1])

        #scan alternatives and find package to install
        candidates = []
        if (len(pkglist)>0):
            for pkg in pkglist:
                req_components = re.split(r'-',sys.argv[1])
                pkg_components = re.split(r'-',pkg)
                if (len(req_components) == (len(pkg_components)-1)):
                    flag = True
                    for n in range(len(pkg_components)-1):
                        if req_components[n].lower() != pkg_components[n].lower():
                            flag = False
                    if (flag):
                        candidates.append(pkg)

        #install package
        if (len(candidates)== 1):
            command = superuser+" xbps-install "+candidates[0]
            print("\033[22;92m* \033[22;97m"+ command)
            os.system(command)
                
        else:
            print("\033[22;91mE \033[22;97mPackage not found")
    else:
        print("\033[22;91mE \033[22;97mAn error occurred")
else:
    print("\033[22;91mE \033[22;97mYou need to specify a package name")
