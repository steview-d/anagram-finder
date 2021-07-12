import finder
import unittest
import sys
import io


class TestAnagram(unittest.TestCase):
    input_1 = 'input1.txt'
    input_2 = 'input2.txt'
    input_3 = 'input3.txt'
    input_4 = 'input4.txt'
    input_5 = 'input5.txt'

    def test_input_1(self):
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            finder.main(self.input_1)
            output = out.getvalue()
            self.assertEqual(output.strip(), "no anagrams found")
        finally:
            sys.stdout = saved_stdout

    def test_input_2(self):
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            finder.main(self.input_2)
            output = out.getvalue()
            self.assertEqual(output.strip(), "eat tea")
        finally:
            sys.stdout = saved_stdout

    def test_input_3(self):
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            finder.main(self.input_3)
            output = out.getvalue()
            self.assertEqual(output.strip(), "no anagrams found")
        finally:
            sys.stdout = saved_stdout

    def test_input_4(self):
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            finder.main(self.input_4)
            output = out.getvalue()
            self.assertEqual(output.strip(), "pots stop spot")
        finally:
            sys.stdout = saved_stdout

    def test_input_5(self):
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            finder.main(self.input_5)
            output = out.getvalue()
            self.assertEqual(output.strip(),
                             "on pots no stop eat ate spot tea")
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
