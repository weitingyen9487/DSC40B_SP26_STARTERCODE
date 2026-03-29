---
layout: page
title: Style Guide
description: Pointers on how to solve common technical issues.
nav_order: 7
---

# Style Guide 👀
{:.no_toc .fs-7 .fw-400 }

## Style Requirements

You will be graded for the style of programming on this assignment. A few key requirements for style are given below:

This is complete Python style guide: [Python Style Guide](https://peps.python.org/pep-0008/). 

**We will grade style on a smaller set of rules below:**
- **Illegal Import Statements**: You should not import any package unless instructed to;
- **Module Docstring**: Every file that you submit should have a module docstring at the very top. In our assignments, it means to fill in name and PID;
- **Method Docstring**: Every method you create should have a docstring (i.e. method description)
    - Each docstring is surrounded by triple quotes (`"""`) instead of triple single quotes (`'''`)
    - This includes any inner function and helper function;
    - You don't need docstrings for lambda functions;
    - You may replace the entire # box with your method description;
    - The description should briefly describe what the method does, instead of what steps you take to achieve the result. Example:
        - Correct: Takes in a list of numbers, doubles each of them, and returns the doubled list;
        - Incorrect: Initializes an empty list and loops through the input list. For each number, I double it and append to the resulting list.
    - It's recommended to include input argument type and information like the examples given in lab01, but not required.
- **Line Limit**: All lines should be limited to a maximum of 79 characters.
    - Setup rulers in your editor
        - Sublime Text ([references](https://stackoverflow.com/questions/9910143/how-to-make-ruler-always-be-shown-in-sublime-text-2)): Go to *Preferences* > *Settings - User*, and add a new line in `{}`:
            ```js
            "rulers": [80]
            ```
        - You may also google "&lt;editor name&gt; set ruler" for your editor of choice
    - You may use backslash (`\`) to break up lines that might overflow:
        ```py
        with open('/path/to/some/file/you/want/to/read') as file_1, \
             open('/path/to/some/file/being/written', 'w') as file_2:
            file_2.write(file_1.read())
        ```
    - You should follow the same rule in the docstring part. For expected doctest results, remove the leading whitespaces:
        ```py
        def foo():
            """
            # Correct
            >>> foo()
            [[1, 2, 3], [1, 2, 3], \
        [1, 2, 3]]

            # Incorrect
            >>> foo()
            [[1, 2, 3], [1, 2, 3], \
            [1, 2, 3]]
            """
            result = []
            for _ in range(3):
                result.append([1, 2, 3])
            return result
        ```
- **Magic Numbers**: Avoid using magic numbers (i.e. any number except 0, 1, -1) directly 
    - If you need to use, say, 17 in your code, create a variable with a meaningful name and use the variable instead
    - The reason behind is that numbers have meanings. 17 might mean distance in some context and age in another context. You should define meaningful variable names to differentiate between the meanings.
    - Do not use a variable name like `"SEVENTEEN"` because it does not define the meaning clearly, so it will be considered as meaningless variable name (see the next rule)
    - ***Exceptions***: We will not deduct points if magic numbers appear in your code in the following scenarios
        1. Checking for mod `n`, where `n` can be any number. You don't have to make a variable for the number `n`.<br>
            ```py 
            number_to_check % 2 == 0  # Example for mod 2
            number_to_check % 3 == 0  # Example for mod 3
            ```
        2. The distance formula (2D & 3D examples are given, but the distance formula is ok for any dimension N).
            ```py
            a ** 2 = b ** 2 + c ** 2              # 2D distance formula
            d ** 2 = x1 ** 2 + x2 ** 2 + x3 ** 2  # 3D distance formula
            ```
        3. Root formulas such as square root, cube root, etc.
            ```py
            square_root = a_number ** (1/2) 
            cube_root   = a_number ** (1/3)
            ```
- **Meaningless Variable Names**: All variable and function names should be descriptive
    - Function names typically evoke operations applied to arguments by the interpreter (e.g., `print`, `add`, `square`) or the name of the quantity that results (e.g., `max`, `abs`, `sum`);
    - Parameter names should evoke the role of the parameter in the function, not just the kind of argument that is allowed. For example, if the variable stores a list of student names, then it could be called `student_names` instead of `lst`;
    - Single letter parameter names are acceptable when their role is obvious, but avoid "l" (lowercase ell), "O" (capital oh), or "I" (capital i) to avoid confusion with numerals;
    - Try to only use `i`, `j`, `k` as index names and avoid them for other uses;
    - Avoid using built-in function names as variable names anywhere, as they break the built-in functions. For example, you should not use `sum`, `dict`, `map`, etc. as variable names.
- **Bad Variable Style**: You should always use `snake_case` when coding in Python
    - Variable and function names are lowercase, with words separated by underscores, e.g. `unusual_sum()`
    - Single-word names are preferred.
- **Indentation**: All indentations MUST be 4 spaces instead of TABs.
    - You can automatically convert tabs into spaces in the settings of your editor. Search for the editor setting "soft tabs" and set the soft tab length to 4;
    - Another indication is that when you upload to gradescope, tabs will have length 8 while 4 spaces will only have length 4.
- **Doctests**: For EACH function created, you should add **at least 3 doctest of your own** unless explicitly instructed otherwise.
    - You should think comprehensively about cases that would possibly break your code rather than testing it on easy-to-pass scenarios;
    - If you create any helper functions, you still need to add docstrings/doctests for them;
    - If you create inner functions, you only need to add docstrings (no doctests required);
    - It's recommended to add as many doctests as you're comfortable with to test the code thoroughly because your code correctness will be graded by hidden tests.

### Style Guide Examples
To further clarify the rules, we have compiled a set of example problems and solutions with an emphasis on style requirements: 

[**Style Guide Examples**](https://docs.google.com/document/d/14GKLDJc9R8cG8MQI6Ml_Io5875Ux4qdAq7WjIn5Us1k/edit?usp=sharing)



## Checking style using programs
It's **highly recommended** that you follow the style guide **while** you write the code, but there are also programs that you may use to check the style of your code. You need to install 3 programs:
- pycodestyle (tool to check your Python code against some of the style conventions)
- pylint (source code, bug and quality checker for the Python. Has more options compared do pycodestyle)
- pydocstyle (tool for checking compliance with Python docstring conventions)
To install: 
Note: Some of the programs (linters) maybe come preinstalled.  
1) Open terminal  
2) type ```pip install pycodestyle```  
3) type ```pip install pylint```  
4) type ```pip install pydocstyle```

To run these programs, you simply type in the name of the program and the file that you wish to run it on e.g.:
```
>>> pylint hw01.py
```

### Long Output
You will receive a fairly long-winded output, but feel free to ignore parts of it that don't seem relevant to our style guide.

For example, here are the results from one of my files, where I cross out the parts that I feel are irrelevant:

 ************* Module hw01solutions  
~~hw1solutions.py:8:64: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:21:0: C0303: Trailing whitespace (trailing-whitespace)~~  
hw1solutions.py:36:23: C0326: Exactly one space required after comma  
&nbsp;&nbsp;&nbsp;&nbsp;assert isinstance(x,int), "first argument must be an integer"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^ (bad-whitespace)  
hw1solutions.py:37:23: C0326: Exactly one space required after comma  
&nbsp;&nbsp;&nbsp;&nbsp;assert isinstance(y,int), "second argument must be an integer"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^ (bad-whitespace)  
hw1solutions.py:38:12: C0326: Exactly one space required around comparison  
&nbsp;&nbsp;&nbsp;&nbsp;assert x>0, "first argument must be positive"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^ (bad-whitespace)  
hw1solutions.py:39:12: C0326: Exactly one space required around comparison  
&nbsp;&nbsp;&nbsp;&nbsp;assert y>=x, "second argument must be >= the first one"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^ (bad-whitespace)  
~~hw1solutions.py:40:0: C0303: Trailing whitespace (trailing-whitespace)~~  
hw1solutions.py:45:30: C0326: Exactly one space required after comma  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for divisor in range(2,int(n**sqrt_factor)+1):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^ (bad-whitespace)  
hw1solutions.py:50:20: C0326: Exactly one space required after comma  
&nbsp;&nbsp;&nbsp;&nbsp;for n in range(x,y+1):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^ (bad-whitespace)  
~~hw1solutions.py:77:42: C0303: Trailing whitespace (trailing-whitespace)~~   
hw1solutions.py:89:18: C0326: No space allowed before bracket  
def numbered_rows (levels = 10):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^ (bad-whitespace)  
hw1solutions.py:89:26: C0326: No space allowed around keyword argument assignment  
def numbered_rows (levels = 10):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^ (bad-whitespace)  
~~hw1solutions.py:93:28: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:94:33: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:95:34: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:96:35: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:97:36: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:98:36: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:99:36: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:100:36: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:101:36: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:102:39: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:105:15: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:106:15: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:107:16: C0303: Trailing whitespace (trailing-whitespace)~~  
~~hw1solutions.py:108:17: C0303: Trailing whitespace (trailing-whitespace)~~  
hw1solutions.py:115:20: C0326: Exactly one space required after comma  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(n, "*",' '.join(out_base),"")  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^ (bad-whitespace)  
hw1solutions.py:115:39: C0326: Exactly one space required after comma  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(n, "*",' '.join(out_base),"")  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^ (bad-whitespace)  
~~hw1solutions.py:26:0: C0103: Argument name "x" doesn't conform to snake_case naming style (invalid-name)~~  
~~hw1solutions.py:26:0: C0103: Argument name "y" doesn't conform to snake_case naming style (invalid-name)~~  
~~hw1solutions.py:44:4: C0103: Argument name "n" doesn't conform to snake_case naming style (invalid-name)~~  
~~hw1solutions.py:50:8: C0103: Variable name "n" doesn't conform to snake_case naming style (invalid-name)~~  
~~hw1solutions.py:113:8: C0103: Variable name "n" doesn't conform to snake_case naming style (invalid-name)~~  
------------------------------------------------------------------  
Your code has been rated at 0.83/10 (previous run: 0.28/10, +0.56)  

From above, we can see that we don't care about the invalid names or the trailing whitespaces. We might care about the bad-whitespaces, so I might choose to fix those. It's really personal judgement that matters for how you parse these results. Effectively, we can conclude that the previous code is good enough for submission, since there were no major errors.  

### Relevant Output
Following, we can see some examples of warnings that we would actually care about
```
(py36) Alexanders-MacBook-Pro-3:hw1 alexanderpotapov$ pylint terribleCode.py  
************* Module terribleCode  
terribleCode.py:6:0: C0305: Trailing newlines (trailing-newlines)  
terribleCode.py:1:0: C0103: Module name "terribleCode" doesn't conform to snake_case naming style (invalid-name)  
terribleCode.py:1:0: C0111: Missing module docstring (missing-docstring)  
terribleCode.py:1:0: C0103: Function name "ALLCAPSFUNC" doesn't conform to snake_case naming style (invalid-name)  
terribleCode.py:1:0: C0111: Missing function docstring (missing-docstring)  
terribleCode.py:3:4: C0103: Variable name "other_VARIABLE" doesn't conform to snake_case naming style (invalid-name)  
terribleCode.py:4:4: C0103: Variable name "o" doesn't conform to snake_case naming style (invalid-name)  
terribleCode.py:5:4: C0103: Variable name "l" doesn't conform to snake_case naming style (invalid-name)  
terribleCode.py:1:16: W0613: Unused argument 'lst' (unused-argument)  
terribleCode.py:3:4: W0612: Unused variable 'other_VARIABLE' (unused-variable)  
terribleCode.py:5:4: W0612: Unused variable 'l' (unused-variable)  
-------------------------------------  
Your code has been rated at -12.00/10
``` 
As we can see, we are actually failing a lot of the requirements that were set forth in the style guide. We've used random capital words, we've used bad variable names, and we're missing docstrings, so we've made a good few mistakes. You would want to fix these before turning in your code. One thing that we cannot use these autocheckers to check are magic numbers and indentation. That must be checked manually by yourself.
 
In conclusion, these are nice tools, but they will not make up for not keeping proper track of your code and making good style choices while writing. Best of luck and feel free to ask on piazza if you have any other questions.