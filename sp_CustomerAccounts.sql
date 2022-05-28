CREATE OR ALTER PROCEDURE sp_CustomerAccounts
@param_beginDate DATETIME= NULL
,@param_endDate DATETIME= NULL
,@param_Is_Deleted BIT =NULL
,@para_clientID INT = NULL
,@param_Customer_Name VARCHAR(25) = NULL
,@param_Customer_LastName VARCHAR(25)=NULL
,@param_customerID INT = NULL

AS
BEGIN
	BEGIN TRY
		DECLARE @local_query VARCHAR(MAX) = 'SELECT * FROM [CUSTOMERS].[tb_CUSTOMER_ACCOUNTS]'
		DECLARE @local_where VARCHAR(MAX) = ' WHERE'
		DECLARE @local_hasWhere BIT = 0
		
		
		--DATES
		IF (@param_beginDate IS NOT NULL)
			BEGIN 
				SET @local_where = @local_where + ' ([LAST_MODIFIED_DATE] >= ''' 
				+ CAST(@param_beginDate AS VARCHAR) + ''')'
				SET @local_hasWhere = 1
			END
		IF (@param_endDate IS NOT NULL)
			BEGIN
				IF (@local_hasWhere = 1)
					BEGIN
						SET @local_where = @local_where + ' AND ([LAST_MODIFIED_DATE] <= ''' + CAST(@param_endDate AS VARCHAR) + ''')'
					END
				ELSE
					BEGIN
						SET @local_where = @local_where + ' ([LAST_MODIFIED_DATE] <= ''' + CAST(@param_endDate AS VARCHAR) + ''')'
					END
				SET @local_hasWhere = 1
			END
		--IS DELETED
		IF (@param_Is_Deleted IS NOT NULL)
			BEGIN
				IF (@local_hasWhere = 1)
					BEGIN
						SET @local_where = @local_where + ' AND ([IS_DELETED] = ''' + CAST(@param_Is_Deleted AS VARCHAR) + ''')'
					END
				ELSE
					BEGIN
						SET @local_where = @local_where + ' ([IS_DELETED] = ''' + CAST(@param_Is_Deleted AS VARCHAR) + ''')'
					END
				SET @local_hasWhere = 1
			END
		
		--client id
		IF (@para_clientID IS NOT NULL)
			BEGIN 
				IF (@local_hasWhere = 1)
					BEGIN
						SET @local_where = @local_where + 'AND ([CLIENT_ID] = ' + CAST(@para_clientID AS VARCHAR) + ')'
					END
				ELSE
					BEGIN
						SET @local_where = @local_where + ' ([CLIENT_ID] = ' + CAST(@para_clientID AS VARCHAR) + ')'
					END
				SET @local_hasWhere = 1
			END

		--customer name
		IF (@param_Customer_Name IS NOT NULL)
			BEGIN 
				IF (@local_hasWhere = 1)
					BEGIN
						SET @local_where = @local_where + 'AND ([CUSTOMER_NAME] = ''' + CAST(@param_Customer_Name AS VARCHAR) + ''')'
					END
				ELSE
					BEGIN
						SET @local_where = @local_where + ' ([CUSTOMER_NAME] = ''' + CAST(@param_Customer_Name AS VARCHAR) + ''')'
					END
				SET @local_hasWhere = 1
			END
		--customer lastname
		IF (@param_Customer_LastName IS NOT NULL)
			BEGIN 
				IF (@local_hasWhere = 1)
					BEGIN
						SET @local_where = @local_where + 'AND ([CUSTOMER_LAST_NAME] = ''' + CAST(@param_Customer_LastName AS VARCHAR) + ''')'
					END
				ELSE
					BEGIN
						SET @local_where = @local_where + ' ([CUSTOMER_LAST_NAME] = ''' + CAST(@param_Customer_LastName AS VARCHAR) + ''')'
					END
				SET @local_hasWhere = 1
			END
		--customer
		IF (@param_customerID IS NOT NULL)
			BEGIN 
				IF (@local_hasWhere = 1)
					BEGIN
						SET @local_where = @local_where + 'AND ([CUSTOMER_ACCOUNT_ID] = ' + CAST(@param_customerID AS VARCHAR) + ')'
					END
				ELSE
					BEGIN
						SET @local_where = @local_where + ' ([CUSTOMER_ACCOUNT_ID] = ' + CAST(@param_customerID AS VARCHAR) + ')'
					END
				SET @local_hasWhere = 1
			END

			
		IF (@local_hasWhere = 1)
			BEGIN
				SET @local_query = @local_query + ' ' + @local_where
			END
		EXEC(@local_query)
	END TRY
	BEGIN CATCH
		PRINT 'N'+ @@ERROR	
	END CATCH
END

--EXEC sp_CustomerAccounts '2012-01-01', '2022-12-31', 0, 1005, null, null, 11