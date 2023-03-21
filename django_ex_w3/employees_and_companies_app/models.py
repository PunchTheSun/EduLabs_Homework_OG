from django.db import models
from django.db.models import RESTRICT


class Company(models.Model):
    name = models.CharField(null=False, blank=False, max_length=128, db_column='company name', db_index=True)
    country = models.CharField(null=False, blank=False, max_length=128, db_column='country', db_index=True)
    city = models.CharField(null=False, blank=False, max_length=128, db_column='city')
    address = models.CharField(null=False, blank=False, max_length=128, db_column='address')
    phone_num = models.CharField(null=True, blank=True, max_length=128, db_column='phone number')

    class Meta:
        db_table = 'Companies'

    def __str__(self):
        return f"Company name: {self.name}\nCountry: {self.country}\nCity: {self.city}\n" \
               f"Address: {self.address}\nPhone: {self.phone_num}\n\n"


class Person(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=128, db_column='first name', db_index=True)
    last_name = models.CharField(null=False, blank=False, max_length=128, db_column='last name', db_index=True)
    email = models.CharField(null=False, blank=False, max_length=128, db_column='email')
    gender = models.CharField(null=True, blank=True, max_length=128, db_column='gender')
    birthday = models.CharField(null=True, blank=True, max_length=128, db_column='birthday')

    class Meta:
        db_table = 'Persons'

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nEmail: {self.email}\nGender: {self.gender}\n" \
               f"Birthday: {self.birthday}\n\n"


class Employee(models.Model):
    person = models.ForeignKey(to='Person', on_delete=RESTRICT, null=False, blank=False)
    company = models.ForeignKey(to='Company', on_delete=RESTRICT, null=False, blank=False)
    job_title = models.CharField(null=False, blank=False, max_length=128, db_column='job title', db_index=True)
    is_current_job = models.BooleanField(null=False, blank=False, db_column='is current job', db_index=True)
    company_email = models.CharField(null=False, blank=False, max_length=128, db_column='company email')

    class Meta:
        db_table = 'Employees'

    def __str__(self):
        return f"person_id: {self.person_id}\ncompany_id: {self.company_id}\nJob Title: {self.job_title}\n" \
               f"Is Current Job: {self.is_current_job}\nCompany Email: {self.company_email}\n\n"
