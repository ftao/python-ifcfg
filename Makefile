clean: clean-build clean-pyc clean-test


clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint:  ## Check python code conventions
	tox -e lint

test:  ## Run automated test suite
	nosetests

test-all:  ## Run tests on all supported Python environments
	tox

coverage:  ## Generate test coverage report
	coverage run --source src/ifcfg `which nosetests`
	coverage report -m

release: dist  ## Generate and upload release to PyPi
	@echo ""
	@echo "Release check list:"
	@echo ""
	@echo "1. Release notes?"
	@echo "2. Did you do a signed commit and push to Github?"
	@echo "3. Check that the .whl and .tar.gz dists work - e.g. that MANIFEST.in is updated."
	@echo ""
	@read -p "CTRL+C or ENTER" dummy
	twine upload -s dist/*

dist: clean  ## Generate wheels distribution
	python setup.py bdist_wheel
	python setup.py sdist
	ls -l dist
