
import requests
import re
from bs4 import BeautifulSoup

class MyTypeError(TypeError):
    def __init__(self, var_name, var):
        super().__init__(f"incorrect type for {var_name}: {type(var)}")


class HTTPRequestsError(Exception):
    def __init__(self, requests_code: int, requests_message: str):
        super().__init__(f"{requests_code}: {requests_message}")
        

class HTTP_Requests_parser:
    def __init__(self, tag: str):
        if not isinstance(tag, str):
            raise MyTypeError("tag", tag)
        self.__tag = tag
        self.__urls = []
        

    def get_list_from_file(path: str) -> list:

        if not isinstance(path, str):
            raise MyTypeError("path", path)
        
        fd = open(path, "r", encoding="utf8")
        words = fd.read().split()
        fd.close()
        return words
    

    def add_url(self, url):
        if isinstance(url, str):
            self.__urls.append(url)
        elif isinstance(url, list):
            self.__urls.extend(url)
        else:
            raise MyTypeError("url", url)
        

    def get_list_of_words(self):
        words = []
        
        for url in self.__urls:
            response = requests.get(url)
            if response.status_code != 200:
                raise HTTPRequestsError(response.status_code,
                                        response.reason)
            soup = BeautifulSoup(response.text, features="html.parser")
            for i in soup.find_all(self.__tag):
                words.append(i.text)
        return words


def search_ipv6_in_text(list_of_word: list) -> list:
    
    if not isinstance(list_of_word, list):
        raise MyTypeError("list_of_word", list_of_word)
    
    redex = r"[0-9a-f]{0,4}(?:[:.][0-9a-f]{0,4}){7}"
    tandem = []
    for i in list_of_word:

        matched_list = re.findall(redex, i)
        if len(matched_list) > 0:

            word = matched_list[0]
            tandem.append(word)

    return tandem if len(tandem) > 0 else None


def get_list_from_file(path: str) -> list:
    if not isinstance(path, str):
        raise MyTypeError("path", path)
    
    fd = open(path, "r", encoding="utf8")
    words = fd.read().split("\n")
    fd.close()
    return words


def file_data():
    words = get_list_from_file("test_input.txt")
    print("FILE: ", search_ipv6_in_text(words))


def url_data():
    url = 'https://ru.wikipedia.org/wiki/IPv6'

    tag_name = "p" #pre, th
    site = HTTP_Requests_parser(tag_name)
    site.add_url(url)
    print("URL: ", search_ipv6_in_text(site.get_list_of_words()))


def main():
    try:
        file_data()
        url_data()
    except Exception as e:
        print("Error: ", e)
  
    
if __name__ == "__main__":
    main()

