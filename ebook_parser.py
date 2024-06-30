import re
from typing import Union
from transitions import Machine, State


class EbookParagraph(object):

    def __init__(self) -> None:
        self.__map = {}
        pass

    def __init_map(self, level: int) -> None:
        if level not in self.__map:
            self.__map[level] = ""

    def clear_paragraph(self, level: int) -> None:
        if self.__map:
            for key_level in self.__map.keys():
                if key_level > level:
                    self.__map[key_level] = ""

    def set_paragraph(self, content: str, level: int, append: bool) -> None:
        self.__init_map(level)
        if append:
            self.__map[level] += content
        else:
            self.__map[level] = content
        self.clear_paragraph(level)

    def get_paragraph(self) -> list[str]:
        paragraph = []
        for key in sorted(self.__map):
            if self.__map[key]:
                paragraph.append(self.__map[key])
        return paragraph


class EbookText(object):

    def __init__(self) -> None:
        self.clear()

    def set_text(self, text: str, append: bool) -> str:
        if append:
            self.text += text
        else:
            self.clear()
            self.text = text

    def clear(self) -> None:
        self.text = ""

    def get_text(self) -> str:
        return "" if self.text == None else self.text


class EbookParser(object):

    def __init__(
        self,
        ignore_files: list[str],
        ignore_tags: list[str],
        states: list[str],
        transitions: list[dict],
        initial: str,
        level_mapping: dict,
        text_formater: dict,
    ) -> None:
        self.ignore_files = ignore_files
        self.ignore_tags = ignore_tags
        self.machine = Machine(
            model=self,
            states=[State(s, on_enter=self.on_enter) for s in states],
            transitions=transitions,
            initial=initial,
            send_event=True,
        )
        self.text_formater = text_formater
        self.__level_mapping = level_mapping
        self.__paragraph = EbookParagraph()
        self.__text = EbookText()

    def extract_element(self, element) -> list[Union[str, str]]:
        elements = []
        if element == '\n':
            return elements
        tag, name = element.name, element.text
        if tag != "div" and tag != 'ol':
            elements = [(tag, name)]
        else:
            for c in element.children:
                elements += self.extract_element(c)
        return elements

    def parse(self, tag: str, content: str, debug: bool = False) -> None:
        if debug:
            print(f"current:{self.state},trigger:{tag},content={content}")
        self.trigger(
            tag,
            content=content,
            previous_state=self.state,
        )

    def on_enter(self, event) -> None:
        content = self.__get_data_from_event(event, "content")
        previous_state = self.__get_data_from_event(event, "previous_state")
        self.__text.clear()
        if self.is_text():
            self.__text.set_text(content, append=False)
        if self.is_paragraph():
            append = False
            if previous_state == self.state:
                append = True
            self.__paragraph.set_paragraph(
                content=content,
                level=self.__level_mapping[self.state],
                append=append,
            )

    def is_text(self):
        return self.state == "text"

    def is_paragraph(self):
        return self.state in self.__level_mapping

    def __get_data_from_event(self, event, key) -> str:
        return event.kwargs[key]

    def get_paragraph(self) -> list[str]:
        return [self.text_format(t) for t in self.__paragraph.get_paragraph()]

    def get_text(self) -> str:
        return self.text_format(self.__text.get_text())

    def text_format(self, content) -> str:
        for f in self.text_formater:
            content = re.sub(pattern=f["pattern"], repl=f["repl"], string=content)
        return content.strip()
