# Proxy-Verifier
 A simple python script that checks if proxies are active and HTTPS-enabled 
 
 ## Usage
1. Install `requests` module
2. Run the `proxy_test.py` coupled with the names of the text files containing proxies to be tested

Example: 
```console
python proxy_test.py list1.txt list2.txt
```

3. After script completes running, it will create two text files - `success_list` (active proxies) & `success_list_secure` (active and HTTPS enabled proxies). Those are your working proxies. 

### Use Case

I wrote this script to test free proxy lists and create a reliable proxy pool for web scraping:

a. Download list of free proxies/Use a script that creates free proxies list by scraping proxy sites\
b. use Proxy-Verifier to test those lists and create a list of free, active and safe proxies\
c. Use generated list as proxy pool for your web scraper
