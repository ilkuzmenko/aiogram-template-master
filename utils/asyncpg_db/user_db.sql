create table if not exists users
(
	id serial
		constraint users_pk
			primary key,
	user_id bigint,
	phone bigint,
	first_name text,
	last_name text
);

alter table users
    owner to postgres;

create unique index if not exists users_user_id_uindex
	on users (user_id);