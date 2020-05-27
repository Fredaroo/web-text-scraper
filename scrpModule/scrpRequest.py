from bs4 import BeautifulSoup
import dbModule.dataArch as dbArch
import requests

# To be implemented
# import threading
i = 1


def set_initial_loc(fetched_length):
    global i
    i = fetched_length


def scrp_loop(data_size):
    global i

    while i < data_size:
        fetched_url = dbArch.get_url(i)
        if fetched_url == "NA":
            i = i + 1
        else:
            try:
                response = requests.get(fetched_url, verify=True, timeout=60)
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
            # Queue error catches :
            except requests.exceptions.ConnectionError:
                output = "HTTP_ERROR"
                dbArch.upload_content(output, i)
                i = i + 1
            except requests.HTTPError:
                output = "HTTP_ERROR"
                dbArch.upload_content(output, i)
                i = i + 1
            except requests.exceptions.BaseHTTPError:
                output = "HTTP_ERROR"
                dbArch.upload_content(output, i)
                i = i + 1
            except requests.exceptions.InvalidURL:
                output = "HTTP_ERROR"
                dbArch.upload_content(output, i)
                i = i + 1
            except requests.exceptions.StreamConsumedError:
                output = "HTTP_ERROR"
                dbArch.upload_content(output, i)
                i = i + 1
            except requests.exceptions.ChunkedEncodingError:
                output = "HTTP_ERROR"
                dbArch.upload_content(output, i)
                i = i + 1
            except requests.exceptions.ReadTimeout:
                output = "HTTP_ERROR"
                dbArch.upload_content(output, i)
                i = i + 1
