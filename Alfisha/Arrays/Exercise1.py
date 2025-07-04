#  Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#   3. March - 2600
#   4. April - 2130
#   5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

exp = [2200, 2350, 2600, 2130, 2190]

print("Monthly expense list : ",exp)

# 1. In Feb, how many dollars you spent extra compare to January?
ex_exp = exp[1] - exp[0]
print("Dollars spent in feb extra compare to jan : ", ex_exp)

# 2. Find out your total expense in first quarter (first three months) of the year.
exp3 = exp[0] + exp[1] + exp[2]
print("Total expense in first quarter (first three months) of the year : ", exp3)

# 3. Find out if you spent exactly 2000 dollars in any month
print("Spent exactly 2000$ in any month?", 2000 in exp)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("Expense at the end of the june month : ",exp)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
exp[3] = exp[3] - 200
print("Correction list of monthly expense list after refund in month of april : ",exp)
