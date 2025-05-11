# Bajaj Finserv Health - Python Qualifier 1

## 🚀 Task Overview

- Automatically trigger an API call to generate a webhook.
- Determine the assigned SQL question based on the registration number.
- Solve the SQL question using Python.
- Submit the final SQL query to the given webhook using a token.

---

## 👤 Developer Info

- Name: Ashutosh Dubey 
- Reg No: REG12347
- Email: ashutoshdubey.ca21@acropolis.in

---

## ✅ SQL Solution

### Question:
Find the highest salary not credited on the 1st of any month, along with the employee’s name, age, and department.

### SQL Query:

```sql
SELECT 
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    TIMESTAMPDIFF(YEAR, e.DOB, CURDATE()) AS AGE,
    d.DEPARTMENT_NAME
FROM PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE DAY(p.PAYMENT_TIME) != 1
ORDER BY p.AMOUNT DESC
LIMIT 1;
