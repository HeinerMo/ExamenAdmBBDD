USE TRANSACTION_PROCESSING_EXAMEN
GO


CREATE OR ALTER PROCEDURE sp_AddPermissions
	@param_Name VARCHAR(50) = NULL 
	,@param_Table_Name VARCHAR(50) = NULL 
	,@param_Permission INT = NULL
AS
	BEGIN
		DECLARE @r nvarchar(4000)
		IF(@param_Permission = 1)
			BEGIN
				BEGIN TRY
					BEGIN TRANSACTION
						--Crear logins
						SET @r = 'GRANT EXEC ON [dbo].[sp_CreateLogin] TO ' + QUOTENAME(@param_Name,'[]') 
						EXEC(@r)
						PRINT('EXEC ON CREATE LOGIN')
						SET @r = 'GRANT INSERT ON [CLI_COMMON].[tb_USERS] TO ' + QUOTENAME(@param_Name,'[]') 
						EXEC(@r)
						--PRINT('GRANT INSERT')
						--SET @r = 'GRANT ALTER ANY USER TO ' + QUOTENAME(@param_Name,'[]') 
						--EXEC(@r)
						--PRINT('GRANT ALTER USER')
						--SET @r = 'GRANT ALTER ANY CREDENTIAL TO ' + QUOTENAME(@param_Name,'[]') 
						--EXEC(@r)
						--PRINT('GRANT ALTER CREDENTIAL')
						--SET @r = 'GRANT ALTER ANY LOGIN TO ' + QUOTENAME(@param_Name,'[]') 
						--EXEC(@r)
						--PRINT('GRANT ALTER LOGIN')
						
						--actualizar tabla usuarios
						UPDATE CLI_COMMON.tb_USERS
						SET [can_create_users] = 1
						WHERE user_name = @param_Name
					COMMIT
					PRINT ('Permiso para crear usuarios asignado')
				END TRY
				BEGIN CATCH
					PRINT ('ERROR: No se ha podido asignar el permiso para crear usuarios')
					ROLLBACK
				END CATCH
			END
		IF(@param_Permission = 2)
			BEGIN
			
				BEGIN TRANSACTION
					BEGIN TRY
						SET @r = 'GRANT SELECT ON ' + @param_Table_Name + ' TO ' + QUOTENAME(@param_Name,'[]')
						EXEC(@r)
						IF (@param_Table_Name LIKE '%tb_CUSTOMER_ACCOUNTS%')
							BEGIN
								SET @r = 'GRANT EXEC ON [dbo].[sp_Phones] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
								SET @r = 'GRANT EXEC ON [dbo].[sp_CreditCard] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
								SET @r = 'GRANT EXEC ON [dbo].[sp_Address] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
								SET @r = 'GRANT EXEC ON [dbo].[sp_CustomerAccounts] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
							END
						
						IF (@param_Table_Name LIKE '%tb_EVENTS%')
							BEGIN
								SET @r = 'GRANT EXEC ON [dbo].[sp_Events] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
								SET @r = 'GRANT SELECT ON [FINANCIAL_DEPOSIT].[tb_CURRENCY] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
								SET @r = 'GRANT SELECT ON [FINANCIAL_DEPOSIT].[tb_PAYMENT_TYPE] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
							END
						
						IF (@param_Table_Name LIKE '%tb_USERS%')
							BEGIN
								SET @r = 'GRANT EXEC ON [dbo].[sp_Users] TO ' + QUOTENAME(@param_Name,'[]')
								EXEC(@r)
							END
						--actualizar tabla usuarios
						UPDATE CLI_COMMON.tb_USERS
						SET [can_read] = 1
						WHERE user_name = @param_Name
						--Actualizar la tabla usuarios_tablas
						
						IF NOT EXISTS(SELECT TOP 1 1 FROM CLI_COMMON.tb_USERS_TABLES WHERE table_name = @param_Table_Name AND user_name = @param_Name)
							BEGIN
								INSERT INTO CLI_COMMON.tb_USERS_TABLES
									(user_name
									,table_name)
								VALUES
									(@param_Name, @param_Table_Name)
							END
						COMMIT
						PRINT ('Permiso para leer asignado en la tabla: ' + @param_Table_Name)
					END TRY
					BEGIN CATCH
						ROLLBACK
						PRINT ('ERROR: No se ha podido asignar el permiso')
					END CATCH
			END
	END

--SELECT * FROM CLI_COMMON.tb_USERS
--GO
--SELECT * FROM CLI_COMMON.tb_USERS_TABLES
--GO
--EXEC sp_AddPermissions 'heiner', '[CUSTOMERS].[tb_CUSTOMER_ACCOUNTS]', 1


