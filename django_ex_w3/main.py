# Ex W3 - employees and companies
import datetime

import django
import csv
import os

os.environ["DJANGO_SETTINGS_MODULE"] = "employees_and_companies.settings"
django.setup()

from employees_and_companies_app.models import Company
from employees_and_companies_app.models import Person
from employees_and_companies_app.models import Employee


def fill_from_file(filepath: str, model_type: str):  # Ex3
    match model_type:
        case 'employees':
            with open(filepath, 'r', encoding="utf-8") as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    employee = Employee(person_id=row["person_id"], company_id=row["company_id"],
                                        job_title=row["job_title"],
                                        is_current_job=str(row["is_current_job"]).lower().capitalize(),
                                        company_email=row["company_email"])
                    employee.save()

        case 'companies':
            with open(filepath, 'r', encoding="utf-8") as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    c = Company(name=row["company_name"], country=row["country"], city=row["city"],
                                address=row["address"], phone_num=row["phone_num"])
                    c.save()

        case 'persons':
            with open(filepath, 'r', encoding="utf-8") as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    p = Person(first_name=row["first_name"], last_name=row["last_name"], email=row["personal_email"],
                               gender=row["gender"], birthday=row["birth_date"])
                    p.save()


def get_person_name_by_id(person_id: int) -> str:
    p = Person.objects.get(id=person_id)
    return f"{p.first_name} {p.last_name}"


def get_people_by_age(age: int) -> list[Person]:
    ret_list = []
    year_of_birth = datetime.date.today().year - age
    qs = Person.objects.all()
    for p in qs:
        _, _, person_year_of_birth = p.birthday.split('/')
        if int(person_year_of_birth) == year_of_birth:
            ret_list.append(p)
    return ret_list


def get_people_by_gender(person_gender: str) -> list[Person]:
    ret_list = []
    qs = Person.objects.filter(gender=person_gender)
    for p in qs:
        ret_list.append(p)
    return ret_list

def get_companies_by_country(company_country: str) -> list[str]:
    ret_list = []
    qs = Company.objects.filter(country=company_country.capitalize())
    for c in qs:
        ret_list.append(c.name)
    return ret_list


def get_company_employees(company_id: int, current_only: bool=False) -> list[Person]:
    ret_list = []
    if current_only:
        qs = Employee.objects.filter(company__id=company_id, is_current_job=True)
    else:
        qs = Employee.objects.filter(company__id=company_id)
    for employee in qs:
        ret_list.append(employee.person)
    return ret_list


def get_person_jobs(person_id: int) -> list[dict[str, str]]:
    ret_list = []
    p = Person.objects.get(id=person_id)
    qs = Employee.objects.filter(person=p)
    for employee in qs:
        companies = Company.objects.filter(id=employee.company.id)
        for c in companies:
            ret_list.append({c.name: employee.job_title})
    return ret_list


if __name__ == '__main__':
    # Run these ONLY ONCE to fill the database from the files
    # fill_from_file('data/companies.csv', 'companies')
    # fill_from_file('data/persons.csv', 'persons')
    # fill_from_file('data/employees.csv', 'employees')

    print(get_person_name_by_id(3))

    print(get_people_by_age(30))

    print(get_people_by_gender('Male'))

    print(get_companies_by_country("China"))

    print(get_company_employees(4))

    print(get_person_jobs(49))
