# Mr. Forsyth's Pseudocode Styles

## Pseudocode is **NOT** Code

* Pseudocode should be written as plain language to allow you to simplify your thinking.
* Pseudocode should be able to be translated to any programming language.
* If your pseudocode looks the same as your Python code, then you are doing something wrong.

## Keywords In Pseudocode
|    Keyword     | Use                                                                                                                                                                                               |
|:--------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    `START`     | Shows the beginning of pseudocode.                                                                                                                                                                |
|     `END`      | Shows the end of pseudocode.                                                                                                                                                                      |
|    `INPUT`     | Shows when a user is providing input.<br>Typically followed by a variable name.                                                                                                                   |
|    `OUTPUT`    | Shows when data is displayed to the user.                                                                                                                                                         |
|      `IF`      | Used for `SELECTION` control structures.<br>Must include a condition.                                                                                                                             |
|     `ELIF`     | Optional for `IF` blocks.<br>Used for secondary conditions in `SELECTION` control structures.<br>Must include a condition.                                                                        |
|     `ELSE`     | Optional for `IF` blocks.<br>Used for the final option in `SELECTION` control structures.<br>Does not include a condition.                                                                        |
|    `END IF`    | Shows the end of a `SELECTION` control structure.<br>Must follow after all `IF`, `ELIF`, and `ELSE` sections of a single block of code.                                                           |
|     `FOR`      | Used for `ITERATION` control structures.<br>Must include a specific pattern for iterating.                                                                                                        |
|   `END FOR`    | Shows the end of a `FOR` `ITERATION` control structure.                                                                                                                                           |
|    `WHILE`     | Used for `ITERATION` control structures.<br>Must include a condition to evaluate.<br>Continues to iterate as long as the condition is `True`.                                                     |
|  `END WHILE`   | Shows the end of a `WHILE` `ITERATION` control structure.                                                                                                                                         |
|   `FUNCTION`   | Used to declare custom `functions`.<br>Must include a function name.<br>May include function parameters.                                                                                          |
| `END FUNCTION` | Used to show the end of a `FUNCTION` that has been declared.                                                                                                                                      |
|    `RETURN`    | Optional for functions.<br>Used to show a value that is being returned.<br>If being used, must come before `END FUNCTION`.<br>Logic that comes after `RETURN` in a `FUNCTION` block will not run. |

## Pseudocode is Indented to Show Hierarchy

Just like in Python and many other programming languages, pseudocode uses indentation to help clarify what code is nested inside other blocks of code.

## Naming Variables, Constants, and Functions in Pseudocode

Variables, constants, and functions follow the same naming conventions in pseudocode as Python.

### Variables

Variables should be named in `snake_case`:

* Names must be full words (no abbreviations).
* Names must be all lowercase.
* Words are connected with underscores (`_`).
* Single characters are only acceptable when they are commonly recognized as a regularly used value:
  * `x`, `y`, `z` for coordinates.
  * `i`, `j`, `k` for iteration control structures.
  * `n` for a number of terms.
  * `a`, `b`, `c` for mathematical numbers used in calculations.
  * `w`, `h` for width and height.

### Constants

Constants should be named in `UPPER_SNAKE_CASE`:

* Names must be full words (no abbreviations).
* Names must be all uppercase.
* Words are connected with underscores (`_`).

### Functions

Functions should be named in `snake_case`:

* Names must be full words (no abbreviations).
* Names must be all lowercase.
* Words are connected with underscores (`_`).
* Parameters should be named like variables *(see above)*.

## Examples of Pseudocode For Common Algorithms

### Adding 2 Numbers

```text
START

INPUT number_a
INPUT number_b

total = number_a + number_b

OUTPUT total

END
```

### List of Odd Numbers

```text
START

FUNCTION find_odds(highest_number)
    Set odd_list to an empty list
    FOR each number < highest_number
        IF number is odd
            Add number to odd_list
        END IF
    END FOR
    RETURN odd_list
END FUNCTION

INPUT user_number

OUTPUT find_odds(user_number)

END
```

### Fibonacci Numbers

```text
START

FUNCTION find_fibonacci_terms(n)
    Set fibonacci to an empty list
    IF n is < 1
        RETURN fibonnaci
    ELIF n < 3
        FOR n times
            Add 1 to fibonacci
        END FOR
        RETURN fibonacci
    ELSE
        a = 1
        b = 1
        Add a and b to fibonacci
        FOR n - 2 times
            c = a + b
            Add c to fibonacci
            a = b
            b = c
        END FOR
        RETURN fibonacci
    END IF
END FUNCTION

INPUT user_number_of_terms

OUTPUT find_fibonacci_terms(user_number_of_terms)

END
```

