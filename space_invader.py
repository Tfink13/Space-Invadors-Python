# I think this is just an escape from an empty function
from sys import exit
# will randomize the strings or numbers based on their index
from random import randint
# when using triple quotes it will strip leading white-space from the beginning
from textwrap import dedent



class Scene(object):

    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self): # play function is where all the switching between rooms is going to happen
        # creating a variable current scene and setting it to whatever is passed in as the opening scene
        current_scene = self.scene_map.opening_scene()
        #
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            current_scene.enter()

class Death(object):
    # creating a dictionary of different text options after you die
    diff_deaths = [
                "You died, You kinda suck at this.",
                "Your Mom would be proud... if she were smarter.",
                "Such a luser.",
                "I have a small puppy that's better at this.",
                "You're worse than your Dad's jokes.",
    ]

    def enter(self):
            print(Death.quips[randint(0, len(self.quips)-1)])
            exit(1)

class Central_Corridor(Scene):

    def enter(self):
        # i am just creating my text that i want to display once i get to this room
        print("""The Gothons of Planet Percel #25 have invaeded your ship and destroyed your entire crew. You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pod.

        You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown custom flowing around his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you.""")

        action = input("> ")

        if action == 'shoot!':
            print(dedent("""
            Quick on the draw you yank out your blaster and fire it at the Gothon. His clown costum is flowing and moving around his body, which throws off your aim. Your laser hits his costum but misses him entirely. This completely ruins his brand new costum his mother bought him. Which makes hi, fly into an insane rage and blast you repeatedly in the face until you are daed. Then he eats you."""))

        return 'death'
class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(object):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
