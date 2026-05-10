# Gross income calculation

pay_rate = 25.50
hours_worked = 55
 
if hours_worked > 40: # check if employee worked more than 40 hours
    overtime_hours = hours_worked - 40 # calculate overtime hours 
    regular_pay = 40 * pay_rate # regular pay for first 40 hrs
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = pay_rate * hours_worked # no overtime

    
print(gross_pay)

