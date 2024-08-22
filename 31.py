# House Robber

# Find maximum possible stolen value from houses (House Robber)


# There are N houses built in a line, each of which contains some value in it. 
# A thief is going to steal the maximum value of these houses, but he can’t steal 
# in two adjacent houses because the owner of the stolen houses will tell his 
# two neighbors left and right sides. The task is to find what is the maximum stolen value.

# calculate the maximum stolen value 
def maxLoot(hval,n): 

	# base case 
	if (n < 0): 
		return 0

	if (n == 0): 
		return hval[0] 
	
	# if current element is pick then previous cannot be 
	# picked 
	pick = hval[n] + maxLoot(hval, n - 2)

	# if current element is not picked then previous 
	# element is picked 
	notPick = maxLoot(hval, n - 1)


	# return max of picked and not picked 
	return max(pick, notPick) 

# Driver to test above code 
hval = [ 6, 7, 1, 3, 8, 2, 4 ] 
n = len(hval) 
print("Maximum loot possible : ",maxLoot(hval, n - 1)); 

# This code is contributed by shinjanpatra
