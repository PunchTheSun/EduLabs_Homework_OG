# Generated by Django 4.1.7 on 2023-03-18 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ex_one_movies_app', '0003_movie_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', db_index=True, max_length=128)),
                ('birth_date', models.DateField()),
            ],
            options={
                'db_table': 'Directors',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ex_one_movies_app.director'),
        ),
    ]
