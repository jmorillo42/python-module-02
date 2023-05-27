import sys
import unittest
from io import StringIO

from src.ex03.csvreader import CsvReader


class Ex03TestCase(unittest.TestCase):
    @staticmethod
    def __test_filename(filename: str):
        with CsvReader(filename, skip_top=18, skip_bottom=0) as reader:
            if reader is None:
                print("File is corrupted or missing")
            else:
                print(reader.getheader(), end="\n")
                print(reader.getdata(), end="\n\n")
        with CsvReader(filename, header=True, skip_top=17, skip_bottom=0) as reader:
            if reader is None:
                print('File is corrupted or missing')
            else:
                print(reader.getheader(), end="\n")
                print(reader.getdata(), end="\n\n")

    def test_good_csv(self):
        print('2.03.01: good.csv')
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out

            self.__test_filename('../res/good.csv')

            output = out.getvalue().strip()
            self.assertEqual(output, '''None
[['Ruth', 'F', '28', '65', '131']]

['Name', 'Sex', 'Age', 'Height (in)', 'Weight (lbs)']
[['Ruth', 'F', '28', '65', '131']]''')
        finally:
            sys.stdout = saved_stdout
        print(f'  output: {output}')

    def test_bad_csv(self):
        print('2.03.02: bad.csv')
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out

            self.__test_filename('../res/bad.csv')

            output = out.getvalue().strip()
            self.assertEqual(output, 'File is corrupted or missing\nFile is corrupted or missing')
        finally:
            sys.stdout = saved_stdout
        print(f'  output: {output}')

    def test_unicorn_csv(self):
        print('2.03.03: unicorn.csv')
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out

            self.__test_filename('../res/missing.csv')

            output = out.getvalue().strip()
            self.assertEqual(output, 'File is corrupted or missing\nFile is corrupted or missing')
        finally:
            sys.stdout = saved_stdout
        print(f'  output: {output}')


if __name__ == '__main__':
    unittest.main()
