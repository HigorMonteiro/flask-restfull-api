format:
		@black ./app

check:
		@black ./app --check

.PYTHON: format check