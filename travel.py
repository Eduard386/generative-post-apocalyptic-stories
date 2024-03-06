import random
from pydub import AudioSegment
from data import *
from useful_functions import append_track

def travel(story, main_time):
    local_logs = []
    encounter = random.choices(encounters, weights=encounters_weights, k=1)[0]
    local_time = 0
    travel_meet_sound = AudioSegment.from_mp3(r'.\audio\travel\travel.mp3')
    if (encounter in encounters_fight):
        answer = r'.\audio\travel\i_am_going_to_give_them_a_fight.mp3'
    if encounter in encounters_peaceful:
        answer = r'.\audio\travel\lets_meet_them.mp3'
    if encounter in encounters_places:
        answer = r'.\audio\travel\lets_see_what_we_can_find.mp3'
    local_time += 7000
    travel_meet_sound, local_time = append_track(travel_meet_sound, random.choice(travel_with_random_sounds), local_time, 15000)
    travel_meet_sound, local_time = append_track(travel_meet_sound, fr'.\audio\random_encounters\{encounter}.mp3', local_time, 8000)
    travel_meet_sound, local_time = append_track(travel_meet_sound, answer, local_time, 10000)
    print(f'You encounter {encounter}.')
    local_logs.append((f'- You encounter {encounter}.', int((main_time + local_time)/1000) * 5))
    travel_meet_sound = travel_meet_sound[:local_time]
    psychobilly = AudioSegment.from_mp3(r'.\audio\travel\travel music\psychobilly.mp3')
    cut_psychobilly_sound = psychobilly[:local_time]
    faded_psychobilly_sound = cut_psychobilly_sound.fade(to_gain=-120.0, end=local_time, duration=4000)
    travel_meet_sound = travel_meet_sound.overlay(faded_psychobilly_sound, position=0)
    story += travel_meet_sound
    story_time = main_time + local_time
    print(story_time)
    return encounter, story, story_time, local_logs

