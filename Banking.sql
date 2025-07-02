
--------------------------------------------------------CREATING TABLES FOR BANKING------------------------------------------------------------

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY IDENTITY(1,1),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    DOB DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15),
    address VARCHAR(255)
);
 


CREATE TABLE Accounts (
    account_id INT PRIMARY KEY IDENTITY(1,1),
    customer_id INT NOT NULL,
    account_type VARCHAR(20) CHECK (account_type IN ('savings', 'current', 'zero_balance')),
    balance DECIMAL(15, 2) CHECK (balance >= 0),

    CONSTRAINT FK_Accounts_Customers FOREIGN KEY (customer_id) 
        REFERENCES Customers(customer_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY IDENTITY(1,1),
    account_id INT NOT NULL,
    transaction_type VARCHAR(20) CHECK (transaction_type IN ('deposit', 'withdrawal', 'transfer')),
    amount DECIMAL(15, 2) CHECK (amount > 0),
    transaction_date DATETIME DEFAULT GETDATE(),

    CONSTRAINT FK_Transactions_Accounts FOREIGN KEY (account_id)
        REFERENCES Accounts(account_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

---------------------------------------------------------TASK 1 - INSERTING-----------------------------------------------------------------

INSERT INTO Customers (first_name, last_name, DOB, email, phone_number, address) VALUES
('Alice', 'Johnson', '1990-03-15', 'alice.j@example.com', '9876543210', '123 Main St'),
('Bob', 'Smith', '1985-06-20', 'bob.smith@example.com', '9876543211', '456 Oak Ave'),
('Carol', 'Davis', '1992-01-10', 'carol.davis@example.com', '9876543212', '789 Pine Ln'),
('David', 'Miller', '1988-11-05', 'david.miller@example.com', '9876543213', '321 Cedar Rd'),
('Eva', 'Brown', '1995-09-30', 'eva.brown@example.com', '9876543214', '654 Maple St'),
('Frank', 'Wilson', '1991-12-22', 'frank.w@example.com', '9876543215', '987 Elm Blvd'),
('Grace', 'Taylor', '1987-07-18', 'grace.taylor@example.com', '9876543216', '159 Birch Ct'),
('Henry', 'Anderson', '1983-04-02', 'henry.anderson@example.com', '9876543217', '753 Walnut Dr'),
('Ivy', 'Thomas', '1996-10-25', 'ivy.thomas@example.com', '9876543218', '951 Spruce Way'),
('Jack', 'Moore', '1989-02-14', 'jack.moore@example.com', '9876543219', '852 Redwood Pl');



INSERT INTO Accounts (customer_id, account_type, balance) VALUES
(1, 'savings', 5000.00),
(2, 'current', 15000.00),
(3, 'savings', 3000.00),
(4, 'zero_balance', 0.00),
(5, 'current', 10000.00),
(6, 'savings', 7500.00),
(7, 'current', 20000.00),
(8, 'zero_balance', 0.00),
(9, 'savings', 8500.00),
(10, 'current', 12000.00);



INSERT INTO Transactions (account_id, transaction_type, amount) VALUES
(1, 'deposit', 2000.00),
(2, 'withdrawal', 3000.00),
(3, 'deposit', 1000.00),
(4, 'deposit', 500.00),
(5, 'withdrawal', 2000.00),
(6, 'deposit', 2500.00),
(7, 'transfer', 4000.00),
(8, 'deposit', 1500.00),
(9, 'withdrawal', 1000.00),
(10, 'deposit', 3000.00);

SELECT * FROM Customers;
SELECT * FROM Accounts;
SELECT * FROM Transactions;


----------------------------------------------------------TASK 2----------------------------------------------------------------

-- 1. Name, account type, and email of all customers
SELECT c.first_name, c.last_name, a.account_type, c.email
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id;

-- 2. All transaction corresponding to each customer
SELECT c.first_name, c.last_name, t.*
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id
JOIN Transactions t ON a.account_id = t.account_id;

-- 3. Increase balance of specific account
UPDATE Accounts SET balance = balance + 1000 WHERE account_id = 1;

-- 4. Combine first and last names as full_name
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM Customers;

-- 5. Remove zero balance savings accounts
DELETE FROM Accounts WHERE balance = 0 AND account_type = 'savings';

-- 6. Find customers in a specific city
SELECT * FROM Customers WHERE address LIKE '%789 Pine Ln%';

-- 7. Get balance for a specific account
SELECT balance FROM Accounts WHERE account_id = 1;

-- 8. List all current accounts with balance > 1000
SELECT * FROM Accounts WHERE account_type = 'current' AND balance > 1000;

-- 9. Retrieve all transactions for a specific account
SELECT * FROM Transactions WHERE account_id = 2;

-- 10. Calculate interest on savings accounts (e.g., 4% interest)
SELECT account_id, balance, balance * 0.04 AS interest FROM Accounts WHERE account_type = 'savings';

-- 11. Accounts with balance < overdraft limit (e.g., < 2000)
SELECT * FROM Accounts WHERE balance < 2000;

-- 12. Customers not in a specific city
SELECT * FROM Customers WHERE address NOT LIKE '%789 Pine Ln%';

-----------------------------------------------------------TASK 3------------------------------------------------------------
-- 1. Average account balance
SELECT AVG(balance) AS avg_balance FROM Accounts;

-- 2. Top 10 highest balances
SELECT TOP 10 * FROM Accounts ORDER BY balance DESC;

-- 3. Total deposits on specific date
SELECT SUM(amount) AS total_deposit
FROM Transactions
WHERE transaction_type = 'deposit'
AND CAST(transaction_date AS DATE) = '2024-06-01'; -- change date as needed

-- 4. Oldest and newest customers
SELECT * FROM Customers ORDER BY DOB ASC; -- oldest first
SELECT * FROM Customers ORDER BY DOB DESC; -- newest first

-- 5. Transaction details with account type
SELECT t.*, a.account_type
FROM Transactions t
JOIN Accounts a ON t.account_id = a.account_id;

-- 6. Customers and account details
SELECT c.*, a.*
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id;

-- 7. Transactions with customer info for specific account
SELECT t.*, c.first_name, c.last_name
FROM Transactions t
JOIN Accounts a ON t.account_id = a.account_id
JOIN Customers c ON a.customer_id = c.customer_id
WHERE a.account_id = 1;

-- 8. Customers with more than one account
SELECT customer_id, COUNT(*) AS account_count
FROM Accounts
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- 9. Difference between deposit and withdrawal
SELECT
    SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE 0 END) -
    SUM(CASE WHEN transaction_type = 'withdrawal' THEN amount ELSE 0 END) AS diff
FROM Transactions;

-- 10. Average daily balance 
SELECT account_id, AVG(balance) AS avg_balance
FROM Accounts
GROUP BY account_id;

-- 11. Total balance per account type
SELECT account_type, SUM(balance) AS total_balance
FROM Accounts
GROUP BY account_type;

-- 12. Accounts with most transactions
SELECT account_id, COUNT(*) AS txn_count
FROM Transactions
GROUP BY account_id
ORDER BY txn_count DESC;

-- 13. Customers with high total balances and account types
SELECT c.first_name, c.last_name, a.account_type, SUM(a.balance) AS total_balance
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id
GROUP BY c.first_name, c.last_name, a.account_type
HAVING SUM(a.balance) > 10000;

-- 14. Duplicate transactions
SELECT account_id, amount, transaction_date, COUNT(*)
FROM Transactions
GROUP BY account_id, amount, transaction_date
HAVING COUNT(*) > 1;

-------------------------------------------------TASK 4-------------------------------------------------------------------------

-- 1. Customer with highest balance
SELECT * FROM Customers
WHERE customer_id = (
    SELECT customer_id FROM Accounts
    WHERE balance = (SELECT MAX(balance) FROM Accounts)
);

-- 2. Avg balance of customers with more than one account
SELECT AVG(balance) FROM Accounts
WHERE customer_id IN (
    SELECT customer_id FROM Accounts
    GROUP BY customer_id
    HAVING COUNT(*) > 1
);

-- 3. Accounts with transactions > average amount
SELECT * FROM Transactions
WHERE amount > (SELECT AVG(amount) FROM Transactions);

-- 4. Customers with no transactions
SELECT * FROM Customers
WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id
    FROM Accounts a
    JOIN Transactions t ON a.account_id = t.account_id
);

-- 5. Total balance for accounts with no transactions
SELECT SUM(balance) FROM Accounts
WHERE account_id NOT IN (SELECT DISTINCT account_id FROM Transactions);

-- 6. Transactions for lowest balance account
SELECT * FROM Transactions
WHERE account_id = (
    SELECT TOP 1 account_id FROM Accounts ORDER BY balance ASC
);

-- 7. Customers with multiple account types
SELECT customer_id FROM Accounts
GROUP BY customer_id
HAVING COUNT(DISTINCT account_type) > 1;

-- 8. Percentage of each account type
SELECT account_type, 
       COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Accounts) AS percentage
FROM Accounts
GROUP BY account_type;

-- 9. All transactions for a customer 
SELECT t.*
FROM Transactions t
JOIN Accounts a ON t.account_id = a.account_id
WHERE a.customer_id = 1;

-- 10. Total balance per account type with subquery
SELECT account_type,
       (SELECT SUM(balance) FROM Accounts a2 WHERE a2.account_type = a1.account_type) AS total_balance
FROM Accounts a1
GROUP BY account_type;
