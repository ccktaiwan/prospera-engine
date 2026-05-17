import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine_runtime import ProsperaEngine

engine = ProsperaEngine()

print("Booting engine...")
engine.emit("BOOT")

print("Stopping engine...")
engine.emit("STOP")
