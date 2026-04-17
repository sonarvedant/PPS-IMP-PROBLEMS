#to calculate salary of employee given his basic pay . 
#calculate gross salary of employee . let hra be 10% of basic pay and TA be 5% of basic pay .
# let employee pay professional tax as 2% of total salary .
# calculate net salary payable after deductions
a = float(input("enter basic pay of employee: "))
hra = 0.1*a
ta = 0.05*a
gross_salary = a + hra + ta
tax = 0.02*gross_salary
net_salary = gross_salary - tax
print("gross salary is : ",gross_salary)
print("net salary is : ",net_salary)
