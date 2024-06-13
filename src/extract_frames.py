import os
import cv2


def extract_frames(video_path, output_folder, frame_interval=20):
    video_name = os.path.basename(video_path)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f'Error: Could not open video file {video_path}')
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = 0
    saved_frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f'{video_name}_{saved_frame_count:04d}.png')
            cv2.imwrite(frame_filename, frame)
            saved_frame_count += 1

        frame_count += 1

    cap.release()
    print(f'Extracted {saved_frame_count} frames to {output_folder}')


if __name__ == '__main__':
    video_path_ = '../vids/videofile'
    output_folder_ = '../vids/frames'
    extract_frames(video_path_, output_folder_)
