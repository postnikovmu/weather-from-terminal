import requests
import os
from dotenv import load_dotenv


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

    clicks_count = 0
    return clicks_count


def main():
    load_dotenv()
    VK_SERVICE_TOKEN = os.environ.get('VK_SERVICE_TOKEN')

    #link = 'dvmn.org/modules'
    link = input()

    try:
        api_error_msg_shorten_link, short_link = shorten_link(VK_SERVICE_TOKEN, link)
    except requests.exceptions.HTTPError as e:
        print(f'Exception error: {e}')
        return

    if api_error_msg_shorten_link:
        print('API error message for shorten link operation:', api_error_msg_shorten_link)
        return

    print('Сокращенная ссылка:', short_link)


if __name__ == '__main__':
    main()
