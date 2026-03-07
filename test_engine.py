from engine_runtime import ProsperaEngine

engine = ProsperaEngine()

print("Booting engine...")
engine.emit("BOOT")

print("Stopping engine...")
engine.emit("STOP")
