USE TRANSACTION_PROCESSING_EXAMEN
GO


CREATE OR ALTER PROCEDURE sp_Events
@param_beginDate DATETIME = NULL
,@param_endDate DATETIME = NULL
,@param_eventID INT = NULL
,@param_currency INT = NULL
,@param_paymentType INT = NULL
,@param_customerID INT = NULL
,@para_clientID INT = NULL
AS
	BEGIN
		DECLARE @local_query VARCHAR(MAX) = 'SELECT * FROM FINANCIAL_DEPOSIT.tb_EVENTS' 
		DECLARE @local_where VARCHAR(MAX) = ' WHERE'
		DECLARE @local_hasWhere BIT = 0

		--dates
		IF (@param_beginDate IS NOT NULL)
			BEGIN 
				SET @local_where = @local_where + ' ([SUBMITTED_DATE] >= ''' 
				+ CAST(@param_beginDate AS VARCHAR) + ''')'
				SET @local_hasWhere = 1
			END
		IF (@param_endDate IS NOT NULL)
			BEGIN
				IF (@local_hasWhere = 1)
					BEGIN
						SET @local_where = @local_where + ' AND ([SUBMITTED_DATE] <= ''' + CAST(@param_endDate AS VARCHAR) + ''')'
					END
				ELSE
					BEGIN
						SET @local_where = @local_where + ' ([SUBMITTED_DATE] <= ''' + CAST(@param_endDate AS VARCHAR) + ''')'
					END
				SET @local_hasWhere = 1
			END
		--eventID
		IF (@param_eventID IS NOT NULL)
			BEGIN 
				IF (@local_hasWhere = 1)
					BEGIN
						SET @local_where = @local_where + 'AND ([EVENT_ID] = ' + CAST(@param_eventID AS VARCHAR) + ')'
					END
				ELSE
					BEGIN
						SET @local_where = @local_where + ' ([EVENT_ID] = ' + CAST(@param_eventID AS VARCHAR) + ')'
					END
				SET @local_hasWhere = 1
			END
		--currency
		IF (@param_currency IS NOT NULL)
			BEGIN 
				IF (@local_hasWhere = 1)
					BEGIN
						SET @local_where = @local_where + 'AND ([CURRENCY_ID] = ' + CAST(@param_currency AS VARCHAR) + ')'
					END
				ELSE
					BEGIN
						SET @local_where = @local_where + ' ([CURRENCY_ID] = ' + CAST(@param_currency AS VARCHAR) + ')'
					END
				SET @local_hasWhere = 1
			END
		--payment type
		IF (@param_paymentType IS NOT NULL)
			BEGIN 
				IF (@local_hasWhere = 1)
					BEGIN
						SET @local_where = @local_where + 'AND ([PAYMENT_TYPE_ID] = ' + CAST(@param_paymentType AS VARCHAR) + ')'
					END
				ELSE
					BEGIN
						SET @local_where = @local_where + ' ([PAYMENT_TYPE_ID] = ' + CAST(@param_paymentType AS VARCHAR) + ')'
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

		IF (@local_hasWhere = 1)
			BEGIN
				SET @local_query = @local_query + ' ' + @local_where
			END
		EXEC(@local_query)
	END --END CREATE OR ALTER PROCEDURE


--EXEC sp_Events '2012-01-01', '2022-10-10', NULL, 2, 3, 11, 1010
