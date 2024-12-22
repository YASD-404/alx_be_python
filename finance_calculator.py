income=float(input("Enter your monthly income: "))
expenses=float(input("Enter your total monthly expenses: "))
saving=income-expenses
projected_savings=saving * 12 + saving * 12 * 0.05
print("Your monthly savings are $", saving)
print("Projected savings after one year, with interest, is: $",projected_savings)