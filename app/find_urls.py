from in_out_data import InOutData
from my_bs4 import MyBs4
from configparser import ConfigParser
import urllib3
from urllib.parse import urlparse
urllib3.disable_warnings()


class FindUrls():
    config = ConfigParser()
    config.read('config.ini')

    folder = config['common']['folder_export']

    data_yml = config['find_urls']['data_yml']

    urls = {'url': True}

    def __init__(self, domain, exclude=None):

        self.exclude = exclude
        self.name_file = self.extract_name_to_url(domain)
        self.domain = domain
        self.first_pass(domain)
        self.run_all_links()

    def extract_name_to_url(self, url):
        parts = urlparse(url)
        name = parts.hostname.replace(".", '_')
        return name

    def first_pass(self, domain):
        # page = MyBs4.read_page(domain)
        links = MyBs4.get_links(domain)
        self.prepare_links(links)

    def run_all_links(self):
        new_links = []
        for link in self.urls:
            if not self.urls[link]:
                new_links += MyBs4.get_links(link)
                self.urls[link] = True
        size_links = len(self.urls)
        self.prepare_links(new_links)
        if size_links < len(self.urls):
            self.run_all_links()
        else:
            self.create_yaml_data()

    def prepare_links(self, links):
        for link in links:
            if link.startswith('http'):
                if not link.startswith(self.domain):
                    link = None
            else:
                link = self.domain + link
            # if link is not None and self.exclude is not None:
            #     for excl in self.exclude.split(','):
            #         if excl in link:
            #             link = None

            if link is not None:
                if link not in self.urls:
                    self.urls[f"{link}"] = False
        print(f"{len(self.urls)} enlaces capturados")

    def create_yaml_data(self):
        data = self.data_yml
        last_key = list(data.keys())[-1]
        for link in self.urls:
            data[last_key].append(link)
        InOutData.create_yaml_data(self.name_file, data)


if __name__ == "__main__":

    params = InOutData.read_file_params()

    FindUrls(params['url'], "/tags,/categories")
