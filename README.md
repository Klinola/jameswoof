## Jameswoof Autointeraction Tools v1.0
### Overview
This tool provides an automated interaction system for managing accounts in the Jameswoof game. It includes functionalities for daily interactions, grouping, and initialization of accounts. The tool uses a GUI built with wxPython for ease of use.

### Features
#### **Daily Interactions**: Automatically performs daily interactions for selected accounts.
#### **Group Management**: Creates groups of accounts and assigns group leaders and members.
#### **Initialization**: Loads accounts from local storage and initializes the database.

### Requirements
- Python 3.x
- wxPython
- plyvel (plyvel-ci on Windows)
- SQLite3
### Installation
#### Windows
```sh
pip install wxPython requests cryptography
pip install plyvel-ci
```
#### Linux
```sh
pip install wxPython requests cryptography
pip install plyvel
```
### Usage

#### Run the Application:

```sh
python strategy.py
```