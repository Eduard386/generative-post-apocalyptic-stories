import random
from pydub import AudioSegment
import copy
from data import *

class Enemy:
    def __init__(self):
        self.health = random.randint(15, 20)
        self.weapon = random.choices(weapons, weights=weapons_weights, k=1)[0]
        self.armor = random.choices(armors, weights=armors_weights, k=1)[0]
        self.inventory = random.choices(body_items, weights=body_items_weights, k=2)

def fight(heros_arr, main_time, encounter, collective_inventory):
    local_logs = []
    local_hero_snapshots = []
    enemy_names = encounter.rsplit(None, 1)[-1]
    enemy_name = enemy_names.rstrip(enemy_names[-1])

    fight_heros = copy.deepcopy(heros_arr)
    initial_enemies = random.randint(4, 5)
    count_enemies = AudioSegment.from_mp3(fr'.\audio\travel\fight\count enemies\enemy_{initial_enemies}.mp3')
    array_of_enemies = [Enemy() for i in range(initial_enemies)]

    looted_items = []

    my_firing_point = random.choice(['bad', 'good'])
    enemies_firing_point = random.choice(['bad', 'good'])
    if (my_firing_point == 'bad' and enemies_firing_point == 'bad') or (my_firing_point == 'good' and enemies_firing_point == 'good'):
        my_shoot_probabilities = ['missed', 'hit']
        enemies_shoot_probabilities = ['missed', 'missed', 'missed', 'hit']
        position = AudioSegment.from_mp3(r'.\audio\travel\fight\positions\position_no_advantage.mp3')
    if my_firing_point == 'bad' and enemies_firing_point == 'good':
        my_shoot_probabilities = ['missed', 'missed', 'hit']
        enemies_shoot_probabilities = ['missed', 'missed', 'hit']
        position = AudioSegment.from_mp3(r'.\audio\travel\fight\positions\position_enemy_good_my_worse.mp3')
    if my_firing_point == 'good' and enemies_firing_point == 'bad':
        my_shoot_probabilities = ['missed', 'hit']
        enemies_shoot_probabilities = ['missed', 'missed', 'missed', 'hit']
        position = AudioSegment.from_mp3(r'.\audio\travel\fight\positions\position_my_good_enemy_worse.mp3')

    fight_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\fight.mp3')
    battle_sound = AudioSegment.from_mp3(random.choice(battle_music))
    fight_sound = fight_sound.overlay(count_enemies + 8, position=1000)
    print(f'You see {initial_enemies} {enemy_names}.')
    local_logs.append((f'- You see {initial_enemies} {enemy_names}.', int((main_time + 1000)/1000) * 5))
    fight_sound = fight_sound.overlay(position + 8, position=4000)
    print(f'Your firing point is {my_firing_point}.')
    local_logs.append((f'- Your firing point is {my_firing_point}.', int((main_time + 4000)/1000 + 1) * 5))
    print(f'{enemy_names.capitalize()} firing point is {enemies_firing_point}.')
    local_logs.append((f'- {enemy_names.capitalize()} firing point is {enemies_firing_point}.', int((main_time + 5000)/1000 + 1) * 5))

    shoot_time = 8000
    enemy_shoot_time = 11000
    enemy_shoot_speed = 6000

    while len(array_of_enemies) != 0 and shoot_time < 900000:
        battle_cry = AudioSegment.from_mp3(random.choice(battle_cries))
        fight_sound = fight_sound.overlay(battle_cry, position=shoot_time + 2000)

        for hero in fight_heros:
            if hero.alive:
                print(f"{hero.name} magazine before shoot is {hero.weapon['magazine']}")
                if hero.weapon['magazine'] != 0:
                    my_shoot = random.choice(my_shoot_probabilities)
                    if my_shoot == 'missed':
                        if hero.weapon['name'] == 'Peacemaker':
                            shoot_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\revolver_ready_and_shoot.mp3')
                        if hero.weapon['name'] == 'Shotgun':
                            shoot_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\shotgun shoot.mp3')
                        fight_sound = fight_sound.overlay(shoot_sound, position=shoot_time)
                        hero.weapon['magazine'] -= 1
                        print(f"{hero.name} magazine after shoot is {hero.weapon['magazine']}")
                        print(f'{hero.name} missed.')
                        local_logs.append((f'- {hero.name} missed.', int((main_time + shoot_time)/1000 + 5) * 5))
                        shoot_time += hero.weapon['speed']
                        shoot_time += int(hero.weapon['speed'] / len(fight_heros))
                    elif my_shoot == 'hit':
                        random_enemy = random.choice(array_of_enemies)
                        armor_saved = random.randint(1, 100)
                        if armor_saved < random_enemy.armor.get('armor'):
                            if hero.weapon['name'] == 'Peacemaker':
                                shoot_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\revolver_ready_and_shoot.mp3')
                            if hero.weapon['name'] == 'Shotgun':
                                shoot_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\shotgun shoot.mp3')
                            fight_sound = fight_sound.overlay(shoot_sound + 8, position=shoot_time)
                            print(f'{enemy_name.capitalize()} was hit by {hero.name}, but {random_enemy.armor.get("wear")} stopped the bullet.')
                            local_logs.append(([f'- {enemy_name.capitalize()} was hit by {hero.name},', f'but {random_enemy.armor.get("wear")} stopped the bullet.'], int((main_time + shoot_time) / 1000) * 5))
                        else:
                            potential_damage = hero.weapon['damage']
                            damage = random.randint(potential_damage[0], potential_damage[1])
                            corrected_damage = round(damage - (damage / 100 * random_enemy.armor.get("armor")))
                            random_enemy.health -= corrected_damage
                            hero.weapon['magazine'] -= 1
                            print(f"{hero.name} magazine after shoot is {hero.weapon['magazine']}")
                            if random_enemy.health > 0:
                                if hero.weapon['name'] == 'Peacemaker':
                                    shoot_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\revolver_ready_and_shoot.mp3')
                                if hero.weapon['name'] == 'Shotgun':
                                    shoot_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\shotgun shoot.mp3')
                                fight_sound = fight_sound.overlay(shoot_sound + 8, position=shoot_time)
                                print(f'{enemy_name.capitalize()} was hit by {hero.name} for {corrected_damage} hit points.')
                                local_logs.append(([f'- {enemy_name.capitalize()} was hit by {hero.name}', f'for {corrected_damage} hit points.'], int((main_time + shoot_time) / 1000 + 2) * 5))
                            if (random_enemy.health <= 5) and (random_enemy.health > 0) and ('Hemostatic agent' in random_enemy.inventory):
                                print(random_enemy.inventory)
                                random_enemy.inventory.remove('Hemostatic agent')
                                print(f"health of enemy before healing {random_enemy.health}")
                                random_enemy.health += random.randint(5, 10)
                                print(f"health of enemy after healing {random_enemy.health}")
                                local_logs.append((f'- {enemy_name.capitalize()} uses Hemostatic agent.', int((main_time + shoot_time) / 1000 + 2) * 5))
                            if random_enemy.health <= 0:
                                array_of_enemies.remove(random_enemy)
                                if hero.weapon['name'] == 'Peacemaker':
                                    shoot_sound = AudioSegment.from_mp3(random.choice(revolver_kills_enemy))
                                if hero.weapon['name'] == 'Shotgun':
                                    shoot_sound = AudioSegment.from_mp3(random.choice(shotgun_kills_enemy))
                                fight_sound = fight_sound.overlay(shoot_sound + 8, position=shoot_time)
                                print(f'{enemy_name.capitalize()} was hit for {corrected_damage} hit points by {hero.name}, and was killed. Left enemies: {len(array_of_enemies)}.')
                                local_logs.append(([f'- {enemy_name.capitalize()} was hit for {corrected_damage} hit points', f'by {hero.name}, and was killed.', f'Left enemies: {len(array_of_enemies)}.'], int((main_time + shoot_time) / 1000 + 2) * 5))

                                looted_items.extend(list(random_enemy.inventory))
                                looted_items.append(random_enemy.weapon.get('name'))
                                if random_enemy.weapon['name'] == 'Peacemaker':
                                    looted_items.append('.44 special ammo')
                                if random_enemy.weapon['name'] == 'Shotgun':
                                    looted_items.append('12-70 ammo')
                                if random_enemy.armor['wear'] != 'Old clothes':
                                    looted_items.append(random_enemy.armor['wear'])

                            if len(array_of_enemies) == 0:
                                cut_battle_sound = battle_sound[:shoot_time]
                                faded_battle_sound = cut_battle_sound.fade(to_gain=-120.0, end=shoot_time + 1000, duration=3000)
                                fight_sound = fight_sound.overlay(faded_battle_sound - 6, position=1000)

                                ambience_sound = AudioSegment.from_mp3(r'.\audio\travel\ambience peaceful and places.mp3') - 3
                                fight_sound = fight_sound.overlay(ambience_sound, position=shoot_time + 5)

                                print('You won this battle.')
                                heros_arr = copy.deepcopy(fight_heros)
                                local_hero_snapshots.append((heros_arr, int((main_time + shoot_time)/1000 + 11) * 5))
                                local_logs.append(('- You won this battle.', int((main_time + shoot_time)/1000 + 11) * 5))
                                #if hero.health < hero.max_health:
                                #    hero.health = hero.max_health
                                #    loot_sound = r'.\audio\travel\fight\win_heal_and_loot.mp3'
                                #    additional_time = 41500
                                #    heros_arr = copy.deepcopy(fight_heros)
                                #    local_hero_snapshots.append((heros_arr, int((main_time + shoot_time)/1000 + 25) * 5))
                                #elif hero.health == hero.max_health:
                                loot_sound = r'.\audio\travel\fight\win_and_loot.mp3'
                                additional_time = 24000
                                fight_sound = fight_sound.overlay(AudioSegment.from_mp3(loot_sound) + 8, position=shoot_time + 6500)

                                print(f'Found: {looted_items}')
                                collective_inventory += looted_items
                                print(f'Inventory: {collective_inventory}')
                                time_for_items = shoot_time + additional_time
                                print(f'initial time for items: {time_for_items}')
                                for item in looted_items:
                                    fight_sound = fight_sound.overlay(AudioSegment.from_mp3(fr'.\audio\items\{item}.mp3') + 8, position=time_for_items)
                                    local_logs.append(([f'- {item} has been added to your', 'inventory.'], int((main_time + time_for_items)/1000) * 5))
                                    time_for_items += 2000
                                    print(f'time for items after each item: {time_for_items}')
                                for man in fight_heros:
                                    if ('Shotgun' in collective_inventory) and (man.weapon['name'] == 'Peacemaker'):
                                        collective_inventory.append('Peacemaker')
                                        collective_inventory.remove('Shotgun')
                                        man.weapon = {
                                            'name': 'Shotgun',
                                            'damage': [8, 14],
                                            'magazine': 6,
                                            'speed': 6000
                                        }
                                        print(f'{man.name} prepared Shotgun for the fight.')
                                        fight_sound = fight_sound.overlay(AudioSegment.from_mp3(fr'.\audio\travel\fight\shotgun reload.mp3') + 8, position=time_for_items + 2)
                                        local_logs.append((f'- {man.name} prepared Shotgun for the fight.', int((main_time + time_for_items)/1000 + 6) * 5))
                                        heros_arr = copy.deepcopy(fight_heros)
                                        local_hero_snapshots.append((heros_arr, int((main_time + time_for_items)/1000 + 6) * 5))
                                        time_for_items += 2000
                                        print(f'time for items after shotgun: {time_for_items}')
                                    if ('Leather jacket' in collective_inventory) and man.armor['wear'] == 'Old clothes':
                                        collective_inventory.remove('Leather jacket')
                                        collective_inventory.append(man.armor['wear'])
                                        man.armor['wear'] = 'Leather jacket'
                                        man.armor['armor'] = 8
                                        fight_sound = fight_sound.overlay(AudioSegment.from_mp3(fr'.\audio\leather_jacket_suit.mp3') + 8, position=time_for_items)
                                        print(f'{man.name} puts on a Leather jacket: {collective_inventory}.')
                                        local_logs.append((f'- {man.name} puts on a Leather jacket.', int((main_time + time_for_items)/1000 + 6) * 5))
                                        heros_arr = copy.deepcopy(fight_heros)
                                        local_hero_snapshots.append((heros_arr, int((main_time + time_for_items)/1000 + 6) * 5))
                                        time_for_items += 2000
                                        print(f'time for items after leather jacket: {time_for_items}')
                                    if ('Leather armor' in collective_inventory) and (man.armor['wear'] == 'Old clothes' or man.armor['wear'] == 'Leather jacket'):
                                        collective_inventory.remove('Leather armor')
                                        collective_inventory.append(man.armor['wear'])
                                        man.armor['wear'] = 'Leather armor'
                                        man.armor['armor'] = 15
                                        fight_sound = fight_sound.overlay(AudioSegment.from_mp3(fr'.\audio\leather_armor_suit.mp3') + 8, position=time_for_items)
                                        print(f'{man.name} put on a Leather armor: {collective_inventory}.')
                                        local_logs.append((f'- {man.name} puts on a Leather armor.', int((main_time + time_for_items)/1000 + 6) * 5))
                                        heros_arr = copy.deepcopy(fight_heros)
                                        local_hero_snapshots.append((heros_arr, int((main_time + time_for_items)/1000 + 6) * 5))
                                        time_for_items += 2000
                                        print(f'time for items after leather armor: {time_for_items}')
                                    for i in range(10):
                                        if 'Hemostatic agent' in collective_inventory:
                                            collective_inventory.remove('Hemostatic agent')
                                            random_hero = random.choice(fight_heros)
                                            random_hero.hemostatic_agent += 1
                                            print(f'{random_hero.name} prepared Hemostatic agent for the fight: {collective_inventory}.')
                                            local_logs.append(([f'- {random_hero.name} prepared', 'Hemostatic agent for the fight'], int((main_time + time_for_items)/1000 + 7) * 5))
                                            heros_arr = copy.deepcopy(fight_heros)
                                            local_hero_snapshots.append((heros_arr, int((main_time + time_for_items)/1000 + 7) * 5))
                                heros_arr = copy.deepcopy(fight_heros)
                                local_hero_snapshots.append((heros_arr, int((main_time + time_for_items) / 1000 + 4) * 5))
                                fight_sound = fight_sound.overlay(AudioSegment.from_mp3(r'.\audio\travel\fight\move_away.mp3'), position=time_for_items)
                                print(f'time for items at the end: {time_for_items}')

                                end_time = time_for_items + 12000  # 12000 is time for move_away.mp3, 40000 worked fine with 27000 gap
                                print(f'end time: {time_for_items}')

                                fight_sound = fight_sound[:end_time]
                                story_time = main_time + end_time
                                print(f'story time: {time_for_items}')

                                #story += fight_sound
                                return heros_arr, fight_sound, story_time, local_logs, local_hero_snapshots, collective_inventory

                        shoot_time += int(hero.weapon['speed'] / len(fight_heros))
                else:
                    if hero.weapon['name'] == 'Peacemaker':
                        reload_sound = fr'.\audio\travel\fight\revolver_reload.mp3'
                    if hero.weapon['name'] == 'Shotgun':
                        reload_sound = fr'.\audio\travel\fight\shotgun reload.mp3'
                    fight_sound = fight_sound.overlay(AudioSegment.from_mp3(reload_sound) + 8, position=shoot_time)
                    hero.weapon['magazine'] = 6
                    print(f'{hero.name} is reloading the gun...')
                    local_logs.append((f'- {hero.name} is reloading the gun...', int((main_time + shoot_time)/1000 + 10) * 5))
                    shoot_time += int(hero.weapon['speed'] / len(fight_heros))

        for i in range(len(array_of_enemies)):
            enemy_missed_or_hit = random.choice(enemies_shoot_probabilities)
            if enemy_missed_or_hit == 'missed':
                enemy_shoot_sound = AudioSegment.from_mp3(random.choice(enemy_missed))
                fight_sound = fight_sound.overlay(enemy_shoot_sound, position=enemy_shoot_time)
                print(f'{enemy_name.capitalize()} missed.')
                local_logs.append((f'- {enemy_name.capitalize()} missed.', int((main_time + enemy_shoot_time)/1000 + 1) * 5))
                enemy_shoot_time += int(enemy_shoot_speed / len(array_of_enemies))
            elif enemy_missed_or_hit == 'hit':
                random_hero = random.choice([d for d in fight_heros if d.alive])
                print(f'Enemy shooted at {random_hero.name} because he is alive')
                armor_saved = random.randint(1, 100)
                if armor_saved < random_hero.armor['armor']:
                    enemy_shoot_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\armor_stopped_the_bullet.mp3')
                    fight_sound = fight_sound.overlay(enemy_shoot_sound + 8, position=enemy_shoot_time)
                    print(f'{random_hero.name} was hit, but {random_hero.armor["wear"]} stopped the bullet.')
                    local_logs.append(([f'- {random_hero.name} was hit, but {random_hero.armor["wear"]}', 'stopped the bullet.'], int((main_time + enemy_shoot_time)/1000) * 5))
                    enemy_shoot_time += int(enemy_shoot_speed / len(array_of_enemies))
                else:
                    potential_damage = array_of_enemies[i].weapon['damage']
                    damage = random.randint(potential_damage[0], potential_damage[1])
                    corrected_damage = round(damage - (damage / 100 * random_hero.armor["armor"]))
                    random_hero.health -= corrected_damage
                    print(f'{random_hero.name} was hit for {corrected_damage} hit points. Health is {random_hero.health}.')
                    if random_hero.health >= 10:
                        enemy_shoot_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\i_been_shot.mp3')
                        fight_sound = fight_sound.overlay(enemy_shoot_sound + 8, position=enemy_shoot_time)
                        local_logs.append((f'- {random_hero.name} was hit for {corrected_damage} hit points.', int((main_time + enemy_shoot_time)/1000 + 1) * 5))
                        heros_arr = copy.deepcopy(fight_heros)
                        local_hero_snapshots.append((heros_arr, int((main_time + enemy_shoot_time)/1000 + 1) * 5))
                    if (0 < random_hero.health < 10) and random_hero.hemostatic_agent > 0:
                        enemy_shoot_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\i_been_shot.mp3')
                        fight_sound = fight_sound.overlay(enemy_shoot_sound + 8, position=enemy_shoot_time)
                        hemostatic_agent_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\using_hemostatic_agent.mp3')
                        fight_sound = fight_sound.overlay(hemostatic_agent_sound + 8, position=enemy_shoot_time + 2500)
                        local_logs.append((f'- {random_hero.name} was hit for {corrected_damage} hit points.', int((main_time + enemy_shoot_time)/1000 + 1) * 5))
                        heros_arr = copy.deepcopy(fight_heros)
                        local_hero_snapshots.append((heros_arr, int((main_time + enemy_shoot_time)/1000 + 1) * 5))
                        random_hero.hemostatic_agent -= 1
                        healing = random.randint(12, 20)
                        random_hero.health += healing
                        print(f'{random_hero.name} is using Hemostatic agent, it heals {healing} hit points. Health is {random_hero.health}.')
                        local_logs.append(([f'{random_hero.name} is using Hemostatic agent,', f'it heals {healing} hit points.'], int((main_time + enemy_shoot_time + 2500)/1000) * 5))
                        heros_arr = copy.deepcopy(fight_heros)
                        local_hero_snapshots.append((heros_arr, int((main_time + enemy_shoot_time + 2500)/1000) * 5))
                    if (0 < random_hero.health < 10) and random_hero.hemostatic_agent == 0:
                        enemy_shoot_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\i_been_shot.mp3')
                        fight_sound = fight_sound.overlay(enemy_shoot_sound + 8, position=enemy_shoot_time)
                        hemostatic_agent_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\no_hemostatic_agent.mp3')
                        fight_sound = fight_sound.overlay(hemostatic_agent_sound + 8, position=enemy_shoot_time + 3000)
                        print(f'{random_hero.name} cant find Hemostatic agent.')
                        local_logs.append((f'- {random_hero.name} was hit for {corrected_damage} hit points.', int((main_time + enemy_shoot_time)/1000 * 5)))
                        local_logs.append((f'- {random_hero.name} cant find Hemostatic agent.', int((main_time + enemy_shoot_time)/1000 + 1) * 5))
                        heros_arr = copy.deepcopy(fight_heros)
                        local_hero_snapshots.append((heros_arr, int((main_time + enemy_shoot_time)/1000) * 5))

                    enemy_shoot_time += 3000  # do I have to remove this line?

                    cut_battle_sound = battle_sound[:enemy_shoot_time]
                    faded_battle_sound = cut_battle_sound.fade(to_gain=-120.0, end=enemy_shoot_time + 3000, duration=3000)
                    fight_sound = fight_sound.overlay(faded_battle_sound - 6, position=1000)

                    if random_hero.health < 1:
                        random_hero.alive = False
                        enemy_shoot_sound = AudioSegment.from_mp3(r'.\audio\travel\fight\hero_shot_died.mp3')
                        fight_sound = fight_sound.overlay(enemy_shoot_sound + 10, position=enemy_shoot_time + 2000)
                        print(f'{random_hero.name} was killed.')
                        local_logs.append((f'- {random_hero.name} was hit for {corrected_damage} hit points.', int((main_time + enemy_shoot_time)/1000 + 1) * 5))
                        local_logs.append((f'- {random_hero.name} was killed.', int((main_time + enemy_shoot_time)/1000 + 4) * 5))

                    if (not fight_heros[0].alive) and (not fight_heros[1].alive) and (not fight_heros[2].alive):
                        heros_arr = copy.deepcopy(fight_heros)
                        local_hero_snapshots.append((heros_arr, int(((main_time + enemy_shoot_time)/1000 + 3) * 5)))
                        enemy_shoot_sound = AudioSegment.from_mp3(random.choice(everyone_killed))
                        fight_sound = fight_sound.overlay(enemy_shoot_sound + 10, position=enemy_shoot_time + 5000)

                        end_time = enemy_shoot_time + 30000
                        fight_sound = fight_sound[:end_time]
                        #story += fight_sound
                        story_time = main_time + end_time
                        print('')
                        return heros_arr, fight_sound, story_time, local_logs, local_hero_snapshots, collective_inventory
