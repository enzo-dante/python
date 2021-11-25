playlist = {
    "title": "Patagonia Bus",
    "creator": "Dante",
    "songs": [
        {
            "title": "title 1",
            "artist": "artist 1",
            "album": "album 1",
            "duration": 10.1
        },
        {
            "title": "title 2",
            "artist": "artist 2",
            "album": "album 2",
            "duration": 10.2
        },
        {
            "title": "title 3",
            "artist": "artist 3",
            "album": "album 3",
            "duration": 10.3
        },
    ]
}

total_duration = 0.0
for song in playlist["songs"]:
    total_duration += song["duration"]
    print(f"{song['title']} has a duration of {song['duration']}")
    
print(f"\nTotal duration of playlist: {round(total_duration, 2)}")
    