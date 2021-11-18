import unittest
from sample import my_func

class SampleTest(unittest.TestCase):
    '''Sample test for code quality demo'''

    def test_foo_foo(self):
        foo = 'foo'
        result = my_func(foo)
        self.assertTrue(result)

    def test_foo_bar(self):
        foo = 'bar'
        result = my_func(foo)
        self.assertTrue(result)