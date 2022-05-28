CREATE OR ALTER PROCEDURE sp_Phones
@param_CustomerAccountId INT = NULL
AS
BEGIN
	BEGIN TRY
	--PHONE
		SELECT
			CCA.CUSTOMER_ACCOUNT_ID
			,CCA.CUSTOMER_NAME
			,CCA.CUSTOMER_LAST_NAME
			,CP.PHONE_NUMBER
		FROM CUSTOMERS.tb_CUSTOMER_ACCOUNTS AS CCA
		LEFT JOIN CUSTOMERS.tb_CUSTOMER_PHONES AS CCP
		ON CCA.CUSTOMER_ACCOUNT_ID=CCP.CUSTOMER_ACCOUNT_ID
		LEFT JOIN CUSTOMERS.tb_PHONE AS CP
		ON CCP.PHONE_ID=CP.PHONE_ID
		WHERE CCA.CUSTOMER_ACCOUNT_ID=@param_CustomerAccountId	
	END TRY

	BEGIN CATCH
		PRINT 'N'+ @@ERROR	
	END CATCH
END