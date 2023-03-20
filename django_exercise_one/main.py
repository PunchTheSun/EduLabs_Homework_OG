import django
import datetime
import csv
import os
from ex_one_movies_app.models import Movie
from ex_one_movies_app.models import Review

os.environ["DJANGO_SETTINGS_MODULE"] = "ex_one_movies.settings"
django.setup()


def fill_from_file(filepath: str):  # Ex3
    with open(filepath, 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            # print(f'Name: {row["Movie_Name"]}, Release Date: {row["Release_date"]}, Rating: {row["Rating"]} ')
            m = Movie(name=row["Movie_Name"], year=row["Release_date"])
            m.save()
            r = Review(rating=float(row["Rating"]), review_year=f'{datetime.date.today().year}', movie=m)
            r.save()


if __name__ == '__main__':

    path_to_file = "imdb_top_250_movies.csv"
    fill_from_file(path_to_file)  # Run ONCE to fill the Movies and Reviews tables in DB from file

    pass  # Ex4
    ex_4a = Movie.objects.filter(year__gt=1990)
    for ma in ex_4a:
        print(f"name: {ma.name}\nyear: {ma.year}\n")  # Ex4a

    ex_4b = Movie.objects.filter(name__icontains='sky', year__lt=2000)
    for mb in ex_4b:
        print(f"name: {mb.name}\nyear: {mb.year}\n")  # Ex4b

    ex_4c = Review.objects.filter(rating__gt=9.4)
    for rc in ex_4c:
        rc.review_text = "GREAT MOVIE"
        rc.save()

    m4d = Review.objects.filter(movie__name='Pulp Fiction')
    print(m4d.all())

    ex_4e = Movie.objects.filter(name__icontains='godfather')
    for m4e in ex_4e:
        r = Review.objects.create(rating=10.0, review_year=datetime.date.today().year, review_text='wow', movie=m4e)
        r.save()

    m4fi = Movie.objects.get(name='Interstellar')
    m4fi.duration_in_min = int(round(datetime.timedelta(hours=2, minutes=49).total_seconds()/60))
    m4fii = Movie.objects.get(name='The Godfather')
    m4fii.duration_in_min = int(round(datetime.timedelta(hours=2, minutes=55).total_seconds()/60))
    m4fiii = Movie.objects.get(name='Scarface')
    m4fiii.duration_in_min = int(round(datetime.timedelta(hours=2, minutes=50).total_seconds()/60))
    m4fi.save()
    m4fii.save()
    m4fiii.save()

    time_limit = int(round(datetime.timedelta(hours=2, minutes=50).total_seconds()/60))
    print(Movie.objects.filter(duration_in_min__gt=time_limit).all())

    time_limit = int(round(datetime.timedelta(hours=2).total_seconds()/60))
    print(Movie.objects.filter(duration_in_min__gt=time_limit, year__lt=2000).all())

    ex_4i = Review.objects.filter(rating__gt=9.4)
    for m4i in ex_4i:
        print(m4i.movie.name, m4i.rating)

    ex_4j = Review.objects.all().order_by('-rating')
    for m4j in ex_4j[0:5]:
        print(m4j.movie.name, m4j.rating)



