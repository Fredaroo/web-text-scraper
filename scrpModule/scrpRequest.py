from bs4 import BeautifulSoup
import dbModule.dataArch as dbArch
import requests

# To be implemented
# import threading


def scrp_loop(data_size):
    i = 0

    while i < data_size:
        fetched_url = dbArch.get_url(i)
        if fetched_url == "NA":
            i = i + 1
        else:
            response = requests.get(fetched_url)
            html_content = BeautifulSoup(response.text, "html.parser")
            text = html_content.find_all(text=True)
            output = ''
            blacklist = [
                '[document]',
                'noscript',
                'header',
                'html',
                'meta',
                'head',
                'input',
                'script',
                'style',
                'footer',
                'button',
                'li',
                'span',
            ]
            for t in text:
                if t.parent.name not in blacklist:
                    output += '{} '.format(t)
            dbArch.upload_content(output, i)
            i = i + 1
