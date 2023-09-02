import connection_string
import oracledb

# This is a simple ETL for only the same databases(structures),
# ETL for two Oracle databases
# Author: Kacper Prusiński

class Simple_ETL:
    def __init__(self, file_source):
        try:
            self.parameters = connection_string.get_connection_string_from_TXT(file_source)
            self.connection = oracledb.connect(self.parameters)
            self.cursor = self.connection.cursor()
        except oracledb.DatabaseError as e:
            print(f'Błąd podczas nawiązywania połączenia: {e}')

    def get_any_values_from_list(self, result_list):
        list_of_results = []
        for row in result_list:
            list_of_results.append(row[0])

        return list_of_results

    def get_schema_name(self):
        return self.parameters.split('/', 1)[0]
    def get_tables_to_extract_or_load(self, operation):
        schema = self.get_schema_name()

        result_cursor = self.cursor.var(oracledb.CURSOR)
        self.cursor.callproc('get_tables_to_extract_or_load_data', [schema, result_cursor])
        result_list = list(result_cursor.getvalue())

        if operation.lower() == 'extract':
            result_list = result_list[::-1]
            result_list = self.get_any_values_from_list(result_list)
        elif operation.lower() == 'load':
            result_list = self.get_any_values_from_list(result_list)
        else:
            print('nie znaleziono operacji')

        return result_list


    def truncate_table_by_delete_query(self, table):
        self.cursor.execute(f'delete from {table}')
        self.connection.commit()
        print('delete wykonano')

    def truncate_table_by_truncate_query(self, table):
        self.cursor.execute(f'truncate table {table}')
        self.connection.commit()
        print('truncate wykonano')

    def insert_query(self, table_target, schema_source, table_source):
        self.cursor.execute(f'insert into {table_target} select * from {schema_source}.{table_source}')
        self.connection.commit()
        print('insert wykonany')
