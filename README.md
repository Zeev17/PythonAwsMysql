# PhytonAzureMySQL

# put folder in .gitignore
git rm -r  --cached


# Create a virtual env
## option 1
https://code.visualstudio.com/docs/python/environments
type (ctrl+shift+P)
SELECT VENV AS VIRTUAL ENV
    SELECT ENVIRONEMENT
## option 2
python -m venv venv
given name of virtual env is "venv"
    [UNIX]source venv/bin/activate
    [cmd]source venv\Scripts\activate.bat
    [ps1] .\\venv\Scripts\Activate.ps1

# Select a python interpreter in VScode
type (ctrl+shift+P)
*** the corresponding to venv ***

# install package dependency
pip install -r requirements.txt


# dumps data
From azure shell console :
mysql -h ipwhitelisting-mysql-dev-mysql.mysql.database.azure.com -u vasco -p employees < employees.sql

# connect to database en query data
SHOW DATABASES;
USE employees;
SELECT * from employees LIMIT 100;
