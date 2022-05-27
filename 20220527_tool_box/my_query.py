def create_select_clause(column_list):
    select_clause = 'select'
    for column_name in column_list:
        select_clause += '\n    '
        if column_name != column_list[0]:
            select_clause += ','
        select_clause += column_name
    return select_clause
def create_from_clause(table_name):
    from_clause = 'from\n    ' + table_name
    return from_clause

def create_where_clause(extract_conditions_list):
    where_clause = 'where'
    for indx, condition_i in enumerate(extract_conditions_list):
        where_clause += '\n    '
        if indx != 0:
            where_clause += 'and '
        where_clause += condition_i
    return where_clause


# def concatenate_sql_clauses(select_clause, from_clause, where_clause):
#     query_str =\
#         select_clause + '\n'\
#         + from_clause + '\n'
#     if len(where_clause) >= 6:
#         query_str += where_clause

#     # print(query_str)
#     return query_str

def concatenate_sql_clauses(column_list, table_name, extract_conditions_list):
    select_clause = create_select_clause(column_list)
    from_clause = create_from_clause(table_name)
    where_clause = create_where_clause(extract_conditions_list)
    
    query_str =\
        select_clause + '\n'\
        + from_clause + '\n'
    if len(where_clause) >= 6:
        query_str += where_clause

    # print(query_str)
    return query_str

if __name__ == '__main__':
    table_name = 'the_table'
    column_list = ['col_01','col_02','col_03']
    extract_conditions_list = [
        "col_01 ='{yyyy}-{mm}-{dd}"
        ]

    # select_clause = create_select_clause(column_list)
    # from_clause = create_from_clause(table_name)
    # where_clause = create_where_clause(extract_conditions_list=extract_conditions_list)
    query_str = concatenate_sql_clauses(column_list, table_name, extract_conditions_list)
    print(query_str)