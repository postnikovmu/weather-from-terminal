import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(token, link):
    url_template = 'https://api.vk.ru/method/utils.getShortLink'
    headers = {'Authorization': f'Bearer {token}'}
    params = {
        # VK API version
        'v': '5.236',
        # URL to be shortened
        'url': link,
        'private': 0
    }
    url = url_template
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    print(response)
    print(response.text)
    print(response.json())
    api_error_msg = ''
    short_link = ''
    if response.ok and response.json().get("response"):
        short_link = response.json().get("response").get("short_url")
    if response.ok and response.json().get("error"):
        api_error_msg = response.json().get("error").get("error_msg")
    return api_error_msg, short_link


def count_clicks(token, link):

    parsed = urlparse(link)
    key = parsed.path.replace('/', '')
    print("key:", key)

    url_template = 'https://api.vk.ru/method/utils.getLinkStats'
    headers = {'Authorization': f'Bearer {token}'}
    params = {
        # VK API version
        'v': '5.236',
        # Shortened link (part of the URL after “vk.cc/”)
        'key': key,
        'extended': 0
    }
    url = url_template
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    print(response)
    print(response.text)
    print(response.json())
    api_error_msg = ''
    clicks_count = 0
    if response.ok and response.json().get("response"):
        clicks_count = int(response.json().get("response").get("stats")[0].get("views"))
    if response.ok and response.json().get("error"):
        api_error_msg = response.json().get("error").get("error_msg")
    return api_error_msg, clicks_count


def main():
    load_dotenv()
    VK_SERVICE_TOKEN = os.environ.get('VK_SERVICE_TOKEN')

    #link = 'dvmn.org/modules'
    link = input()

    try:
        api_error_msg_shorten_link, short_link = shorten_link(VK_SERVICE_TOKEN, link)
        api_error_msg_count_clicks, clicks_count = count_clicks(VK_SERVICE_TOKEN, short_link)
    except requests.exceptions.HTTPError as e:
        print(f'Exception error: {e}')
        return

    if api_error_msg_shorten_link:
        print('API error message for shorten link operation:', api_error_msg_shorten_link)
        return

    if api_error_msg_count_clicks:
        print('API error message for count clicks:', api_error_msg_count_clicks)
        return

    print('Сокращенная ссылка:', short_link)
    print('Количество кликов по ссылке:', clicks_count)


if __name__ == '__main__':
    main()
