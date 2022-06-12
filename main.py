# Some Ideas from: KIPAS, Geruays & Revan AR
# Script created by PhynX

import requests, threading, datetime, sys, os

os.system('cls' if os.name == 'nt' else 'clear')
print(f"\t   Simple Crown/Trophy Duplicators for Stumble Guys")
print(f"\t\t\tBy: KIPASGTS & PhynX")
print("="*64)
api = "kitkabackend.eastus.cloudapp.azure.com:5010"
auth = str(input("Auth Key: "))
pos = int(input("""0 = Round 1 (Eliminated)
1 = Round 2 (Eliminated)
2 = Round 3 (Eliminated)
3 = Round 3 (Winner)
Note: Please input Correctly to Avoid Ban.
Input: """))
thr = int(input("Threads: "))

def s():
        while True:
                dt = datetime.datetime.now()
                try:
                        headers = {
                            'authorization': auth,
                            'use_response_compression': 'true',
                            'Accept-Encoding': 'gzip',
                            'Host': api,
                            'Connection': None,
                            'User-Agent': None,
                        }
                        response = requests.get(f'http://{api}/round/finishv2/{pos}', headers=headers)
                        if response.status_code == 200:
                                trof = response.text.split('"SkillRating":')[1].split(',')[0]
                                cro = response.text.split('"Crowns":')[1].split(',')[0]
                                sys.stdout.write(f"\r[{dt.year}-{dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}] SUCCESS!! | Trophy: {trof} | Crowns: {cro}")
                                sys.stdout.flush()
                        else:
                                print(f"[{response.status_code}] Failed")
                except Exception as e:
                        print(e)
                        sys.exit(0)

for _ in range(thr):
        threading.Thread(target=s).start()
