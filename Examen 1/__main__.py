#pip install tkcalendar
from gui.LoginWindow import LoginWindow

def main():

    lw = LoginWindow()
    lw.setSize(800, 600)
    lw.setLocationCenter()
    lw.setTitle("Iniciar Sesión")
    lw.startWin()

    """    
    # Get table from Postgres and convert it to pandas dataframe
    sql = "SELECT [CountryRegionCode], [Name] FROM Person.CountryRegion;"
    df =  ssConn.tableToDataFrame(sql)
    print(df)

    # Indicates the columns to be used in the same order both
    dfColumns:list[str] = ["id", "day", "airline", "destination"]
    ssColumns:list[str] = ["id", "day", "airline", "destination"]
    
    # Insert all values of the dataframe into a SQL Server table
    #ssConn.dataFrameToSS(df, dfColumns, "dbo.airlines_final1", ssColumns)

    # Close all the connections
    ssConn.closeConnection()
    """

if __name__ == '__main__':
    main()