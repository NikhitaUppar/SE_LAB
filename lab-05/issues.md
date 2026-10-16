# Issues Document

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Mutable default arg | Bug | 9 | `playlist=[]` shared across function calls | Change default to `None` and initialize locally |
| SQL Injection | Security | 10 | Unsafe string formatting in SQL query | Use parameterized queries `(?, ?, ?)` |
| Bare `except` clause | Quality | 39 | Bare `except:` catches all errors blindly | Specify `sqlite3.Error` |
| Line too long | Style | 6, 10 | Line exceeds character limit | Wrap lines to adhere to PEP 8 |