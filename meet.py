from find_and_loot import find_and_loot
import copy
from data import *
from pydub import AudioSegment
import random
from useful_functions import append_track

def meet(heros_arr, encounter, story, main_time, collective_inventory):
    meet_heros = copy.deepcopy(heros_arr)
    local_logs = []
    local_hero_snapshots = []
    if encounter in encounters_peaceful:
        meet_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\fight.mp3')
        talking_time = 4000
        if encounter == 'small tribe':
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\hey there.mp3', talking_time, 2000)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\tribe with goat.mp3', talking_time, 11000)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\no thanks.mp3', talking_time, 5000)
        if encounter == 'several farmers':
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\hey there.mp3', talking_time, 2000)
            meet_sound, talking_time = append_track(meet_sound, random.choice([
                r'.\audio\travel\meet peaceful\farmer speech 1.mp3',
                r'.\audio\travel\meet peaceful\farmer speech 2.mp3',
                r'.\audio\travel\meet peaceful\farmer speech 3.mp3'
            ]), talking_time, 9000)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\sorry to hear that.mp3', talking_time, 2000)
        if encounter == 'group of nomads':
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\hey there.mp3', talking_time, 2000)
            meet_sound, talking_time = append_track(meet_sound, random.choice([
                r'.\audio\travel\meet peaceful\nomad speech 1.mp3',
                r'.\audio\travel\meet peaceful\nomad speech 2.mp3'
            ]), talking_time, 12000)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\i see good luck.mp3', talking_time, 3000)
        if encounter == 'homeless people':
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\hey there.mp3', talking_time, 2000)
            meet_sound, talking_time = append_track(meet_sound, random.choice([
                r'.\audio\travel\meet peaceful\homeless speech 1.mp3',
                r'.\audio\travel\meet peaceful\homeless speech 2.mp3',
                r'.\audio\travel\meet peaceful\homeless speech 3.mp3'
            ]), talking_time, 7000)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\sorry to hear that.mp3', talking_time, 2000)
        if encounter == 'hunting party':
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\hey there.mp3', talking_time, 2000)
            meet_sound, talking_time = append_track(meet_sound, random.choice([
                r'.\audio\travel\meet peaceful\hunting party speech 1.mp3',
                r'.\audio\travel\meet peaceful\hunting party speech 2.mp3'
            ]), talking_time, 5000)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\yeah sounds good.mp3', talking_time, 2000)
        if encounter == 'some scavengers':
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\hey there.mp3', talking_time, 2000)
            meet_sound, talking_time = append_track(meet_sound, random.choice([
                r'.\audio\travel\meet peaceful\scavenger speech 1.mp3',
                r'.\audio\travel\meet peaceful\scavenger speech 2.mp3'
            ]), talking_time, 5000)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\i see good luck.mp3', talking_time, 3000)

        array_of_questions = ['more weapons', 'hemostatic agent', 'broken - radio', 'broken - gas analyzer', 'broken - shotgun',
                              'broken - solar panel', 'broken - windmill', 'broken - cartridge machine']
        array_of_broken = ['broken - radio', 'broken - gas analyzer', 'broken - shotgun', 'broken - solar panel',
                           'broken - windmill', 'broken - cartridge machine']
        question = random.choice(array_of_questions)
        if question == 'more weapons':
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\we need more weapons.mp3', talking_time, 9000)
            if 'Peacemaker' not in collective_inventory:
                meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\sorry cant help.mp3', talking_time, 4000)
            if 'Peacemaker' in collective_inventory:
                collective_inventory.remove('Peacemaker')
                random_hero = random.choice(meet_heros)
                random_hero.hemostatic_agent += 1
                local_logs.append(('- Peacemaker was removed from inventory.', int((main_time + talking_time) / 1000) * 5))
                local_logs.append(('- You armed a farmer.', int((main_time + talking_time) / 1000) * 5))
                local_logs.append((['- Hemostatic agent was added to your', 'inventory.'], int((main_time + talking_time) / 1000) * 5))
                heros_arr = copy.deepcopy(meet_heros)
                local_hero_snapshots.append((heros_arr, int((main_time + talking_time) / 1000) * 5))
                meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\here you go.mp3', talking_time, 6000)
                meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\take this hemostatic agent.mp3', talking_time, 6000)
                meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\okay thanks.mp3', talking_time, 3000)
        if question == 'hemostatic agent':
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\share hemostatic agent.mp3', talking_time, 6000)
            for hero in meet_heros:
                if hero.hemostatic_agent == 0:
                    meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\sorry cant help.mp3', talking_time, 4000)
                if hero.hemostatic_agent > 0:
                    hero.hemostatic_agent -= 1
                    local_logs.append((['- Hemostatic agent was removed from your', 'inventory.'], int((main_time + talking_time) / 1000) * 5))
                    local_logs.append(('- You saved a human life.', int((main_time + talking_time) / 1000) * 5))
                    heros_arr = copy.deepcopy(meet_heros)
                    local_hero_snapshots.append((heros_arr, int((main_time + talking_time) / 1000) * 5))
                    meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\here you go.mp3', talking_time, 6000)
                    break
        if question in array_of_broken:
            meet_sound, talking_time = append_track(meet_sound, fr'.\audio\travel\meet peaceful\{question}.mp3', talking_time, 7000)
            choice = random.randint(1, 100)
            if choice < 26:
                meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet peaceful\sorry cant help.mp3', talking_time, 4000)
            if choice > 25:
                meet_sound, talking_time = append_track(meet_sound, fr'.\audio\steps 5 sec.mp3', talking_time, 5000)
                meet_sound, talking_time = append_track(meet_sound, fr'.\audio\travel\meet peaceful\repairing.mp3', talking_time, 20000)
                meet_sound, talking_time = append_track(meet_sound, fr'.\audio\travel\meet peaceful\looks better now.mp3', talking_time, 2000)
                meet_sound, talking_time = append_track(meet_sound, fr'.\audio\travel\meet peaceful\thanks for your help.mp3', talking_time, 2000)
                heros_arr = copy.deepcopy(meet_heros)
                local_hero_snapshots.append((heros_arr, int((main_time + talking_time) / 1000) * 5))
                meet_sound, talking_time = append_track(meet_sound, fr'.\audio\travel\meet peaceful\no problem take care.mp3', talking_time, 3000)
                meet_sound, talking_time = append_track(meet_sound, fr'.\audio\steps 5 sec.mp3', talking_time, 5000)

        ride_away = AudioSegment.from_mp3(r'.\audio\travel\meet peaceful\ride_away.mp3')
        meet_sound = meet_sound.overlay(ride_away, position=talking_time)
        end_time = talking_time + 3000
        meet_sound = meet_sound[:end_time]

        ambience_sound = AudioSegment.from_mp3(r'.\audio\travel\ambience peaceful and places.mp3') - 3
        if encounter == 'small tribe':
            ambience_sound = AudioSegment.from_mp3(r'.\audio\travel\meet peaceful\07 - Bread from the oven.mp3') - 3
        if encounter == 'several farmers':
            ambience_sound = AudioSegment.from_mp3(r'.\audio\travel\meet peaceful\01 - On the way to the fair.mp3') - 3
        if encounter == 'group of nomads':
            ambience_sound = AudioSegment.from_mp3(r".\audio\travel\meet peaceful\08 - Watering place in a no man's land.mp3") - 3

        cut_ambience_sound = ambience_sound[:end_time]
        faded_ambience_sound = cut_ambience_sound.fade(to_gain=-120.0, end=end_time, duration=4000)
        meet_sound = meet_sound.overlay(faded_ambience_sound, position=0)

        story += meet_sound
        story_time = main_time + end_time
        return heros_arr, story, story_time, local_logs, local_hero_snapshots, collective_inventory

    if encounter in encounters_places:
        talking_time = 4000
        meet_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\fight.mp3')
        choice = random.randint(1, 100)
        if choice < 51:
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\steps 5 sec.mp3', talking_time, 5000)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\open door.mp3', talking_time, 2000)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet places\nothing interesting move on.mp3', talking_time, 3000)
            local_logs.append((['- Nothing interesting found in the', f'{encounter}'], int((main_time + talking_time)/1000) * 5))
            print(f'Nothing interesting found in the {encounter}')
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\steps 5 sec.mp3', talking_time, 5000)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet places\start motorcycle.mp3', talking_time, 2500)
            meet_sound = meet_sound[:talking_time]

            ambience_sound = AudioSegment.from_mp3(r'.\audio\travel\ambience peaceful and places.mp3')
            cut_ambience_sound = ambience_sound[:talking_time]
            faded_ambience_sound = cut_ambience_sound.fade(to_gain=-120.0, end=talking_time, duration=4000)
            meet_sound = meet_sound.overlay(faded_ambience_sound, position=0)

            story += meet_sound
            story_time = main_time + talking_time
            return heros_arr, story, story_time, local_logs, local_hero_snapshots, collective_inventory
        else:
            amount_of_boxes = random.randint(1, 3)
            for box in range(amount_of_boxes):
                meet_sound, talking_time = append_track(meet_sound, random.choice(box_types), talking_time, 2500)
                meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet places\steps.mp3', talking_time, 3000)
                locked_or_opened = random.randint(1, 100)
                if locked_or_opened < 26:
                    meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet places\open.mp3', talking_time, 3000)
                    print(f'Box {box + 1} opened.')
                    local_logs.append((f'- Box {box + 1} opened.', int((main_time + talking_time)/1000) * 5))
                    empty_or_fulfilled = random.randint(1, 100)
                    if empty_or_fulfilled < 26:
                        meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet places\it is empty.mp3', talking_time, 1000)
                        print(f'Box {box + 1} empty.')
                        local_logs.append((f'- Box {box + 1} empty.', int((main_time + talking_time)/1000) * 5))
                    if empty_or_fulfilled > 25:
                        result_of_loot = find_and_loot(meet_heros, meet_sound, talking_time, local_logs, local_hero_snapshots, collective_inventory)
                        meet_heros = copy.deepcopy(result_of_loot[0])
                        meet_sound = result_of_loot[1]
                        talking_time = result_of_loot[2]
                        local_logs = local_logs + result_of_loot[3]
                        local_hero_snapshots = local_hero_snapshots + result_of_loot[4]
                        collective_inventory = result_of_loot[5]
                elif locked_or_opened > 25:
                    meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet places\locked up master key.mp3', talking_time, 7000)
                    print(f'Box {box + 1} closed. Trying to pick the lock...')
                    local_logs.append((f'- Box {box + 1} closed. Trying to pick the lock...', int((main_time + talking_time)/1000) * 5))
                    broken_or_opened = random.randint(1, 100)
                    if broken_or_opened < 26:
                        meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet places\broke the lock.mp3', talking_time, 2000)
                        print(f'You broke the lock of box {box + 1}.')
                        local_logs.append((f'- You broke the lock of box {box + 1}.', int((main_time + talking_time)/1000) * 5))
                    if broken_or_opened > 25:
                        meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet places\open.mp3', talking_time, 2500)
                        print(f'The lock of box {box + 1} was opened.')
                        local_logs.append((f'- The lock of box {box + 1} was opened.', int((main_time + talking_time)/1000) * 5))
                        heros_arr = copy.deepcopy(meet_heros)
                        local_hero_snapshots.append((heros_arr, int((main_time + talking_time + 1000)/1000 + 6) * 5))
                        empty_or_fulfilled = random.randint(1, 100)
                        if empty_or_fulfilled < 26:
                            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet places\it is empty.mp3', talking_time, 1000)
                            print(f'box {box + 1} empty.')
                            local_logs.append((f'- Box {box + 1} empty.', int((main_time + talking_time)/1000) * 5))
                        if empty_or_fulfilled > 25:
                            result_of_loot = find_and_loot(meet_heros, meet_sound, talking_time, local_logs, local_hero_snapshots, collective_inventory)
                            meet_heros = copy.deepcopy(result_of_loot[0])
                            meet_sound = result_of_loot[1]
                            talking_time = result_of_loot[2]
                            local_logs = local_logs + result_of_loot[3]
                            local_hero_snapshots = local_hero_snapshots + result_of_loot[4]
                            collective_inventory = result_of_loot[5]
            heros_arr = copy.deepcopy(meet_heros)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet places\nothing else here move on.mp3', talking_time, 3000)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\steps 5 sec.mp3', talking_time, 5000)
            meet_sound, talking_time = append_track(meet_sound, r'.\audio\travel\meet places\start motorcycle.mp3', talking_time, 2500)
            print(f'You leave {encounter}.')
            local_logs.append((f'- You leave {encounter}.', int((main_time + talking_time)/1000) * 5))
            meet_sound = meet_sound[:talking_time]

            ambience_sound = AudioSegment.from_mp3(r'.\audio\travel\ambience peaceful and places.mp3')
            cut_ambience_sound = ambience_sound[:talking_time]
            faded_ambience_sound = cut_ambience_sound.fade(to_gain=-120.0, end=talking_time, duration=4000)
            meet_sound = meet_sound.overlay(faded_ambience_sound, position=0)

            story += meet_sound
            story_time = main_time + talking_time
            return heros_arr, story, story_time, local_logs, local_hero_snapshots, collective_inventory

