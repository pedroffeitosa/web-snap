
# Web Section Screenshot Taker

This Python project uses Selenium to navigate to a specified website, find all the sections on the page, and take screenshots of each section. The screenshots are saved in a local folder named `screenshots`.

## Features

- **Headless Browser Operation**: The script uses a headless Chrome browser to operate without a GUI.
- **Section and Div Element Screenshot**: Automatically finds all `<section>` tags on the page, and if none are found, it will fall back to `<div>` tags.
- **Dynamic Content Handling**: The script scrolls to each section and waits for dynamic content to load before taking a screenshot.

## Project Structure

```
WebScreenshotTaker/
├── script.py             # Main Selenium script
├── config.py             # Configuration file for the URL
├── screenshots/          # Folder where screenshots will be saved
├── requirements.txt      # List of dependencies
└── README.md             # This file
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/pedroffeitosa/web-snap.git
   cd web-snap
   ```

2. **Set Up the Virtual Environment:**

   ```bash
   python3 -m venv web-screenshot-env
   source web-screenshot-env/bin/activate  # On Windows: web-screenshot-env\Scriptsctivate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up ChromeDriver:**

   - Ensure that you have [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed and the path to `chromedriver.exe` is correctly set in the script.

## Usage

1. **Configure the URL:**

   - Set the `URL` in `config.py` to the website you want to take screenshots of.

2. **Run the Script:**

   ```bash
   python script.py
   ```

   - The script will navigate to the specified URL, find all the sections (or divs) on the page, and save screenshots in the `screenshots` folder.

## Example Output

- The screenshots will be saved in the `screenshots` folder with filenames like `section_1.png`, `section_2.png`, etc.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
