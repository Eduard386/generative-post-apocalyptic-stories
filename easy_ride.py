from moviepy.editor import *
import numpy as np
import cv2
import os
from natsort import os_sorted
from travel import *
from fight import *
from meet import *

time = 0
all_logs = []
hero_snapshots = []
the_story = AudioSegment.empty()

collective_inventory = []
class Hero:
    def __init__(self):
        self.alive = True
        self.avatar = random.choice(avatars)
        self.name = f'{random.choice(list_of_names)} {random.choice(list_of_surnames)}'
        self.health = random.randint(28, 35)
        self.max_health = self.health
        self.weapon = random.choices(weapons, weights=weapons_weights, k=1)[0]
        self.armor = random.choices(armors, weights=armors_weights, k=1)[0]
        self.hemostatic_agent = random.randint(0, 2)

array_of_heros = [Hero() for i in range(3)]

hero_0_copy = copy.deepcopy(array_of_heros[0])
hero_1_copy = copy.deepcopy(array_of_heros[1])
hero_2_copy = copy.deepcopy(array_of_heros[2])

result_of_travel = travel(the_story, time)
encounter = result_of_travel[0]
the_story = result_of_travel[1]
time = result_of_travel[2]
all_logs = all_logs + result_of_travel[3]
print(f'time after travel {time}')
if encounter in encounters_fight:
    result_of_fight = fight(array_of_heros, time, encounter, collective_inventory)
    array_of_heros = copy.deepcopy(result_of_fight[0])
    the_story += result_of_fight[1]
    time = result_of_fight[2]
    all_logs = all_logs + result_of_fight[3]
    hero_snapshots = hero_snapshots + result_of_fight[4]
    collective_inventory = result_of_fight[5]
    print(f'time after fight {time}')
if (encounter in encounters_peaceful) or (encounter in encounters_places):
    result_of_encounter = meet(array_of_heros, encounter, the_story, time, collective_inventory)
    array_of_heros = copy.deepcopy(result_of_encounter[0])
    the_story = result_of_encounter[1]
    time = result_of_encounter[2]
    all_logs = all_logs + result_of_encounter[3]
    hero_snapshots = hero_snapshots + result_of_encounter[4]
    collective_inventory = result_of_encounter[5]
    print(f'time after encounter {time}')
heros_arr = copy.deepcopy(array_of_heros)
hero_snapshots.append((heros_arr, int(time / 1000) * 5))

print('final')
the_story.export(f"story_ends.mp3", format='mp3')
audio = AudioFileClip("story_ends.mp3")
random_background = random.choice(background_image)
image = ImageClip(fr'.\images\{random_background}')
video = image.set_audio(audio)
video.duration = audio.duration
video.fps = 5
video.write_videofile("adventure.mp4")


# take video with length of audio file, and save its frames
video = cv2.VideoCapture('adventure.mp4')
num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print(f'amount of frames: {num_frames}')


all_new_logs = []
sorted_all_logs = sorted(all_logs, key=lambda tup: tup[1])
size = len(sorted_all_logs)
print('All sorted logs length')
print(f'{len(sorted_all_logs)}')
print('All sorted logs')
print(sorted_all_logs)
print('All sorted ended')

for i in range(size):  # loop for length of initial logs array
    all_new_logs.append(sorted_all_logs[i])  # append current log to new array of logs
    second = sorted_all_logs[i][1]
    if i < size - 1:
        for j in range(sorted_all_logs[i+1][1] - sorted_all_logs[i][1] - 1):  # do it amount of times, between current and next log
            all_new_logs.append(('', second + 1))
            second += 1
length_till_first_log = all_new_logs[0][1]
for i in range(length_till_first_log):
    if length_till_first_log != 1:
        all_new_logs.insert(0, ('', length_till_first_log - 1))
        length_till_first_log -= 1
frames_to_add_at_the_end = num_frames - len(all_new_logs)
second = all_new_logs[-1][1]
for i in range(frames_to_add_at_the_end):
    all_new_logs.append(('', second + 1))
    second += 1

print(all_new_logs)
logs_to_print = []
print(f'length of array with logs: {len(all_new_logs)}')
assert len(all_new_logs) == num_frames


all_new_hero_snapshots = []
sorted_hero_snapshots = sorted(hero_snapshots, key=lambda tup: tup[1])
size = len(sorted_hero_snapshots)
print()
print(f'Sorted hero snapshots: {sorted_hero_snapshots}')
print()
for i in range(size):  # loop for length of initial logs array
    all_new_hero_snapshots.append(sorted_hero_snapshots[i])  # append current log to new array of logs
    second = sorted_hero_snapshots[i][1]
    if i < size - 1:
        for j in range(sorted_hero_snapshots[i+1][1] - sorted_hero_snapshots[i][1] - 1):  # do it amount of times, between current and next log
            all_new_hero_snapshots.append(('', second + 1))
            second += 1
