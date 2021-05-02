import os

import cv2


class ScannerException(Exception):
    """Base Class for all Scanner Exceptions"""
    pass


class InvalidCaptureDevice(ScannerException):
    """The provided camera_id was invalid or no device with this id exists"""
    pass


class Scanner:
    def __init__(self, camera_id=0, path="./", base_name="Dia_", suffix=""):
        """
        Show a preview of your camera and take and modify your images
        :param path: The path where the images shall be stored (default: '.')
        :param camera_id: The ID of the camera you want to use
        :param base_name: The base name of the produced files (default: dia_)
        :param suffix: A suffix for the saved images (default: '')
        """
        self.camera = cv2.VideoCapture(camera_id)
        if not self.camera.isOpened():
            raise InvalidCaptureDevice(f"The provided camera_id has now assigned device.")
        self.path = path
        self.base_name = base_name
        self.suffix = suffix
        self.orientation = 0

    def preview(self):
        """Show a preview Window with the current camera input"""
        cv2.namedWindow("Dia Scanner")
        while True:
            rval, frame = self.camera.read()
            frame = cv2.resize(frame, (1920, 1080))
            if self.rotate() is not None:
                frame = cv2.rotate(frame, self.rotate())
            cv2.imshow("Dia Scanner", frame)
            # Get key for action
            key = cv2.waitKey(20)
            if key == 27:  # exit on ESC
                break
            if key == 99 or key == 32:  # c or space for capture
                self.capture(frame)
            if key == 108:  # l for rotate left
                self.rotate(270)
            if key == 114:  # r for rotate right
                self.rotate(90)
        self.camera.release()
        cv2.destroyWindow("Dia Scanner")

    def capture(self, frame):
        incremental = 0
        filename = f"{self.path}{self.base_name}{incremental}{self.suffix}.png"
        while os.path.exists(filename):
            incremental += 1
            filename = f"{self.path}{self.base_name}{incremental}{self.suffix}.png"
        cv2.imwrite(filename, frame)
        print(f"{filename} written!")

    def rotate(self, orientation=None) -> int:
        if orientation:
            self.orientation = (self.orientation + orientation) % 360
        return None if self.orientation == 0 else int(self.orientation / 90) - 1
