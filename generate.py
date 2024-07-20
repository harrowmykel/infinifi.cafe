import torchaudio
from audiocraft.models.musicgen import MusicGen
from audiocraft.data.audio import audio_write

MODEL_NAME = "facebook/musicgen-large"

print(f"getting {MODEL_NAME}...")

model = MusicGen.get_pretrained(MODEL_NAME)
descriptions = ["gentle lo-fi beats"]

print("model obtained. generating wav files...")

wav = model.generate(descriptions)

print(f"{len(wav)} generated.")

for idx, one_wav in enumerate(wav):
    # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
    audio_write(
        f"{idx}",
        one_wav.cpu(),
        model.sample_rate,
        strategy="loudness",
        loudness_compressor=True,
    )
