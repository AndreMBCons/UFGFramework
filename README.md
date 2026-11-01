# UFGFramework

Projeto Django `bdpratico` (apps `exemplo01` e `exemplo02`), em `BigData-env/Scripts/bdpratico/`.

## Rodando

```powershell
python -m venv BigData-env
BigData-env\Scripts\python.exe -m pip install -r requirements.txt
cd BigData-env\Scripts\bdpratico
..\python.exe manage.py migrate
..\python.exe manage.py createsuperuser
..\python.exe manage.py runserver
```

Admin em http://127.0.0.1:8000/admin/.

O banco `db.sqlite3` não é versionado: cada máquina cria o seu com `migrate`.
