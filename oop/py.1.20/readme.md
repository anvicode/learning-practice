# Linting

py.1.20

1. Consider iterating with .items() PylintC0206:consider-using-dict-items

py.1.18/main.py

```python
# from
for key in my_dict:
  print(f"Key: {key}, Value: {my_dict[key]}")

# to
for key, value in my_dict.items():
  print(f"Key: {key}, Value: {value}")
```

2. Unused variable 'i'PylintW0612:unused-variable

py.1.18/main.py

```python
# from
for i in range(100):

# to
for _ in range(100):
```

3. Redefining name 'key' from outer scope (line 34)PylintW0621:redefined-outer-name and Redefining name 'value' from outer scope (line 34)PylintW0621:redefined-outer-name

py.1.18/main.py

```python
# from
key = random.randint(1, 100)

# to
k = random.randint(1, 100)
```

```python
# from
value = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=5))

# to
val = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=5))
```

4. Missing function or method docstringPylintC0116:missing-function-docstring

py.1.18/main.py

```python
# add docstring
"""Generates a dictionary with 100 random key-value pairs."""
```

5. Missing module docstringPylintC0114:missing-module-docstring

py.1.18/main.py

```python
# add docstring
""" Module with create_dict_with_random_pairs function """
```

6. py.1.18/main_the_second.py

- Missing module docstringPylintC0114:missing-module-docstring
- Missing function or method docstringPylintC0116:missing-function-docstring
- Redefining name 'values' from outer scope (line 5)PylintW0621:redefined-outer-name
- Argument name "n" doesn't conform to snake_case naming stylePylintC0103:invalid-name
