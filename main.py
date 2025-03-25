import time
import pygetwindow as gw
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

def get_spotify_window():
    windows = gw.getWindowsWithTitle("Spotify")
    return windows[0] if windows else None

def is_ad_playing():
    window = get_spotify_window()
    if window:
        return "Advertisement" in window.title
    return False

def mute_spotify(mute=True):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Active(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(1 if mute else 0)

def main():
    print("🎵 Spotify Ad Muter is running...")
    while True:
        if is_ad_playing():
            print("🔇 Ad detected! Muting Spotify...")
            mute_spotify(True)
            time.sleep(30)
            mute_spotify(False)
            print("🔊 Unmuted Spotify after ad.")
        time.sleep(5)

if __name__ == "__main__":
    main()
