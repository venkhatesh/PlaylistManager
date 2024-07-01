class Song:
    def __init__(self, index, acousticness, class_, danceability, duration_ms, energy, id, instrumentalness, key, liveness, loudness, mode, num_bars, num_sections, num_segments, star_rating, tempo, time_signature, title, valence):
        self.index = index
        self.acousticness = acousticness
        self.class_ = class_
        self.danceability = danceability
        self.duration_ms = duration_ms
        self.energy = energy
        self.id = id
        self.instrumentalness = instrumentalness
        self.key = key
        self.liveness = liveness
        self.loudness = loudness
        self.mode = mode
        self.num_bars = num_bars
        self.num_sections = num_sections
        self.num_segments = num_segments
        self.star_rating = star_rating
        self.tempo = tempo
        self.time_signature = time_signature
        self.title = title
        self.valence = valence

    def to_dict(self):
        return {
            "index": self.index,
            "acousticness": self.acousticness,
            "class": self.class_,
            "danceability": self.danceability,
            "duration_ms": self.duration_ms,
            "energy": self.energy,
            "id": self.id,
            "instrumentalness": self.instrumentalness,
            "key": self.key,
            "liveness": self.liveness,
            "loudness": self.loudness,
            "mode": self.mode,
            "num_bars": self.num_bars,
            "num_sections": self.num_sections,
            "num_segments": self.num_segments,
            "star_rating": self.star_rating,
            "tempo": self.tempo,
            "time_signature": self.time_signature,
            "title": self.title,
            "valence": self.valence
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            index=data["index"],
            acousticness=data["acousticness"],
            class_=data["class"],
            danceability=data["danceability"],
            duration_ms=data["duration_ms"],
            energy=data["energy"],
            id=data["id"],
            instrumentalness=data["instrumentalness"],
            key=data["key"],
            liveness=data["liveness"],
            loudness=data["loudness"],
            mode=data["mode"],
            num_bars=data["num_bars"],
            num_sections=data["num_sections"],
            num_segments=data["num_segments"],
            star_rating=data["star_rating"],
            tempo=data["tempo"],
            time_signature=data["time_signature"],
            title=data["title"],
            valence=data["valence"]
        )
