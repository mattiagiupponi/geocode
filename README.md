Software note:
------------------

- Django 3.1
- Sqlite
- python 3.8


<h3>How to run the applications</h3>
The design of the project is divided in 2 component:
- UI app made with VueJs
- Backend app made with Django

note: create a virtual environment (use the way you prefer, in this case i used [miniconda](https://docs.conda.io/en/latest/miniconda.html))

```
1) clone project https://github.com/mattiagiupponi/geocode.git
2) create a conda env: conda create -n geo
3) activate your environent: conda activate geo
4) install pip: conda install pip
3) install the requirements.txt: pip install -r requirements.txt
```
----------
<h5>Frontend</h5>

The UI project is based on the npm command for create an app with [VueJS](https://github.com/vuejs/vue-cli)

```markdown
- install NPM -> https://www.npmjs.com/get-npm
- sudo npm install -g vue-cli
```

To run the frontend app, move to ```geocode/frontenv``` and than run this command:
```npm run dev```
The Application will run at this link: http://localhost:8081/#/

the main code is available under ```src/components/GeoCoordinate.vue```

Given a X,Y coordinates, nof points and the type of the action, a call to the backend will retrieve the desired data into the textbox present.

Is possible also to see all the request made to re-use an old request. Once selected, the inputbox are automatically filled.
  

----------
<h5>Backend</h5>

The backend project is based on Django

To run the backend app, move to ```geocode/geo``` and than run this command:
```python manange.py runserver```
The Application will run at this link: http://localhost:8000/

<h4>API</h4>

There are two api available in the project:

```markdown
Getting the coordinates:

URL: http://localhost:8000/api/v1/coordinates
Params: - operation: REQUIRED -> nearest/coso
        - x        : REQUIRED -> the X coordinate
        - y        : REQUIRED -> the Y coordinate
        - points   : REQUIRED -> The number of points to return

Example: 
http://localhost:8000/api/v1/coordinates?operation=nearest&x=880702.0&y=1432946.5&points=3
------------------------------------------------------------------------------------

Getting the request History
(since there is no logic for this, i decided to use a simple Serializer from DjangoRestFramework)

URL: http://localhost:8000/api/v1/coordinates
Params: None

Example: 
http://127.0.0.1:8000/api/v1/history/
```

<h4>Import csv from CLI</h4>
The software has a custom command to load the csv with the coordinates into the database.

How to import the csv:

````markdown
Move to geocode/geo/ and than use the following commands

python manange.py importcsv "Absolute_path_of_the_file"

Example:
python manange.py importcsv "/Users/mattia.giupponi/Downloads/points.csv"

SUCCESS:
File successfully loaded

IF FILE DOES NOT EXIST:
File does not exists, please check the file_path: asdasd
````
Notes:

Why two different apps?

The idea is to have 2 different and stand-alone environment where each deploy/edit ecc... does not have impact on the other application.

Next Features:
- docker compose for run the applications
- use Postgres/MySql instead of SQlite
