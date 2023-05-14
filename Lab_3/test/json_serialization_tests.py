import unittest
import math
from Lab_3.Serializer import SerializersFactory, SerializerType

from test_constants import PRIMITIVES
from test_constants import gen
from test_constants import decorated_func


class SerializationTestCase(unittest.TestCase):

    def setUp(self):
        self.json = SerializersFactory.create_serializer(SerializerType.JSON)

    def test_primitives(self):
        """Test primitive types json serialization"""

        primitives = self.json.dumps(PRIMITIVES)
        primitives = self.json.loads(primitives)

        self.assertEqual(PRIMITIVES, primitives)

    def test_gen(self):
        """Test gen serialization"""

        s_gen = self.json.dumps(gen)
        s_gen = self.json.loads(s_gen)

        before = [*gen()]
        after = [*s_gen()]

        self.assertEqual(before, after)

    def test_decorator(self):
        """Test decorator serialization"""

        df = self.json.dumps(decorated_func)
        df = self.json.loads(df)

        before = [decorated_func(i) for i in range(100)]
        after = [df(i) for i in range(100)]

        self.assertEqual(before, after)


if __name__ == '__main__':
    unittest.main()
