# python-project
simple template using vscode devcontainer

### Install the project in editable mode along with its dependencies
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

### Use the Command-Line Tool, after installation it can be invoke directly (entry_points in setup.py)
```bash
greet [-h] "YourName"
```