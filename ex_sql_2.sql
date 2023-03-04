-- ex_sql_2


CREATE TABLE public.directors (
	id serial primary key,
	name varchar(256) not null

);

create table public.series (
id serial primary key,
name varchar(256) not null,
total_films int not null
);

create TABLE public.movies (
	id serial primary key,
	name varchar(256) not null,
	year int not null,
	director_id int not null,
	length_in_min float not null,
	series_id int,
	CONSTRAINT fk_director
      FOREIGN KEY(director_id)
	  REFERENCES directors(id),
	foreign key (series_id) references series(id)
);


insert into directors(name) values ('Frank Darabont');
insert into directors(name) values ('Francis Ford Coppola');
insert into directors(name) values ('Steven Spielberg');
insert into directors(name) values ('Quentin Tarantino');
insert into directors(name) values ('James Cameron');

insert into series (id, name, total_films) values (1, 'Kill Bill Series', 2);
insert into series (id, name, total_films) values (2, 'God Father Series', 3);
insert into series (id, name, total_films) values (3, 'Avatar Series', 2);

INSERT INTO movies ("id", "name", "year", director_id, length_in_min, series_id) VALUES(1, 'The Godfather', 1972, 2, 60, 2);
INSERT INTO movies ("id", "name", "year", director_id, length_in_min) VALUES(2, 'The Shawshank Redemption', 1994, 1, 65);
insert into movies (id, name, year, director_id, length_in_min) values (3, 'The Green Mile', 1999, 1, 120);
insert into movies (id, name, year, director_id, length_in_min) values (4, 'The Mist', 2007, 1, 130);
insert into movies (id, name, year, director_id, length_in_min) values (5, 'Dracula', 1992, 2, 80);
insert into movies (id, name, year, director_id, length_in_min) values (6, 'Gardens of stone', 1987, 2, 60);
insert into movies (id, name, year, director_id, length_in_min) values (7, 'Pulp fiction', 1994, 4, 60);
insert into movies (id, name, year, director_id, length_in_min, series_id) values (8, 'Kill Bill 1', 2003, 4, 120, 1);
insert into movies (id, name, year, director_id, length_in_min, series_id) values (9, 'Kill Bill 2', 2004, 4, 70, 1);
insert into movies (id, name, year, director_id, length_in_min, series_id) values (10, 'Avatar', 2009, 5, 300, 3);
insert into movies (id, name, year, director_id, length_in_min, series_id) values (11, 'Avatar: Way Of The Water', 2022, 5, 333, 3);


-- (5) write some queries:

-- a
select *
from movies m full join directors d on m.director_id = d.id
full join series s on m.series_id = s.id;

-- b
select name, total_films 
from series s;

-- or without cheating:
select s.name, count(m.id)
from series s left join movies m
on s.id = m.series_id
group by s.name;

-- c
select d.name, count(m.id)
from directors d left join movies m
on d.id = m.director_id
group by d.name;

-- d
select d.name, count(m.id) as movie_per_director, count(distinct s.id) as series_per_director
from directors d left join movies m 
on d.id = m.director_id
left join series s 
on m.series_id = s.id 
group by d.name;

-- e
select m.name as movie_name, s.name as series_name, d.name as director_name
from movies m left join series s 
on m.series_id = s.id 
left join directors d 
on m.director_id = d.id 
where s.total_films >= 2;

-- f
select m.name as movie_name, d.name as director_name
from movies m left join directors d 
on m.director_id = d.id 
where m.series_id is null;