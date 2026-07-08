"""Frame preprocessing stub: resize to 224x224, normalize, crop.

TODO: implement preprocessing to match the input tensors expected by the
TFLite models loaded in infer.py.
"""

from __future__ import annotations

import numpy as np

TARGET_SIZE = (224, 224)


def prepare_frame(frame: np.ndarray) -> np.ndarray:
    """Resize, crop, and normalize a raw camera frame for model input.

    TODO: implement resize to TARGET_SIZE, any center/crop logic, and
    pixel value normalization.

    Args:
        frame: Raw frame from capture.grab_frame().

    Returns:
        Preprocessed frame ready for infer.run_models().
    """
    raise NotImplementedError
