# Queries Generated after Creating a User & Post And Deleting it

{'sql': 'INSERT INTO "auth_user" ("password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined") VALUES (\'hello@123!\', NULL, 0, \'vinay989\', \'\\\'\', \'\\\'\', \'\\\'\', 0, 1, \'2025-09-28 19:32:36.54365\') RETURNING "auth_user"."id"', 'time': '0.002'},
{'sql': 'INSERT INTO "notifications_post" ("title", "slug", "notify_users", "notify_users_timestamp", "active") VALUES (\'New Post\', \'new-post\', 0, NULL, 1) RETURNING "notifications_post"."id"', 'time': '0.001'},
{'sql': 'BEGIN', 'time': '0.000'},
{'sql': 'INSERT INTO "notifications_deletepost" ("title", "slug", "notify_users", "notify_users_timestamp", "active") VALUES (\'New Post\', \'new-post\', 0, NULL, 0) RETURNING "notifications_deletepost"."id"', 'time': '0.001'},
{'sql': 'DELETE FROM "notifications_post_tags" WHERE "notifications_post_tags"."post_id" IN (6)', 'time': '0.000'},
{'sql': 'DELETE FROM "notifications_post" WHERE "notifications_post"."id" IN (6)', 'time': '0.000'},
{'sql': 'COMMIT', 'time': '0.006'},
{'sql': 'SELECT "notifications_deletepost"."id", "notifications_deletepost"."title", "notifications_deletepost"."slug", "notifications_deletepost"."notify_users", "notifications_deletepost"."notify_users_timestamp", "notifications_deletepost"."active" FROM "notifications_deletepost" LIMIT 21', 'time': '0.000'},
{'sql': 'SELECT "notifications_deletepost"."id", "notifications_deletepost"."title", "notifications_deletepost"."slug", "notifications_deletepost"."notify_users", "notifications_deletepost"."notify_users_timestamp", "notifications_deletepost"."active" FROM "notifications_deletepost" LIMIT 1 OFFSET 1', 'time': '0.000'},
{'sql': 'SELECT "notifications_deletepost"."id", "notifications_deletepost"."title", "notifications_deletepost"."slug", "notifications_deletepost"."notify_users", "notifications_deletepost"."notify_users_timestamp", "notifications_deletepost"."active" FROM "notifications_deletepost" LIMIT 1 OFFSET 1', 'time': '0.000'}

- You can see the give here:
![Queries GIF](./demo.gif)

# ORM Script SQL Outputs

### a. Italian or Mexican Restaurants
- **Description**: Selects restaurants where type is 'IT' (Italian) or 'MX' (Mexican).
- **SQL**:
  ```sql
  SELECT "complex_queries_restaurant"."id", "complex_queries_restaurant"."name", "complex_queries_restaurant"."restaurant_type", "complex_queries_restaurant"."date_opened" 
  FROM "complex_queries_restaurant" 
  WHERE ("complex_queries_restaurant"."restaurant_type" = IT OR "complex_queries_restaurant"."restaurant_type" = MX)
  ```

### b. Not Recently Opened Restaurants
- **Description**: Selects restaurants opened before August 29, 2025 (not recent).
- **SQL**:
  ```sql
  SELECT "complex_queries_restaurant"."id", "complex_queries_restaurant"."name", "complex_queries_restaurant"."restaurant_type", "complex_queries_restaurant"."date_opened" 
  FROM "complex_queries_restaurant" 
  WHERE NOT ("complex_queries_restaurant"."date_opened" >= 2025-08-29)
  ```

### c. Italian/Mexican or Recently Opened
- **Description**: Selects Italian/Mexican restaurants or those opened on/after August 29, 2025.
- **SQL**:
  ```sql
  SELECT "complex_queries_restaurant"."id", "complex_queries_restaurant"."name", "complex_queries_restaurant"."restaurant_type", "complex_queries_restaurant"."date_opened" 
  FROM "complex_queries_restaurant" 
  WHERE ("complex_queries_restaurant"."restaurant_type" = IT OR "complex_queries_restaurant"."restaurant_type" = MX OR "complex_queries_restaurant"."date_opened" >= 2025-08-29)
  ```

### d. Name Contains 'grill'
- **Description**: Selects restaurants with 'grill' in the name (case-sensitive).
- **SQL**:
  ```sql
  SELECT "complex_queries_restaurant"."id", "complex_queries_restaurant"."name", "complex_queries_restaurant"."restaurant_type", "complex_queries_restaurant"."date_opened" 
  FROM "complex_queries_restaurant" 
  WHERE "complex_queries_restaurant"."name" LIKE %grill% ESCAPE '\'
  ```

### e. Name Ends with 'Cafe'
- **Description**: Selects restaurants whose name ends with 'Cafe'.
- **SQL**:
  ```sql
  SELECT "complex_queries_restaurant"."id", "complex_queries_restaurant"."name", "complex_queries_restaurant"."restaurant_type", "complex_queries_restaurant"."date_opened" 
  FROM "complex_queries_restaurant" 
  WHERE "complex_queries_restaurant"."name" LIKE %Cafe ESCAPE '\'
  ```

### f. Name Contains Digits
- **Description**: Selects restaurants with digits in the name (using REGEXP).
- **SQL**:
  ```sql
  SELECT "complex_queries_restaurant"."id", "complex_queries_restaurant"."name", "complex_queries_restaurant"."restaurant_type", "complex_queries_restaurant"."date_opened" 
  FROM "complex_queries_restaurant" 
  WHERE "complex_queries_restaurant"."name" REGEXP \d+
  ```

### g. Profitable Sales or Digit in Restaurant Name
- **Description**: Joins `Sale` and `Restaurant` models; selects where sales are profitable (income > expenditure) or restaurant name has digits.
- **SQL**:
  ```sql
  SELECT "complex_queries_sale"."id", "complex_queries_sale"."restaurant_id", "complex_queries_sale"."income", "complex_queries_sale"."expenditure", "complex_queries_restaurant"."id", "complex_queries_restaurant"."name", "complex_queries_restaurant"."restaurant_type", "complex_queries_restaurant"."date_opened" 
  FROM "complex_queries_sale" 
  INNER JOIN "complex_queries_restaurant" ON ("complex_queries_sale"."restaurant_id" = "complex_queries_restaurant"."id") 
  WHERE ("complex_queries_sale"."income" > ("complex_queries_sale"."expenditure") OR "complex_queries_restaurant"."name" REGEXP \d+)
  ```


_Note: orm script is in script folder and the queries generated from it too_
