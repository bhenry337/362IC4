def words(string):
	if isinstance(string, str):
		words = len(string.split())
		return words
	else:
		return "Enter string"

