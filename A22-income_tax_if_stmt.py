# A22 - income tax, if stmt

salary = int(input("Enter annual salary: "))
if salary >= 6632341:
    annual_income_tax = (salary - 663240)*0.5 + (663240-514921)*0.47 + (514920-247441)*0.35 + (247440-178081)*0.31 + (178080-110881)*0.2 + (110880-77401)*0.14 + 77400*0.1
if salary >= 514921 and salary <= 663240:
    annual_income_tax = (salary-514921)*0.47 + (514920-247441)*0.35 + (247440-178081)*0.31 + (178080-110881)*0.2 + (110880-77401)*0.14 + 77400*0.1
if salary >= 247441 and salary <= 514920:
    annual_income_tax = (salary-247441)*0.35 + (247440-178081)*0.31 + (178080-110881)*0.2 + (110880-77401)*0.14 + 77400*0.1
if salary >= 178081 and salary <= 247440:
    annual_income_tax = (salary-178081)*0.31 + (178080-110881)*0.2 + (110880-77401)*0.14 + 77400*0.1
if salary >= 110881 and salary <= 178080:
    annual_income_tax = (salary-110881)*0.2 + (110880-77401)*0.14 + 77400*0.1
if salary >= 77401 and salary <= 110880:
    annual_income_tax = (salary-77401)*0.14 + 77400*0.1
if salary >= 0 and salary <= 77400:
    annual_income_tax = salary*0.1
print(f"Your annual income tax will be: {annual_income_tax}")