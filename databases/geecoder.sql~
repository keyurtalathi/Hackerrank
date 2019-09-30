
drop table exam_testcase_result;
drop table exam_attempt;
drop table exam_question;
drop table exam;
drop table testcase_result;
drop table user_attempt;
drop table languages;
drop table options;
drop table testcase;
drop table question;
drop table sub_topic;
drop table topic;

create table topic(id int primary key auto_increment,
	name varchar(20) not null unique);

create table sub_topic(id int primary key auto_increment,
	name varchar(20) not null unique,
	topic_id int not null,
	foreign key(topic_id) references topic(id) ON DELETE CASCADE);

create table question(id int primary key auto_increment,
	question varchar(100) not null unique,
	description varchar(1000) not null,
	weightage int,
	difficulty_level varchar(20),
	question_type varchar(20),
	created_by int not null,
	created_on BIGINT,
	sub_topic_id int not null,
	foreign key(sub_topic_id) references sub_topic(id));

create table testcase(id int primary key auto_increment,
	testcase_number int,
	input varchar(1000),
	output varchar(1000),
	marks int,
	is_example boolean,
	question_id int not null,
	foreign key(question_id) references question(id) ON DELETE CASCADE);

create table options(id int primary key auto_increment,
	options varchar(20),
	is_answer boolean not null,
	question_id int not null,
	foreign key(question_id) references question(id) ON DELETE CASCADE);

create table languages(id int primary key auto_increment,
	name varchar(20) unique);

create table user_attempt(id int primary key auto_increment,
	question_id int not null,
	language_id int not null,
	total_testcases_passed int,
	code_snippet varchar(1000),
	marks_obtained float,
        foreign key(question_id) references question(id) ON DELETE CASCADE,
        foreign key(language_id) references languages(id));

create table testcase_result(id int primary key auto_increment,
	testcase_id int not null,
	user_attempt_id int not null,
	is_passed boolean,
	foreign key(testcase_id) references testcase(id) ON DELETE CASCADE,
	foreign key(user_attempt_id) references user_attempt(id) ON DELETE CASCADE);

create table exam(id int primary key auto_increment,
	name varchar(40),
	starttime  BIGINT,
	endtime  BIGINT);

create table exam_question(id int primary key auto_increment,
	exam_id int not null,
	question_id int not null,
	total_marks int,
	difficulty_level varchar(20),
	foreign key(exam_id) references exam(id) ON DELETE CASCADE,
	foreign key(question_id) references question(id));

create table exam_attempt(id int primary key auto_increment,
        exam_question_id int not null,
        language_id int not null,
        total_testcases_passed int,
        code_snippet varchar(1000),
        marks_obtained float,
	attempt_starttime  BIGINT,
	attempt_endtime  BIGINT,
        foreign key(exam_question_id) references exam_question(id) ON DELETE CASCADE,
        foreign key(language_id) references languages(id));

create table exam_testcase_result(id int primary key auto_increment,
        exam_attempt_id int not null,
        testcase_id int not null,
        is_passed boolean,
        foreign key(testcase_id) references testcase(id) ON DELETE CASCADE,
        foreign key(exam_attempt_id) references exam_attempt(id) ON DELETE CASCADE);

