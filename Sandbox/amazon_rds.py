import pyodbc

#driver= '{ODBC Driver 13 for SQL Server}'
driver = "{SQL Server}"
server = "leagueanalysis.cj13h9wmho9i.us-east-2.rds.amazonaws.com"
port = "1433"
username = 'namestaken'
password = 'H1LpQ3Rzf'

conn = "DRIVER={driver};SERVER={server};PORT={port};UID={uid};PWD={pwd}".format(driver=driver,
                                                                                server=server,
                                                                                port=port,
                                                                                uid=username,
                                                                                pwd=password)

cnxn = pyodbc.connect(conn)
cursor = cnxn.cursor()
cursor.execute("select @@VERSION")
row = cursor.fetchone()
if row:
    print row