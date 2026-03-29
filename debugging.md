---
layout: page
title: Debugging
description: Pointers on how to solve common technical issues.
nav_order: 5
---

# Debugging 🐞
{:.no_toc .fs-7 .fw-400 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Run Tests

Before debugging, you need to run doctests in your local terminal. There are two ways to do:

1. Run all doctests.
2. Open an interactive mode and run a particular test.

For the first option, you can do either

```
python3 -m doctest <filename>.py
```
or
```
python3 -m doctest <filename>.py -v
```
If you passed all of the doctests with the first command, nothing will be shown in your terminal. In contrast, the second command will shown the tests you have passed, but the output is a bit long so we don't recommend it. However, if you would prefer seeing a summary of the tests you have passed, feel free to use the second command!

For the second option, you can do
```
python3 -i <filename>.py
```
This will open an interactive mode and you will be able to test the functions you have in that file!

I bet most people in this world will always be able to pass all of the doctests in their first try. Therefore, error messages will be shown on the terminal and please take a look at the later sections on how to inteprete the message and how to debug!


## Debugging Techniques

### What to debug?
In DSC 20, we will always give you some explicit doctests in homeworks and labs. However, different from DSC 10, you are **not guaranteed to get full credit** after passing these explicit doctests. Yes, we have hidden tests! The reason for hidden tests is that we want you to think more when coding, including edge cases. We highly recommend you to write more doctests testing on edge cases, for example, empty space, zero, and random cases.

### How to debug?
I bet you must have asked such question when coding, "Why my code is not returning my expected output?"

Don't worry, and don't panic! This happens often and happens to everyone, including everyone in the DSC 20 TEAM! Remember Python is different to humans brain🧠, it follows strict instructions. Try to calm down and TRACE your code line by line. Here is a useful "tutor" to help you trace your code, [python tutor](https://pythontutor.com), and we will further discuss this friend in class! Another helpful trick would be insert `print()` in your function to check if the code passes through the correct place and gets expected variable. When your function is called and passes these print statements, Python will show what happened inside the function.

## Questions you might ask...

### Why does my answer seems to have the same output, but not passing the doctest?

This can happen by several possible situations. 
1. Check if you're having an empty space in either end of your doctest or output. 
2. This could happen when your notations are not typed by English keyboard. 
3. Make sure you used `return` instead of `print()`.

### Why do I `got nothing` in the terminal?

Check if you **saved your file** before you run it (there is no dot next to the title in your text editor). Also, make sure you are running the exact file that you edited (You could check the filepath by right clicking the file => "Get Info", make sure your terminal is at the same filepath).

## Specific Errors

When debugging, we usually trace the error message from bottom to top. The last line in error message often presents most error information. 🔍

### SyntaxError

This error is telling you that the code contains invalid syntax. Note that Python will check syntax before executing code.
Example:
``` python
def foo(i)
    print("hello")
    return "Hello World"
```
Your terminal will look like this:
``` bash
  File "/Users/apple/Desktop/trial.py", line 1 
    def foo(i)
              ^
SyntaxError: invalid syntax
```
>Solution: Usually `^` refers to the place where contains syntax error. Check that line and around that line! In the example, the code is missing a colon. Some common mistakes are: indentation is not consistent; missing colon after `for`, `while`, `if`, `def`; unclosed bracket; `=` instead of `==` when checking conditions, and so on...

### IndentationError

This error is telling you that the indentation is not consistent.
Example:
``` python
def foo(i):
   print("hello")
    return "Hello World"
```
Your terminal will look like this:

``` bash
  File "/Users/apple/Desktop/trial.py", line 3
    return "Hello World"
IndentationError: unexpected indent
```
>Solution: Just delete the indentation and reinsert consistent indentation. Note that in this course, we highly recommend using 4 spaces instead of a tab for indentation!

### TypeError

This usually occurs when the operation is executed with an inappropriate/unsupported object type.

Example:
``` python
>>> 1+"hello world"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

>>> 1>"a"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'int' and 'str'

>>> 1('a')
<stdin>:1: SyntaxWarning: 'int' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable

>>> ["a", "b"]["1"]
<stdin>:1: SyntaxWarning: list indices must be integers or slices, not str; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not str
```
>Solution: make sure you are using valid input!

### NameError
This usually happens when you are trying to use the variable which has not been defined.
Example:
``` python
>>> dsc20 = 1
>>> dsc30
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dsc30' is not defined
```
>Solution: Make sure to define the variable before using it. (Maybe you are having a typo in calling variable)

### IndexError
This might happen when you are retrieving invalid index (out of range).
Example:
``` python
>>> lst = [1,2,3]
>>> lst[20]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
>Solution: Make sure the valid index range is -len(lst) <= idx<= len(lst) - 1.

### ... object is not callable

This often happens when you use a default keyword (like `str` or `list`) as a variable name, for instance `list = [1, 2, 3]`. These errors can be tricky because they don't error on their own, but cause problems when we try to use (for example) the name `list` later on in your code (e.g. to convert something to a list).
Example:
``` python
>>> list("Hello")
['H', 'e', 'l', 'l', 'o']
>>> list = [1,2,3]
>>> list("Hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
```

>Solution: To fix the issue, identify any such lines of code, change your variable names to be something else, and re-run your script.

### Other errors

Error messages are complex in Python, especially when you have multiple classes and each methods are interrelated. [Here is a useful guide](https://swcarpentry.github.io/python-novice-inflammation/07-errors/index.html). You can also ask in [office hours](https://dsc20.org/staffhours/), or on [Piazza](https://piazza.com/class/l12oxbjkn9i7ah), but remember never post your code in public! Understanding cryptic error messages is a skill that comes with experience ;)

## Gradescope Common Errors

Sometimes Gradescope will failed to execute. There are two different cases on what you will see.

1. The output shows that:
```
The autograder failed to execute correctly. Please ensure that your submission is valid. Contact your course staff for help in debugging this issue. Make sure to include a link to this page so that they can help you most effectively.
```
or
```
Your submission timed out. It took longer than 600 seconds to run.
```
> Solution: These types of output usually suggest that there is an infinite loop going on in your code. The easiest fix is that comment out all problems, leave one problem uncommented, and resubmit. Keeps doing the above steps will help you locate which problem is giving you the issue. Then you can try to think about some edge cases that will cause the infinite loops and debug! Another potential reason is that your code involves syntax errors such as extra whitespace in docstring or doctests. You could run the code using `python3 -m doctest <filename>.py` locally to detect that error as well.

2. The output shows that No module named <>

One example:
``` bash
Test Failed: Failed to import test module: testBjack
Traceback (most recent call last):
  File "/autograder/source/run_tests.py", line 13, in <module>
    import blackjack as bj
  File "/autograder/source/blackjack.py", line 2, in <module>
    from turtle import st
  File "/usr/lib/python3.9/turtle.py", line 107, in <module>
    import tkinter as TK
ModuleNotFoundError: No module named 'tkinter'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3.9/unittest/loader.py", line 436, in _find_test_path
    module = self._get_module_from_name(name)
  File "/usr/lib/python3.9/unittest/loader.py", line 377, in _get_module_from_name
    __import__(name)
  File "/autograder/source/tests/testBjack.py", line 10, in <module>
    from blackjack import Blackjack
  File "/autograder/source/blackjack.py", line 2, in <module>
    from turtle import st
  File "/usr/lib/python3.9/turtle.py", line 107, in <module>
    import tkinter as TK
ModuleNotFoundError: No module named 'tkinter'
```
This is usually because you have used IDE such as VS Code or PyCharm. They automatically imported something when you are unawared. Gradescope did not have these modules downloaded so that causes the error and resulted in a zero on this assignment if you don't fix it.

> Solution: Just delete the import statements in your code!

