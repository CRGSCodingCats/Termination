# Termination
Termination is a simple, modular GUI application built with Python’s `tkinter`. Designed to evoke a retro terminal vibe, it provides a foundation for expanding into a full-featured desktop command center—perfect for running shell commands, viewing processes, or adding interactive UI components.
## Features
- Minimalist interface with dark theme
- Exit coinfirmation dialogue, because I don't like fustration
- Modular code structure
- Easy to expand: add command execution, process viewing, etc.
## Installation
1. Clone the repository:
```bash
git clone https://github.com/CRGSCodingCats/Termination.git
cd Termination
```
2. Create a virtual environment and activate it (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate # On windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
Note: `tkinter` is bundled with standard Python installations. No external installation needed for basic UI.
## Usage
Make sure you're in the project root directory, then launch the app using:
```bash
python -m termination.app
```
For first time use, you could also just copy and paste the following into your Terminal:
```bash
git clone https://github.com/CRGSCodingCats/Termination.git
cd Termination
python -m venv venv
source venv/bin/activate # On windows: venv\Scripts\activate
pip install -r requirements.txt
python -m termination.app
```
You’ll see a black-themed window with a welcome message and a quit button. Clicking "Exit" will prompt for confirmation before closing.
## Contributing
Pull requests are welcome. For major changes, open an issue first to discuss proposed modifications.
## License
This project is licensed under the MIT License. See `LICENSE` for details.
