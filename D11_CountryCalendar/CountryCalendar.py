# D11 - Country calendar, classes, datetime, timezones
import datetime


class CountryCalendar:
    def __init__(self, country_name: str, country_work_days: set[str], year: int,
                 country_public_holidays: list[datetime.date]):

        self.country_public_holidays = country_public_holidays
        self.year = year
        self.country_work_days = country_work_days
        self.country_name = country_name

    def total_working_days(self, from_date: datetime.date, to_date: datetime.date) -> int:
        working_days = datetime.timedelta()
        temp_date = from_date
        while temp_date <= to_date:
            if from_date <= temp_date <= to_date and temp_date not in self.country_public_holidays \
                    and datetime.date.strftime(temp_date, "%A") in self.country_work_days:
                working_days += datetime.timedelta(days=1)
            temp_date += datetime.timedelta(days=1)
        return working_days.days

    def total_vacation_days(self, from_date: datetime.date, to_date: datetime.date) -> int:
        return ((to_date - from_date).days + 1) - self.total_working_days(from_date, to_date)

    def total_working_hours(self, from_datetime: datetime.datetime, to_datetime: datetime.datetime,
                            start_working_time: datetime.time, end_working_time: datetime.time) -> float:
        start_working_datetime = datetime.datetime.combine(from_datetime.date(), start_working_time)
        end_working_datetime = datetime.datetime.combine(to_datetime.date(), end_working_time)
        if from_datetime.date() == to_datetime.date() and from_datetime.date() not in self.country_public_holidays and \
                from_datetime.strftime("%A") in self.country_work_days:
            working_seconds = (min(to_datetime, end_working_datetime) - max(from_datetime,
                                                                            start_working_datetime)).total_seconds()
            return working_seconds / 3600.0
        work_seconds_in_full_day = (
                datetime.datetime.combine(datetime.date(2023, 1, 1), end_working_time) - datetime.datetime.combine(datetime.date(2023, 1, 1), start_working_time)).total_seconds()
        working_seconds = 0.0
        temp_datetime = from_datetime
        while temp_datetime.date() <= to_datetime.date():
            if temp_datetime.date() not in self.country_public_holidays and \
                    temp_datetime.strftime("%A") in self.country_work_days:
                if from_datetime.date() < temp_datetime.date() < to_datetime.date():
                    working_seconds += work_seconds_in_full_day
                elif temp_datetime.date() == from_datetime.date() and temp_datetime.time() < end_working_time:
                    working_seconds += (
                            datetime.datetime.combine(from_datetime.date(), end_working_time) - max(temp_datetime, start_working_datetime)).total_seconds()
                elif temp_datetime.date() == to_datetime.date():
                    working_seconds += (
                            min(to_datetime, end_working_datetime) - datetime.datetime.combine(to_datetime.date(), start_working_time)).total_seconds()
            temp_datetime += datetime.timedelta(days=1)
        return working_seconds / 3600.0

    def next_vacation_day(self) -> datetime.date:
        ret_day = datetime.datetime.now()
        while ret_day not in self.country_public_holidays and ret_day.strftime("%A") in self.country_work_days \
                and ret_day.year == 2023:
            ret_day += datetime.timedelta(days=1)
        return ret_day.date()

    def next_working_day(self) -> datetime.date:
        ret_day = datetime.datetime.now() + datetime.timedelta(days=1)
        while ret_day in self.country_public_holidays or ret_day.strftime("%A") not in self.country_work_days \
                and ret_day.year == 2023:
            ret_day += datetime.timedelta(days=1)
        return ret_day.date()

    def longest_holiday_span(self, from_date: datetime.date, to_date: datetime.date) -> tuple:
        days_count = 0
        max_days_count = -1
        ret_day = start_count_day = from_date
        now_counting = False
        index_day = from_date
        while index_day <= to_date:
            if index_day in self.country_public_holidays or index_day.strftime("%A") not in self.country_work_days:
                if not now_counting:
                    now_counting = True
                    start_count_day = index_day
                    days_count = 1
                else:
                    days_count += 1
            else:
                now_counting = False
                if days_count > max_days_count:
                    max_days_count = days_count
                    ret_day = start_count_day
            index_day += datetime.timedelta(days=1)
        if max_days_count == -1:  # If the function hasn't found anything it returns -1 in total number of days
            return -1, ret_day
        return max_days_count, ret_day
