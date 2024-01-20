from requests import get
from bs4 import BeautifulSoup
from re import compile, search

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.2210.144'}

def get_articles_length(url):

    soup = get(url, headers=headers).content
    soup = BeautifulSoup(soup, 'html.parser')

    div_recents_posts = soup.find('div', attrs={'id':'recent-posts-2'})
    link = div_recents_posts.find('a')
    
    title_last_article = link.text.strip().lower()
    
    number_last_article = search(r'cap[ií]tulo (\d+) –', title_last_article).group(1)
    
    return int(number_last_article)

def get_pages(url):
    
    print(url)
    response = get(url, headers=headers)
    soup = response.content
    soup = BeautifulSoup(soup, 'html.parser')

    article = soup.find('article', attrs={'id':compile("post-(.+?)")})
    
    next_page = soup.find('a', attrs={'rel':'next'})
    if next_page is not None:
        next_title_article = next_page.text.strip()
        next_page = next_page['href'].strip()
    
    return {
        'next_page':next_page,
        'article':article
    }