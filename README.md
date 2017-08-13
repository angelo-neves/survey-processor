# Angelo's Coding Challenge

## Running Instructions

### Using Docker

This project can be easily run in any operating system using docker-compose.
The only requirement is to have a recent version of docker including docker-compose.
A shell script is provided to build and run the container with a single command:

```
./run.sh [survey-questions.csv] [survey-responses.csv]
```

The file paths can be absolute or relative to the root of the project,
it’s recommended that you place the desired files inside the “files” folder in this project:

```
./run.sh files/survey-1.csv files/survey-1-responses.csv
```

To run the tests using docker you can simply execute the provided shell script:

```
./test.sh
```

### Using local Python

This project has been developed using Python 3.6.2 and
in order to run it locally you must first install the requirements using pip

```
pip install -r requirements.txt
```

then you can run the app.py script directly:

```
python app.py files/survey-1.csv files/survey-1-responses.csv
```

to run the tests locally you can execute:

```
python -m unittest discover
```

## Design Decisions

During the development of this application I have tried to implement an architecture that would be easy enough to maintain,
test and expand while at the same time avoiding over-engineering.

### Docker

The decision to include docker was made early on to facilitate the execution of this app on any operating system,
regardless of the version of python installed locally.

### Gateways, Models, Factories and Enums

Even though I haven’t followed any particular design approach,
I have tried to use concepts that would make the code easier to read and to change.

Gateways have been used to interact with the file in the operating system and deliver the contents of the CSV in a standard format,
that way I can later add other sources of information and plug them right in, as long as every gateway uses the same output standard.

Models have been created where needed to allow for a standard definition of the most important objects,
even though they are not like a framework’s ORM they serve a similar purpose.

Factories have been used to load data from the gateways and create instances of the adequate Models for use in the rest of the application.
By isolating this routine it becomes more reliable and easy to test.

Enums have been used because in this project a string can represent a data type and it’s important to reliably provide
 a way to test if a given string represents a given data type.
 If new types are introduced they will work even though they are not declared in the Enum,
 it only becomes necessary to do that if you need to implement logic based on that new type of data.
