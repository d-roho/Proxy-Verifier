#cd Rohit\PyEnvironments\amazon_scraper\AmazonBestsellerScraper\scrapy_files\scrapy_files\spiders\
"""This script takes given proxy lists and separates active proxies and active proxies confirmed safe to use into two new text files  
To be used as proxy pools for web scrapers"""

import sys
import requests
import urllib.parse 
proxy_lists = [] #list of proxy lists provided by user as command line arguments 
proxies_list = [] # proxies extracted from provided proxy lists 
success_list = [] # active proxy servers
success_list_secure = [] #active, HTTPS enabled proxy servers

#read command line argument for proxy lists
for i in range(len(sys.argv)):
	if i == 0:
		continue
	proxy_lists.append(sys.argv[i])
	print(f"Proxy List - {sys.argv[i]} read successfully")

# read proxy lists and create list of proxies
for i in range(len(proxy_lists)):
	proxies_list = proxies_list + open(str(proxy_lists[i]), "r").read().strip().split("\n") 

# eliminating duplicate proxies
no_duplicates = []
[no_duplicates.append(x) for x in proxies_list if x not in no_duplicates]
proxies_list = no_duplicates

print(f'Proxies List - {proxies_list}')


def get(url, proxy):
# checks if proxy is active 
	try: 
		# Send proxy requests to the final URL 
		response = requests.get(url, proxies={'http': f"http://{proxy}"}, timeout=1)
		reply = response.status_code
		if reply == 200:   
			print (proxy)
			success_list.append(proxy)
			print("added to success_list")
	except: 
		print("fail")

def sec_check(proxy):
#checks if proxy is safe (HTTPS enabled) 	
	try:
	# verify and create list of HTTPS enabled proxies 
		params = {'proxies': f"{proxy}\n", 'type': 'html', 'key': ''}
		query = urllib.parse.urlencode(params)
		url = f"https://proxycheck.haschek.at/api.php?&{query}"
		print(url)
		response = requests.post(url, timeout=10)
		results = response.json()
		if results.get("results", {}).get("", {}).get('https') is True:
			print(proxy)
			success_list_secure.append(proxy)
			print("added to success_list_secure")
		else: print("HTTPS not supported by this proxy")			
	except: 
		print("fail")

# creating list of active proxies
for i in range(len(proxies_list)):
	proxy = proxies_list[i]
	get("http://ident.me/", proxy) 

print("active proxies seperated")

# creating list of safe proxies 
for i in range(len(success_list)):
	proxy = success_list[i]
	sec_check(proxy)

print("secure proxies seperated")

# write active proxies to txt file
with open('success_list.txt', 'w') as fp:
    for item in success_list:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')

#write safe proxies to txt file
with open('success_list_secure.txt', 'w') as fp:
    for item in success_list_secure:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')

