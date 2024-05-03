## Init project

```bash
cd scripts/
sudo /bin/bash install.sh
```

## Recreate databases:

```bash
sudo /bin/bash scripts/recreate_databases.sh
```

## For developers:
### Requiremenets:
- Python >= 3.12
- RedDatabase >= 3.0.14

### Install requirements:
```bash
pip install -r requirements.txt
```
Tkinter is used for GUI.

### Before run (Linux)
```bash
sudo chmod 775 -R /tmp/firebird
```

## Run
In project directory
```bash
source venv/bin/activate && pip install -r requirements.txt && python main.py
```