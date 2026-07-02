.PHONY: install test lint format run stop

install:
	cd backend && make install
	cd frontend && npm install

test:
	cd backend && make test

lint:
	cd backend && make lint

format:
	cd backend && make format

run:
	@echo "Starting backend..."
	@setsid /workspace/backend/.venv/bin/python -m flask --app /workspace/backend/app run --host=0.0.0.0 --port=5000 > /tmp/backend.log 2>&1 &
	@sleep 2
	@echo "Starting frontend..."
	@cd /workspace/frontend && setsid npx vite --host --port 5173 > /tmp/frontend.log 2>&1 &
	@sleep 3
	@echo "Backend: http://localhost:5000"
	@echo "Frontend: http://localhost:5173"
	@echo "Logs: tail -f /tmp/backend.log /tmp/frontend.log"

stop:
	@echo "Stopping servers..."
	@-pkill -f "flask --app /workspace/backend/app" 2>/dev/null && echo "Backend stopped"
	@-pkill -f "vite" 2>/dev/null && echo "Frontend stopped"