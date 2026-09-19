import rumps
import threading

from app.clipboard import get_clipboard, is_youtube_url, watch_clipboard
from app.converter import convert_to_wav
from app.downloader import download_audio

class YTopus2wavBarApp(rumps.App):
    def __init__(self):
        super().__init__("YT")

        self.activate_notification = rumps.MenuItem("Activate Notifications")
        self.activate_notification.state = True

        self.menu = [
            self.activate_notification,
            "Download",
            None,
        ]

    def start_watch_thread(self):
        thread = threading.Thread(target=watch_clipboard, args=(self.download_notification,), daemon=True)
        thread.start()

    def download_notification(self, url):
        if self.activate_notification.state == True:
            rumps.notification(
                title="YouTube URL gefunden",
                subtitle="",
                message="Datei herunterladen?",
                action_button="download",
                data={"url": url},
                sound= False
            )

    @rumps.clicked("Activate Notifications")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.notifications
    def notification_start_download(self, info):
        url = info.get("url")
        if url:
            audio_file = download_audio(url)
            converted_file = convert_to_wav(audio_file)

    @rumps.clicked("Download")
    def download(self, _):
        url = get_clipboard()

        if not is_youtube_url(url):
            rumps.alert("Fehler", "Kein YouTube-Link in der Zwischenablage.")
            return

        audio_file = download_audio(url)
        converted_file = convert_to_wav(audio_file)

if __name__ == "__main__":
    app = YTopus2wavBarApp()
    app.start_watch_thread()
    app.run()