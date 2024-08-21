# Language Translation Flask App

This Flask application provides a simple web interface for translating text between different languages using Google Translate.

## Features

- **Text Translation**: Translate text from one language to another using Google Translate.
- **Language Selection**: Choose source and destination languages from a list of available languages.
- **Web Interface**: User-friendly interface built with Flask and HTML for interacting with the translation service.

## Prerequisites

- Python 3.6 or later
- Flask
- googletrans library

## Installation

1. **Clone the repository**:

    ```bash
   https://github.com/krishkrishna03/Language_Translation.git
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `requirements.txt` file** with the following content:

    ```txt
    Flask
    googletrans==4.0.0-rc1
    ```

## Running the Application

1. **Start the Flask application**:

    ```bash
    python app.py
    ```

2. **Open a web browser** and navigate to `http://127.0.0.1:5000/`.

3. **Use the web interface** to input text, select source and destination languages, and get the translated text.

## Code Explanation

- `app.py`: The main Flask application file that sets up the web server and handles text translation.
- `index.html`: The HTML template used to render the translation form and display the translated text.

## Example Usage

1. Open the application in a web browser.
2. Select the source and destination languages from the dropdown menus.
3. Enter the text you want to translate in the input field.
4. Click the submit button to see the translated text.

## Troubleshooting

- Ensure that all dependencies are installed correctly.
- If you encounter issues with translation, verify that the `googletrans` library is up-to-date and properly installed.

## Contributing

Feel free to open issues or submit pull requests to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions or comments, please contact [your-email@example.com](mailto:your-email@example.com).
