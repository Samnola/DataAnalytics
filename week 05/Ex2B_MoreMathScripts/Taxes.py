# Tax Withholding calculations 

salary = float(input("Enter your salary: "))
tax_rate = 0.23  # 23% federal tax


tax_withheld = round(salary * tax_rate, 2)
take_home_pay = round(salary - tax_withheld, 2)


print(f"Your salary is ${salary}")
print(f"Federal taxes withheld: ${tax_withheld}")
print(f"Take-home pay: ${take_home_pay}")
