
def pallindrome(val):
	if isinstance(val, str):
		rvs = val[::-1]

		if val == rvs:
			return "Pallindrome"
		else:
			return "Not Pallindrome"
	else:
		return "Enter string"

