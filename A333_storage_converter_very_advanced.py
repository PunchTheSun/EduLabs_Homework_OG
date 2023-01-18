# A333 - storage converter very advanced

units = int(input("Enter amount of units: "))
type1 = input("Enter the unit's type (bytes, kb, mb, gb, tb): ")

if type1 == "bytes":
    if units // 2**40 > 0:
        converted_units = round(units // 2**40,1) + round((units % 2**40)*10**-12,1)
        type2 = "tb"
        print(f"Converted to: {converted_units}{type2}")
    elif units // 2**30 > 0:
        converted_units = round(units // 2**30,1) + round((units % 2**30)*10**-9,1)
        type2 = "gb"
        print(f"Converted to: {converted_units}{type2}")
    elif units // 2**20 > 0:
        converted_units = round(units // 2**20,1) + round((units % 2**20)*10**-6,1)
        type2 = "mb"
        print(f"Converted to: {converted_units}{type2}")
    elif units // 2**10 > 0:
        converted_units = units // 2**10 + round((units % 2**10)*10**-3,1)
        type2 = "kb"
        print(f"Converted to: {converted_units}{type2}")
    else:
        print(f"{units}{type1} isn't sufficient to be transformed to a higher unit type.")
if type1 == "kb":
    if units // 2**30 > 0:
        converted_units = round(units // 2**30,1) + round((units % 2**30)*10**-9,1)
        type2 = "tb"
        print(f"Converted to: {converted_units}{type2}")
    elif units // 2**20 > 0:
        converted_units = round(units // 2**20,1) + round((units % 2**20)*10**-6,1)
        type2 = "gb"
        print(f"Converted to: {converted_units}{type2}")
    elif units // 2**10 > 0:
        converted_units = round(units // 2**10,1) + round((units % 2**10)*10**-3,1)
        type2 = "mb"
        print(f"Converted to: {converted_units}{type2}")
    else:
        print(f"{units}{type1} isn't sufficient to be transformed to a higher unit type.")
if type1 == "mb":
    if units // 2**20 > 0:
        converted_units = round(units // 2**20,1) + round((units % 2**20)*10**-6,1)
        type2 = "tb"
        print(f"Converted to: {converted_units}{type2}")
    elif units // 2**10 > 0:
        converted_units = round(units // 2**10,1) + round((units % 2**10)*10**-3,1)
        type2 = "gb"
        print(f"Converted to: {converted_units}{type2}")
    else:
        print(f"{units}{type1} isn't sufficient to be transformed to a higher unit type.")
if type1 == "gb":
    if units // 2**10 > 0:
        converted_units = round(units // 2**10,1) + round((units % 2**10)*10**-3,1)
        type2 = "tb"
        print(f"Converted to: {converted_units}{type2}")
    else:
        print(f"{units}{type1} isn't sufficient to be transformed to a higher unit type.")
if type1 == "tb":
    print(f"{units}{type1} is already the highest unit type for this application's capability.")