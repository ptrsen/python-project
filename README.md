# python-project
simple project template to work with python using a devcontainer

### Pre-req: vscode with Dev containers extension
#### 1 - Clone and open in vscode
#### 2 - (ctrl+shift+p): >Dev Containers: Rebuild and Reopen in Container

#### 3 - Open a terminal in vscode and install the project in editable mode along with its dependencies
```bash
cd python-project
pip install -e .
```

##### (Optional) Run all tests
```bash
pytest tests
```

##### (Optional) Run script directly using Python3
```bash 
python3 src/main.py "YourName"
```

### 4 - Use the command-line tool, after installation it can be invoke directly (see entry_points in setup.py)
```bash
greet [-h] "YourName"
```
