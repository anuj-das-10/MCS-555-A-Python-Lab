# MCS-555-(A): Python LAB

1. Write a python function to find all the factors of a given number `n`.
- [See Solution](solutions/Q-01.py)✅

2. Write a python function for Euclid's GCD Algorithm.
- [See Solution](solutions/Q-02.py)✅

3. Write a python function to find x<sup>n</sup>.
- [See Solution](solutions/Q-03.py)✅

4. Write a python function to check if the given number is prime or not.
- [See Solution](solutions/Q-04.py)✅

5. Write a python function to find prime numbers upto 'n'.
- [See Solution](solutions/Q-05.py)✅

6. Write a python function to find first 'n' prime numbers.
- [See Solution](solutions/Q-06.py)✅

7. Write a python function to pass function as a parameter.
- [See Solution](solutions/Q-07.py)✅

<br />

### Recursion/Inductive Definition

8. Write a python function to compute the length of a list using inductive definition (means recursion).
- [See Solution](solutions/Q-08.py)✅

9. Write a python function to find Fibonacci Series using recursion.
- [See Solution](solutions/Q-09.py)✅

10. Write a python function to check if the given string is Palindrome or not using recursion. 
- [See Solution](solutions/Q-10.py)✅

<br />

### File Handling

11. Write a python program to check if file exists or not in the directory.
- [See Solution](concepts/file-handling/program-03.py)✅

12. Write a python program to demonstrate different file opening modes.
- [See Solution](concepts/file-handling/01_File_Opening_Modes.py)✅

13. Write a python program to read contents from an external file.
- [See Solution](concepts/file-handling/02_Read_Operation.py)✅

14. Write a python program to read contents line by line from an external file.
- [See Solution](concepts/file-handling/program-01.py)✅

15. Write a python program to write contents to an external file.
- [See Solution](concepts/file-handling/04_Write_Operation.py)✅

16. Write a python program to write list of strings line by line to an external file.
- [See Solution](concepts/file-handling/05_Write_Methods.py)✅

17.  Write a python program to take input from a file and write the retrieved contents to another file.
- [See Solution](concepts/file-handling/program-02.py)✅


<br />

### Exception Handling

18. Write a python program to demonstrate the concept of exception handling.
- [See Solution](concepts/exception-handling/ZeroDivisionError.py)✅

19. Write a python program to demonstrate IndexError.
- [See Solution](concepts/exception-handling/IndexError.py)✅

20. Write a python program to demonstrate NameError.
- [See Solution](concepts/exception-handling/NameError.py)✅

21. Write a python program to demonstrate ValueError.
- [See Solution](concepts/exception-handling/ValueError.py)✅

22. Write a python program to demonstrate FileExistsError.
- [See Solution](concepts/exception-handling/FileExistsError.py)✅




<br />

### Python Modules

23. Write a python program to demonstrate the use of built-in module.
- [See Solution](concepts/modules/built_in_module.py)✅
  
24. Write a python program to demonstrate the use of user-defined module that performs basic geometric calculation.
- [See Solution](concepts/modules/main.py)✅

```python
# Module Code
import math

def euclidean_distance(point1: tuple , point2: tuple):
    x1, y1 = point1
    x2, y2 = point2
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def area(shape, *param):
    if(shape.lower() == 'circle'):
        radius = param[0]
        return math.pi * radius**2
       
    if(shape.lower() == 'rectangle'):
        length = param[0]
        width = param[1]
        return length * width
    
    if(shape.lower() == 'square'):
        side = param[0]
        return side * side   
```


<br />

### Object Oriented Programming (OOPs)

25. Write a python program to demonstrate the concept of Inheritance.
- [See Solution](concepts/oops/Inheritance.py)✅

26. Write a python program to demonstrate the use of magic methods(dunder methods) for operator overloading.
- [See Solution](concepts/oops/Vector.py)✅ 

<br />

### Scopes in Python

27. Write a python program to demonstrate the concept of different scopes in python.
- [Local Scope](concepts/scopes/local_scope.py)✅ 
- [Global Scope](concepts/scopes/global_scope.py)✅ 
- [Non-Local Scope](concepts/scopes/nonlocal_scope.py)✅ 


<br />

## Internal Questions

1. Write a python program using map function to cumpute the sum of all the elements in a 2D-Array.

- [See Solution](internals/solution-01.py)✅

2. Write a python program to compute the sum of all elements in a 2D-Array using List Comprehension.

- [See Solution](internals/solution-02.py)✅


<br />

## Examples Done in Class

1. Write a python program by creating a class `Inset` which has an attribute list of integers incorporate methods in the class to initialize `Inset`, insert, remove from the attribute list also use a method to get all the members of the attribute list and write a `__str__` method to give a string representation of the attribute list.

- [See Solution](examples-by-sir/example01.py)✅



1. Write a python program to demonstrate the concept of getter, setter and `None` keyword inside class.

- [See Solution](examples-by-sir/example02.py)✅


