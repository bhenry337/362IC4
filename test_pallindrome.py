import unittest
import pallindrome
class TestCase(unittest.TestCase):
	def test_ispal(self):
		self.assertEqual(pallindrome.pallindrome("anna"),"Pallindrome")

	def test_notpal(self):
		self.assertEqual(pallindrome.pallindrome("atna"), "Not Pallindrome")

	def test_enternum(self):
		self.assertEqual(pallindrome.pallindrome(123), "Not Pallindrome")

