your_expenses={"Hotel":2000,
               "Food":1000,
               "Transportation":500,
               "Clothes":1500,
               "Miscellaneous":100}

partner_expenses={"Hotel":1500,
                  "Food":2000,
                  "Transportation":300,
                  "Clothes":900,
                  "Miscellaneous":500}

#Calculate total Expenses of each
total_yourExpense=sum(your_expenses.values())
total_partnerExpense=sum(partner_expenses.values())

print("Your total expenses:",total_yourExpense)
print("Your Partner's total expenses:",total_partnerExpense)

#Calculate who spents more
if(total_yourExpense>total_partnerExpense):
    print("You spent more money overall")
elif(total_partnerExpense>total_yourExpense):
    print("Your Partner spent more money overall")
else:
    print("Both spent equally")

#For max diff and its category
max_diff_category=None
max_diff=0
for category in your_expenses:
    diff=abs(your_expenses[category]-partner_expenses[category])

    if(diff>max_diff):
        max_diff=diff
        max_diff_category=category
print(f"The maximum diffenece is in {max_diff_category} category is {max_diff}")
