"""Load and run the species and health TFLite models.

TODO: implement model loading (tflite_runtime.interpreter.Interpreter) and
inference for both models.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

MODELS_DIR = Path(__file__).parent / "models"
SPECIES_MODEL_PATH = MODELS_DIR / "species.tflite"
HEALTH_MODEL_PATH = MODELS_DIR / "health.tflite"


def load_models() -> tuple[Any, Any]:
    """Load the species and health TFLite interpreters.

    TODO: implement interpreter creation and tensor allocation for both
    SPECIES_MODEL_PATH and HEALTH_MODEL_PATH.

    Returns:
        Tuple of (species_interpreter, health_interpreter).
    """
    raise NotImplementedError


def run_models(
    frame: np.ndarray,
    species_interpreter: Any,
    health_interpreter: Any,
) -> dict:
    """Run inference on a preprocessed frame with both models.

    TODO: implement invoking both interpreters and collecting their outputs.

    Args:
        frame: Preprocessed frame from preprocess.prepare_frame().
        species_interpreter: Loaded species TFLite interpreter.
        health_interpreter: Loaded health TFLite interpreter.

    Returns:
        Dict with species and health inference results.
    """
    raise NotImplementedError
