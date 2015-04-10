First thing you need to know
-------------------------------------------
It is important to keep a good habbit.
For POSIX-standard operating systems,
do a chmod +x before_coding.py to make the file before_coding.py executable. 


About executable script
--------------------------------------------    
When execute mode is true, the shell must then check 
the first few bytes to see what kind of file it is. 
The first few bytes are termed the magic number; 

When an executable file’s content begins with ‘\#!’, it is a script file. 
The rest of the first line names the program that will interpret the script. 
In this case, we asked the env program to find the python interpreter. 
The shell finds the named program and runs it automatically, 
passing the name of script file as the last argument to the interpreter it found.

The very cool part of this trick is that ‘#!’ is a comment to Python. 
This first line is, in effect, directed at the shell, and ignored by Python. 
The shell glances at it to see what the language is, and Python studiously ignores it, 
since it was intended for the shell.
    
Content and formatting of documentation strings
---------------------------------------------------
The first line should always be a short, concise summary of the object’s purpose.
This line should begin with a capital letter and end with a period.

If there are more lines in the documentation string, the second line should be blank, 
visually separating the summary from the rest of the description. 
The following lines should be one or more paragraphs describing 
the object’s calling conventions, its side effects, etc.

    
Coding style
---------------------
Wrap lines so that they don’t exceed 79 characters.
CamelCase for classes and lower_case_with_underscores for functions and methods.
Plain ASCII works best in any case.

More precisely, the first or second line must match the regular
expression "coding[:=]\s*([-\w.]+)".
More about "Defining Python Source Code Encodings" is at:

http://legacy.python.org/dev/peps/pep-0263/


Interactive test
----------------------------    
You can `reload()` a module after modification.

    
About path
-----------------------------
sys.path is initialized from these locations:
* the directory containing the input script (or the current directory).
* PYTHONPATH (the same syntax as the shell variable PATH). 
* the installation-dependent default.

After initialization, Python programs can modify sys.path. 
The directory containing the script being run is placed at 
the beginning of the search path, ahead of the standard library path. 
This means that scripts in that directory will be loaded 
instead of modules of the same name in the library directory.

    
About doctest module
-------------------------------
The doctest module provides a tool for scanning a module and validating 
tests embedded in a program’s docstrings. Test construction is as simple as 
cutting-and-pasting a typical call along with its results into the docstring. 
This improves the documentation by providing the user with an example and it 
allows the doctest module to make sure the code remains true to the documentation.

Computes the arithmetic mean of a list of numbers
```python    
print average([20, 30, 70])
# 40.0

def average(values):
    """Computes the arithmetic mean of a list of numbers.
    
    >>> print average([20, 30, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)

if __name__ == "__main__":
    import doctest
    print doctest.testmod()
```
