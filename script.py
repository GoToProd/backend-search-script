import requests
from bs4 import BeautifulSoup

with open("input.txt", "rb") as myfile:
    data = myfile.read()
    print(data.decode())

var = data.decode().replace(' ', '+')
response = requests.get(f"https://google.com/search?q={var}")
soup = BeautifulSoup(response.text, 'lxml')
div_list = soup.find_all('div')

print(len(div_list))
result = list()
for item in div_list:
    try:
        tag_a = item.find_all('a')[0]
        tag_h3 = tag_a.find_all("h3")[0]
        href = tag_a.get('href').replace('/url?q=', '')
        if not href.startswith('/search'):
            string = f"{tag_h3.text} -- {href}"
            if string not in result:
                result.append(string)
    except:
        pass

for item in result:
    with open("result.txt", "a+") as f:
        f.write(f"{item}\n\n\n")
