import random
from pydub import AudioSegment
import copy
from data import *

def find_and_loot(heros_arr, original_story, talking_time, logs, hero_snapshots, collective_inventory):
    loot_heros = copy.deepcopy(heros_arr)
    item = random.choice(body_items)
    print(f'Found: {item}')
    collective_inventory.append(item)
    print(f'Inventory: {collective_inventory}')
    original_story = original_story.overlay(AudioSegment.from_mp3(fr'.\audio\items\{item}.mp3') + 8, position=talking_time)
    hero_snapshots.append((loot_heros, int(talking_time / 1000) * 5))
    talking_time += 2000
    for hero in loot_heros:
        if 'Hemostatic agent' in collective_inventory:
            collective_inventory.remove('Hemostatic agent')
            random_hero = random.choice(loot_heros)
            random_hero.hemostatic_agent += 1
            print(f'Prepared Hemostatic agent for the fight: {collective_inventory}.')
            hero_snapshots.append((loot_heros, int((talking_time / 1000) + 2) * 5))
        if 'Shotgun' in collective_inventory and (hero.weapon['name'] == 'Peacemaker'):
            if hero.weapon['name'] == 'Peacemaker':
                collective_inventory.append('Peacemaker')
            collective_inventory.remove('Shotgun')
            hero.weapon = {
                'name': 'Shotgun',
                'damage': [8, 14],
                'magazine': 6,
                'speed': 6000
            }
            print(f'Prepared Shotgun for the fight.')
            original_story = original_story.overlay(AudioSegment.from_mp3(fr'.\audio\travel\fight\shotgun reload.mp3') + 8, position=talking_time + 2000)
            logs.append(('- Prepared Shotgun for the fight.', int((talking_time / 1000) + 6) * 5))
            hero_snapshots.append((loot_heros, int((talking_time / 1000) + 6) * 5))
            talking_time += 2000
        if 'Leather armor' in collective_inventory and (hero.armor['wear'] == 'Old clothes' or hero.armor['wear'] == 'Leather jacket'):
            collective_inventory.remove('Leather armor')
            collective_inventory.append(hero.armor['wear'])
            hero.armor['wear'] = 'Leather armor'
            hero.armor['armor'] = 15
            print(f'Put on a Leather armor: {collective_inventory}.')
            original_story = original_story.overlay(AudioSegment.from_mp3(fr'.\audio\leather_armor_suit.mp3') + 8, position=talking_time)
            logs.append(('- Put on a Leather armor.', int((talking_time / 1000) + 6) * 5))
            hero_snapshots.append((loot_heros, int((talking_time / 1000) + 6) * 5))
            talking_time += 2000
        if 'Leather jacket' in collective_inventory and hero.armor['wear'] == 'Old clothes':
            collective_inventory.remove('Leather jacket')
            collective_inventory.append(hero['wear'])
            hero.armor['wear'] = 'Leather jacket'
            hero.armor['armor'] = 8
            print(f'Put on a Leather jacket: {collective_inventory}.')
            original_story = original_story.overlay(AudioSegment.from_mp3(fr'.\audio\leather_jacket_suit.mp3') + 8, position=talking_time)
            logs.append(('- Put on a Leather jacket.', int((talking_time / 1000) + 6) * 5))
            hero_snapshots.append((loot_heros, int((talking_time / 1000) + 6) * 5))
            talking_time += 2000
    return loot_heros, original_story, talking_time, logs, hero_snapshots, collective_inventory