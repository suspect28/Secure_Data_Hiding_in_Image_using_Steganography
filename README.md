# Project:  Secure Data Hiding in Image using Steganography 

## Overview
This project implements **Image Steganography**, allowing users to hide and retrieve secret messages inside images. The implementation is done in Python using the **PIL (Pillow)** and **NumPy** libraries.

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Implementation Details](#implementation-details)

## Technologies Used
This project makes use of the following libraries and technologies:
- **Python 3.x** - Programming language
- **Pillow (PIL)** - Image processing
- **NumPy** - Handling image data efficiently
- **OpenCV (Optional)** - For additional image processing

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can install the required dependencies using:
```bash
pip install pillow numpy opencv-python
```

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/RushendraNuthi/ImageSteganography_usingPython.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ImageSteganography_usingPython
   ```
3. Run the script:
   ```bash
   python Image_Steganography.py
   ```

## Usage
The script allows you to hide and retrieve messages within images.

### Encoding a Message:
```bash
python3 Image_Steganography.py --encode --image input.png --message "Secret Message" --output encoded.png
```

### Decoding a Message:
```bash
python3 Image_Steganography.py --decode --image encoded.png
```

## Features
- Hide secret text messages within an image
- Extract hidden messages from steganographic images
- Supports PNG and JPEG formats
- Simple command-line interface

## Project Structure
```
ImageSteganography_usingPython/
│-- Image_Steganography.py
│-- README.md
│-- sample_images/
│   │-- input.png
│   │-- encoded.png
│-- requirements.txt
```

## Implementation Details
The script modifies the least significant bits (LSB) of the image pixels to embed secret text without noticeable changes in the image quality.
