import fire
def artist(name, artist_id, album):
    print(" Artist Info")
    return {
        "Artist": name,
        "Artist ID": artist_id,
        "Album": album
    }

def album(title, album_id, artist_id):
    print(" Album Info")
    return {
        "Album": title,
        "Album ID": album_id,
        "Artist ID": artist_id
    }
def track(title, track_id, album_id, artist_id):
    print(" Track Info")
    return {
        "Track": title,
        "Track ID": track_id,
        "Album ID": album_id,
        "Artist ID": artist_id
    }
if __name__ == "__main__":
    fire.Fire({
        'artist': artist,
        'album': album,
        'track': track  
    })
    # track("Song A", "T123", "A456", "AR789")