-- FULL JOIN - вывод всех продуктов, поставленных определенным поставщиком

SELECT pd.* FROM products pd
JOIN delivery d ON pd.delivery_id = d.delivery_id
JOIN provider pr ON d.provider_id = pr.provider_id
WHERE pr.provider_name = 'ООО "Светлое будущее"';

-- LEFT JOIN - вывод всех сотрудников с датами их заказов. Если у сотрудника нет заказов, он не выведется
-- Но если у заказа нет назначенного сотрудника, выведет заказ, а в полях из таблицы employeers выведет NULL

SELECT 
    e.employee_id,
    e.last_name,
    e.first_name,
    o.order_id,
    o.creation_date
FROM 
    orders o
LEFT JOIN 
    employees e ON o.employee_id = e.employee_id;

-- RIGHT JOIN - правое соединение таблицы orders с таблицей employees
-- Выведет всех сотрудников, если у сотрудника нет заказов, выведет NULL в соответствующих ячейках

SELECT 
    e.employee_id,
    e.last_name,
    e.first_name,
    o.order_id,
    o.creation_date
FROM 
    orders o
RIGHT JOIN 
    employees e ON o.employee_id = e.employee_id;

-- INNER JOIN - выведет только те строки, которые имеют соответствия в обеих таблицах

SELECT 
    e.employee_id,
    e.last_name,
    e.first_name,
    o.order_id,
    o.creation_date
FROM 
    orders o
INNER JOIN 
    employees e ON o.employee_id = e.employee_id;

-- CROSS JOIN - декартово произведение, все сотрудники соединяются со всеми продуктами

SELECT 
    e.employee_id,
    e.last_name,
    e.first_name,
    pd.product_id,
    pd.product_name
FROM 
    employees e
CROSS JOIN 
    products pd;

-- JOIN ... USING - соединение по столбцу employee_id, который имеет одинаковое имя в обеих таблицах

SELECT 
    employee_id,
    e.last_name,
    e.first_name,
    o.order_id,
    o.creation_date
FROM 
    employees e
JOIN 
    orders o USING (employee_id);