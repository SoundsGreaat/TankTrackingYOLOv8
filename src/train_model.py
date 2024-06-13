from clearml import Task
from ultralytics import YOLO


def main():
    task = Task.init(project_name='Tank tracking app', task_name='Train model')

    model = YOLO('yolov8m.pt')
    model.train(data='data.yaml', epochs=60, plots=True)


if __name__ == '__main__':
    main()
