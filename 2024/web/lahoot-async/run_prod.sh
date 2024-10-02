echo Starting Application
python -m uvicorn server:app --host '::' --port 8000
echo Application terminated
