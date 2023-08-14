import os
from dataclasses import dataclass

from PyQt6.QtSql import QSqlDatabase, QSqlQuery


@dataclass
class LawyerData:
    first_name: str
    middle_name: str
    last_name: str


@dataclass(slots=True, frozen=True)
class DBLawyer:
    id: int

    first_name: str
    middle_name: str
    last_name: str


class LaywerRepository:
    def __init__(self):
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName(os.sep.join(["media", "lawyers.sqlite"]))

        self.create_table()

    def __enter__(self):
        self.database.open()

    def __exit__(self, exc_type, exc_val, exc_tb):  # pyright: ignore
        self.database.close()

    def create_table(self):
        with self:
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

    def add(self, lawyer: LawyerData):
        with self:
            query = QSqlQuery()
            query.exec(
                f"""
                INSERT INTO lawyers(
                    first_name, 
                    middle_name,
                    last_name
                )
                VALUES ('{lawyer.first_name}', '{lawyer.middle_name}', '{lawyer.last_name}')
                """
            )

    def get_all(self) -> list[DBLawyer]:
        with self:
            query = QSqlQuery("SELECT * FROM lawyers", db=self.database)
            lawyers = []

            while query.next():
                id = query.value("id")
                first_name = query.value("first_name")
                middle_name = query.value("middle_name")
                last_name = query.value("last_name")

                db_lawyer = DBLawyer(
                    id=int(id),
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                )
                lawyers.append(db_lawyer)

            query.first()

        return lawyers


repo = LaywerRepository()
