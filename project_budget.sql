CREATE DATABASE project_budget;
use project_budget;
CREATE TABLE signup (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100),
    income FLOAT,
    funds FLOAT,
    pay_schedule INT
);

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(100),
    cost FLOAT,
    date DATE,
    category VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE subscriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    subscription_name VARCHAR(100),
    cost FLOAT,
    one_time_payment FLOAT,
    pay_period VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(id)
);


CREATE TABLE debts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    debt FLOAT,
    interest FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE meals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    food VARCHAR(100),
    price FLOAT,
    ingredients TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
select * from users;
-- Insert sample data into the users table
INSERT INTO users (name, email, password, income, funds, pay_schedule)
VALUES ('Romario Salama', 'romariosalama@yahoo.com', 'test', 5000.00, 3000.00, 1);

-- Insert sample data into the expenses table
INSERT INTO expenses (user_id, name, cost, date, category)
VALUES (1, 'Groceries', 200.00, '2024-05-07', 'Food'),
       (1, 'Utilities', 100.00, '2024-05-06', 'Bills');

-- Insert sample data into the subscriptions table
INSERT INTO subscriptions (user_id, subscription_name, cost, one_time_payment, pay_period)
VALUES (1, 'Netflix', 15.00, NULL, 'Monthly'),
       (1, 'Gym Membership', 30.00, NULL, 'Monthly');

-- Insert sample data into the debts table
INSERT INTO debts (user_id, debt, interest)
VALUES (1, 2000.00, 0.05);

-- Insert sample data into the meals table
INSERT INTO meals (user_id, food, price, ingredients) VALUES
(1, 'Spaghetti with Meatballs', 8.99, 'Spaghetti, Tomato Sauce, Meatballs, Parmesan Cheese'),
(1, 'Chicken Stir Fry', 7.49, 'Chicken, Bell Peppers, Broccoli, Soy Sauce, Rice'),
(1, 'Vegetable Curry', 6.99, 'Potatoes, Carrots, Cauliflower, Peas, Curry Paste, Coconut Milk'),
(1, 'Grilled Salmon', 9.99, 'Salmon Fillet, Lemon, Garlic, Olive Oil, Salt, Pepper'),
(1, 'Caprese Salad', 5.49, 'Tomatoes, Mozzarella Cheese, Basil, Balsamic Vinegar, Olive Oil'),
(1, 'Vegetable Soup', 4.99, 'Carrots, Celery, Onion, Garlic, Vegetable Broth, Pasta'),
(1, 'Tofu Stir Fry', 6.49, 'Tofu, Bell Peppers, Snow Peas, Soy Sauce, Ginger, Garlic'),
(1, 'Mushroom Risotto', 7.99, 'Arborio Rice, Mushrooms, Onion, Garlic, White Wine, Parmesan Cheese'),
(1, 'BBQ Chicken Pizza', 8.49, 'Pizza Dough, BBQ Sauce, Chicken, Red Onion, Mozzarella Cheese');

use project_budget;
select * from users;
select * from expenses;
select * from subscriptions;
select * from debts;
select * from meals;
