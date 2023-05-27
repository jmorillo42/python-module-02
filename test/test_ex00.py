import collections.abc
import unittest

from src.ex00.ft_filter import ft_filter
from src.ex00.ft_map import ft_map
from src.ex00.ft_reduce import ft_reduce


class Ex00TestCase(unittest.TestCase):
    def test_ft_filter_is_generator(self):
        print('Example 2: Checking the return type of ft_filter')
        x = [1, 2, 3, 4, 5]
        print(f'  input: {x}')
        result = ft_filter(lambda n: not (n % 2), x)
        print(f'  type: {type(result)}')
        self.assertIsInstance(result, collections.abc.Generator)

    def test_ft_filter_even_numbers(self):
        print('Example 2: ft_filter even numbers')
        x = [1, 2, 3, 4, 5]
        print(f'  input: {x}')
        print('  lambda n: not (n % 2)')
        result = list(ft_filter(lambda n: not (n % 2), x))
        print(f'  output: {result}')
        self.assertEqual(result, [2, 4])

    def test_ft_map_is_generator(self):
        print('Example 1: ft_map check the return type')
        x = [1, 2, 3, 4, 5]
        print(f'  input: {x}')
        result = ft_map(lambda n: n + 1, x)
        print(f'  type: {type(result)}')
        self.assertIsInstance(result, collections.abc.Generator)

    def test_ft_map_add_one(self):
        print('Example 1: ft_map add one to all the numbers in the list')
        x = [1, 2, 3, 4, 5]
        print(f'  input: {x}')
        print('  lambda n: n + 1')
        result = list(ft_map(lambda num: num + 1, x))
        print(f'  output: {result}')
        self.assertEqual(result, [2, 3, 4, 5, 6])

    def test_ft_reduce_concatenate_letters(self):
        print('Example 3: ft_reduce concatenation of letters')
        lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
        print(f'  input: {lst}')
        result = ft_reduce(lambda u, v: u + v, lst)
        print(f'  result: {result}')
        self.assertEqual(result, "Hello world")

    def test_ft_map_plus_two_in_empty_list(self):
        print('2.00.00: ft_map add two to all the numbers in empty list')
        x = []
        print(f'  input: {x}')
        print('  lambda n: n + 2')
        result = list(ft_map(lambda num: num + 2, x))
        print(f'  output: {result}')
        self.assertEqual(result, [])

    def test_ft_map_plus_two_in_list_with_one_element(self):
        print('2.00.01: ft_map add two to all the numbers in a list with one element')
        x = [1]
        print(f'  input: {x}')
        print('  lambda n: n + 2')
        result = list(ft_map(lambda num: num + 2, x))
        print(f'  output: {result}')
        self.assertEqual(result, [3])

    def test_ft_map_square_in_list(self):
        print('2.00.02: ft_map square all the numbers in a list')
        x = [1, 2, 3, 4, 5]
        print(f'  input: {x}')
        print('  lambda n: n^2')
        result = list(ft_map(lambda num: num ** 2, x))
        print(f'  output: {result}')
        self.assertEqual(result, [1, 4, 9, 16, 25])

    def test_ft_filter_less_or_equal_one_in_empty_list(self):
        print('2.00.03: ft_filter numbers less than or equal to one in empty list')
        x = []
        print(f'  input: {x}')
        print('  lambda n: n ≤ 1')
        result = list(ft_filter(lambda num: num <= 1, x))
        print(f'  output: {result}')
        self.assertEqual(result, [])

    def test_ft_reduce_sum_all_numbers_in_a_list_with_one_element(self):
        print('2.00.04: ft_reduce sum all the numbers in a list with one element')
        numbers = [1]
        print(f'  input: {numbers}')
        print('  lambda x, y: x + y')
        result = ft_reduce(lambda x, y: x + y, numbers)
        print(f'  output: {result}')
        self.assertEqual(result, 1)

    def test_ft_reduce_multiply_all_numbers_in_a_list(self):
        print('2.00.05: ft_reduce multiply all the numbers in a list')
        numbers = [1, 2, 3, 4]
        print(f'  input: {numbers}')
        print('  lambda x, y: x * y')
        result = ft_reduce(lambda x, y: x * y, numbers)
        print(f'  output: {result}')
        self.assertEqual(result, 24)


if __name__ == '__main__':
    unittest.main()
