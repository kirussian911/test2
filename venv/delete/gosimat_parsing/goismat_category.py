import requests
from fake_useragent import UserAgent
import fake_useragent
from bs4 import BeautifulSoup as bs
import csv
from time import sleep
import os


def get_html(url):
    user_agent = fake_useragent.UserAgent()
    user = user_agent.random
    cookies = dict(cookies_are='working')
    headers = {'User-Agent': UserAgent().chrome}
    r = requests.get(url, headers=headers, cookies=cookies, timeout=5)

    return r.text


def get_file(url):
    user_agent = fake_useragent.UserAgent()
    user = user_agent.random
    cookies = dict(cookies_are='working')
    headers = {'User-Agent': UserAgent().chrome}
    r = requests.get(url, headers=headers, cookies=cookies, timeout=5, stream=True)
    return r


def get_name(title):
    name_image = title.split('/')[-2]
    new_name = ''.join(name_image).split('-')[:-1]
    folder_category = '_'.join(new_name)  # chemical_products
    print(folder_category)
    # try:
    #     os.mkdir(path)
    # except OSError:
    #     print("Создать директорию %s не удалось" % path)
    # else:
    #     print("Успешно создана директория %s " % path)
    os.makedirs(r'D:\gosimat', exist_ok=True)
    folder = os.path.abspath(r'D:\gosimat' + folder_category)
    return print(os.makedirs(r'D:\gosimat', exist_ok=True))



links = []
def get_all_linlks(html):
    soup = bs(html, 'html.parser')
    ads = soup.find('aside', class_='col-lg-3 col-md-3 col-sm-3 p_top_4').find('ul', class_='categories_list second_font w_break')

    for ids, litag in enumerate(ads.find_all('li')):
        link = 'http://gosimat.pt' + litag.find('a').get('href')
        links.append(link)
        print(link)

    return links



def page_sliding_door(link):
    soup = bs(link, 'html.parser')

    try:
        title = soup.find('h3', class_="second_font m_bottom_10").text.splitlines()[2]
        print(title)
    except Exception as err:
        title = ''
    try:
        description = soup.find('div', id="tab1").text.splitlines()[2]
    except Exception as err:
        description = ''
    try:
        available_options = soup.find('div', id="tab1").text.splitlines()[5].strip('-').strip('»')
    except Exception as err:
        available_options = ''
    try:
        t_application_type = soup.find('div', id="tab1").find('table').text.splitlines()  # 'Drywall | Plaster'
        application_type = list(filter(None, t_application_type))[1]
    except Exception as err:
        application_type = ''
    try:
        t_door_type = soup.find('div', id="tab1").find('table').text.splitlines()  # 'Glass'
        door_type = list(filter(None, t_door_type))[3]
    except Exception as err:
        door_type = ''
    try:
        t_max_door_weight = soup.find('div', id="tab1").find('table').text.splitlines()  # '80 kg'
        max_door_weight = list(filter(None, t_max_door_weight))[5]
    except Exception as err:
        max_door_weight = ''
    try:
        t_pocket_frame_thickness = soup.find('div', id="tab1").find('table').text.splitlines()  # '70 | 90 mm'
        pocket_frame_thickness = list(filter(None, t_pocket_frame_thickness))[7]
    except Exception as err:
        pocket_frame_thickness = ''
    try:
        t_min_wall_thickness = soup.find('div', id="tab1").find('table').text.splitlines()  # 96 | 116 mm
        min_wall_thickness = list(filter(None, t_min_wall_thickness))[9]
    except Exception as err:
        min_wall_thickness = ''
    try:
        img = soup.find('ul', class_="slides").find('a').get('href')
    except Exception as err:
        img = ''

    # save_image(get_name(title, img), get_file(img))



def main():
    url = 'http://gosimat.pt/en/products/'
    html = get_html(url)
    link = get_all_linlks(html)

    for i in link:
        get_name(i)


    # for i in link:
    #     sleep(5)
    #     print(i)
    #     link_html = get_html(i)
    #     link_page = page_sliding_door(link_html)


if __name__ == '__main__':
    main()
