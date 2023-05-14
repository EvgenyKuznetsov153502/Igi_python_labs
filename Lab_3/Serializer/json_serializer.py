import re
import regex
from base_serializer import BaseSerializer
from dict_serializer import DictSerializer

from constants import nonetype


class JsonSerializer(BaseSerializer):

    NF_LITERAL = str(1E1000)
    NAN_LITERAL = str(1E1000 / 1E1000)

    TRUE_LITERAL = "true"
    FALSE_LITERAL = "false"

    NULL_LITERAL = "null"

    INT_PATTERN = fr"[+-]?\d+"
    FLOAT_PATTERN = fr"(?:[+-]?\d+(?:\.\d+)?(?:e[+-]?\d+)?|[+-]?{INF_LITERAL}\b|{NAN_LITERAL}\b)"
    BOOL_PATTERN = fr"({TRUE_LITERAL}|{FALSE_LITERAL})\b"
    STRING_PATTERN = fr"\"(?:(?:\\\")|[^\"])*\""
    NULL_PATTERN = fr"\b{NULL_LITERAL}\b"

    ELEMENTARY_TYPES_PATTERN = fr"{FLOAT_PATTERN}|{INT_PATTERN}|{BOOL_PATTERN}|{STRING_PATTERN}|{NULL_PATTERN}"

    # This regex use recursive statements to be able to capture nested lists and objects.
    ARRAY_PATTERN = r"\[(?R)?(?:,(?R))*\]"
    OBJECT_PATTERN = r"\{(?:(?R):(?R))?(?:,(?R):(?R))*\}"

    VALUE_PATTERN = fr"\s*({ELEMENTARY_TYPES_PATTERN}|" + \
                    fr"{ARRAY_PATTERN}|{OBJECT_PATTERN})\s*"

    def __dumps_from_dict(self, obj) -> str:
        if type(obj) in (int, float):
            return str(obj)

        if type(obj) is bool:
            return self.TRUE_LITERAL if obj else self.FALSE_LITERAL

        if type(obj) is str:
            return '"' + self.__mask_quotes(obj) + '"'

        if type(obj) is nonetype:
            return self.NULL_LITERAL

        if type(obj) is list:
            return '[' + ", ".join([self.__dumps_from_dict(item) for item in obj]) + ']'

        if type(obj) is dict:
            return '{' + ", ".join([f"{self.__dumps_from_dict(item[0])}: "
                                    f"{self.__dumps_from_dict(item[1])}" for item in obj.items()]) + '}'
        else:
            raise ValueError


