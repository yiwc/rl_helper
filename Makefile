PY_SOURCE_FILES=fmrl/ tests/ scripts/

install:
	pip install -e .
	
test:
	pytest tests -vv ./tests/

build:
	python3 -m build

format:
	autoflake --in-place --remove-all-unused-imports --recursive ${PY_SOURCE_FILES}

.PHONY: default test doc bulid package publish install lint format
