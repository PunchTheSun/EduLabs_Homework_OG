# Generated by Django 4.1.7 on 2023-03-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_and_companies_app', '0002_rename_birthdate_person_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.CharField(blank=True, db_column='birthday', max_length=128, null=True),
        ),
    ]
