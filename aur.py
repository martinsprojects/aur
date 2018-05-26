import sys
import subprocess
def bash_command(cmd):
    subprocess.Popen(cmd, shell=True, executable='/bin/bash')
""" INSTALL AUR FILE """
def aur_install(pkgname):
    """ get extension """
    ending = len(pkgname) - 7
    endname = ''
    extension = ''
    extensiontest = False
    
    for i in range(-7, 0):
        endname = endname + str(pkgname[i])
    extension = endname
    endname = ''
    """ get filename"""
    while extensiontest == False:
        for i in range(len(pkgname)):
            if str(pkgname[i]) != '.':
                endname = endname+str(pkgname[i])
                #extendlist = list(endname)
            elif str(pkgname[i]) == '.':
                extensiontest=True
                break
        break
    commands = 'tar -xvf '+str(pkgname)+' && cd '+endname+' && makepkg -si'
    bash_command(commands)
try:
    aur_install(sys.argv[1])
except:
    print("Usage: In packaged tarball directory use name of tarball as argument for installing from AUR like this:\n python ~/scripts/aur.py package_name.tar.gz'\n")