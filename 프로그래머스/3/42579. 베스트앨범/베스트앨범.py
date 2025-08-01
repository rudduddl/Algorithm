def solution(genres, plays):
    from collections import defaultdict
    
    genres_to_songs = defaultdict(list)
    genre_play_count = defaultdict(int)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genres_to_songs[genre].append((play,i))
        genre_play_count[genre] += play
    
    sorted_genres = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)
    
    answer = []
    
    for genre, _ in sorted_genres:
        songs = genres_to_songs[genre]
        sorted_songs = sorted(songs, key=lambda x: (-x[0], x[1]))
        answer.extend([song[1] for song in sorted_songs[:2]])
        
    
    
    return answer