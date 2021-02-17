## Import Mysql-Connector
import mysql.connector

## Connect to database
def ConnectDatabase():
    Database = mysql.connector.connect(
        host="127.0.0.1",
        user="USERNAME",
        password="PASSWORD",
        database="MessagingApp",
        auth_plugin='mysql_native_password'
    )
    return Database
