import requests


def main():

    url_template = 'https://wttr.in/{}'
    headers = {'Accept-Language': 'ru-RU'}
    locations = [
        'london',
        'svo',
        'Череповец'
    ]
    params = {
        'lang': 'ru',
        'M': '',
        'm': '',
        'T': '',
        'n': '',
        'q': '',
    }

    for location in locations:
        url = url_template.format(location)
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
