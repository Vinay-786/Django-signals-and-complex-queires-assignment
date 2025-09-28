# Task: Advanced Query Filtering with Q Objects and Lookups

Objective: Implement a series of complex database queries using Q objects, pattern matching, and regex lookups based on the video demonstration.

Requirements:

Model Setup:

- Ensure you have a Restaurant model with fields:
  - name (CharField)
  - restaurant_type (CharField with choices)
  - date_opened (DateField)

- Ensure you have a Sale model with fields:

  - restaurant (ForeignKey to Restaurant)
  - income (DecimalField)
  - expenditure (DecimalField)

Q Object Queries:
a. Retrieve all restaurants where restaurant_type is Italian OR Mexican using Q objects.
b. Retrieve all restaurants NOT opened in the last 30 days using Q object negation.
c. Combine both conditions: OR restaurants of type Italian/Mexican OR opened in last 30 days.

Pattern Matching Lookups:
a. Retrieve all restaurants whose name contains the substring "grill" (case-insensitive).
b. Retrieve all restaurants whose name ends with "Cafe".

Regex Lookups:
a. Retrieve all restaurants whose name contains one or more digits using a regex lookup.
b. Retrieve all Sale records where income is greater than expenditure OR the associated restaurant's name contains any digit (combine Q objects and regex).

Encapsulation and Reuse:

- Encapsulate each Q condition into a variable (e.g., italian_mexican_q, recently_opened_q, name_has_digit_q, profitable_q).
- Compose these Q objects in a final queryset filter for the Sale model as shown in the video.

Performance Optimization:

- Use select_related('restaurant') when querying Sale to minimize database hits.

Deliverables:

- A Django management command or script (manage.py q_filter_demo) demonstrating all queries.
- Printed output of each queryset and the corresponding SQL using Django's connection.queries.
- Encapsulated Q object variables in a separate module or at the top of your script.
- A brief report (REPORT.md) explaining each query, the lookup used, and the SQL generated.
