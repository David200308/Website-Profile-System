import mysql.connector
from mysql.connector import errorcode
from prettytable import PrettyTable

def database(queryStr):
    cnx = mysql.connector.connect(user='root', 
                                    password='',
                                    host='127.0.0.1',
                                    database='WEBSITE')
    cursor = cnx.cursor()

    query = (queryStr)

    cursor.execute(query)

    if (query.split(" ")[0] == "SELECT"):
        table = PrettyTable(['Name', 'Link'])
        for (WEBSITE_NAME, LINK) in cursor:
            table.add_row([WEBSITE_NAME, LINK])

        print(table)
    if (query.split(" ")[0] == "INSERT"):
        cnx.commit()
        print("Website Inserted")

    cursor.close()
    cnx.close()
