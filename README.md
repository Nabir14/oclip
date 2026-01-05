# oClip - Optical Clipboard

oClip is a program that can copy text from an image to the clipboard.

**How It Works:**
- It uses `ImageGrab` from `Pillow` and lets you "snip" the portion of the image you want to copy.
- This image is then provided to Tesseract OCR to scan and extract the text.
- Tkinter is used for Ui and this let's you copy the extracted text to your clipboard.

**Available Platforms:** Windows, Linux.

**Compile From Source:**
- Clone The Repo
- Open Repo Directory:
```sh
cd oclip
```
- Setup Environment:
```sh
python3 -m venv .env
```
- Activate Environment:
**Windows:**
```ps
.\.env\bin\activate.ps1
```
**Linux:**
```sh
./env/bin/activate
```
- Install Deps:
```py
pip install pillow pytesseract pyinstaller
```
- Build:
**Windows:**
```py
pyinstaller --onefile --windowed --icon=icon.ico --add-data "assets;assets" --add-data "tesseract;tesseract" .\main.py
```
**Linux:**
```py
pyinstaller --onefile --windowed --icon=icon.ico --add-data "assets;assets" --add-data "tesseract;tesseract" .\main.py
```
- Deactivate Environment After Build:
```py
deactivate
```

This will create an executable in dist folder for the host operating system.