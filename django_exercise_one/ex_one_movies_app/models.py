import datetime

from django.db import models
from django.db.models import RESTRICT


# Create your models here.


class Movie(models.Model):
    name = models.CharField(null=False, blank=False, db_column='name', db_index=True, max_length=128)
    year = models.IntegerField(null=False, blank=False, db_column='year')
    description = models.TextField(null=True, blank=True, db_column='description')
    duration_in_min = models.IntegerField(null=True, blank=True, db_column='duration')  # Ex1
    director = models.ForeignKey(to='Director', on_delete=RESTRICT, null=True, blank=True)

    def __str__(self):
        return f"{self.name}, Year: {self.year}, Duration (minutes): {self.duration_in_min}"

    class Meta:
        db_table = 'Movies'


class Director(models.Model):
    name = models.CharField(null=False, blank=False, db_column='name', db_index=True, max_length=128)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'Directors'


class Review(models.Model):  # Ex2
    rating = models.FloatField(null=False, blank=False, db_column='rating', db_index=True)
    review_year = models.CharField(null=False, blank=False, db_column='review_year', default=datetime.date.today().year,
                                   db_index=True, max_length=128)
    review_text = models.CharField(null=True, blank=True, db_column='review_text', db_index=True, max_length=256)
    movie = models.ForeignKey('Movie', on_delete=RESTRICT, null=False, blank=False)

    class Meta:
        db_table = 'Reviews'

    def __str__(self):
        return f"Rating: {self.rating}, Review Year: {self.review_year}, Text: {self.review_text}, Movie ID: {self.movie_id}"
