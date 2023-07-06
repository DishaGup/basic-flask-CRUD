# Flask CRUD Application

This is a simple Flask application that demonstrates basic CRUD (Create, Read, Update, Delete) operations without using a database.

## Getting Started

### Prerequisites

- Python (version 3.x)
- Flask (install using `pip install flask`)

### Installation

1. Clone the repository or download the project files.

```bash
git clone https://github.com/DishaGup/basic-flask-CRUD.git
```

2. Create and activate a virtual environment. (Optional but recommended)

```bash
python -m venv env
```

- On Windows:
```bash
.\env\Scripts\activate
```

- On macOS/Linux:
```bash
source env/bin/activate
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

### Usage

1. Start the Flask development server.

```bash
python app.py
```

2. Open a web browser and visit `http://127.0.0.1:5000` to access the application.

## Functionality

The Flask application provides the following routes:

- `/` : Displays a welcome message.
- `/greet/<username>` : Displays a greeting message for the specified username.
- `/farewell/<username>` : Displays a farewell message for the specified username.
- `/create` : Allows users to create a new entry in the dictionary.
- `/read` : Displays the current state of the dictionary.
- `/update` : Allows users to update an existing entry in the dictionary.
- `/delete` : Allows users to delete an existing entry from the dictionary.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvement, please feel free to submit a pull request or open an issue.
