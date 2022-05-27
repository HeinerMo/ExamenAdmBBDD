CREATE OR ALTER PROCEDURE sp_Address
@param_CustomerAccountId INT = NULL
AS
BEGIN
	BEGIN TRY
	--Address
		SELECT
			CCA.CUSTOMER_ACCOUNT_ID
			,CCA.CUSTOMER_NAME
			,CCA.CUSTOMER_LAST_NAME
			,CAD.DETAILS
			,CSP.STATE_NAME
			,CC.COUNTRY_NAME
		FROM CUSTOMERS.tb_CUSTOMER_ACCOUNTS AS CCA
		LEFT JOIN CUSTOMERS.tb_CUSTOMER_ADDRESSES AS CCAD
		ON CCA.CUSTOMER_ACCOUNT_ID=CCAD.CUSTOMER_ACCOUNT_ID
		LEFT JOIN CUSTOMERS.tb_ADDRESS AS CAD
		ON CCAD.ADDRESS_ID=CAD.ADDRESS_ID
		LEFT JOIN CUSTOMERS.tb_STATE_PROVINCE AS CSP
		ON CAD.STATE_PROVINCE_ID = CSP.STATE_PROVINCE_ID
		LEFT JOIN CUSTOMERS.tb_COUNTRY AS CC 
		ON CSP.COUNTRY_ID=CC.COUNTRY_ID
		WHERE CCA.CUSTOMER_ACCOUNT_ID=@param_CustomerAccountId	
	END TRY

	BEGIN CATCH
		PRINT 'N'+ @@ERROR	
	END CATCH
END

