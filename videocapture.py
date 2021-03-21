import cv2
import time

def record_wcam(length,file_destination):
	start = time.time()
#Capture video from webcam
	vid_capture = cv2.VideoCapture(0)
	vid_cod = cv2.VideoWriter_fourcc(*'XVID')
	output = cv2.VideoWriter(file_destination, vid_cod, 24.0, (640,480))

	while time.time() < start + length:
	 # Capture each frame of webcam video
		ret,frame = vid_capture.read()
		output.write(cv2.flip(frame,1))
	 # Close and break the loop after pressing "x" key
		if cv2.waitKey(1) &0XFF == ord('x'):
			break

# close the already opened camera
	vid_capture.release()
# close the already opened file
	output.release()
# close the window and de-allocate any associated memory usage
	cv2.destroyAllWindows()