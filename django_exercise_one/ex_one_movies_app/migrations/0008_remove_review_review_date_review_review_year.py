# Generated by Django 4.1.7 on 2023-03-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex_one_movies_app', '0007_alter_review_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_date',
        ),
        migrations.AddField(
            model_name='review',
            name='review_year',
            field=models.CharField(db_column='review_year', db_index=True, default=2023, max_length=128),
        ),
    ]
