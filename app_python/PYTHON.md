# Best practices for python

1. Format the code according to PEP8 - if you do not do this, then it will be much more difficult for other people to understand your code.

2. Do not allow declared, but unused variables / functions / imports - again, this complicates the perception of the code.

3. Write short functions - functions that are too complex with a lot of branches and loops are hard to understand.

4. Do not use a mutable object as the default value of the function argument - otherwise, you can get very unexpected effects as a result.

5. Follow PEP 257's docstring guidelines.

6. Line lengths around 80-100 characters is fine.

7. Use linters. (Flake8)
