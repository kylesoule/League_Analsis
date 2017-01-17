import pyodbc, sys

"""
TODO:
    Error handling
"""

class MSSQL:
    cursor = None
    db = "LeagueAnalysis"
    
    def __init__(self):
        #cnxn = pyodbc.connect("DSN=mssql_namestaken")
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
        self.cursor = cnxn.cursor()
    
    def insert(self, sql, data):
        """
        Insert data.
        
        Args:
            sql: Preformated SQL statement
            data: Data list
            
        Returns:
            True if success otherwise False
        """
        cursor = self.cursor
        
        try:
            cursor.execute(sql, data)
            cursor.commit()
            return True
        except:
            print sys.exc_info()[1]
            return False

    def bulk_insert(self, sql, data):
        """
        Bulk insert a list.
        
        Args:
            sql: Preformated SQL statement
            data: Data list
            
        Returns:
            True if success otherwise False
                
        Example:
            bulk_insert("INSERT INTO db.table (col1, col2) VALUES (?, ?)", data)
        """
        cursor = self.cursor

        try:
            cursor.executemany(sql, data)
            cursor.commit()
            return True
        except:
            print sys.exc_info()[1]
            return False

    def select(self, what, db, table, where):
        """
        Retrieves data from database.
        
        Args:
            what: Data being selected
            db: Database
            table: Table
            where: Where statement
        
        Returns:
            List of results
        """
        cursor = self.cursor
        
        sql = "SELECT {what} FROM {db}.dbo.{table} {where}".format(what=what, db=db, table=table, where=where)
        cursor.execute(sql)
        
        return cursor.fetchall()
    
    def get_champion_name(self, id):
        return self.select("name", self.db, "ChampionNames", "WHERE id={id}".format(id=id))[0][0]