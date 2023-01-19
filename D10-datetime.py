# D10 - datetime
import datetime


# Ex1

# def ex1(num: float) -> str:
#     return str(datetime.timedelta(seconds=num))
#
#
# if __name__ == "__main__":
#     print(ex1(1000000.0))


# Ex2

# def ex2(text: str) -> str:
#     temp_date = datetime.datetime.strptime(text, "%Y-%m-%d, %a, %H:%M")
#     temp_delta = datetime.timedelta(days=3)
#     return (temp_date + temp_delta).strftime("%A")
#
#
# if __name__ == "__main__":
#     print(ex2("2021-12-08, Wed, 10:00"))

# Ex3
#
# def ex3(user_date_text: str) -> datetime.timedelta:
#     user_date = datetime.datetime.strptime(user_date_text, "%a, %b %d, %Y %H:%M %p")
#     return user_date - datetime.datetime.now()
#
# if __name__ == "__main__":
#     print(ex3("Fri, Jan 20, 2023 15:00 PM"))

# Ex4

# def ex4(user_date_text: str) -> str:
#     user_date = datetime.datetime.strptime(user_date_text, "%d-%m-%y")
#     temp_delta = datetime.timedelta(days=1)
#     while user_date.weekday() != 4:
#         user_date += temp_delta
#     return user_date.strftime("%d-%m-%Y")
#
#
# if __name__ == "__main__":
#     print(ex4("18-01-23"))

# Ex5

# def ex5(user_time_text: str) -> str:
#     user_time = datetime.datetime.strptime(user_time_text, "%H:%M")
#
#     return user_time.replace(day=datetime.datetime.today().day, month=datetime.datetime.today().month, year=datetime.datetime.today().year) - datetime.datetime.now()
#
#
# if __name__ == "__main__":
#     print(ex5("18:00"))

# Ex6

# def ex6() -> datetime.timedelta.days:
#     return (datetime.date(datetime.date.today().year, 12, 31) - datetime.date.today()).days
#
#
# if __name__ == "__main__":
#     print(ex6())


# Ex7

# def ex7(user_day_text: str) -> int:
#     same_day_counter = 0
#     user_day = datetime.datetime.strptime(user_day_text, "%a")
#     temp_today = datetime.datetime.now()
#     while temp_today.month == datetime.datetime.now().month:
#         if temp_today.weekday() == user_day.day:
#             same_day_counter += 1
#         temp_today += datetime.timedelta(days=1)
#     return same_day_counter
#
#
# if __name__ == "__main__":
#     print(ex7("Fri"))
