# Generated by Django 4.1.7 on 2023-03-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='company name', db_index=True, max_length=128)),
                ('country', models.CharField(db_column='country', db_index=True, max_length=128)),
                ('city', models.CharField(db_column='city', max_length=128)),
                ('address', models.CharField(db_column='address', max_length=128)),
                ('phone_num', models.CharField(blank=True, db_column='phone number', max_length=128, null=True)),
            ],
            options={
                'db_table': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first name', db_index=True, max_length=128)),
                ('last_name', models.CharField(db_column='last name', db_index=True, max_length=128)),
                ('email', models.CharField(db_column='email', max_length=128)),
                ('gender', models.CharField(blank=True, db_column='gender', max_length=128, null=True)),
                ('birthdate', models.CharField(blank=True, db_column='birthdate', max_length=128, null=True)),
            ],
            options={
                'db_table': 'Persons',
            },
        ),
    ]
