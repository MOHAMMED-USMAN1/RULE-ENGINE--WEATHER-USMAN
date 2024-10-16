                                                                 Application 1 : Rule Engine with AST
To implement and run the code for this rule engine with AST (Abstract Syntax Tree), you can follow these steps. I'll break down the development process and suggest where and how to run the code.

1. Environment Setup
For this project, you'll need to set up a development environment where you can write and execute Python code (since Python is well-suited for handling AST and APIs). You can run the application on your local machine, in an IDE, or on the cloud. Here's what you'll need:

Required Tools:
Python 3.x: Install Python from python.org.
Flask  
Install Flask: pip install Flask
 Database: Use SQLite for simplicity, or opt for PostgreSQL or MySQL for more complex data handling.
SQLite is built-in with Python.
 For MySQL: pip install mysql-connector-python
IDEs or Editors:
VS Code: A popular choice for coding, supports Python with extensions.


 2. Project Structure
You can organize your code in a directory structure as follows:
rule-engine-ast/
│
├── app.py          # Main application file (API layer)
├── ast_engine.py   # Rule engine logic (AST handling)
├── database.py     # Database models and interactions
├── models.py       # Data classes or schemas (for request/response)
└── requirements.txt # Dependencies (Flask/FastAPI, databases)


3. Data Structure (AST Representation)
You can define a Node class to represent the AST. Here’s a simple Python class:

REFER TO ruleengine_ast.py file

4. API Design (with Flask or FastAPI)
app.py - API Layer
You can design RESTful APIs using Flask or FastAPI. Here’s an example of how to set up an API with Flask:


REFER TO ruleengine_app.py file

5. Rule Creation and Evaluation
Here’s an example of the core rule creation and evaluation functions.

REFER TO ruleengine_ast.py file

6. Database Storage
You can store the AST rules in a database like SQLite or PostgreSQL. Here's an example of using SQLite.

for schema representation REFER TO  REFER TO ruleengine_schema_database_sqllite.db file

for database - REFER TO ruleengine_database.py file

7. Test Cases
Test the system by creating unit tests for the main functionalities


refer to ruleengine_test.py file

8. Running the Application

   refer to ruleengine_runafile


                                                                                          

                                                     Application 2 : Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates
 
To implement and run the Real-Time Data Processing System for Weather Monitoring, follow these step-by-step instructions. I'll break the process into setup, code implementation, and running the system:


FOR CODE REFER TO FILE weather_monitor.py
Step 1: Prerequisites

•	Python Installed: Make sure you have Python 3.x installed on your machine.
•	
•	Libraries: You'll need some Python libraries to handle API calls, data processing, storage, and visualization:


o	requests: For calling the OpenWeatherMap API
o	pandas: For data handling and aggregation
o	matplotlib or plotly: For data visualization
o	sqlite3 or SQLAlchemy: For database management
o	smtplib: For sending email alerts (if you choose email alerts)



To install these libraries, run:

-pip install requests pandas matplotlib plotly sqlite3 SQLAlchemy




Sign up for OpenWeatherMap API: Sign up on OpenWeatherMap and get your API key. You will need this to retrieve weather data.


Step 2: Create the Python Script

1.	API Configuration: Set up the API URL and key, and define the metro cities you want to monitor (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
2.	Retrieve Weather Data: Write a function to call the OpenWeatherMap API, retrieve real-time data for each city, and parse the response.
3.	Convert Temperature: Create a function to convert temperature from Kelvin to Celsius.
4.	Rollup Aggregation: Implement daily aggregation calculations:
o	Average temperature
o	Maximum temperature
o	Minimum temperature
o	Dominant weather condition (can be based on frequency or priority)
5.	Alerting Mechanism: Set up alert thresholds (e.g., temperature exceeding 35°C) and trigger alerts if the conditions are met. You can either log the alert in the console or send an email notification.
6.	Data Storage: Use a database (SQLite or a similar option) to store daily summaries for further analysis.
7.	Visualization: Implement a function to visualize weather summaries and triggered alerts using matplotlib or plotly.

Step 3: Code Implementation

Here’s a basic structure of how the code might look: refer github

STEP 4 : RUN THE APP

python weather_monitor.py

Step 5: Testing the System
•	Test Case 1: Run the script with your API key and verify that data is fetched from the OpenWeatherMap API.
•	Test Case 2: Modify the interval or simulate API responses and ensure weather data for each city is parsed and stored correctly.
•	Test Case 3: Test temperature conversion by printing the results for different API responses.
•	Test Case 4: Simulate weather data over multiple days and verify daily summaries (average, max, min temperatures, and dominant condition).
•	Test Case 5: Set temperature alert thresholds and ensure alerts trigger when thresholds are breached.














