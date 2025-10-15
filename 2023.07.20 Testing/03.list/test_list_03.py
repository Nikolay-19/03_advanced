class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class ListTest(unittest.TestCase):
    def setUp(self):
        self.list1 = IntegerList(1, 2, 3, 4, 5.5)

    def test_initialization(self):
        self.assertEqual([1, 2, 3, 4], self.list1.get_data())

    def test_add_right_element(self):
        self.assertEqual([1, 2, 3, 4], self.list1.get_data())
        self.list1.add(5)
        self.assertEqual([1, 2, 3, 4, 5], self.list1.get_data())

    def test_add_wrong_element(self):
        self.assertEqual([1, 2, 3, 4], self.list1.get_data())
        with self.assertRaises(Exception) as ex:
            self.list1.add(5.5)
        self.assertEqual("Element is not Integer", str(ex.exception.args[0]))

    def test_remove_right_index(self):
        self.assertEqual([1, 2, 3, 4], self.list1.get_data())
        self.list1.remove_index(0)
        self.assertEqual([2, 3, 4], self.list1.get_data())

    def test_remove_wrong_index(self):
        self.assertEqual([1, 2, 3, 4], self.list1.get_data())
        with self.assertRaises(Exception) as ex:
            self.list1.remove_index(9)
        self.assertEqual("Index is out of range", str(ex.exception.args[0]))

    def test_get_right_index(self):
        self.assertEqual([1, 2, 3, 4], self.list1.get_data())
        el = self.list1.get(0)
        self.assertEqual(1, el)

    def test_get_wrong_index(self):
        self.assertEqual([1, 2, 3, 4], self.list1.get_data())
        with self.assertRaises(Exception) as ex:
            self.list1.get(9)
        self.assertEqual("Index is out of range", str(ex.exception.args[0]))

    def test_insert_integer_right_index(self):
        self.assertEqual([1, 2, 3, 4], self.list1.get_data())
        self.list1.insert(0, 5)
        self.assertEqual([5, 1, 2, 3, 4], self.list1.get_data())

    def test_insert_integet_wrong_index(self):
        self.assertEqual([1, 2, 3, 4], self.list1.get_data())
        with self.assertRaises(Exception) as ex:
            self.list1.insert(9, 5)
        self.assertEqual("Index is out of range", str(ex.exception.args[0]))

    def test_insert_non_integer(self):
        self.assertEqual([1, 2, 3, 4], self.list1.get_data())
        with self.assertRaises(Exception) as ex:
            self.list1.insert(0, 5.5)
        self.assertEqual("Element is not Integer", str(ex.exception.args[0]))

    def test_get_biggest(self):
        self.assertEqual([1, 2, 3, 4], self.list1.get_data())
        self.assertEqual(4, self.list1.get_biggest())

    def test_get_index_of_element(self):
        self.assertEqual([1, 2, 3, 4], self.list1.get_data())
        self.assertEqual(3, self.list1.get_index(4))


if __name__ == "__main__":
    unittest.main()
