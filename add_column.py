import cx_Oracle

connection = None

username = 'XXXXXX'
password = 'XXXXXX'
dsn = '172.22.132.113/anonipac'
port = 1521
encoding = 'UTF-8'
service_name= 'anonipac'
table = 'PLN_HPC.PNL_TEXTO_ATENDIMENTO'

try:
    connection = cx_Oracle.connect(
        username,
        password,
        dsn,
        encoding=encoding)

    # imprime la version de la base de datos
    print(connection.version)
    print("select count(*) from PLN_HPC.PNL_TEXTO_ATENDIMENTO")
    
    cur = connection.cursor()
    cur.execute("select count(*) from PLN_HPC.PNL_TEXTO_ATENDIMENTO")
    res = cur.fetchall()
    
    query="ALTER TABLE "+str(table)+" ADD textoProcessado TEXT;"
    print query;
    cur.execute(query);

    # ALTER TABLE table_name ADD column_name data_type constraint;

except cx_Oracle.Error as error:
    print(error)

finally:
    # release the connection
    if connection:
        connection.close()
