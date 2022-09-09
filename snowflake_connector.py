'''!pip install snowflake-connector-python==2.7.6
    !pip install snowflake'''
def run_query(Query):
    rows = 0
    snowflake_connection = snowflake.connector.connect(user='', password='',
                                                       account='', role='',
                                                       database='')
    try:
        result = snowflake_connection.cursor().execute('use warehouse ' + 'WAREHOUSE_NAME')
        print(result)

        result = snowflake_connection.cursor().execute(Query)
        lines = result.fetchall()
    except Exception as e:
        raise Exception(str(e) + '\n\n' + Query)
    finally:
        snowflake_connection.cursor().close()
    return lines

