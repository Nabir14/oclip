# oClip - Optical Clipboard

oClip is a program that can copy text from an image to the clipboard.

**How It Works:**
- It uses `ImageGrab` from `Pillow` and lets you "snip" the portion of the image you want to copy.
- This image is then provided to Tesseract OCR to scan and extract the text.
- Tkinter is used for Ui and this let's you copy the extracted text to your clipboard.

**Available Platforms:** Windows.

**Compile From Source:**
- Clone The Repo:
```sh
git clone https://github.com/Nabir14/oclip.git
```
- Open Repo Directory:
```sh
cd oclip
```
- Setup Environment:
```sh
python3 -m venv .env
```
- Activate Environment:
```ps
.\.env\Scripts\activate.ps1
```
- Install Deps:
```py
pip install pillow pytesseract pyinstaller
```
- Build:
```py
pyinstaller --onefile --windowed --icon=icon.ico --add-data "assets;assets" --add-data "tesseract;tesseract" .\main.py
```
- Deactivate Environment After Build:
```py
deactivate
```

This will create an executable in dist folder for Windows.