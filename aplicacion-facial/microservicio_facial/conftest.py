import sys
from unittest.mock import MagicMock

# Mockea deepface para que los tests no necesiten instalar TensorFlow/DeepFace
sys.modules["deepface"] = MagicMock()
