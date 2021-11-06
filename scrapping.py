import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/all'
domain = "https://habr.com"

response = requests.get(url)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, features='html.parser')
articles = soup.find_all('article')

print(f'Статьи с сайта {url}, с присутствием ключевых слов {KEYWORDS}')
print(f'Дата - Заголовок - Ссылка')


def find_article(current_article, article_scrap):
    for key in KEYWORDS:
        if key.title() in article_scrap or key.lower() in article_scrap or key.upper() in article_scrap:

            title = current_article.find('h2').text.strip()
            href = current_article.find(class_='tm-article-snippet__title-link').attrs['href']
            current_link = domain + href
            #  вытащили заголовок и ссылку

            data = current_article.find("span", class_="tm-article-snippet__datetime-published").find("time").get("title")
            #  вытаскиеваем по тегу time дату и время из title
            print(f'{data} - {title} - {current_link}. ключевое слово: {key}')
            break
print()

print('Поиск по превью')
for article in articles:
    preview = article.find("div", class_="tm-article-body tm-article-snippet__lead").text.strip()
    #  Получаем превью статей
    find_article(article, preview)

print()