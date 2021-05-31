format:
		@black ./app

check:
		@black ./app --check

test:
		@FLASK_ENV=testing pytest -vv -s
.PYTHON: format check test