import unittest

# def add(a, b):
#     return a + b


# def subtract(a, b):
#     return a - b




# class TestMathFunctions(unittest.TestCase):

#     def test_add(self):
#         self.assertEqual(add(3, 4), 7)
#         self.assertEqual(add(-1, 1), 0)
#         self.assertEqual(add(-1, -1), -2)

#     def test_subtract(self):
#         self.assertEqual(subtract(10, 5), 5)
#         self.assertEqual(subtract(-1, -1), 0)
#         self.assertEqual(subtract(-1, 1), -2)


# unittest.main()



class Test(unittest.TestCase):
    
    def setlist(self):
        self.list = []
    
    def testappend(self):
        self.list.append(1)
        self.assertEqual