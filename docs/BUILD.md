# Build oClip From Source
This page includes instructions to build oClip from source.
oClip supports **Windows**.
(**Linux** support is a work in progress.)

## Prerequisite
Before starting the build process we first need to setup required files.
- Clone The Repo:
```sh
git clone https://github.com/Nabir14/oclip.git
```
- Open Repo Directory:
```sh
cd oclip
```
- Setup A Python Environment:
```sh
python3 -m venv .env
```
- Activate The Python Environment:
> **Windows:**
>```ps
>.\.env\Scripts\Activate.ps1
>```
- Install Deps:
> **Windows:**
>```py
>pip install pillow pytesseract pyinstaller
>```
- Download and Install Tesseract OCR:
Tesseract OCR is what is used to scan text from image. So you need it installed in the repo directory before building oClip.
For Windows you can download it from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki). Full instructions for installing tesseract-ocr for different platforms is available [here](https://tesseract-ocr.github.io/tessdoc/Installation.html).

**NOTE:** Make sure Tesseract OCR is installed in `tesseract` folder in the root directory of oClip repository. Because to build oClip it needs data in folder `tesseract` in root.

## Build
Now you can start the build process.

### Windows:
- Generate Executable:
```py
pyinstaller --onefile --windowed --icon=icon.ico --add-data "assets;assets" --add-data "tesseract;tesseract" .\main.py
```

This will generate a `.exe` in the `dist` folder.

## After Building
Deactivate The Python Environment:
```py
deactivate
```

Great! If you have followed the steps correctly you will have an executable of oClip ready for use.