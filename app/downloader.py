from pathlib import Path
import yt_dlp

DOWNLOADS = Path.home() / "Downloads"

def download_audio(url):
    options = {
        "format": "bestaudio[acodec=opus]/bestaudio",
        "outtmpl": str(DOWNLOADS / "%(title)s.%(ext)s"),
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
    return Path(ydl.prepare_filename(info))