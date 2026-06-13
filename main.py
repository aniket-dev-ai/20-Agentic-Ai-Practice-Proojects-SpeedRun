from faster_whisper import WhisperModel

model = WhisperModel(
    "turbo",
    device="cuda",
    compute_type="float16"
)

print("Loaded")