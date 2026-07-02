.PHONY: install test lint format

install:
	cd backend && make install
	cd frontend && npm install

test:
	cd backend && make test

lint:
	cd backend && make lint

format:
	cd backend && make format