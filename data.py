list_of_names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Charles', 'Joseph', 'Thomas',
                 'Daniel', 'Paul', 'Donald', 'George', 'Steven', 'Edward', 'Brian', 'Ronald', 'Anthony', 'Kevin',
                 'Jason', 'Matthew', 'Gary', 'Larry', 'Jeffrey', 'Frank', 'Scott', 'Eric', 'Andrew', 'Raymond']

list_of_surnames = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez',
                    'Martinez', 'Gonzalez', 'Wilson', 'Anderson', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee',
                    'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Robinson', 'Walker', 'Young', 'Allen', 'King',
                    'Torres', 'Hill', 'Green', 'Adams', 'Nelson', 'Baker', 'Mitchell', 'Carter', 'Roberts']

encounters = ['small tribe', 'several farmers', 'group of nomads',  'homeless people', 'hunting party', 'some scavengers',
              'old gas station', 'abandoned houses', 'ruined houses', 'ruined farm', 'burned farm', 'few cannibals',
              'group of slavers', 'several raiders', 'band of robbers', 'several gangsters', 'few mobsters',
              'band of rogues', 'band of marauders']
encounters_weights = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0)  #

encounters_peaceful = ['small tribe', 'several farmers', 'group of nomads', 'homeless people', 'hunting party',
                       'some scavengers', 'few outcasts', 'few hermits', 'some bootleggers', 'several prospectors',
                       'merchant with guards', 'small caravan']
encounters_places = ['old gas station', 'abandoned houses', 'ruined houses', 'ruined farm', 'burned farm']
encounters_fight = ['few cannibals', 'several raiders', 'group of slavers', 'band of robbers', 'several gangsters',
                    'few mobsters', 'band of rogues', 'band of marauders']

body_items = ['Hemostatic agent', 'Knife', 'Canned beans', 'Engine spark plugs', 'Wheel repair kit', 'Cabbage',
         'Jerked beef', 'Gun oil', 'Watch', 'Deck of cards', 'Cookies', 'Beer']
body_items_weights = (26, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6)

armors = [{'wear': 'Old clothes', 'armor': 0}, {'wear': 'Leather jacket', 'armor': 8}, {'wear': 'Leather armor', 'armor': 15}]
armors_weights = (85, 10, 5)
weapons = [{'name': 'Peacemaker', 'damage': [6, 12], 'magazine': 6, 'speed': 6000}, {'name': 'Shotgun', 'damage': [8, 14], 'magazine': 6, 'speed': 6000}]
weapons_weights = (80, 20)

travel_with_random_sounds = [r'.\audio\travel\travel with random sounds\coyote missed.mp3',
                             r'.\audio\travel\travel with random sounds\engine sounds weird.mp3',
                             r'.\audio\travel\travel with random sounds\lips are dry.mp3',
                             r'.\audio\travel\travel with random sounds\why did i agree to this.mp3',
                             r'.\audio\travel\travel with random sounds\this weapon hammer nails.mp3']

box_types = [r'.\audio\travel\meet places\cabinet near the wall.mp3',
             r'.\audio\travel\meet places\box near the window.mp3',
             r'.\audio\travel\meet places\table in the corner.mp3']

battle_music = [r'.\audio\travel\fight\fight music\fight music 1.mp3',
                r'.\audio\travel\fight\fight music\fight music 2.mp3',
                r'.\audio\travel\fight\fight music\fight music 3.mp3',
                r'.\audio\travel\fight\fight music\fight music 4.mp3',
                r'.\audio\travel\fight\fight music\fight music 5.mp3',
                r'.\audio\travel\fight\fight music\fight music 6.mp3',
                r'.\audio\travel\fight\fight music\fight music 7.mp3']

battle_cries = [r'.\audio\travel\fight\battle_cries\battle_cry_1.wav',
                r'.\audio\travel\fight\battle_cries\battle_cry_2.wav',
                r'.\audio\travel\fight\battle_cries\battle_cry_3.wav',
                r'.\audio\travel\fight\battle_cries\battle_cry_4.wav',
                r'.\audio\travel\fight\battle_cries\battle_cry_5.wav',
                r'.\audio\travel\fight\battle_cries\battle_cry_6.wav']

revolver_kills_enemy = [r'.\audio\travel\fight\revolver_shoot_and_hit1.mp3',
                        r'.\audio\travel\fight\revolver_shoot_and_hit2.mp3',
                        r'.\audio\travel\fight\revolver_shoot_and_hit3.mp3',
                        r'.\audio\travel\fight\revolver_shoot_and_hit4.mp3']

shotgun_kills_enemy = [r'.\audio\travel\fight\shotgun shoot and kill 1.mp3',
                       r'.\audio\travel\fight\shotgun shoot and kill 2.mp3',
                       r'.\audio\travel\fight\shotgun shoot and kill 3.mp3']

enemy_missed = [r'.\audio\travel\fight\enemy_shoot_miss\enemy_shoot_miss.mp3',
                r'.\audio\travel\fight\enemy_shoot_miss\enemy_shoot_miss1.mp3',
                r'.\audio\travel\fight\enemy_shoot_miss\enemy_shoot_miss2.mp3',
                r'.\audio\travel\fight\enemy_shoot_miss\enemy_shoot_miss_car.mp3',
                r'.\audio\travel\fight\enemy_shoot_miss\enemy_shoot_miss_car1.mp3',
                r'.\audio\travel\fight\enemy_shoot_miss\enemy_shoot_miss_wall.mp3',
                r'.\audio\travel\fight\enemy_shoot_miss\enemy_shoot_miss_wall1.mp3',
                r'.\audio\travel\fight\enemy_shoot_miss\enemy_shoot_miss_window.mp3',
                r'.\audio\travel\fight\enemy_shoot_miss\enemy_shoot_miss_window1.mp3']

everyone_killed = [r'.\audio\travel\fight\everyone killed\everyone_killed1.mp3',
                      r'.\audio\travel\fight\everyone killed\everyone_killed2.mp3',
                      r'.\audio\travel\fight\everyone killed\everyone_killed3.mp3',
                      r'.\audio\travel\fight\everyone killed\everyone_killed4.mp3',
                      r'.\audio\travel\fight\everyone killed\everyone_killed5.mp3']

background_image = ['wasteland.jpg', 'wasteland1.jpg', 'wasteland2.jpg', 'wasteland3.jpg', 'wasteland4.jpg']

avatars = ['avatar1.jpg', 'avatar2.jpg', 'avatar3.jpg', 'avatar4.jpg', 'avatar5.jpg', 'avatar6.jpg', 'avatar7.jpg',
           'avatar8.jpg', 'avatar9.jpg', 'avatar10.jpg', 'avatar11.jpg', 'avatar12.jpg', 'avatar13.jpg', 'avatar14.jpg',
           'avatar15.jpg', 'avatar16.jpg', 'avatar17.jpg', 'avatar18.jpg', 'avatar19.jpg', 'avatar20.jpg',
           'avatar21.jpg', 'avatar22.jpg', 'avatar23.jpg', 'avatar24.jpg', 'avatar25.jpg']

