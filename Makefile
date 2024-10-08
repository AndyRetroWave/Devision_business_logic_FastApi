PYTHON = python
UVI = uvicorn
RUFF = ruff
POETRY = poetry
COMMIT ?= Обновление 


.PHONY: run
run:
	$(UVI) main:app --reload

lint:
	$(RUFF) check .
	mypy .

git-commit:
	git add .
	git commit -m "$(COMMIT)"
	git push

install:
	$(POETRY) shell
	$(POETRY) install

test:
	pytest