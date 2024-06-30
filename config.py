from ebook import Ebook
from ebook_parser import EbookParser

file_prefix = "data/"
extract_prefix = "extract/"

ignore_tags = [
    "img",
    "svg",
]
text_formater = [
    {
        "pattern": "\r\n",
        "repl": " ",
    }
]
ebook_repo = [
    Ebook(
        name="儿童教育心理学",
        path="儿童教育心理学.epub",
        type="epub",
        category="children_education",
        isbn="9787544272063",
        parser=EbookParser(
            ignore_files=[
                "cover1.html",
                "text00000.html",
                "text00001.html",
                "text00002.html",
                "text00003.html",
            ],
            ignore_tags=ignore_tags,
            text_formater=text_formater,
            initial="init",
            states=["init", "text", "p1", "p2"],
            level_mapping={
                "p1": 1,
                "p2": 2,
            },
            transitions=[
                {"trigger": "blockquote", "source": "*", "dest": "init"},
                {"trigger": "div", "source": "*", "dest": "init"},
                ##
                {"trigger": "p", "source": "init", "dest": "text"},
                {"trigger": "h1", "source": "init", "dest": "p1"},
                {"trigger": "h2", "source": "init", "dest": "p2"},
                ##
                {"trigger": "p", "source": "text", "dest": "text"},
                {"trigger": "h1", "source": "text", "dest": "p1"},
                {"trigger": "h2", "source": "text", "dest": "p2"},
                ##
                {"trigger": "p", "source": "p1", "dest": "text"},
                ##
                {"trigger": "p", "source": "p2", "dest": "text"},
            ],
        ),
    ),
    Ebook(
        name="培养高情商的孩子",
        path="培养高情商的孩子.epub",
        type="epub",
        category="children_education",
        isbn="9787213055416",
        parser=EbookParser(
            ignore_files=[
                "cover1.html",
                "text00000.html",
                "text00001.html",
                "text00002.html",
                "text00003.html",
                "text00004.html",
                "text00004.html",
                "text00006.html",
                "text00009.html",
                "text000010.html",
            ],
            ignore_tags=ignore_tags,
            text_formater=text_formater,
            initial="init",
            states=["init", "text", "p1", "p2", "p3"],
            level_mapping={
                "p1": 1,
                "p2": 2,
                "p3": 3,
            },
            transitions=[
                {"trigger": "blockquote", "source": "*", "dest": "init"},
                {"trigger": "div", "source": "*", "dest": "init"},
                {"trigger": "hr", "source": "*", "dest": "init"},
                ##
                {"trigger": "p", "source": "init", "dest": "text"},
                {"trigger": "h1", "source": "init", "dest": "p1"},
                {"trigger": "h2", "source": "init", "dest": "p2"},
                ##
                {"trigger": "p", "source": "text", "dest": "text"},
                {"trigger": "h1", "source": "text", "dest": "p1"},
                {"trigger": "h2", "source": "text", "dest": "p2"},
                {"trigger": "h3", "source": "text", "dest": "p3"},
                ##
                {"trigger": "p", "source": "p1", "dest": "text"},
                {"trigger": "h2", "source": "p1", "dest": "p2"},
                ##
                {"trigger": "p", "source": "p2", "dest": "text"},
                {"trigger": "h3", "source": "p2", "dest": "p3"},
                ##
                {"trigger": "p", "source": "p3", "dest": "text"},
            ],
        ),
    ),
    Ebook(
        name="孩子如何思考",
        path="孩子如何思考.epub",
        type="epub",
        isbn="9787213093913",
        category="children_education",
        parser=EbookParser(
            ignore_files=[
                "cover1.html",
                "text/part0000.html",
                "text/part0001.html",
                "text/part0002.html",
                "text/part0003.html",
                "text/part0004.html",
                "text/part0005.html",
                "text/part0007_split_000.html",
                "text/part0007_split_001.html",
                "text/part0011_split_000.html",
                "text/part0011_split_001.html",
                "text/part0014_split_000.html",
                "text/part0014_split_001.html",
            ],
            ignore_tags=ignore_tags,
            text_formater=text_formater,
            initial="init",
            states=["init", "text", "p1", "p2", "p3"],
            level_mapping={
                "p1": 1,
                "p2": 2,
                "p3": 3,
            },
            transitions=[
                {"trigger": "blockquote", "source": "*", "dest": "init"},
                {"trigger": "div", "source": "*", "dest": "init"},
                {"trigger": "hr", "source": "*", "dest": "init"},
                ##
                {"trigger": "p", "source": "init", "dest": "text"},
                {"trigger": "h1", "source": "init", "dest": "p1"},
                {"trigger": "h3", "source": "init", "dest": "p2"},
                ##
                {"trigger": "p", "source": "text", "dest": "text"},
                {"trigger": "h1", "source": "text", "dest": "p1"},
                {"trigger": "h3", "source": "text", "dest": "p2"},
                {"trigger": "h4", "source": "text", "dest": "p3"},
                ##
                {"trigger": "p", "source": "p1", "dest": "text"},
                {"trigger": "h3", "source": "p1", "dest": "p2"},
                ##
                {"trigger": "p", "source": "p2", "dest": "text"},
                {"trigger": "h4", "source": "p2", "dest": "p3"},
                ##
                {"trigger": "p", "source": "p3", "dest": "text"},
            ],
        ),
    ),
    Ebook(
        name="美国儿科学会育儿百科：第7版 ",
        path="美国儿科学会育儿百科：第7版 .epub",
        type="epub",
        category="children_education",
        isbn="9787571409005",
        parser=EbookParser(
            ignore_files=[
                "Text/feiye.xhtml",
                "Text/copyright.xhtml",
                "Text/Chapter3.xhtml",
                "Text/Chapter4.xhtml",
                "Text/Chapter5.xhtml",
                "Text/Chapter6.xhtml",
                "Text/Chapter7.xhtml",
                "Text/Chapter8.xhtml",
                "Text/Chapter47.xhtml",
                "Text/Chapter48.xhtml",
                "Text/cover.xhtml",
                "Text/TOC.xhtml",
            ],
            ignore_tags=ignore_tags,
            text_formater=text_formater,
            initial="init",
            states=["init", "text", "p1", "p2", "p3", "p4"],
            level_mapping={
                "p1": 1,
                "p2": 2,
                "p3": 3,
                "p4": 4,
            },
            transitions=[
                {"trigger": "blockquote", "source": "*", "dest": "init"},
                {"trigger": "div", "source": "*", "dest": "init"},
                {"trigger": "hr", "source": "*", "dest": "init"},
                {"trigger": "table", "source": "*", "dest": "init"},
                ##
                {"trigger": "p", "source": "init", "dest": "text"},
                {"trigger": "li", "source": "init", "dest": "text"},
                {"trigger": "h1", "source": "init", "dest": "p1"},
                {"trigger": "h2", "source": "init", "dest": "p2"},
                {"trigger": "h3", "source": "init", "dest": "p3"},
                {"trigger": "h4", "source": "init", "dest": "p4"},
                ##
                {"trigger": "h1", "source": "text", "dest": "p1"},
                {"trigger": "h2", "source": "text", "dest": "p2"},
                {"trigger": "h3", "source": "text", "dest": "p3"},
                {"trigger": "h4", "source": "text", "dest": "p4"},
                ##
                {"trigger": "h2", "source": "p1", "dest": "p2"},
                {"trigger": "h3", "source": "p2", "dest": "p3"},
                {"trigger": "h4", "source": "p3", "dest": "p4"},
                ##
                {"trigger": "p", "source": "text", "dest": "text"},
                {"trigger": "p", "source": "p1", "dest": "text"},
                {"trigger": "p", "source": "p2", "dest": "text"},
                {"trigger": "p", "source": "p3", "dest": "text"},
                {"trigger": "p", "source": "p4", "dest": "text"},
                ##
                {"trigger": "li", "source": "text", "dest": "text"},
                {"trigger": "li", "source": "p1", "dest": "text"},
                {"trigger": "li", "source": "p2", "dest": "text"},
                {"trigger": "li", "source": "p3", "dest": "text"},
                {"trigger": "li", "source": "p4", "dest": "text"},
            ],
        ),
    ),
]
