######################################################################
## Connect to MySQL
######################################################################
import mysql.connector

cnx = mysql.connector.connect(
    user="vasco",
    password="K9vGtQ4AOZUH3aAserdY",
    host="ipwhitelisting-mysql-dev-mysql.mysql.database.azure.com",
    port=3306,
    database="employees",
    ssl_ca="/PhytonAzureMySQL/BaltimoreCyberTrustRoot.crt.pem",
    ssl_disabled=False
)

#cnx.close()

######################################################################
## query data
######################################################################
import datetime
import mysql.connector

#cnx = mysql.connector.connect(user='scott', database='employees')
cursor = cnx.cursor()

query = ("SELECT emp_no, first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (emp_no, first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y} as matricule {}".format(
    last_name, first_name, hire_date, emp_no))

cursor.close()
cnx.close()