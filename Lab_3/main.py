from Serializer import JsonSerializer, XmlSerializer, SerializersFactory, SerializerType


class MyClass:
    a = 10

    @staticmethod
    def info(x):
        return x*x


if __name__ == '__main__':

    s = SerializersFactory.create_serializer(SerializerType.JSON)
    a = s.dumps(MyClass)
    l = s.loads(a)
    obj = l
    print(obj.info(2))




