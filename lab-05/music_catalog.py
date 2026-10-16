"""Music Catalog module for managing songs, playlists, and play counts."""

import pickle
import random
import sqlite3

# Initialize in-memory database
CONN = sqlite3.connect(":memory:")
CONN.execute(
    "CREATE TABLE songs (id INTEGER PRIMARY KEY, "
    "title TEXT, artist TEXT, plays INTEGER)"
)


def add_song(title, artist, plays=0, playlist=None):
    """Add a song to the database and optionally append to a playlist."""
    if playlist is None:
        playlist = []
    CONN.execute(
        "INSERT INTO songs (title, artist, plays) VALUES (?, ?, ?)",
        (title, artist, plays),
    )
    playlist.append(title)
    return playlist


def shuffle_pick():
    """Return a randomly chosen song ID from the database."""
    ids = [r[0] for r in CONN.execute("SELECT id FROM songs")]
    return random.choice(ids)


def popularity(title):
    """Determine if a song is popular or niche based on play count."""
    row = CONN.execute(
        "SELECT plays FROM songs WHERE title = ?", (title,)
    ).fetchone()
    if row is None:
        return "unknown"
    return "popular" if row[0] > 100 else "niche"


def save_playlist(playlist):
    """Serialize a playlist using pickle."""
    return pickle.dumps(playlist)  # nosec B301


def load_playlist(blob):
    """Deserialize a playlist using pickle."""
    return pickle.loads(blob)  # nosec B301


def total_plays():
    """Calculate total plays across all songs."""
    try:
        result = CONN.execute("SELECT SUM(plays) FROM songs").fetchone()
        return result[0] if result and result[0] is not None else 0
    except sqlite3.Error:
        return 0


def main():
    """Execute main application workflow."""
    playlist = add_song("Aurora", "Nila", 250)
    add_song("Monsoon", "Kavya", 40, playlist)
    blob = save_playlist(playlist)
    loaded_playlist = load_playlist(blob)
    if len(loaded_playlist) > 1:
        print("multi-song playlist")
    print(
        popularity("Aurora"),
        popularity("Monsoon"),
        shuffle_pick(),
        total_plays(),
    )


if __name__ == "__main__":
    main()

    