# hash matcher 
# based on code from: https://tryhackme.com/room/pythonforcybersecurity
import hashlib
from time import sleep
print("""
--------------------------------------
BAT SLAPPER Beta              /^;;^\\
MD5 & SHA256 hash matcher 
--------------------------------------
""")
wordlist = input("path to wordlist: ")
hash_in = input("hash value: ")
count = 0
kind = input("Select: 1 ~ MD5 \nor 2 ~ SHA256  ").strip().lower()
if kind == '2':
    sha = True
    md = False
else:
    md = True
    sha = False
if kind not in ['1','2']:
    print("defaulting to MD5\n")
    sleep(2)     	
with open(wordlist, 'r') as f:
    for line in f.readlines():
        count += 1 
        if md:
            hash_ob = hashlib.md5(line.strip().encode())
        if sha: 
            hash_ob = hashlib.sha256(line.strip().encode())

        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_in:
            broken_pass = line.strip()            
            print(f"\n\nOne match: {broken_pass}. Wah ah ah ah ah!")
            exit(0)
        else:
    	    print(f"flapping {count} times so far.")
print(f"""
                       {count} words checked!
/^;;^\ Zero m5d hashes matched! 
                               Wah ah ah ah ah! 

""") 
