# Python Coding Guide

f-string = syntax

Python 3.8 

```python
print(f"{foo=} {bar=}")
```

The "walrus operator", also known as the "assignment expression" operator.

Python 3.8

```python
if match := re.search(r"\d+", "The number is 12345"):
    print(f"Number: {match.group()}")

while (line := input("Enter a line (or 'q' to quit): ")) != 'q':
    print(line)
```