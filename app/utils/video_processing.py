import cv2
import numpy as np
import tempfile


async def create_video(text, width=100, height=100, duration=3 ):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    bg_color = (255, 255, 255)
    bg = np.zeros((height, width, 3), np.uint8)
    bg[:] = bg_color

    font = cv2.FONT_HERSHEY_COMPLEX
    text_size = cv2.getTextSize(str(text), font, 1, 2)[0]
    start_pos = (width // 4, height // 2)

    frames = []
    for t in np.linspace(0, 1, int(60 * duration)):
        frame = np.copy(bg)
        text_x = int(start_pos[0] - t * (text_size[0] + width // 4))
        text_pos = (text_x, start_pos[1])
        cv2.putText(frame, str(text), text_pos, font, 1, (0, 0, 0), 2)

        frames.append(frame)

    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp:
        out = cv2.VideoWriter(temp.name, fourcc, 60.0, (width, height))
        for frame in frames:
            out.write(frame)
        out.release()

        return temp.name
