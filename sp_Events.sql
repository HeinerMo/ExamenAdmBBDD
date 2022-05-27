USE TRANSACTION_PROCESSING_EXAMEN
GO


CREATE OR ALTER PROCEDURE sp_Events
@param_beginDate DATETIME = NULL
,@param_endDate DATETIME = NULL
,@param_trasactionID INT = NULL
,@param_currency INT = NULL
,@param_paymentType INT = NULL
,@param_customerID INT = NULL
,@para_clientID INT = NULL
AS
	BEGIN
		DECLARE @local_query VARCHAR(MAX) = 'SELECT * FROM FINANCIAL_DEPOSIT.tb_EVENTS WHERE [SUBMITTED_DATE] >= ' 
		+ @param_beginDate 
		+ ' AND ' 
		+ '[SUBMITTED_DATE] <= ' + @param_endDate

		EXEC(@local_query)
	END --END CREATE OR ALTER PROCEDURE
	
	SELECT * FROM FINANCIAL_DEPOSIT.tb_CURRENCY


