from ebook_parser import EbookParser


class Ebook(object):

    def __init__(
        self,
        name: str,
        path: str,
        type: str,
        category: str,
        isbn: str,
        parser: EbookParser,
    ) -> None:
        self.name = name
        self.path = path
        self.type = type
        self.category = category
        self.isbn = isbn
        self.parser = parser
