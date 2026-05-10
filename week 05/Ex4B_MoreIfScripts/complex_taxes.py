# Calculating federal tax based on annual gross income

pay_rate = 25.50
hours_worked = 50
filing_status = "joint"

# calculate weekly gross pay 
if hours_worked > 40: 
    overtime_hours = hours_worked - 40 
    regular_pay = 40 * pay_rate 
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = pay_rate * hours_worked 
  
# calculate annual income
annual_income = gross_pay * 52

# Determine tax rate
if filing_status == "single":
    if annual_income < 12000:
        tax_rate = 0.05
    elif annual_income < 25000:
        tax_rate = 0.10
    elif annual_income < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
        
        
elif filing_status == "joint":
    if annual_income < 12000:
        tax_rate = 0.00
    elif annual_income < 25000:
        tax_rate = 0.06
    elif annual_income < 75000:
        tax_rate = 0.11 
    else:
        tax_rate = 0.20

# Calculate taxes 
tax_withheld = gross_pay * tax_rate
net_pay = gross_pay - tax_withheld

# print results
print("Gross weekly pay:", gross_pay)
print("Annual income:", annual_income)
print("Tax rate:", tax_rate)
print("Tax withheld:", tax_withheld)
print("Net pay:", net_pay)

print("You worked", hours_worked, "hours this period.")
print("Your filing status is", filing_status)
print("Your tax withholding is $", tax_withheld)
print("Your net pay is $", net_pay)
      