
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st

client_id = "kendi client id'n"
client_secret = "kendi client secreti'in"   

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))

emotion_to_keywords = {
    "sadness": ["sad", "lonely", "melancholy", "heartbreak", "tears", "blue", "lost", "goodbye"],
    "joy": ["happy", "celebration", "smile", "fun", "sunshine", "joyful", "excited", "cheerful", "good vibes"],
    "love": ["love", "romantic", "heart", "together", "passion", "affection", "crush", "soulmate", "forever"],
    "anger": ["angry", "rage", "revenge", "breakup", "mad", "frustration", "burn", "fight", "explode"],
    "fear": ["fear", "scared", "dark", "nightmare", "alone", "paranoid", "shiver", "creepy", "panic"],
    "surprise": ["surprise", "unexpected", "wow", "shock", "suddenly", "new", "discovery", "amazed", "epic"]
}
def recommend_songs(emotion_label, market="TR", per_keyword_limit=2, total_limit=5):
    keywords = emotion_to_keywords.get(emotion_label, ["music"])
    seen_track_ids = set()
    results = []

    for kw in keywords:
        res = sp.search(q=kw, type="track", market=market, limit=per_keyword_limit)
        tracks = res.get("tracks", {}).get("items", [])
        for track in tracks:
            track_id = track["id"]
            if track_id not in seen_track_ids:
                seen_track_ids.add(track_id)
                name = track["name"]
                artist = track["artists"][0]["name"]
                url = track["external_urls"]["spotify"]
                results.append(f"🎵 {name} – {artist} → [Dinle]({url})")
                if len(results) >= total_limit:
                    return results
    return results
