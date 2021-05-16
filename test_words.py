import unittest
import words
class TestCase(unittest.TestCase):
	def test_five(self):
		self.assertEqual(words.words("anna is a good person"),5)

	def test_notpal(self):
		self.assertEqual(words.words(""), 0)

	def test_enternum(self):
		self.assertEqual(words.words(123), "Enter string")
