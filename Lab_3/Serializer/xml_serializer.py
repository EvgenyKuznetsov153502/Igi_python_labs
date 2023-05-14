import re

import regex
from base_serializer import BaseSerializer
from dict_serializer import DictSerializer

from constants import nonetype


class XmlSerializer(BaseSerializer):

    NONE_LITERAL = "null"

    KEY_GROUP_NAME = "key"
    VALUE_GROUP_NAME = "value"

    XML_SCHEME_SOURCE = "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " + \
                        "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\""

    XML_SCHEME_PATTERN = "xmlns:xsi=\"http://www\.w3\.org/2001/XMLSchema-instance\" " + \
                         "xmlns:xsd=\"http://www\.w3\.org/2001/XMLSchema\""

    ELEMENTARY_NAMES_PATTERN = "int|float|bool|str|NoneType|list|dict"

    XML_ELEMENT_PATTERN = fr"(\<(?P<{KEY_GROUP_NAME}>{ELEMENTARY_NAMES_PATTERN})\>" + \
                          fr"(?P<{VALUE_GROUP_NAME}>([^<>]*)|(?R)+)\</(?:{ELEMENTARY_NAMES_PATTERN})\>)"

    FIRST_XML_ELEMENT_PATTERN = fr"(\<(?P<{KEY_GROUP_NAME}>{ELEMENTARY_NAMES_PATTERN})\s*({XML_SCHEME_PATTERN})?\>" + \
                                fr"(?P<{VALUE_GROUP_NAME}>([^<>]*)|(?R)+)\</(?:{ELEMENTARY_NAMES_PATTERN})\>)"

    def __dumps_from_dict(self, obj, is_first=False) -> str:
        if type(obj) in (int, float, bool, nonetype):
            return self.__create_xml_element(type(obj).__name__, str(obj), is_first)

        if type(obj) is str:
            data = self.__mask_symbols(obj)
            return self.__create_xml_element(str.__name__, data, is_first)

        if type(obj) is list:
            data = ''.join([self.__dumps_from_dict(o) for o in obj])
            return self.__create_xml_element(list.__name__, data, is_first)

        if type(obj) is dict:
            data = ''.join(
                [f"{self.__dumps_from_dict(item[0])}{self.__dumps_from_dict(item[1])}" for item in obj.items()])
            return self.__create_xml_element(dict.__name__, data, is_first)

        else:
            raise ValueError
