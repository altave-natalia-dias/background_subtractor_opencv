Background Subtraction using OpenCV

This repository contains Python scripts demonstrating background subtraction techniques using the OpenCV library. Background subtraction is a fundamental computer vision task that helps in isolating foreground objects by removing the static background.
Table of Contents

    Background
    Features
    Requirements
    Usage
    Scripts
    License

Background

Background subtraction is a crucial step in various computer vision applications, including object detection, tracking, and motion analysis. It involves distinguishing moving objects from the static background in a video stream.

This repository provides simple Python scripts utilizing OpenCV's background subtraction algorithms, including MOG (Mixture of Gaussians), MOG2, and GMG (Global Motion-based Background Subtract).
Features

    MOG (Mixture of Gaussians): Detects moving objects based on a mixture of Gaussian distributions.
    MOG2 (Improved MOG): An improved version of MOG, offering better performance and adaptability.
    GMG (Global Motion-based Background Subtract): Utilizes a statistical method to model the background and adapt to global motion changes.

Each script is designed to showcase a specific feature, including additional demonstrations such as blob detection, contour detection, and dilated foreground masks.
Requirements

Ensure you have the following dependencies installed:

    Python (3.6 or later)
    OpenCV (4.x)

You can install the required packages using the following command:

bash

pip install opencv-python

Usage

    Clone the repository:

bash

git clone https://github.com/your-username/Background_Subtractor_Opencv.git
cd Background_Subtractor_Opencv

    Run the desired script:

bash

python script_name.py

Replace script_name.py with the name of the script you want to execute.
Scripts

    blob_detection.py: Demonstrates blob detection using OpenCV's SimpleBlobDetector.
    contour_detection.py: Highlights moving objects using contour detection.
    dilated_mask.py: Applies dilation to the foreground masks, connecting broken parts.

Feel free to explore and modify the scripts based on your specific requirements.
License

This project is licensed under the MIT License.
