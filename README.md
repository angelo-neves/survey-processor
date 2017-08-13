# Angelo's Coding Challenge

## Running Instructions

### Using Docker

This project can be easily run using docker-compose.
A shell script is provided to build and run the container with a single command:

```
./run.sh [survey-questions.csv] [survey-responses.csv]
```

The file paths can be absolute or relative to the root of the project,
it’s recommended that you place the desired files inside the “files” folder in this project:

```
./run.sh files/survey-1.csv files/survey-1-responses.csv
```

### Using local Python

This project has been developed using Python 3.6.2
in order to run it locally you must first install the requirements using pip

```
pip install -r requirements.txt
```

then you can run the app.py script directly:

```
python app.py files/survey-1.csv files/survey-1-responses.csv
```

## Design Decisions
