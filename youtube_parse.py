import re
import datetime
import requests


def get_likes(page_source_code):
    """
    :param page_source_code = requests.get('url').text
    :return: value of likes: int
    """
    match = re.findall(r'\"likeStatus\":\"[\w]+\",\"[\w]+\":\"([\w\W]+?) /[\w\W]+?\"}},', page_source_code)
    match = match[0].replace('\xa0', '')  # removing non-break spaces
    return int(match)


def get_dislikes(page_source_code):
    match = re.findall(r'\"likeStatus\":\"[\w]+\",\"[\w]+\":\"[\w\W]+? / ([\w\W]+?)\"}},', page_source_code)
    match = match[0].replace('\xa0', '')
    return int(match)


def get_views(page_source_code):
    match = re.findall(r'\{\"viewCount\":\{\"[\w]+\":\"([\w\W]*?) [\s\S]+?\"}', page_source_code)
    match = match[0].replace('\xa0', '')
    return int(match)


def get_name(page_source_code):
    match = re.findall(r'<meta name=\"title\" content=\"([\s\S]+?)\">', page_source_code)
    return match[0]


def get_duration(page_source_code):
    """

    :param page_source_code = requests.get('url').text
    :return: duration in milliseconds
    """
    match = re.search(r'\"approxDurationMs\":\"([\d]+)\"', page_source_code)
    return int(match.group(1))


def get_publish_date(page_source_code):
    """

    :param page_source_code = requests.get('url').text
    :return: date of publishing 'YYYY-mm-dd'
    """
    months = {
        'янв': 1, 'февр': 2, 'мар': 3, 'апр': 4, 'мая': 5, 'июн': 6,
        'июл': 7, 'авг': 8, 'сен': 9, 'окт': 10, 'нояб': 11, 'дек': 12,
    }
    match = re.search(r'\"dateText\":\{\"simpleText\":\"([\d]+?)[\s]([а-я]{3,4}).?[\s+?]([\d]+?)[\s][а-я]\.\"\}\}\}', page_source_code)
    date = datetime.date(int(match[3]), months[match[2]], int(match[1]))
    return str(date)


def collect_data_from_page(url: str):
    try:
        r = requests.get(url)
    except requests.exceptions.MissingSchema:
        print(f'Cannot access page: {url}')
        return False
    text = r.text
    return (get_name(text),
            get_duration(text),
            get_likes(text),
            get_dislikes(text),
            get_views(text),
            get_publish_date(text))

a = collect_data_from_page('s')