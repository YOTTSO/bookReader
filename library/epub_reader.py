from ebooklib import epub
from bs4 import BeautifulSoup


def extract_epub_content(file_path):
    book = epub.read_epub(file_path)
    chapters = []

    for item in book.items:
        if item.get_type() == epub.EpubItem:
            soup = BeautifulSoup(item.content, 'html.parser')
            text = soup.get_text()
            chapters.append(text)

    return chapters
