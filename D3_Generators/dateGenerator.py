# D3 - DateGenerator
import calendar
import datetime


def date_generator(date: datetime.date):
    end_date = datetime.datetime.combine(datetime.date(date.year, date.month, calendar.monthrange(date.year, date.month)[1]), datetime.time(23, 59, 59))
    temp_date = datetime.datetime.combine(date, datetime.datetime.now().time())
    curr_date = temp_date

    while temp_date < end_date:
        curr_date = temp_date
        temp_date += datetime.timedelta(days=1)
        yield curr_date.date()


# if __name__ == '__main__':
#     for date in date_generator(datetime.datetime.now().date()):
#         print(date)
