import sys
import requests
from bs4 import BeautifulSoup

# import urllib3

# urllib3.disable_warnings()

class MyBs4:

    @staticmethod
    def read_page(url):
        soup=None
        USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0"
        headers = {"user-agent": USER_AGENT}
        try:
            resp = requests.get(url, headers=headers, verify=False)
            code = resp.status_code 
        except requests.exceptions.ConnectionError as e:
            print("Error Read Url", e)
        if code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
        return soup
    
    @staticmethod
    def get_links(url):
        soup= MyBs4.read_page(url)
        if soup is None: return []
        response =[]
        for tag_a in soup.find_all('a'):
            if tag_a.has_attr('href'):
                url = tag_a['href']
                if '#' in url or '@' in url or 'tel:' in url:
                    add_element = False
                else:
                    add_element = True
            if add_element==True and url not in response:
                response.append(url) 
        return response

    @staticmethod
    def read_content_url(url,tag, obj_id):
        print(f"leyendo: {url} -> {tag} - {obj_id}")
        soup = MyBs4.read_page(url)
        if soup is None: return None
        content = soup.find(tag, obj_id)
        return content





