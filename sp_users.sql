
CREATE OR ALTER PROCEDURE sp_Users
@param_name VARCHAR(50) = NULL
,@param_canRead BIT = NULL
,@param_canAddUsers BIT = NULL
,@param_isActive BIT = NULL
AS
	BEGIN
		DECLARE @local_query VARCHAR(MAX) = 'SELECT * FROM [CLI_COMMON].[tb_USERS]' 
		DECLARE @local_where VARCHAR(MAX) = ' WHERE'
		DECLARE @local_hasWhere BIT = 0

		--name
		IF (@param_name IS NOT NULL)
			BEGIN
				SET @local_where = @local_where + ' ([user_name] = ''' + CAST(@param_name AS VARCHAR) + ''')'
				SET @local_hasWhere = 1
			END
		--read
			IF (@param_canRead IS NOT NULL)
				BEGIN
					IF (@local_hasWhere = 1)
						BEGIN
							SET @local_where = @local_where + ' AND ([can_read] = ''' + CAST(@param_canRead AS VARCHAR) + ''')'
						END
					ELSE
						BEGIN
							SET @local_where = @local_where + ' ([can_read] = ''' + CAST(@param_canRead AS VARCHAR) + ''')'
							SET @local_hasWhere = 1
						END
				END
		--users
			IF (@param_canAddUsers IS NOT NULL)
				BEGIN
					IF (@local_hasWhere = 1)
						BEGIN
							SET @local_where = @local_where + ' AND ([can_create_users] = ''' + CAST(@param_canAddUsers AS VARCHAR) + ''')'
						END
					ELSE
						BEGIN
							SET @local_where = @local_where + ' ([can_create_users] = ''' + CAST(@param_canAddUsers AS VARCHAR) + ''')'
							SET @local_hasWhere = 1
						END
				END
		--isActive
			IF (@param_isActive IS NOT NULL)
				BEGIN
					IF (@local_hasWhere = 1)
						BEGIN
							SET @local_where = @local_where + ' AND ([is_active] = ''' + CAST(@param_isActive AS VARCHAR) + ''')'
						END
					ELSE
						BEGIN
							SET @local_where = @local_where + ' ([is_active] = ''' + CAST(@param_isActive AS VARCHAR) + ''')'
							SET @local_hasWhere = 1
						END
				END
			IF (@local_hasWhere = 1)
				BEGIN
					SET @local_query = @local_query + ' ' + @local_where
				END
			EXEC(@local_query)
	END


--EXEC sp_Users 'Heiner', 0, 0, 1