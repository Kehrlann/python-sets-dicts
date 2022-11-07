import unittest
from timeit import timeit
from custom_set import add, contains, size, create


class TestCustomSet(unittest.TestCase):

    def test_not_set(self):
        self.assertNotIsInstance(
            create(), set, "Le custom_set ne doit pas un vrai set(), mais une liste")

    def test_size(self):
        empty = create()
        one = create()
        many = create()

        add(one, "something")
        add(many, "foo")
        add(many, "bar")

        self.assertEqual(
            size(empty), 0, "Un set vide doit avoir une taille de 0")
        self.assertEqual(
            size(one), 1, "Un set avec un élément doit avoir une taille de 1")
        self.assertGreater(size(
            many), 1, "Un set avec plusieurs éléments doit avoir une taille strictement supérieure 1")

    def test_add_simple(self):
        empty = create()
        one = create()
        many = create()

        add(one, "1")
        add(many, "1")
        add(many, "2")

        self.assertFalse(contains(empty, "1"),
                         "Un set vide ne doit pas contenir '1'")
        self.assertFalse(contains(empty, "2"),
                         "Un set vide ne doit pas contenir '2'")
        self.assertTrue(contains(one, "1"), "Le set ['1'] doit contenir '1'")
        self.assertFalse(contains(one, "2"),
                         "Le set ['1'] ne doit pas contenir '2'")
        self.assertTrue(contains(many, "1"),
                        "Le set ['1', '2'] doit contenir '1'")
        self.assertTrue(contains(many, "2"),
                        "Le set ['1', '2'] doit contenir '2'")

    def test_no_duplicates(self):
        one = create()

        add(one, "1")
        add(one, "1")

        self.assertEqual(
            size(one), 1, "Le set ne doit pas contenir deux fois le même élément")

    def test_faster_than_list(self):
        iterations = 10_000
        custom_list = [str(x) for x in range(iterations)]

        custom_set = create()
        for i in range(iterations):
            add(custom_set, str(i))

        time_with_list = timeit("'alpha' in custom_list", number=100, globals={
                                "custom_list": custom_list})
        time_with_set = timeit("contains(custom_set, 'alpha')", number=100, globals={
                               "custom_set": custom_set, "contains": contains})

        self.assertGreater(time_with_list, time_with_set * 100,
                           "Le set doit être beaucoup plus rapide qu'une liste")


if __name__ == '__main__':
    unittest.main(verbosity=2)
