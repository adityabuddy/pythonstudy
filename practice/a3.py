import fire
class demo_app:
    def artists(self, artist_id=None, artist_name=None):
        print(" Artist Info")
        print(f"Artist ID: {artist_id}")
        print(f"Artist Name: {artist_name}")
        
        
    def albums(self, album_id=None, album_name=None, artist_id=None):
        print(" Album Info")
        print(f"Album ID: {album_id}")
        print(f"Album Name: {album_name}")
        print(f"Artist ID: {artist_id}")
        
    def tracks(self, track_id=None, track_name=None, album_id=None, artist_id=None):
        print(" Track Info")
        print(f"Track ID: {track_id}")
        print(f"Track Name: {track_name}")
        print(f"Album ID: {album_id}")
        print(f"Artist ID: {artist_id}")


if __name__ == "__main__":
    fire.Fire(demo_app)


















# class Album:
#     def info(self, album_id=None, album_name=None, artist_id=None, year=None):
#         print("=== Album Info ===")
#         print(f"Album ID: {album_id}")
#         print(f"Album Name: {album_name}")
#         print(f"Artist ID: {artist_id}")
#         print(f"Year: {year}")


# class Track:
#     def info(self, track_id=None, track_name=None, album_id=None, artist_id=None):
#         print("=== Track Info ===")
#         print(f"Track ID: {track_id}")
#         print(f"Track Name: {track_name}")
#         print(f"Album ID: {album_id}")
#         print(f"Artist ID: {artist_id}")


# if __name__ == "__main__":
#     fire.Fire({
#         "artist": Artist,
#         "album": Album,
#         "track": Track
#     })
