create or replace PROCEDURE get_tables_to_extract_or_load_data(
    source_or_target_schema VARCHAR2,
    result_cursor OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN result_cursor FOR
        SELECT
            rc.table_name AS referenced_table
        FROM
            all_constraints c
        JOIN
            all_cons_columns cc ON c.owner = cc.owner AND c.table_name = cc.table_name AND c.constraint_name = cc.constraint_name
        LEFT JOIN
            all_constraints rc ON c.r_owner = rc.owner AND c.r_constraint_name = rc.constraint_name
        LEFT JOIN
            all_cons_columns rcc ON rc.owner = rcc.owner AND rc.table_name = rcc.table_name AND rc.constraint_name = rcc.constraint_name
        WHERE
            c.owner IN (source_or_target_schema)
        AND
            c.constraint_type = 'R'
        UNION
        SELECT
            cc.table_name
        FROM
            all_constraints c
        JOIN
            all_cons_columns cc ON c.owner = cc.owner AND c.table_name = cc.table_name AND c.constraint_name = cc.constraint_name
        LEFT JOIN
            all_constraints rc ON c.r_owner = rc.owner AND c.r_constraint_name = rc.constraint_name
        LEFT JOIN
            all_cons_columns rcc ON rc.owner = rcc.owner AND rc.table_name = rcc.table_name AND rc.constraint_name = rcc.constraint_name
        WHERE
            c.owner IN (source_or_target_schema)
        AND
            c.constraint_type = 'R';
END get_tables_to_extract_or_load_data;