length_till_first_snapshot = all_new_hero_snapshots[0][1]
for i in range(length_till_first_snapshot):
    if length_till_first_snapshot != 1:
        all_new_hero_snapshots.insert(0, ('', length_till_first_snapshot - 1))
        length_till_first_snapshot -= 1
frames_to_add_at_the_end = num_frames - len(all_new_hero_snapshots)
second = all_new_hero_snapshots[-1][1]
for i in range(frames_to_add_at_the_end):
    all_new_hero_snapshots.append(('', second + 1))
    second += 1
for i in range(len(all_new_hero_snapshots) - 1):  # if we have several logs at the same time
    if all_new_hero_snapshots[i][1] == all_new_hero_snapshots[i+1][1]:
        all_new_hero_snapshots[i+1] = (all_new_hero_snapshots[i+1][0], all_new_hero_snapshots[i][1] + 1)
print(all_new_hero_snapshots)
print(f'length of array hero snapshots: {len(all_new_hero_snapshots)}')
assert len(all_new_hero_snapshots) == num_frames


random_background_new = random.choice(background_image)

# write frames to the folder
height_max = 1070
height_at_start = 500
for i in range(len(all_new_logs)):
    frame_original = cv2.VideoCapture(fr"C:\Users\estepanyshchenko\Documents\script\game\images\{random_background_new}")
    ret, frame1 = frame_original.read()
    frame = frame1.copy()
    avatar_0 = cv2.VideoCapture(fr"C:\Users\estepanyshchenko\Documents\script\game\avatars\{array_of_heros[0].avatar}")
    avatar_1 = cv2.VideoCapture(fr"C:\Users\estepanyshchenko\Documents\script\game\avatars\{array_of_heros[1].avatar}")
    avatar_2 = cv2.VideoCapture(fr"C:\Users\estepanyshchenko\Documents\script\game\avatars\{array_of_heros[2].avatar}")
    ret0, frame_avatar_0 = avatar_0.read()
    ret1, frame_avatar_1 = avatar_1.read()
    ret2, frame_avatar_2 = avatar_2.read()
    resized_0 = cv2.resize(frame_avatar_0, (200, 200), interpolation=cv2.INTER_AREA)
    resized_1 = cv2.resize(frame_avatar_1, (200, 200), interpolation=cv2.INTER_AREA)
    resized_2 = cv2.resize(frame_avatar_2, (200, 200), interpolation=cv2.INTER_AREA)
    x_0_offset = 1290
    y_0_offset = 10
    x_1_offset = 1290
    y_1_offset = 220
    x_2_offset = 1290
    y_2_offset = 430
    frame[y_0_offset:y_0_offset + resized_0.shape[0], x_0_offset:x_0_offset + resized_0.shape[1]] = resized_0
    frame[y_1_offset:y_1_offset + resized_1.shape[0], x_1_offset:x_1_offset + resized_1.shape[1]] = resized_1
    frame[y_2_offset:y_2_offset + resized_2.shape[0], x_2_offset:x_2_offset + resized_2.shape[1]] = resized_2
    img_flip_ud = cv2.flip(frame, 0)

    # create black rectangle for logs
    shapes = np.zeros_like(img_flip_ud, np.uint8)
    cv2.rectangle(shapes, (10, 500), (620, 1070), (1, 1, 1), cv2.FILLED)  # main logs at the left
    cv2.rectangle(shapes, (1490, 870), (1910, 1070), (1, 1, 1), cv2.FILLED)  # black area for hero info
    cv2.rectangle(shapes, (1490, 660), (1910, 860), (1, 1, 1), cv2.FILLED)  # black area for hero info
    cv2.rectangle(shapes, (1490, 450), (1910, 650), (1, 1, 1), cv2.FILLED)  # black area for hero info
    img_flip_ud = img_flip_ud.copy()
    alpha = 0.2
    mask = shapes.astype(bool)
    img_flip_ud[mask] = cv2.addWeighted(img_flip_ud, alpha, shapes, 1 - alpha, 0)[mask]

    height = 520

    if isinstance(all_new_logs[i][0], list):
        for k in range(len(all_new_logs[i][0])):
            if len(logs_to_print) == 14:  # keep 14 lines of logs on the screen
                del logs_to_print[-1]
            logs_to_print.insert(0, all_new_logs[i][0][k])

    elif len(all_new_logs[i][0]) > 0:  # if there are any logs in current second
        if len(logs_to_print) == 14:  # keep 14 lines of logs on the screen
            del logs_to_print[-1]
        logs_to_print.insert(0, all_new_logs[i][0])

    for j in range(len(logs_to_print)):  # put all the logs from logs_to_print array on the frame
        cv2.putText(img_flip_ud, f'{logs_to_print[j]}', (25, height), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 235, 30), 2, cv2.LINE_AA, True)
        height += 40  # move every next log on 40 pixels higher
        if height >= height_max:
            height = height_at_start
    # show latest hero if nothing happens, update when happens

    obj = all_new_hero_snapshots[i][0]
    if isinstance(obj, list):
        cv2.putText(img_flip_ud, f'{obj[0].name}', (1575, 1035), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'Hit Points: {obj[0].health}/{obj[0].max_health}', (1505, 995), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'{obj[0].weapon["name"]} (Damage: {obj[0].weapon["damage"][0]}-{obj[0].weapon["damage"][1]})', (1505, 960), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'{obj[0].armor["wear"]} (AC: {obj[0].armor["armor"]})', (1505, 925), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'Hemostatic agent: {obj[0].hemostatic_agent}', (1505, 890), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)

        cv2.putText(img_flip_ud, f'{obj[1].name}', (1575, 825), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'Hit Points: {obj[1].health}/{obj[1].max_health}', (1505, 785), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'{obj[1].weapon["name"]} (Damage: {obj[1].weapon["damage"][0]}-{obj[1].weapon["damage"][1]})', (1505, 750), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'{obj[1].armor["wear"]} (AC: {obj[1].armor["armor"]})', (1505, 715), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'Hemostatic agent: {obj[1].hemostatic_agent}', (1505, 680), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)

        cv2.putText(img_flip_ud, f'{obj[2].name}', (1575, 615), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'Hit Points: {obj[2].health}/{obj[2].max_health}', (1505, 575), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'{obj[2].weapon["name"]} (Damage: {obj[2].weapon["damage"][0]}-{obj[2].weapon["damage"][1]})', (1505, 540), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'{obj[2].armor["wear"]} (AC: {obj[2].armor["armor"]})', (1505, 505), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'Hemostatic agent: {obj[2].hemostatic_agent}', (1505, 470), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)

        hero_0_copy = copy.deepcopy(obj[0])
        hero_1_copy = copy.deepcopy(obj[1])
        hero_2_copy = copy.deepcopy(obj[2])
    else:
        cv2.putText(img_flip_ud, f'{hero_0_copy.name}', (1575, 1035), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'Hit Points: {hero_0_copy.health}/{hero_0_copy.max_health}', (1505, 995), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'{hero_0_copy.weapon["name"]} (Damage: {hero_0_copy.weapon["damage"][0]}-{hero_0_copy.weapon["damage"][1]})', (1505, 960), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'{hero_0_copy.armor["wear"]} (AC: {hero_0_copy.armor["armor"]})', (1505, 925), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'Hemostatic agent: {hero_0_copy.hemostatic_agent}', (1505, 890), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)

        cv2.putText(img_flip_ud, f'{hero_1_copy.name}', (1575, 825), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'Hit Points: {hero_1_copy.health}/{hero_1_copy.max_health}', (1505, 785), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'{hero_1_copy.weapon["name"]} (Damage: {hero_1_copy.weapon["damage"][0]}-{hero_1_copy.weapon["damage"][1]})', (1505, 750), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'{hero_1_copy.armor["wear"]} (AC: {hero_1_copy.armor["armor"]})', (1505, 715), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'Hemostatic agent: {hero_1_copy.hemostatic_agent}', (1505, 680), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)

        cv2.putText(img_flip_ud, f'{hero_2_copy.name}', (1575, 615), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'Hit Points: {hero_2_copy.health}/{hero_2_copy.max_health}', (1505, 575), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'{hero_2_copy.weapon["name"]} (Damage: {hero_2_copy.weapon["damage"][0]}-{hero_2_copy.weapon["damage"][1]})', (1505, 540), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'{hero_2_copy.armor["wear"]} (AC: {hero_2_copy.armor["armor"]})', (1505, 505), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)
        cv2.putText(img_flip_ud, f'Hemostatic agent: {hero_2_copy.hemostatic_agent}', (1505, 470), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 235, 30), 2, cv2.LINE_AA, True)

    frame = cv2.flip(img_flip_ud, 0)
    cv2.imwrite(fr".\frames\frame{i+1}.jpg", frame)


# write video with logs, from frames
image_folder = 'frames'
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

video_file = 'video_from_frames.mp4'
fps = 5
image_size = (1920, 1080)
out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, image_size)

for filename in os_sorted(images):
    img = cv2.imread(os.path.join(image_folder, filename))
    out.write(img)

out.release()

# overlay video with audio
audio = AudioFileClip('story_ends.mp3')
video_clip = VideoFileClip('video_from_frames.mp4')
final_clip = video_clip.set_audio(audio)
final_clip.write_videofile("Final End video.mp4")
