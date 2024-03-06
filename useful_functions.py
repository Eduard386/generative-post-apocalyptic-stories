from pydub import AudioSegment

def append_track(main_track, track_to_append, local_time_variable, end_time_seconds):
    main_track = main_track.overlay(AudioSegment.from_mp3(track_to_append) + 8, position=local_time_variable)
    local_time_variable += end_time_seconds
    return main_track, local_time_variable