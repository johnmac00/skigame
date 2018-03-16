from sys import exit
from random import randint
from textwrap import dedent

class Map(object):

    scenes = {
        'death': Death(),
        'travel': Travel(),
        'ski': Ski(),
        'restaurant': Restaurant(),
        'bar': Bar(),
        'hotel': Hotel()
        'finished': Finished(),
        }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


#how switching betwee scenes works
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene
        last_scene = self.scene_map.next_scene('finished')

    while current != last_scene:
        next_scene_name = current_scene.enter()
        current_scene = self.scene_map.next_scene(next_scene_name)

    current_scene.enter()

class Scene(object):

    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter")
        exit(1)

class Death(Scene):

    quips = [
        "You made a poor choice here, and thus don't leave the lake",
        "Bested once again by Whiteface",
        "The land of no consequences...has consequences"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])

class Travel(Scene):

class Ski(Scene):

class Restaurant(Scene):

class Bar(Scene):

class Hotel(Scene):

class Finished(Scene):

    def enter(self):
        print("You Won! Good Job")
        return 'finished'

a_map = Map('tavel')
a_game = Engine(a_map)
a_game.play()
