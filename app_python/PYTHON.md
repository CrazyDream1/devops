# Best practices for python

1. Format the code according to PEP8 - if you do not do this, then it will be much more difficult for other people to understand your code.

2. Do not allow declared, but unused variables / functions / imports - again, this complicates the perception of the code.

3. Write short functions - functions that are too complex with a lot of branches and loops are hard to understand.

4. Do not use a mutable object as the default value of the function argument - otherwise, you can get very unexpected effects as a result.

5. Follow PEP 257's docstring guidelines.

6. Line lengths around 80-100 characters is fine.

7. Use linters. (Flake8)

## Best unit-testing practices

### (more or less) Python-specific

- using specific unit-testing-oriented frameworks (e.g., pytest, unittest)
- avoid writing unit tests in a form of one-line asserts in the middle of the other code; instead, write unit tests as separate functions each dedicated to a single test case
- naming functions as "test_", and then test purpose
- using test fixtures

### not-Python-specific

- tests shouldn’t duplicate implementation logic
- tests should be as simple as possible
- tests should be fase
- unit tests should be isolated (should not have any dependencies or outside factors)
