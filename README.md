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

## Arquivos Ignorados (Gitignore)

Para garantir a segurança e a limpeza do projeto, configuramos o Git para ignorar arquivos que não devem ser versionados. As principais exclusões são:

- **venv/**: Pasta do ambiente virtual (contém arquivos pesados do sistema e dependências).
- **data/alunos.db**: Arquivo de banco de dados (evita versionar dados locais).
- **__pycache__/**: Arquivos temporários gerados pelo Python.
- **.vscode/**: Configurações personalizadas do editor de código.