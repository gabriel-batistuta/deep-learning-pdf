import os
import pdfkit
import platform
from tqdm import tqdm

def mount_html(articles:list):
    book_string = ''
    start_html = """
    <html>
    <head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
    </head>
    <body>"""
    end_html = """</body>
    </html>"""
    book_string = start_html
    for article in articles:
        book_string += str(article)
    book_string += end_html
    
    return book_string

def _get_wkhtmltopdf_config():
    if platform.system() == 'Windows': 
        try:
            path_wkhtmltopdf = os.popen('where wkhtmltopdf').read()
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            return config
        except:
            path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            return config
    else:
        try:
            path_wkhtmltopdf = os.popen('which wkhtmltopdf').read()
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            return config
        except:
            try:
                path_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf'
                config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
                return config
            except:
                path_wkhtmltopdf = '/Applications/wkhtmltopdf.app/Contents/MacOS/wkhtmltopdf'
                config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
                return config

def make_pdf(book_string:str):    
    pdfkit.from_string(book_string, f'./deep_learning.pdf', 
    configuration=_get_wkhtmltopdf_config(), css='templates/.css', options={
        'enable-local-file-access': None, 
        'encoding':'UTF-8', 
        '--image-quality': 100
    })