import oracledb
def get_connection_string_from_TXT(file_source):
    connection_string = ''
    index_parameter = 0

    try:
        with open(file_source, 'r', encoding='UTF-8') as file:
            for line in file:
                index_parameter += 1
                connection_string += line.rstrip()
                if index_parameter == 2:
                    connection_string += '@'
                elif index_parameter == 4:
                    pass
                else:
                    connection_string += '/'

        return connection_string
    except oracledb.exceptions.DatabaseError:
        print('Odmowa zalogowania z powodu błędnych lub niewystarczającej ilości danych do bazy')


'''print(get_connection_string_from_TXT('oracle_oltp_connection_parameters.txt'))


text = "OLTP/Kacperowy2001!@localhost:1521/xepdb1"
result = text.split('/', 1)[0]
print(result)'''



# cursor.execute('select * from categoryMasterKP')
# connection.commit()
# for result in cursor.fetchall():
#     print(result)

