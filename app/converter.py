from pathlib import Path
import subprocess

FFMPEG = Path(__file__).parent.parent / "bin" / "ffmpeg"

def convert_to_wav(input_file):
    input_file = Path(input_file)
    output_file = input_file.with_suffix(".wav")

    subprocess.run(
        [
            str(FFMPEG),
            "-i",
            str(input_file),
            "-c:a",
            "pcm_s24le",
            str(output_file),
        ],
        check=True,
    )

    input_file.unlink()

    return output_file