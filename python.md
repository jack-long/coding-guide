# Python Coding Guide

## f-string = syntax

Python 3.8 

```python
print(f"{foo=} {bar=}")
```

## The "walrus" / "assignment expression" operator

Python 3.8

```python
if match := re.search(r"\d+", "The number is 12345"):
    print(f"Number: {match.group()}")

while (line := input("Enter a line (or 'q' to quit): ")) != 'q':
    print(line)
```

## Force keyword arguments

```python
def login(*, username: str, pw: str):
    ...
```
The asterisk (*) is used to indicate that the parameters that 
follow must be passed using keyword arguments rather than positional arguments.

