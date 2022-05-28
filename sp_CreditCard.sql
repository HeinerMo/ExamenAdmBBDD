CREATE OR ALTER PROCEDURE sp_CreditCard
@param_CustomerAccountId INT = NULL
AS
BEGIN
	BEGIN TRY
	--Credit Card
		SELECT
			CCA.CUSTOMER_ACCOUNT_ID
			,CCA.CUSTOMER_NAME
			,CCA.CUSTOMER_LAST_NAME
			,CCC.CREDIT_CARD_NUMBER_ENCRYPTED
		FROM CUSTOMERS.tb_CUSTOMER_ACCOUNTS AS CCA
			LEFT JOIN CUSTOMERS.tb_CUSTOMER_CREDIT_CARDS AS CCCC
				ON CCA.CUSTOMER_ACCOUNT_ID=CCCC.CUSTOMER_ACCOUNT_ID
					LEFT JOIN CUSTOMERS.tb_CREDIT_CARD AS CCC
						ON CCCC.CREDIT_CARD_ID=CCC.CREDIT_CARD_ID
		WHERE CCA.CUSTOMER_ACCOUNT_ID=@param_CustomerAccountId	
	END TRY

	BEGIN CATCH
		PRINT 'N'+ @@ERROR	
	END CATCH
END


--EXEC sp_CreditCard 10
