import inspect
from Serializer import nonetype, moduletype, codetype, celltype, functype, bldinfunctype, smethodtype, \
    cmethodtype, mapproxytype, wrapdesctype, metdesctype, getsetdesctype, \
    CODE_PROPS, UNIQUE_TYPES


class DictSerializer:
    TYPE_KW = "type"
    SOURCE_KW = "source"

    CODE_KW = "__code__"
    GLOBALS_KW = functype.__globals__.__name__
    NAME_KW = "__name__"
    DEFAULTS_KW = "__defaults__"
    CLOSURE_KW = functype.__closure__.__name__

    BASES_KW = "__bases__"
    DICT_KW = "__dict__"

    CLASS_KW = "__class__"

    OBJECT_KW = "object"

    @classmethod
    def to_dict(cls, obj, is_inner_func=False):
        if type(obj) in (int, float, bool, str, nonetype):
            return obj

        if type(obj) is list:
            return [cls.to_dict(o) for o in obj]

        if type(obj) is dict:
            return {cls.TYPE_KW: dict.__name__,
                    cls.SOURCE_KW: [[cls.to_dict(item[0]), cls.to_dict(item[1])] for item in obj.items()]}

        if type(obj) in (set, frozenset, tuple, bytes, bytearray):
            return {cls.TYPE_KW: type(obj).__name__,
                    cls.SOURCE_KW: cls.to_dict([*obj])}

        if type(obj) is complex:
            return {cls.TYPE_KW: complex.__name__,
                    cls.SOURCE_KW: {complex.real.__name__: obj.real,
                                    complex.imag.__name__: obj.imag}}

