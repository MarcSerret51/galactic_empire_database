# Empire database

This app allows to save the rebel data in a txt file.
Uses [CherryPy](https://cherrypy.org/) in back-end and simple JavaScript in front-end.
**Only tested on Windows 10 **

## Installation

Clone the repository
```bash
git clone https://github.com/MarcSerret51/galactic_empire_database.git
```

Go to the repository directory 

```bash
cd galactic_empire_database
```

Download anaconda from the [oficial source](https://anaconda.org/anaconda/python) and install it


Create the enviroment

```bash
conda env create -f enviroment.yml
```

Activate the enviroment

```bash
conda activate EmpireEnviroment
```

Go to exer directory

```bash
cd exer
```

Execute the web service

```bash
python exws.py
```

##Main features
- Back-end logging system
- Field validations
- Configuration file
- Lord Vader approval

##Configuration file
Please write the route like this
```
"path": "C:/Users/marc/Desktop/galactic_empire_database/exer/Database.txt"
```

##Unit tests
Just type in the directory
```bash
python unitTests.py
```

