from ffpyplayer.player import MediaPlayer
import cv2
import time
import ctypes

# Esconde o mouse na hora
ctypes.windll.user32.ShowCursor(False)

video_path = "calcz.mp4"

player = MediaPlayer(video_path)
cap = cv2.VideoCapture(video_path)

# Fullscreen
cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

start_time = time.time()

while True:
    ret, frame = cap.read()
    audio_frame, val = player.get_frame()

    if not ret:
        break

    # Trata timestamp (float ou tuple)
    if isinstance(val, tuple):
        frame_time = val[0]
    else:
        frame_time = val

    if frame_time is not None:
        while (time.time() - start_time) < frame_time:
            time.sleep(0.001)

    cv2.imshow("video", frame)

    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
player.close_player()
cv2.destroyAllWindows()

# Mostra o mouse de volta
ctypes.windll.user32.ShowCursor(True)
