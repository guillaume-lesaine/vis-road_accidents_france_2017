# vis-road_accidents_france_2017

This project is designed to simplify testing with python and pytests. We provide a simple folder structure template for writing code and testing it. We give a few examples showing how to industrialize and simplify testing functions taking common python objects as inputs and outputs, such as integer, strings, lists, as well as pandas dataframes and series.

<p align="center">
  <img src="folder_structure.png" width="75%"/>
</p>

The folder provides the following elements that can be customized depending on your needs :
- main.py : file at the root of the directory
- functions.py : file in the package directory with example functions to use in the main or to be tested
- test_functions.py : file to test the functions available in the functions.py file
- test_functions.json : file to store scenarios to test. The JSON file is then imported in test_functions.py the @pytest.mark.parametrize decorator is ultimately used to pass the scenarios the each test function.
- .json files : files providing inputs and outputs for testing functions with lists as inputs. When used, these files are mentionned in test_functions.json.
- .csv files : files providing inputs and outputs for testing functions with pandas dataframe or series as inputs. When used, these files are mentionned in test_functions.json.
- setup.py : file to run the first time the directory is used, see **Requirements & Setup** below.

## Requirements & Setup

Make sure you have the following packages installed.

```console
pip3 install pytest
pip3 install json
```

The first time you use the repository, run the following command from the root.

```console
python3 setup.py develop
```

## How to use the folder

All commands can be run from the root of the directory.

To run the main :

```console
python3 main.py
```

To run the tests :

```console
pytest -v
```
