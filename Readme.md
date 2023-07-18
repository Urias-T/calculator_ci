# Simple CI workflow

1. Create GitHub/GitLab repo

2. Create CircleCi account & connect it to GitHub/GitLab

3. python3 -m venv calculator

4. . calculator/bin/activate

5. git add .

6. git commit -m"Added + and - funcs"

7. pip install flake8 pytest pytest-cov

8. pip freeze > requirements.txt

9. flake8 --statistics

10. pytest -v --cov

11. git add test_calculator.py

12. git commit -m"added 1st unit test"

13. git push

Detailed description:
https://realpython.com/python-continuous-integration/