import requests
import os
from dotenv import load_dotenv


def shorten_link(token, url):
    api_url_template = 'https://api.vk.ru/method/utils.getShortLink'
    headers = {'Authorization': f'Bearer {token}'}
    params = {
        # VK API version
        'v': '5.236',
        # URL to be shortened
        'url': url,
        'private': 0
    }
    api_url = api_url_template
    response = requests.get(api_url, headers=headers, params=params)
    response.raise_for_status()

    print(response)
    print(response.text)
    print(response.json())
    error = ''
    short_url = ''
    if response.ok and response.json().get("response"):
        short_url = response.json().get("response").get("short_url")
    if response.ok and response.json().get("error"):
        error = response.json().get("error").get("error_msg")
    return error, short_url


def main():
    load_dotenv()
    VK_SERVICE_TOKEN = os.environ.get('VK_SERVICE_TOKEN')

    #url = 'dvmn.org/modules'
    url = input()

    error = ''
    short_url = ''

    try:
        error, short_url = shorten_link(VK_SERVICE_TOKEN, url)
    except requests.exceptions.HTTPError as e:
        print(f'Error: {e}')
        return

    if error:
        print('API error:', error)
        return

    print('Сокращенная ссылка:', short_url)


if __name__ == '__main__':
    main()
