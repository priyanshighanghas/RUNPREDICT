import sys
import unittest

sys.path.insert(0, "src")

from algorithms import factorial, fibonacci, reverse_number, gcd, sum_to_n
from validation import valid_menu_choice, same_output
from progress import new_progress, record_answer


class TestAlgorithms(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(6), 8)

    def test_reverse(self):
        self.assertEqual(reverse_number(1234), 4321)

    def test_gcd(self):
        self.assertEqual(gcd(24, 18), 6)

    def test_sum(self):
        self.assertEqual(sum_to_n(5), 15)


class TestValidation(unittest.TestCase):
    def test_menu(self):
        self.assertTrue(valid_menu_choice("3", 1, 5))
        self.assertFalse(valid_menu_choice("9", 1, 5))

    def test_output(self):
        self.assertTrue(same_output("18", "18"))
        self.assertFalse(same_output("17", "18"))


class TestProgress(unittest.TestCase):
    def test_progress(self):
        progress = new_progress()
        record_answer(progress, True)
        record_answer(progress, False)
        self.assertEqual(progress["attempts"], 2)
        self.assertEqual(progress["correct"], 1)


if __name__ == "__main__":
    unittest.main()
