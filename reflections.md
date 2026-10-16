# Reflection: Static Code Analysis

1. **What is the purpose and scope of static code analysis?**
   Static code analysis examines source code without executing it to detect potential bugs, security vulnerabilities, and style violations early in the development cycle.

2. **How did Pylint, Bandit, and Flake8 help improve your code?**
   - **Pylint** flagged code quality issues, missing docstrings, dangerous default arguments, and naming convention violations, helping raise code maintainability.
   - **Bandit** detected high and medium-risk security vulnerabilities, specifically highlighting unparameterized SQL queries (SQL injection risks).
   - **Flake8** enforced PEP 8 style guidelines, ensuring correct spacing, line lengths, and formatting.

3. **What were the most critical issues found, and how did you fix them?**
   The most critical issues were the SQL injection vulnerability (fixed by switching to parameterized queries `(?, ?, ?)`) and the mutable default argument (fixed by defaulting `playlist=None` and initializing locally).

4. **How does static code analysis contribute to overall software quality?**
   It automates code reviews, enforces consistency across developer teams, prevents common runtime bugs, and stops security flaws from reaching production.