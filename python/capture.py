"""Camera frame capture from the USB UVC webcam via OpenCV/V4L2.

Hardware: Logitech 1080p Pro Stream Webcam, connected over USB alongside
board power through a USB splitter. Standard UVC device, no MIPI-CSI carrier
board or device-tree configuration required.

TODO: implement capture using cv2.VideoCapture(CAMERA_DEVICE), including
resolution/format selection and frame decode.
"""

from __future__ import annotations

import numpy as np

# TODO: confirm the webcam's actual V4L2 device path/index once connected
# through the USB splitter.
CAMERA_DEVICE = "/dev/video0"


def open_camera() -> None:
    """Open and configure the USB webcam.

    TODO: implement cv2.VideoCapture(CAMERA_DEVICE) setup, including
    resolution/format selection.
    """
    raise NotImplementedError


def grab_frame() -> np.ndarray:
    """Capture a single frame from the webcam.

    TODO: implement frame capture and return it as an RGB numpy array.

    Returns:
        Captured frame.
    """
    raise NotImplementedError


def close_camera() -> None:
    """Release the webcam device.

    TODO: implement camera teardown.
    """
    raise NotImplementedError
