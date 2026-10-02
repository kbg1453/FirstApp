import subprocess

def run_servers():
    # Starte Uvicorn (FastAPI) in einem separaten Prozess
    uvicorn_process = subprocess.Popen(["uvicorn", "backend.main:app", "--reload"])

        # Starte Streamlit in einem separaten Prozess
    streamlit_process = subprocess.Popen(["streamlit", "run", "frontend/main.py"])    
    try:
        # Warte darauf, dass beide Prozesse beendet werden (z.B. durch Strg+C)
        uvicorn_process.wait()
        streamlit_process.wait()
        
    except KeyboardInterrupt:
        # Beende beide Prozesse bei einer Unterbrechung
        streamlit_process.terminate()
        uvicorn_process.terminate()

if __name__ == "__main__":
    run_servers()
