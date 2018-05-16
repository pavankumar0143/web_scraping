import requests
from bs4 import BeautifulSoup
import time
from constants import MAX_RETRIES, GOOD_STATUS


class GetRequest:
    def __init__(self):
        self.return_data = None

    def get_content(self, url):
        try:
            response = self.get_request(url)
            if response is None:
                return None
            else:
                return BeautifulSoup(response.content, "lxml")
        except Exception as e:
            print("Error in get_content requesting again| {}".format(e))
            return self.get_content(url)

    def get_request(self, url):

        for _ in range(MAX_RETRIES):
            try:
                self.return_data = requests.get(url)
                # req = urlopen(url)
                # print(req)
                if self.return_data.status_code == GOOD_STATUS:
                    break

                else:
                    print("got invalid response | {}".format(url))
                    time.sleep(3)

            except Exception as e:
                print("waiting to get response | {} | {}".format(url, e))
                time.sleep(3)

        return self.return_data

#print(get_content("https://www.etsy.com/in-en/search/accessories?explicit=1&use_mmx=1"))
