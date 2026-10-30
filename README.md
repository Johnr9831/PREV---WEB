# PREVIA - inicio del backend

FastAPI + Pydantic. Catalogo ficticio, sin base de datos, autenticacion ni frontend.
El catalogo publico es parte del contrato de la propuesta. MySQL y SQLAlchemy se
incorporaran en una etapa posterior. No verifica prerrequisitos ni matricula.

## Windows PowerShell, desde esta carpeta

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m uvicorn previa.main:app --reload
```

Abrir http://127.0.0.1:8000/docs y http://127.0.0.1:8000/public/courses.
Detener con Ctrl+C.

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m pytest -v
.\.venv\Scripts\python.exe -m build
```

CI valida PR hacia main y pushes a main. El paquete se construye solo si validate
pasa. No hay despliegue automatico. No incluir credenciales ni datos reales.
Versiones directas fijadas; dependencias transitivas no estan bloqueadas.
