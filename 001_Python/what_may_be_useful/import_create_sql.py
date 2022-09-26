import my_query


# table_name = 'the_table'
# column_list = ['col_01','col_02','col_03']
# extract_conditions_list = [
#     "col_01 ='{yyyy}-{mm}-{dd}"
#     ]

table_name = 'The_local_table'
column_list = ['production_date','machine_code','product_code']
extract_conditions_list = [
    "production_date ='{yyyy}-{mm}-{dd}"
    ,"machin_code = '1234aaa'"
    ]

query_str = my_query.concatenate_sql_clauses(column_list, table_name, extract_conditions_list)
print(query_str)

# from test_my_tools import screamer

# print(screamer(query_str))
