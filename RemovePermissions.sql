USE TRANSACTION_PROCESSING_EXAMEN
GO


CREATE OR ALTER PROCEDURE sp_RemovePermissions
	@param_Name VARCHAR(50) = NULL 
	,@param_Table_Name VARCHAR(50) = NULL 
	,@param_Permission INT = NULL
AS
	BEGIN
		DECLARE @r nvarchar(4000)
		IF(@param_Permission LIKE 1)
			BEGIN
				BEGIN TRY
					BEGIN TRANSACTION
				--Crear logins
					SET @r = N'REVOKE EXEC ON [dbo].[sp_CreateLogin] TO ' + QUOTENAME(@param_Name,'[]') 
					EXEC(@r)
					SET @r = N'REVOKE EXEC ON [dbo].[sp_CreateLogin] TO ' + QUOTENAME(@param_Name,'[]') 
					EXEC(@r)						--actualizar tabla usuarios
						UPDATE CLI_COMMON.tb_USERS
						SET [can_create_users] = 0
						WHERE user_name = @param_Name
					COMMIT
					PRINT ('Permiso para crear usuarios revocado')
				END TRY
				BEGIN CATCH
					PRINT ('ERROR: No se ha podido eliminar el permiso para crear usuarios')
					ROLLBACK
				END CATCH
			END
		IF(@param_Permission LIKE 2)
			BEGIN
				BEGIN TRY
					IF (@param_Table_Name LIKE '%tb_CUSTOMER_ACCOUNTS%')
							BEGIN
								SET @r = 'REVOKE EXEC ON [dbo].[sp_Phones] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
								SET @r = 'REVOKE EXEC ON [dbo].[sp_CreditCard] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
								SET @r = 'REVOKE EXEC ON [dbo].[sp_Address] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
								SET @r = 'REVOKE EXEC ON [dbo].[sp_CustomerAccounts] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
							END
						
						IF (@param_Table_Name LIKE '%tb_EVENTS%')
							BEGIN
								SET @r = 'REVOKE EXEC ON [dbo].[sp_Events] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
								SET @r = 'REVOKE SELECT ON [FINANCIAL_DEPOSIT].[tb_CURRENCY] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
								SET @r = 'REVOKE SELECT ON [FINANCIAL_DEPOSIT].[tb_PAYMENT_TYPE] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
							END
						
						IF (@param_Table_Name LIKE '%tb_USERS%')
							BEGIN
								SET @r = 'REVOKE EXEC ON [dbo].[sp_Users] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
							END					
					--actualizar tabla usuarios
					UPDATE CLI_COMMON.tb_USERS
					SET [can_read] = 0
					WHERE user_name = @param_Name

					IF EXISTS(SELECT TOP 1 1 FROM CLI_COMMON.tb_USERS_TABLES WHERE table_name = @param_Table_Name AND user_name = @param_Name)
						BEGIN
							DELETE CLI_COMMON.tb_USERS_TABLES
							WHERE user_name = @param_Name AND table_name = @param_Table_Name
						END

					PRINT ('Permiso para leer revocado en la tabla: ' + @param_Table_Name)
				END TRY
				BEGIN CATCH
					PRINT ('ERROR: No se ha podido eliminar el permiso')
				END CATCH
			END
	END

--EXEC sp_RemovePermissions 'prueba', '[CUSTOMERS].[tb_CUSTOMER_ACCOUNTS]', 2
