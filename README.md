# Python Practice: Problem Set 1

There are 10 problems of increasing difficulty to solve in `problem_set_1.py`. Tests are included to check your code.

These problems are **exactly the same as the JavaScript problems you did in Phase 1**. You are welcome to look at your JavaScript code for help. The logic you need is the same but the syntax will, of course, be different.


## Run the tests with `pytest`

To run the tests, run `pytest -x` at the command line in this project directory. The tests will stop on the first incorrect answer. Read the failure, make a change to the code, and run the tests again. Repeat this process until you can get the test to pass.

You can look at `test_problem_set_1.py` in order to see what is being tested. That file contains Python code that you have not seen yet. Its job is to check your variables (in the first problem) and after that to call the functions that you write. Make sure you name your functions exactly what the directions tell you to.

### Fix import errors by defining functions that are imported

You can define a function and include a placeholder for the body of the function using the `pass` keyword like this:

```py
def sum(list):
    pass
```

[See the python docs for more detail about the `pass` keyword.](https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement)

### Skipping tests

If you get stuck on a problem and want to skip it so that you can move on, you can mark that test to be skipped by adding one line above the test function definition, like this:

```py
@pytest.mark.skip() # add this line
def test_greeting(input, expected):
    assert greeting(input) == expected
```

After you have added that line, save the file and run `pytest -x` again.

When you want to work on that test again, you can simply delete that line.
