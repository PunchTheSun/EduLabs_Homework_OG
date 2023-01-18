# A6-Match case
country = input("Write country name:")

match country:
    case "USA":
        coin = "US Dollar"
    case "Israel":
        coin = "Shequel (NIS)"
    case "UK":
        coin = "Pound"
    case "Germany":
        coin = "EU"
    case "Austria":
        coin = "EU"
    case "Czech":
        coin = "EU"
    case "France":
        coin = "EU"
    case "Italy":
        coin = "EU"
    case "Spain":
        coin = "EU"
    case _:
        coin = "I don't know."
print(coin)
