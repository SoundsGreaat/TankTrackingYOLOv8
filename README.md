# Tank Tracking App

This is a Python application that uses the YOLO (You Only Look Once) object detection system for tracking tanks in video files.
![](/model/example_photo.png)
## Features

- Train a YOLO model with custom dataset.
- Track tanks in video files.
- Calculate the distance of the tank from the camera.

## Examples

You can find examples of the application's output here:
- [**Example 1**](https://youtu.be/ZJapZC4ejBQ)
- [**Example 2**](https://youtu.be/GS8DPy2xE2k)

## Installation

This project requires Python and pip installed. You can install the project dependencies with:

```bash
pip install -r requirements.txt
```
Also, you need to install an up-to-date version of [**PyTorch**](https://pytorch.org/get-started/locally/) and [**CUDA Toolkit**](https://docs.nvidia.com/deploy/cuda-compatibility/) that fits your system if you want to use GPU instead of CPU.

## Usage

### Training the model

If necessary, you can train the model by running the `train_model.py` script. This will initialize a ClearML task and train a YOLO model with the specified dataset and parameters.

```bash
python train_model.py
```

### Dataset

The dataset used for training the model can be found at [**RoboFlow**](https://universe.roboflow.com/tanksdataset/tank-tracking).

### Running the application

You can run the application by executing the `run.py` script. This will open a GUI where you can select a video file to process.

```bash
python run.py
```

The application will then track the tanks in the video and calculate their distance from the camera. The processed video will be saved as `output.mp4`.

You can customize the camera settings and the approximate size of the object for more accurate operation.

## Graphs and Statistics

You can view the training graphs and statistics on the [**ClearML**](https://app.clear.ml/projects/7d4774d728d04711b9bbb7747a8ceb4f/experiments/ccd6ee23f81141368218f379771d0a74/output/execution) web interface.

![](/results/results.png)