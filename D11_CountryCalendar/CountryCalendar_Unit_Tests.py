from CountryCalendar import *

def test_total_working_days1():
    usa_public_holidays = [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2), datetime.date(2023, 1, 16),
                               datetime.date(2023, 2, 20), datetime.date(2023, 5, 29), datetime.date(2023, 6, 19),
                               datetime.date(2023, 7, 4), datetime.date(2023, 9, 4), datetime.date(2023, 10, 9),
                               datetime.date(2023, 11, 10), datetime.date(2023, 11, 11), datetime.date(2023, 11, 23),
                               datetime.date(2023, 12, 25)]
    usa_work_days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
    usa_calendar = CountryCalendar("USA", usa_work_days, 2023, usa_public_holidays)

    result = usa_calendar.total_working_days(datetime.date(2023, 1, 21), datetime.date(2023, 1, 28))
    expected = 5

    assert result == expected, "There should be 5 working days between these two dates"


def test_total_working_days2():
    usa_public_holidays = [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2), datetime.date(2023, 1, 16),
                           datetime.date(2023, 2, 20), datetime.date(2023, 5, 29), datetime.date(2023, 6, 19),
                           datetime.date(2023, 7, 4), datetime.date(2023, 9, 4), datetime.date(2023, 10, 9),
                           datetime.date(2023, 11, 10), datetime.date(2023, 11, 11), datetime.date(2023, 11, 23),
                           datetime.date(2023, 12, 25)]
    usa_work_days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
    usa_calendar = CountryCalendar("USA", usa_work_days, 2023, usa_public_holidays)

    result = usa_calendar.total_working_days(datetime.date(2023, 1, 21), datetime.date(2023, 1, 20))
    expected = 0

    assert result == expected, "The 'To' Date is earlier than the 'From' date, Function should return 0 days"

def test_total_vacation_days():
    usa_public_holidays = [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2), datetime.date(2023, 1, 16),
                           datetime.date(2023, 2, 20), datetime.date(2023, 5, 29), datetime.date(2023, 6, 19),
                           datetime.date(2023, 7, 4), datetime.date(2023, 9, 4), datetime.date(2023, 10, 9),
                           datetime.date(2023, 11, 10), datetime.date(2023, 11, 11), datetime.date(2023, 11, 23),
                           datetime.date(2023, 12, 25)]
    usa_work_days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
    usa_calendar = CountryCalendar("USA", usa_work_days, 2023, usa_public_holidays)

    result = usa_calendar.total_vacation_days(datetime.date(2023, 1, 21), datetime.date(2023, 1, 28))
    expected = 3

    assert result == expected, "There should be 3 Vacation days between these two dates"

def test_total_working_hours():
    usa_public_holidays = [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2), datetime.date(2023, 1, 16),
                           datetime.date(2023, 2, 20), datetime.date(2023, 5, 29), datetime.date(2023, 6, 19),
                           datetime.date(2023, 7, 4), datetime.date(2023, 9, 4), datetime.date(2023, 10, 9),
                           datetime.date(2023, 11, 10), datetime.date(2023, 11, 11), datetime.date(2023, 11, 23),
                           datetime.date(2023, 12, 25)]
    usa_work_days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
    usa_calendar = CountryCalendar("USA", usa_work_days, 2023, usa_public_holidays)

    result = usa_calendar.total_working_hours(datetime.datetime(2023, 1, 7, 14, 00, 00), datetime.datetime(2023, 1, 10, 11, 30, 00), datetime.time(9, 0), datetime.time(19, 0))
    expected = 12.5

    assert result == expected, "There should be 12.5 working hours between these two dates"
