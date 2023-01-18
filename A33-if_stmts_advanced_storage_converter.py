# A33  - if stmts, advanced - storage converter

units = int(input("Enter amount of units: "))
type1 = input("Enter the unit's type (bytes, kb, mb, gb, tb): ")
type2 = input("Convert to type (bytes, kb, mb, gb, tb): ")

if type1 == "bytes":
    if type2 == "kb":
        converted_units = units*(2**-10)
    if type2 == "mb":
        converted_units = units*(2**-20)
    if type2 == "gb":
        converted_units = units*(2**-30)
    if type2 == "tb":
        converted_units = units*(2**-40)
if type1 == "kb":
    if type2 == "bytes":
        converted_units = units*(2**10)
    if type2 == "mb":
        converted_units = units*(2**-10)
    if type2 == "gb":
        converted_units = units*(2**-20)
    if type2 == "tb":
        converted_units = units*(2**-30)
if type1 == "mb":
    if type2 == "bytes":
        converted_units = units*(2**20)
    if type2 == "kb":
        converted_units = units*(2**10)
    if type2 == "gb":
        converted_units = units*(2**-10)
    if type2 == "tb":
        converted_units = units*(2**-20)
if type1 == "gb":
    if type2 == "bytes":
        converted_units = units*(2**30)
    if type2 == "kb":
        converted_units = units*(2**20)
    if type2 == "mb":
        converted_units = units*(2**10)
    if type2 == "tb":
        converted_units = units*(2**-10)
if type1 == "tb":
    if type2 == "bytes":
        converted_units = units*(2**40)
    if type2 == "kb":
        converted_units = units*(2**30)
    if type2 == "mb":
        converted_units = units*(2**20)
    if type2 == "gb":
        converted_units = units*(2**10)

print(f"Result: {converted_units} {type2}")