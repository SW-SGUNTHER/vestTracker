import picamera as picam
import time
                                                           


camera = picam.PiCamera()
camera.start_preview()
camera.capture("test.png")
camera.stop_preview()
print("capture taken")

