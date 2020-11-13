CREATE TABLE user (
	email INTEGER PRIMARY KEY,
	full_name TEXT NOT NULL,
	phone_no TEXT NOT NULL,
	password TEXT NOT NULL,
	created_dt TEXT NOT NULL
);

CREATE TABLE bug (
    id INTEGER PRIMARY KEY AUTO INCREMENT,
	reporter TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT NOT NULL,
	created_dt TEXT NOT NULL,
    FOREIGN KEY (reporter) REFERENCES user (email) 
);