import rumps

from app.clipboard import get_clipboard, is_youtube_url, watch_clipboard
from app.converter import convert_to_wav
from app.downloader import download_audio

class YTopus2wavBarApp(rumps.App):
    def __init__(self):
        super().__init__("YT")

        self.activate_item = rumps.MenuItem("Activate")
        self.activate_item.state = True

        self.menu = [
            "Download",
            None,
        ]

    @rumps.clicked("Download")
    def download(self, _):
        url = get_clipboard()

        if not is_youtube_url(url):
            rumps.alert("Fehler", "Kein YouTube-Link in der Zwischenablage.")
            return

        audio_file = download_audio(url)
        converted_file = convert_to_wav(audio_file)

if __name__ == "__main__":
    YTopus2wavBarApp().run()