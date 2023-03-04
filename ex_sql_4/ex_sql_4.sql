-- ex_sql_4


create table "bank"(
	id serial primary key,
	name varchar(256) not null
);


create table "account_owner"(
	passport serial primary key,
	name varchar(256) not null,
	address varchar(256),
	bank_id int not null,
	foreign key (bank_id) references bank(id)
);


create table "bank_account"(
	account_number serial primary key,
	max_limit float not null,
	balance float default 0.0,
	bank_id int not null,
	foreign key (bank_id) references bank(id)
);


create table "ownership"(
	id serial primary key,
	type varchar(256) not null,
	owner_passport int not null,
	account_number int not null,
	foreign key (owner_passport) references account_owner(passport),
	foreign key (account_number) references bank_account(account_number)
);


create table "transaction"(
	id serial primary key,
	type varchar(256) not null,
	timestamp int,
	account_number int not null,
	foreign key (account_number) references bank_account(account_number)
);


create table "transaction_accounts"(
	id serial primary key,
	account_number int not null,
	from_account_number int not null,
	to_account_number int not null,
	transaction_id int not null,
	foreign key (account_number) references bank_account(account_number),
	foreign key (from_account_number) references bank_account(account_number),
	foreign key (to_account_number) references bank_account(account_number),
	foreign key (transaction_id) references transaction(id)
);