from unittest import TestCase
import Exam


class test_exam(TestCase):
    def test_fizzbuzz_1(self):
        self.exam = Exam.Exam()
        print("Testing 1 and 15")
        self.assertEqual(self.exam.fizzbuzz(1, 16), [5, 3, 1])

    def test_fizzbuzz_2(self):
        self.exam = Exam.Exam()
        print("Testing 1 and 60")
        self.assertEqual(self.exam.fizzbuzz(1, 60), [19, 11, 3])

    def test_fizzbuzz_3(self):
        self.exam = Exam.Exam()
        print("Testing 1 and 500")
        self.assertEqual(self.exam.fizzbuzz(1, 500), [166, 99, 33])

    def test_fizzbuzz_4(self):
        self.exam = Exam.Exam()
        print("Testing 1700 and 30000")
        self.assertEqual(self.exam.fizzbuzz(1700, 30000), [9433, 5660, 1886])

