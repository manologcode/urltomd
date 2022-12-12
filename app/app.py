#!/usr/bin/python

from markdownify import markdownify
import urllib.parse

from in_out_data import InOutData
from find_urls import FindUrls
from my_bs4 import MyBs4

class UrlToMd():

  config = InOutData.read_yaml('config.yml')

  folder = config['folder_export']

  def __init__(self, tag=None, selector=None):
    self.tag = tag
    self.selector = selector

  def create_file(self, name, data):
    f = open(f'{self.folder}{name}', 'a')
    f.write(data)
    f.close()

  def read_list(self,list):
      for item in list:
        self.url_to_file(item)

  def url_to_file(self, url):
    if MyBs4.uri_exists(url): 
      name_file = UrlToMd.extract_name_to_url(url) + '.md'
      md_text=self.html_to_md(url)
      if md_text is not None:
        print(f'creando: {name_file}')
        self.create_file(name_file, md_text)

  def html_to_md(self,url):
      html_text=MyBs4.read_content_url(url,self.tag, self.selector)
      if html_text is None: return None
      text_md = markdownify(str(html_text), heading_style="ATX")
      return text_md
  
  @staticmethod
  def extract_name_to_url(url):
    url_s = urllib.parse.unquote(url)
    parts = url_s.split('/')
    name = parts[-1] if parts[-1]!="" else parts[-2]
    return name

if __name__ == '__main__':
  
  param = InOutData.read_params()

  if param is not None:
    in_data = InOutData.read_yaml(param["file"])
    md = UrlToMd(in_data['tag'],in_data['selector'])
    md.read_list(in_data['pages'])
  else:
    menu = {
        'title': 'CONVERT URL TO MARKDOWN',
        'description': 'Convertir una url o conjunto de urls en archivo markdown. \n \
            Se puede introducir una url o pasar un archivo con un conjunto de url mediante un archivo yml. \n \
            Este programa también genera automáticamente este archivo con todas las urls encontradas a partir de una url inicial',
            'items': [ 
                '1 - Introducir url para convertir en markdown',
                '2 - Crear archivo yml de links a partir una url inicial'
                ]
    }

    opt = InOutData.menu(menu)

    if opt == '1':
      config = {
              'title': "Convertir a markdown la siguiente url ",
              'fields': {
                  'url': 'Url: '
                  }  
              }
      in_data = InOutData.input_data(config)
      md = UrlToMd()
      md.url_to_file(in_data['url'])

    elif opt == '2':
      config = {
              'title': "Crear archivo yml a partir de la búsqueda automática de enlace sobre url",
              'fields': {
                  'url': 'Url inicio: ',
                  }  
              }
      in_data = InOutData.input_data(config)
      FindUrls(in_data['url'])

