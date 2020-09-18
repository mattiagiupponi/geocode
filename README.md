Software note:
------------------

- Django 3.1
- Sqlite
- python 3.8

<h3>Import csv from CLI</h3>
The software has a custom command to load the csv with the coordinates into the database and is available through the Admin UI

How to import the csv:

````
General Command:
python manange.py importcsv "Absolute_path_of_the_file"

Example:
python manange.py importcsv "/Users/mattia.giupponi/Downloads/points.csv"

SUCCESS:
File successfully loaded

IF FILE DOES NOT EXIST:
File does not exists, please check the file_path: asdasd
````