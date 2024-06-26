import os
import re

from .downloader import Downloader

class Playlist:
    path_list: list
    name: str
    output_path: str

    def __init__(
        self,
        name: str,
        output_path: str):
        self.name = re.sub(r'[\\/*?:"<>|]', '', name)
        self.path_list = []
        self.output_path = output_path.__str__()

    def add_path(self, path):
        self.path_list.append(path.__str__().replace(self.output_path + "/", "../Apple Music/"))

    def save_to_file(self):
        playlist_path = os.path.join(self.output_path, "..", "Playlists")
        os.makedirs(playlist_path, exist_ok=True)
        with open(os.path.join(playlist_path, self.name + ".m3u"), 'w') as f:
            f.write('\n'.join(self.path_list) + "\n")
