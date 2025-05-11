import requests

# Send POST request to generate webhook 
payload = {
    "name": "Ashutosh Dubey",
    "regNo": "REG12347",
    "email": "ashutoshdubey.ca21@acropolis.in"
}

response = requests.post(
    "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON",
    json=payload
)

# Handle failure
if response.status_code != 200:
    print("Failed to generate webhook. Status code:", response.status_code)
    print(response.text)
    exit()

data = response.json()
webhook_url = data['webhook']
access_token = data['accessToken']

print("[+] Webhook URL:", webhook_url)
print("[+] Access Token:", access_token)

# Final SQL Query for Question 1 
final_query = """
SELECT 
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    TIMESTAMPDIFF(YEAR, e.DOB, CURDATE()) AS AGE,
    d.DEPARTMENT_NAME

FROM 
    PAYMENTS p
JOIN 
    EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN 
    DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID

WHERE 
    DAY(p.PAYMENT_TIME) != 1

ORDER BY 
    p.AMOUNT DESC

LIMIT 1;

"""

# Submit final SQL query to webhook 
headers = {
    "Authorization": access_token,  
    "Content-Type": "application/json"
}

solution_payload = {
    "finalQuery": final_query.strip()
}

submission_response = requests.post(webhook_url, headers=headers, json=solution_payload)

print("[+] Submission Status:", submission_response.status_code)
print("[+] Server Response:", submission_response.text)
