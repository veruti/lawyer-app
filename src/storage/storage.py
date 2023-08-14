import sys

from PyQt6.QtSql import QSqlDatabase, QSqlQuery

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("lawyers.sqlite")

if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)

query = QSqlQuery()
query.exec(
    """
    CREATE TABLE lawyers (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        
        first_name VARCHAR(30) NOT NULL,
        middle_name VARCHAR(35) NOT NULL, 
        last_name VARCHAR(30) NOT NULL
    )
    """
)

print(con.tables())
