# Bukutamu App

This is a web-based Python application built using Flask. The application serves a simple web page with custom styles and client-side functionality.

## Project Structure

```
bukutamu_app
├── app.py                # Main application file
├── requirements.txt      # Project dependencies
├── static                # Static files (CSS, JS)
│   ├── css
│   │   └── style.css     # Styles for the application
│   └── js
│       └── script.js     # Client-side JavaScript
├── templates             # HTML templates
│   └── index.html        # Main HTML template
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/pxmelki/bukutamu_app.git
   cd bukutamu_app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.