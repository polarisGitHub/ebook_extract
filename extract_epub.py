import json
import codecs
import config
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

print_files, print_tags, print_parse = False, False, False
files, tags = [], set()


def extract(isbn: str):
    book_info = list(filter(lambda x: x.isbn == isbn, config.ebook_repo))[0]
    book = epub.read_epub(config.file_prefix + book_info.path)

    htmls = []
    book_parser = book_info.parser
    for item in book.get_items():
        file_name = item.get_name()
        if file_name in book_info.parser.ignore_files:
            continue
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            if print_files:
                print(file_name)
            soup = BeautifulSoup(item.get_content(), "lxml")
            for c in soup.body.children:
                elements = book_parser.extract_element(c)
                if len(elements) == 0:
                    continue
                htmls += list(
                    filter(
                        lambda x: len(x["content"])>0 and x['tag'] not in book_parser.ignore_tags,
                        [
                            {
                                "file_name": file_name,
                                "tag": tag,
                                "content": content,
                            }
                            for (tag, content) in elements
                        ],
                    )
                )
                for t in [tag for (tag, _) in elements]:
                    tags.add(t)

    if print_tags:
        print(tags)

    contents = []
    for h in htmls:
        file_name, tag, content = h["file_name"], h["tag"], h["content"]
        if print_parse:
            print(file_name)
        book_parser.parse(tag, content=content, debug=print_parse)
        text, paragraph = book_parser.get_text(), book_parser.get_paragraph()
        if book_parser.is_paragraph() or len(text) == 0:
            continue
        contents.append(
            {
                "text": text,
                "paragraph": paragraph,
            }
        )

    with codecs.open(
        config.extract_prefix + book_info.name + ".json",
        mode="w",
        encoding="utf-8",
    ) as f:
        json.dump(
            {
                "name": book_info.name,
                "category": book_info.category,
                "isbn": book_info.isbn,
                "contents": contents,
            },
            f,
            ensure_ascii=False,
        )


if __name__ == "__main__":
    for book in config.ebook_repo:
        extract(book.isbn)
