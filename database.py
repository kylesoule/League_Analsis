import pyodbc

"""
TODO:
    Error handling
"""

class MSSQL:
    cursor = None
    db = "LeagueAnalysis"
    
    def __init__(self):
        cnxn = pyodbc.connect("DSN=mssql_namestaken")
        self.cursor = cnxn.cursor()

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