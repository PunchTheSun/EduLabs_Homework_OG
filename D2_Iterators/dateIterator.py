# D2 - Iterators Class: DateIterator
import datetime
import calendar


class DateIterator:

    def __init__(self, date: datetime.date):
        self._date = date
        self._end_date = datetime.datetime.combine(datetime.date(date.year, date.month, calendar.monthrange(date.year, date.month)[1]), datetime.time(23, 59, 59))
        self._date_iterator = datetime.datetime.combine(self._date, datetime.datetime.now().time())

    def __iter__(self):
        self._date_iterator = datetime.datetime.combine(self._date, datetime.datetime.now().time())
        return self

    def __next__(self):
        curr_val = self._date_iterator
        if curr_val > self._end_date:
            raise StopIteration()
        self._date_iterator += datetime.timedelta(days=1)
        return curr_val.date()


if __name__ == "__main__":
    my_date = datetime.date(2023, 2, 8)
    my_date_iterator = DateIterator(my_date)

    for date in my_date_iterator:
        print(date)
