# A4-if stmt - jack store
# Book prices - Change here to price differently:
price_sci = 58
price_com = 32
price_his = 24
# Discount prices - Change here to price differently:
discount_sci = 0.1 # 10% discount on Sci-Fi books price only if purchased 3 or more Sci-Fi books
discount_over300 = 20 # 20$ discount on total price after discount, if pre-discount total price is over 300$
# Buy 2 History books get 1 History book for free - Calculated in an "if" condition below
# User Input:
books_sci = int(input("How many Sci-Fi books would you like to buy: "))
books_com = int(input("How many Comic books would you like to buy: "))
books_his = int(input("How many History books would you like to buy: "))
# Total price before discounts calculation:
total_price_before_discount = (books_sci * price_sci) + (books_com * price_com) + (books_his * price_his)
# Total Comic books price calculation:
total_price_com = books_com * price_com
# Discount calculation:
if books_sci >= 3:
    total_price_sci = (books_sci * price_sci) - (books_sci * price_sci * discount_sci)
else:
    total_price_sci = books_sci * price_sci
if books_his % 3 == 0:
    total_price_his = (books_his * price_his) - ((books_his // 3) * price_his)
else:
    total_price_his = books_his * price_his
if total_price_before_discount >= 300:
    total_price_after_discount = (total_price_sci + total_price_his + total_price_com) - discount_over300
else:
    total_price_after_discount = total_price_sci + total_price_his + total_price_com
# Program Outputs:
print(f"Total before discount: {total_price_before_discount}")
print(f"Total discount: {total_price_before_discount - total_price_after_discount}")
print(f"Total after discount: {total_price_after_discount}")

