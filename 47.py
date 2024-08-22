# Validate IP address

# Function to check whether the string passed is valid or not
def valid_part(s):
	n = len(s)

	# If the length of the passed string is more than 3, it is not valid
	if n > 3:
		return False

	# Check if the string only contains digits, if not, return false
	for i in range(n):
		if not s[i].isdigit():
			return False

	# Convert the string to an integer
	x = int(s)

	# The string is valid if the number generated is between 0 to 255
	return 0 <= x <= 255

# Return True if the IP string is valid, else return False
def is_valid_ip(ip_str):
	# If the string is empty, return False
	if ip_str is None:
		return False

	parts = ip_str.split('.')
	count = 0

	# The number of dots in the original string should be 3 for it to be valid
	for i in range(len(ip_str)):
		if ip_str[i] == '.':
			count += 1

	if count != 3:
		return False

	for part in parts:
		if not valid_part(part):
			return False

	return True

# Driver code
ip1 = "128.0.0.1"
ip2 = "125.16.100.1"
ip3 = "125.512.100.1"
ip4 = "125.512.100.abc"

# Check and print whether the IPs are valid or not
print("Valid" if is_valid_ip(ip1) else "Not valid")
print("Valid" if is_valid_ip(ip2) else "Not valid")
print("Valid" if is_valid_ip(ip3) else "Not valid")
print("Valid" if is_valid_ip(ip4) else "Not valid")
