
def pallindrome(val):
	rvs = val[::-1]

	if val == rvs:
		return "Pallindrome"
	else:
		return "Not Pallindrome"
