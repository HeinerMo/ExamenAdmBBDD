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
				--Agregar usuarios
					SET @r = N'GRANT EXEC ON sp_AddUsers TO ' + QUOTENAME(@param_Name,'[]') 
					EXEC(@r)
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
					PRINT ('Permiso para leer asignado en la tabla: ' + @param_Table_Name)
				END TRY
				BEGIN CATCH
					PRINT ('ERROR: No se ha podido asignar el permiso')
				END CATCH
			END
	END