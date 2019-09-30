drop table user_groups;
drop table role; 
drop table user_session;
drop table users;

create table users(id int primary key AUTO_INCREMENT,
	fname varchar(20),
	lname varchar(20),
	email varchar(50) not null unique,
	password varchar(20) not null);

create table user_session(id varchar(40) primary key,
	token varchar(40) unique not null,
	user_id int not null,expiry BIGINT not null,
	foreign key(user_id) references users(id));

create table role(id int primary key auto_increment,
	name varchar(20));

create table user_groups(id int primary key auto_increment,
	role_id int not null,
	user_id int not null,
	foreign key(role_id) references role(id),
	foreign key(user_id) references users(id));
