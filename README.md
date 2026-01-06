# oClip - Optical Clipboard

![preview](assets/preview.gif)

oClip is a program that can copy text from an image to the clipboard.

**Information:**
- version: `1.0`
- platforms: `Windows`

**How It Works:**
- It uses `ImageGrab` from `Pillow` and lets you clip the portion of the image you want to scan.
- This image is then provided to Tesseract OCR to scan and extract the text.
- Tkinter is used for UI and this let's you preview the snipped image or copy the extracted text to your clipboard.

**Compile From Source:**
To Compile oClip from source [follow this guide](docs/BUILD.md).