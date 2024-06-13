import cv2
from ultralytics import YOLO


def calculate_distance(focal_length, obj_length, bbox_height):
    distance_to_obj = (obj_length * focal_length) / bbox_height
    return distance_to_obj


def rbg_to_bgr(color):
    return color[2], color[1], color[0]


focal_length_ = 3000
obj_length_ = 4

model = YOLO('../model/best.pt')


def track_objects(video_path, output_path='../output.mp4'):
    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.track(frame, persist=True, conf=0.3)

        for result in results:
            try:
                for bbox, obj_id, obj_prob in zip(result.boxes.xyxy, result.boxes.id, result.boxes.conf):
                    x1, y1, x2, y2 = bbox
                    bbox_height = y2 - y1

                    distance = calculate_distance(focal_length_, obj_length_, bbox_height)

                    box_color = (rbg_to_bgr((255, 100, 100)))
                    box_thickness = 2

                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), box_color, box_thickness)

                    text = f'{int(obj_id)} {obj_prob:.2f} {distance:.2f}m'
                    cv2.putText(frame, text, (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                rbg_to_bgr((255, 100, 100)), 2)
            except TypeError:
                pass

        out.write(frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    video_path_ = '../vids/video file.mp4'
    track_objects(video_path_)
