USE TRANSACTION_PROCESSING_EXAMEN
GO


CREATE OR ALTER PROCEDURE sp_AddPermissions
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
						SET @r = N'GRANT EXEC ON sp_CreateLogin TO ' + QUOTENAME(@param_Name,'[]') 
						EXEC(@r)
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
		IF(@param_Permission LIKE 2)
			BEGIN
				BEGIN TRY
					SET @r = N'GRANT SELECT ON ' + @param_Table_Name + ' TO ' + QUOTENAME(@param_Name,'[]') 
					EXEC(@r)
						--actualizar tabla usuarios
						UPDATE CLI_COMMON.tb_USERS
						SET [can_read] = 1
						WHERE user_name = @param_Name						--Actualizar la tabla usuarios_tablas
						
						IF NOT EXISTS(SELECT TOP 1 1 FROM CLI_COMMON.tb_USERS_TABLES WHERE table_name = @param_Table_Name AND user_name = @param_Name)
							BEGIN
								INSERT INTO CLI_COMMON.tb_USERS_TABLES
									(user_name
									,table_name)
								VALUES
									(@param_Name, @param_Table_Name)
							END
					PRINT ('Permiso para leer asignado en la tabla: ' + @param_Table_Name)
				END TRY
				BEGIN CATCH
					PRINT ('ERROR: No se ha podido asignar el permiso')
				END CATCH
			END
	END


--SELECT * FROM CLI_COMMON.tb_USERS
--GO
--SELECT * FROM CLI_COMMON.tb_USERS_TABLES
--GO
--EXEC sp_AddPermissions 'Heiner', '[CUSTOMERS].[tb_CUSTOMER_ACCOUNTS]', 2