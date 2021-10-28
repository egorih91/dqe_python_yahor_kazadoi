import pyodbc


class WorkingWithDb:
    def __init__(self, result_list, database_name=None):
        self.result_list = result_list  # list with dictionaries
        self.type_of_publication = ''

        if database_name is None:
            self.database_name = 'files_with_results/result_db.db'
        else:
            self.database_name = database_name

        # structure of tables that should be created if not exists in DB
        self.tables = {
            'news': 'insert_date date, text varchar, city varchar, date_of_news date',
            'private_ad': 'insert_date date, text varchar, date_of_ad date, expiration_date date',
            'sport_result': 'insert_date date, kind_of_sport varchar, participant1 varchar, participant2 varchar, '
                            'game_result varchar, winner varchar',
            'text_information': 'insert_date date, text varchar'
        }
        conn_string = "DRIVER={SQLite3 ODBC Driver}; " \
                      "Direct=True;" \
                      f"Database={self.database_name};" \
                      "String Types= Unicode"
        with pyodbc.connect(conn_string) as con:
            self.cur = con.cursor()

    def run_statement(self, statement):  # not sure if the method is needed but it can be
        self.cur.execute(statement)

    # first of all we need to create tables (of they do not exist in DB)
    def creating_result_table(self):
        for table_name, structure in self.tables.items():
            if not self.cur.tables(table=table_name, tableType='TABLE').fetchone():  # check not existence of the tables
                self.cur.execute(f"create table {table_name} ({structure})")
                self.cur.commit()

    def check_if_record_exists(self, result_dict):  # method for checking if the record exists in the table
        self.type_of_publication = result_dict.pop('type')

        # creating where-statement
        where_statement = "1=1 and "
        for column, value in result_dict.items():

            # exclude columns that have different values of dates
            # that depends on time of running the program
            if column not in ['date_of_news', 'date_of_ad']:
                where_statement = where_statement + f"{column}='{value}' and "

        where_statement = where_statement[:-5]

        statement = f"select * from {self.type_of_publication} where {where_statement}"

        # print(statement)
        try:
            self.cur.execute(statement)
            statement_result = self.cur.fetchall()
        except pyodbc.Error as e:
            print(f"Existence of the record cannot be checked due to error")
            print(f"Record: {result_dict}")
            print(f"Error: {e}")
            statement_result = False

        return statement_result

    def __insert_row(self, result_dict):  # method for inserting the row from the dictionary
        values = ''
        columns = 'insert_date, '
        for column, value in result_dict.items():
            columns = columns + column + ", "
            values = values + "'" + str(value) + "', "
        columns = columns[:-2]
        values = values[:-2]

        statement = f"insert into {self.type_of_publication} ({columns}) values (current_date, {values})"
        # print(statement)
        try:
            self.cur.execute(statement)
            self.cur.commit()
        except pyodbc.Error as e:
            print(f"Next record were not published into DB due to error")
            print(f"Record: {result_dict}")
            print(f"Error: {e}")

    # method that includes a few steps - checking if row exists, adding the row if not
    def adding_rows_to_db(self):
        inserted_rows = 0

        for result in self.result_list:
            if len(result) != 0:
                select_result = self.check_if_record_exists(result)
                if type(select_result) is not bool:
                    if len(select_result) == 0:
                        self.__insert_row(result)
                        inserted_rows += 1

        if inserted_rows == 0:
            print(f"No rows to add to db")
        else:
            print(f"Rows were added to the {self.database_name}")

    # method that includes creating tables for results (if needed) and adding_rows_to_db
    def adding_data_to_db(self):
        self.creating_result_table()
        self.adding_rows_to_db()
