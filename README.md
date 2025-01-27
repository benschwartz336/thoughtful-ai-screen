# Thoughtful AI Technical Screen

This project demonstrates a simple AWS Lambda function for sorting packages into different categories based on their dimensions and weight. The function classifies packages as `STANDARD`, `SPECIAL`, or `REJECTED` based on predefined rules.

## Features

- **Package Classification**:
  - **STANDARD**: Packages that are neither bulky nor heavy.
  - **SPECIAL**: Packages that are either bulky or heavy.
  - **REJECTED**: Packages that are both bulky and heavy.
- **AWS Lambda Integration**:
  - Deployed as a serverless function in AWS Lambda using Terraform for IaC.
  - Accepts JSON input to classify packages.
- **Validation**:
  - Handles invalid or missing input gracefully.
  - Validates numeric fields and prevents negative values.

---

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Testing](#testing)
- [Usage](#usage)
- [Example Output](#example-inputoutput)

---

## Setup

### Prerequisites

- **Python 3.12+**
- **AWS CLI** installed and configured.
- **Git** for version control.
- **Poetry** for running tests and dependency management.
- **Docker** for containerization.

### Installation

1. Clone this repository:
   ```bash
   git clone git@github.com:benschwartz336/thoughtful-ai-screen.git
   cd thoughtful-ai-screen

## Testing & Formatting

### Running Unit Tests Locally

1. Install Poetry dependencies on your machine
    ```bash
    poetry install

This prepares your environment to run unit tests.

2. Use Poetry to run all unit tests:
    ```bash
    poetry run pytest --cov -vvv

This will output pass/fail for all tests and any errors that occur. This will also tell you the test coverage (%). If test coverage is below 100% (as defined in our poetry project - lambdas/pyproject.toml), the output text will be red. If all tests pass with 100% coverage, the output text will be green.

3. Use Poetry to run an individual unit test:
    ```bash
    poetry run pytest -k test_lambda_handler_valid_input_standard -vvv

The '-k' command is used to test fewer than all tests at once. The input after '-k' will be the 'shortcut' for running certain tests. In this example, it will only run 1 test since only 1 test has the exact input as its name (test_lambda_handler_valid_input_standard). If you were to use 'test_lambda_handler_valid_input' instead, it would run every test that starts with this shortcut.

### Formatting the code

1. Run the black formatter on all code in the 'lambdas' directory
    ```bash
    cd lambdas
    poetry run black .

## Usage

You can test the Lambda function locally by providing a payload file. This method allows you to pass JSON input to the Lambda function without hardcoding it into the command.

### Steps

1. Create a JSON Payload File 
   Save the payload to a file, for example, `payload.json`.  
   Example contents of `payload.json`:
   ```json
   {
     "width": "10",
     "height": "20",
     "length": "30",
     "mass": "5"
   }

2. AWS CLI Command to Invoke Lambda with a Payload File

To invoke the Lambda function using a local payload file, use the following command:

```bash
payload=$(cat payload.json | base64)
aws lambda invoke \
    --function-name package-sorter \
    --payload "$payload" \
    output.json
```

## Example Output

### After running Lambda Function with above input as a JSON payload:

1. View Output
    ```bash
    cat output.json
    ```

2. Expected Output
   ```json
   {
     "statusCode": 200,
     "body": "STANDARD"
   }
   ```

