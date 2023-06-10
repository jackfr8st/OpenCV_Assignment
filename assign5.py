import cv2

video_capture = cv2.VideoCapture('Resources/sample-1.mp4')

fps = video_capture.get(cv2.CAP_PROP_FPS)
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

output_file = 'temp/assign5.mp4'
codec = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter(output_file, codec, fps, (frame_width, frame_height))

while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    output_video.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
