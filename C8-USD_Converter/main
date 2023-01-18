from USDConverter_class import USDConverter

rates = USDConverter()
rates.add_exchange_rate("NIS", 3.16)
rates.add_exchange_rate("Japanese yen", 113.73)
rates.add_exchange_rate("Euro", 0.89)
print(rates.get_exchange_rate("Japanese yen", False))
print(rates.get_exchange_rate("Japanese yen", True))
print(rates.get_converted_currency_amount("Japanese yen", 30000.0))
print(rates.get_converted_usd_amount("Euro", 134.0))
rates.add_exchange_rate("Euro", 0.96)
rates.delete_exchange_rate("Japanese yen")
print(rates.get_exchange_rate("Euro", False))
print(rates.get_all_currencies())
print(rates.get_all_currencies(False))


