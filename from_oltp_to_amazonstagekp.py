from Oracle_Simple_ETL import Simple_ETL

# test official for ETL: OLTP -> AMAZONSTAGEKP

oltp_connection = Simple_ETL('oracle_oltp_connection_parameters.txt')
amazonstagekp_connection = Simple_ETL('oracle_amazonstagekp_connection_parameters.txt')

oltp_load_tables = oltp_connection.get_tables_to_extract_or_load('load')
amazonstagekp_extract_tables = amazonstagekp_connection.get_tables_to_extract_or_load('extract')

print(len(oltp_load_tables), len(amazonstagekp_extract_tables))

if len(amazonstagekp_extract_tables) == len(oltp_load_tables):
    for i in range(len(oltp_load_tables) -1, -1, -1):
        amazonstagekp_connection.insert_query(oltp_load_tables[len(oltp_load_tables) - i - 1],
                                              amazonstagekp_connection.get_schema_name(),
                                              oltp_load_tables[len(oltp_load_tables) - i - 1])

    for i in range(len(amazonstagekp_extract_tables)):
        amazonstagekp_connection.truncate_table_by_truncate_query(amazonstagekp_extract_tables[i])
else:
    print('Schematy nie są takie same lub mają różne struktury. Nie można zatem zrealizować procesu ETL')