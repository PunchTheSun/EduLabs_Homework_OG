# USDConverter Class

class USDConverter:

    def __init__(self):
        self.__usd_exchange_rates = {}

    def add_exchange_rate(self, selected_currency: str, rate: float, from_usd: bool = True) -> bool:
        if selected_currency.replace(" ", "").isalpha():
            if isinstance(rate, float) and rate > 0:
                if from_usd:
                    self.__usd_exchange_rates[selected_currency.lower().title()] = rate
                else:
                    self.__usd_exchange_rates[selected_currency.lower().title()] = 1/rate
            else:
                print("Invalid input, Rate has to be a number and larger than 0")
                return False
        else:
            print("Invalid input, Please enter a text to represent the currency to convert to/from"
                  "\n(No numbers or special characters allowed)")
            return False
        return True

    def get_exchange_rate(self, selected_currency: str, from_usd: bool = True) -> float:
        if selected_currency.replace(" ", "").isalpha():
            for currency in self.__usd_exchange_rates.keys():
                if selected_currency.lower().title() == currency:
                    if from_usd:
                        return self.__usd_exchange_rates[currency]
                    else:
                        return 1/self.__usd_exchange_rates[currency]
        else:
            print("Invalid input, Please enter a text to represent the currency to convert to/from"
                  "\n(No numbers or special characters allowed)")
            return -1.0

    def delete_exchange_rate(self, selected_currency: str) -> bool:
        if selected_currency.replace(" ", "").isalpha():
            for currency in self.__usd_exchange_rates.keys():
                if selected_currency.lower().title() == currency:
                    self.__usd_exchange_rates.pop(currency)
                    break
        else:
            print("Invalid input, Please enter a text to represent the currency to delete"
                  "\n(No numbers or special characters allowed)")
            return False
        return True

    def get_converted_usd_amount(self, to_currency: str, amount: float) -> float:
        if to_currency.replace(" ", "").isalpha():
            if isinstance(amount, float) and amount > 0:
                for currency in self.__usd_exchange_rates.keys():
                    if to_currency.lower().title() == currency:
                        return amount * self.__usd_exchange_rates[currency]
            else:
                print("Invalid input, Amount has to be a number and larger than 0")
                return -1.0
        else:
            print("Invalid input, Please enter a text to represent the currency to convert to"
                  "\n(No numbers or special characters allowed)")
            return -1.0

    def get_converted_currency_amount(self, from_currency: str, amount: float) -> float:
        if from_currency.replace(" ", "").isalpha():
            if isinstance(amount, float) and amount > 0:
                for currency in self.__usd_exchange_rates.keys():
                    if from_currency.lower().title() == currency:
                        return amount * 1/self.__usd_exchange_rates[currency]
            else:
                print("Invalid input, Amount has to be a number and larger than 0")
                return -1.0
        else:
            print("Invalid input, Please enter a text to represent the currency to convert from"
                  "\n(No numbers or special characters allowed)")
            return -1.0

    def get_all_currencies(self, from_usd: bool = True) -> dict:
        if from_usd:
            return self.__usd_exchange_rates
        to_usd_dict = {}
        for currency in self.__usd_exchange_rates.keys():
            to_usd_dict[currency] = 1/self.__usd_exchange_rates[currency]
        return to_usd_dict


