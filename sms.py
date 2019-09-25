# MR.BELL

from requests import Session
import re, sys
s = Session()

try:
	print(''' \033[96m	
         _,met$$$$$gg.           
      ,g$$$$$$$$$$$$$$$P.        
    ,g$$P""       """Y$$.".      
   ,$$P'              `$$$.      
  ',$$P       ,ggs.     `$$b:    
  `d$$'     ,$P"'   .    $$$     
   $$P      d$'     ,    $$P     
   $$:      $$.   -    ,d$$'     
   $$\;      Y$b._   _,d$P'      
   Y$$.    `.`"Y$$$$P"'          
   `$$b      "-.__
    `Y$$
     `Y$$.
       `$$b.
         `Y$$b.
            `"Y$b._
                `""""
|Version   : V.1(Beta)      |
|Team      : THE NEXT LEVEL |
|Create    : Mr.Bell        |
| Free SMS FOR ALL OPERATOR |
############################## \n \033[91m''')

	
	no = int(input(" Nomor : "))
	msg = input(" Pesan : ")
except:
	print("\n\t* Cek nomermu atau pesanmu! *")
	sys.exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
    'Referer': 'http://sms.payuterus.biz/alpha/'
}

bypass = s.get("http://sms.payuterus.biz/alpha/?a=keluar", headers=headers).text
key = re.findall(r'value="(\d+)"', bypass)[0]
jml = re.findall(r'<span>(.*?) = </span>', bypass)[0]
captcha = eval(jml.replace("x", "*").replace(":", "/"))

data = {
	'nohp':no,
	'pesan':msg,
	'captcha':captcha,
	'key':key
}

send = s.post("http://sms.payuterus.biz/alpha/send.php", headers=headers, data=data).text

if 'SMS Gratis Telah Dikirim' in send:
	print(f"\n  [ Pengiriman sukses ]\n  [ {no} : {msg} ]\n")
elif 'MAAF....!' in send:
	print("\n  [ Mohon tunggu 15 menit untuk mengirim pesan yg sama ]\n")
else:
	print("\n  [ Pengiriman gagal ]\n")
