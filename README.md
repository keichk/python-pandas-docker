cat > README.md <<'EOF'
# python-pandas-demo

A small Python project that uses **pandas** to create a simple DataFrame, display basic information, run tests, and execute a CI pipeline with GitHub Actions.

## Objective

This project is designed to show a minimal example of:
- a Python script using `pandas`,
- tests with `pytest`,
- code style checks with `flake8`,
- containerization with Docker,
- a CI pipeline with GitHub Actions.

## Project structure

```text
python-pandas-demo/
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── README.md
├── requirements.txt
├── script.py
└── test_script.py
```

## Prerequisites

Before running the project, make sure you have:
- Python 3.12 or a close version,
- `pip`,
- Docker (optional, if you want to run the container),
- Git (optional, if you want to version the project).

## Local installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest flake8
```

## Run the script

```bash
python script.py
```

The script:
- creates a pandas DataFrame,
- displays its shape,
- displays the first rows,
- displays descriptive statistics,
- displays DataFrame structure information,
- calculates the average of the `Age` column.

## Run the tests

```bash
pytest test_script.py -v
```

## Check code style

```bash
flake8 script.py
```

## Run with Docker

Build the image:

```bash
docker build -t python-pandas-demo .
```

Run the container:

```bash
docker run --rm python-pandas-demo
```

## Continuous integration

The GitHub Actions workflow runs 3 jobs in sequence:

```text
lint -> test -> build
```

## Dependencies

The `requirements.txt` file contains at least:

```txt
pandas
```

## Expected result

The script displays a simple table with 4 people and calculates the average age:

```text
Mean of all age : 32.5
```

## License

This project can be distributed under an MIT License if you want to publish it publicly on GitHub.
EOF
