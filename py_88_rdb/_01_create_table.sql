CREATE TABLE employees
(
	employee_id integer PRIMARY KEY,
	last_name varchar(50) NOT NULL,
	first_name varchar(50) NOT NULL,
	middle_name varchar(50) NOT NULL,
	job_title varchar(80) NOT NULL,
	address text NOT NULL,
	home_phone varchar(11),
	date_of_birth date NOT NULL
);

CREATE TABLE clients
(
	client_id integer PRIMARY KEY,
	fio varchar(150) NOT NULL,
	address text NOT NULL,
	phone varchar(11)
);

CREATE TABLE provider
(
	provider_id integer PRIMARY KEY,
	provider_name varchar(80) NOT NULL,
	provider_agent varchar(80) NOT NULL,
	short_name varchar(60) NOT NULL,
	contact_phone varchar(11) NOT NULL,
	address text NOT NULL
);

CREATE TABLE delivery
(
	delivery_id integer PRIMARY KEY,
	provider_id integer NOT NULL,
	delivery_date date NOT NULL,

	CONSTRAINT fk_provider FOREIGN KEY(provider_id) REFERENCES provider(provider_id)
);

CREATE TABLE products
(
	product_id integer PRIMARY KEY,
	delivery_id integer NOT NULL,
	product_name varchar(60) NOT NULL,
	product_specs text NOT NULL,
	description text NOT NULL,
	image text,
	provider_cost decimal NOT NULL,
	in_stock bool NOT NULL,
	amount integer NOT NULL,
	selling_price decimal NOT NULL,

	CONSTRAINT fk_delivery FOREIGN KEY(delivery_id) REFERENCES delivery(delivery_id)
);

CREATE TABLE orders
(
	order_id integer PRIMARY KEY,
	employee_id integer NOT NULL,
	product_id integer NOT NULL,
	creation_date date NOT NULL,
	completion_date date NOT NULL,
	client_id integer NOT NULL,

	CONSTRAINT fk_employee FOREIGN KEY(employee_id) REFERENCES employees(employee_id),
	CONSTRAINT fk_product FOREIGN KEY(product_id) REFERENCES products(product_id),
	CONSTRAINT fk_client FOREIGN KEY(client_id) REFERENCES clients(client_id)
);
