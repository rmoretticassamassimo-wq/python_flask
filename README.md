# Lista de Comandos
- Cria o ambiente virtual na pasta venv
```python
python -m venv venv

```
- Ativar o ambiente virtual
```python
venv\Scripts\activate
```

- Instalar todos os pacotes necessários
```python
pip install flask
pip install flask-wtf
pip install requests
pip install pytest
pip install pytest-flask
```
- Salva a  lista de pacotes instalados
- no arquivo requiriments.txt
- isso permite que outras pessoas instalem as mesmas versões.

```
pip freeze > requiriments.txt
```