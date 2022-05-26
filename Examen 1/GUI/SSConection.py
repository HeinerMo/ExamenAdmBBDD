# pip install pandas
# pip install pyodbc
import pyodbc
import pandas as pd

class PySSAdmin():
    def __init__(self):
        self.dbConnection = None

    def connectToDB(self, connServer:str, dbName:str, userName:str, userPassword:str):
        try:
            self.dbConnection = pyodbc.connect('DRIVER={SQL Server};SERVER='+connServer+';DATABASE='+dbName+';UID='+userName+';PWD='+userPassword)
            return 1
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '08001':
                return "SQL Server does not exist or access denied."
            if sqlstate == '28000':
                return "Login failed for user "+ "'"+userName+"'"

            return ex.args[1]
            

    def dataFrameToSS(self, dataFrame:pd.DataFrame, dfColumns:list[str], tableName:str, ssColumns:list[str]):
        cursor = self.dbConnection.cursor()

        # Loop through each row of the dataframe
        for index, row in dataFrame.iterrows():
            valuesToInsert = self.rowValuesToInsert(row, dfColumns)
            columnsToModify = self.ssColumnsToInsert(ssColumns)

            #NOTE: valuesToInsert must be in the same order that columnsToModify
            insertQuery = "INSERT INTO "+tableName+"("+columnsToModify+")"+"VALUES("+valuesToInsert+")"
            cursor.execute(insertQuery)
            self.dbConnection.commit()

        cursor.close()

    def tableToDataFrame(self, sql:str):
        dataFrame = pd.read_sql(sql, self.dbConnection)
        return dataFrame

    def rowValuesToInsert(self, row, dfColumns:list[str]):
        """Returns the values of a row (row) of the dataframe prepared to be added to the VALUE 
        of the insertion query according to the columns (dfColumns) of that dataframe that are indicated. Code by: Antony Seas Vega"""
        insertValues = ""
        # Get columns values in the actual row depending on the variable dfColumns (index 0 to last)
        for columnName in dfColumns:
            columnValue = row[str(columnName)]
            if (isinstance(columnValue, int)):
                insertValues = insertValues + ", " + str(columnValue)
            if (isinstance(columnValue, str)):
                columnValue = columnValue.replace('\'', '\'\'')
                columnValue = columnValue.rstrip() # Removes all whitespace in the end of the string
                insertValues = insertValues + ", " + "'"+columnValue+"'"

        # Remove ", 'space'" that is at the beginning of the variable insertValues
        insertValues = insertValues[2:]
        return insertValues

    def ssColumnsToInsert(self, ssColumns:list[str]):
        """Returns the names of the columns (ssColumns) that the user indicates from the 
        SQL Server database table that are going to be modified. Code by: Antony Seas Vega"""
        return ','.join(ssColumns)

    def execQuery(self, sqlQuery):
        cursor = self.dbConnection.cursor()
        cursor.execute(sqlQuery)
        return cursor

    def closeConnection(self):
        self.dbConnection.close()
        self.dbConnection = None
