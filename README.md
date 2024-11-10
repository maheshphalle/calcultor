Project Name - Calculator-Python-Flask


Prerequisites:
-----------------------
1) Python 3.x
2) Flask Library
3) VSCode (Visual Studio Code)

Installation Steps
-----------------------
1) Install Python: Download and install Python from the official website.
2) Verify Python and pip Installation: Open a terminal and run:

![Alt Text for Image]

![image](https://github.com/user-attachments/assets/9f6f36e9-b0a8-4ebc-9a68-77a9efb162d1)


Install Flask: Install Flask using pip:

sh
pip install flask
Create Flask Application: Set up your Flask application by creating a new file app.py and writing your code.

Run the Application: Start your Flask app by running:

sh
python app.py
Description
This project demonstrates how to build a basic calculator application using the Flask framework. We will go through the necessary steps to set up the environment, install prerequisites, and run the application to perform basic arithmetic operations.

Usage
To use the calculator API, follow these steps:

Start the Flask Application:

sh
python app.py
Access the Calculator:

Open your web browser and navigate to http://127.0.0.1:5000/calculate?num1=5&num2=3 to perform calculations.

Replace num1 and num2 with the numbers you want to calculate.

Example Requests
To perform addition, send a GET request to the /calculate endpoint with the appropriate query parameters:

plaintext
http://127.0.0.1:5000/calculate?operation=+&num1=5&num2=3
Example Response
The response will be in JSON format, providing the result of the calculation:

json
{
    "result": 8.0
}
Key Features:
Perform addition (+)

Perform subtraction (-)

Perform multiplication (*)

Perform
