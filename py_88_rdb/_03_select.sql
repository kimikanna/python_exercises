-- Вывести все столбцы и строки таблицы сотрудников

SELECT * FROM employees;

-- Вывести клиентов, у которых ФИО начинается на Л

SELECT * FROM clients WHERE fio LIKE 'Л%';

-- Вывести поставщиков, у которых телефон заканчивается на "4832"

SELECT 
    provider_name AS "Название поставщика",
    provider_agent AS "Представитель",
    contact_phone AS "Телефон"
FROM 
    provider
WHERE 
    contact_phone LIKE '%4832';

-- Вывести все доставки, у которых дата доставки с января по май 2024 года

SELECT * FROM delivery WHERE delivery_date BETWEEN '2024-01-01' AND '2024-05-31';

-- Вывести все продукты, которые в данный момент в наличии

SELECT
	product_name AS "Наименование товара",
	in_stock AS "Наличие",
	amount AS "Количество",
	selling_price AS "Цена"
FROM
	products
WHERE
	in_stock = TRUE;

-- Вычислить прибыль с продажи всех товаров, где прибыль = (цена_продажи - цена_закупки) * количество_товаров

SELECT 
	product_name AS "Наименование товара",
    (selling_price - provider_cost) * amount AS "Прибыль"
FROM 
    products;

-- Вывести всех сотрудников, которые родились раньше 1991 года

SELECT * FROM employees WHERE DATE_TRUNC('year', date_of_birth) < DATE '1991-01-01';
