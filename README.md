# python-project
simple python project template 

### Pre-req: vscode with Dev containers extension
### 1 - Clone and open in vscode
### 2 - (ctrl+shift+p): >Dev Containers: Rebuild and Reopen in Container

### 3 - Install the project in editable mode along with its dependencies
```bash
cd python-project
pip install -e .
```

### Run all tests
```bash
pytest tests
```

### Run script directly using Python3
```bash 
python3 src/main.py "YourName"
```

### 4 - Use the Command-Line Tool, after installation it can be invoke directly (entry_points in setup.py)
```bash
greet [-h] "YourName"
```