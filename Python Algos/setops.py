#set union
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
            'Wait For Limit': ['rap', 'upbeat', 'romance'],
            'Stomping Cue': ['country', 'fiddle', 'party'],
            'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

new_song_data = {}

for key, val in song_data.items():
    song_tag_set = set(val)
    user_tag_set = set(user_tag_data[key])
    new_song_data[key] = song_tag_set | user_tag_set

print(new_song_data)

#intersection
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
            'Wait For Limit': ['rap', 'upbeat', 'romance'],
            'Stomping Cue': ['country', 'fiddle', 'party'],
            'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
            'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
            'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
            'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
            'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                    'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

tags_int = set(user_recent_songs['Retro Words']) & set(user_recent_songs['Lowkey Space'])

recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
        if tag in tags_int:
            if key not in user_recent_songs:
                recommended_songs[key] = val

print(recommended_songs)

#difference 

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
            'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
            'Stomping Cue': ['country', 'fiddle', 'party'],
            'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
            'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
            'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
            'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
            'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

tag_diff = set(user_liked_song["Back To Art"]) - set(user_disliked_song['Retro Words'])
recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
        if tag in tag_diff:
            if key not in user_liked_song:
                recommended_songs[key] = val

print(recommended_songs)

#symetric difference

user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                    'Stomping Cue': ['country', 'fiddle', 'party'],
                    'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                    'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                    'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                    'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                    'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_tags = set()
for key, val in user_song_history.items():
    for tag in val:
        user_tags.add(tag)
friend_tags = set()
for key, val in friend_song_history.items():
    for tag in val:
        friend_tags.add(tag)
unique_tags = set(user_tags) ^ set(friend_tags)
print(unique_tags)

# review on sets

music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

my_tags = frozenset({'pop', 'electronic', 'relaxing', 'slow', 'synth'})

frozen_tag_union = my_tags | set(music_tags)

regular_tag_intersect = set(music_tags) & my_tags

frozen_tag_difference = my_tags - set(music_tags)

regular_tag_sd = set(music_tags) ^ my_tags
