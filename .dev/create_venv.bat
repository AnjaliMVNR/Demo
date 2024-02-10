py -m venv env
call .venv\scripts\activate.bat
py -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pause