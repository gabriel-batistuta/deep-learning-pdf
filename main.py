from dl_pdf import get_articles_length, get_pages, mount_html, make_pdf
from tqdm import tqdm
import requests

INITIAL_URL = 'https://www.deeplearningbook.com.br/deep-learning-a-tempestade-perfeita/'

FINAL_URL = 'https://www.deeplearningbook.com.br/machine-learning-guia-definitivo-parte-9/'

if __name__ == '__main__':

    articles_length = get_articles_length(INITIAL_URL)

    with tqdm(total=articles_length) as progress_bar:
        progress_bar.desc=f'carregando artigos...'
        progress_bar.colour='blue'
        page = get_pages(INITIAL_URL)
        articles = []
        print(page['article'])
        articles.append(page['article'])
        next_page = page['next_page']
        progress_bar.update(1)
        
        while next_page is not None:
            page = get_pages(next_page)
            article = page['article']
            # print(article)
            articles.append(article)
            # print(articles)
            progress_bar.update(1)
            next_page = page['next_page']
            # print(page['next_page'])
           
        
        book_string = mount_html(articles)
        print(f'making the pdf on: ./deep_learning.pdf')
        make_pdf(book_string)