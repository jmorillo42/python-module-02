import sys
import unittest
from io import StringIO

from src.ex01.main import what_are_the_vars, doom_printer


class Ex01TestCase(unittest.TestCase):
    def test_none(self):
        print('2.01.00: With None as unique parameter')
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out

            obj = what_are_the_vars(None)
            doom_printer(obj)

            output = out.getvalue().strip()
            self.assertEqual(output, 'var_0: None\nend')
        finally:
            sys.stdout = saved_stdout

    def test_function_arg_and_function_karg(self):
        print('2.01.01: With a function as argument and a function as keyword argument')
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out

            obj = what_are_the_vars(lambda x: x, function=what_are_the_vars)
            doom_printer(obj)

            output = out.getvalue().strip()
            self.assertNotRegex(output,
                                r'function: <function what_are_the_vars at 0x[0-9a-f]+>\nvar_0: <function <lambda> at 0x[0-9a-f]+>\nend')
        finally:
            sys.stdout = saved_stdout

    def test_arg_named_var_0(self):
        print('2.01.02: With a kwarg named var_0')
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out

            obj = what_are_the_vars(3, var_0=2)
            doom_printer(obj)

            output = out.getvalue().strip()
            self.assertEqual(output, 'ERROR\nend')
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
