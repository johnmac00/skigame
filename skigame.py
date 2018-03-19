from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter")
        exit(1)

#how switching betwee scenes works
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


        current_scene.enter()

class Death(Scene):

    quips = [
        "You made a poor choice here, and thus don't leave the lake",
        "Bested once again by Whiteface",
        "The land of no consequences...has consequences"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])

class SnowDay(Scene):

    def enter(self):
        print(dedent(""""
            You wake up, and a fluffy white coating is spread beneath
            your window, as far as you can see. It is in fact, a snow day.
            A quick check of your phone will confirm it, will you check?
        """))

        action = input("check, or don't check: > ")

        if action == "check":
            print(dedent("""
                Confirmed, a text, it's a snow day! You call your friends
                and wrassle up a threesome, and now it's time to drive out to
                Lake Placid for the weekend, because this snow day was
                conveniently on a Friday!
            """))

            return 'travel'

        elif action == "don't check":
            print(dedent("""That's a bold move Sir, AWOL mayhaps! Well off
            you go, enjoy the Snow Day
            """))

            return 'travel'

        else:
            print('You\'ve broken Space-Time')
            return 'death'

class Travel(Scene):

    def enter(self):
        print(dedent(""""
            You three pile into a car and head out East on RTE 3.
            The weather is a little dicy but it's pushing 0900. Do you speed?
        """))

        speed = input("speed, or don't speed:> ")

        if speed == "speed":
            print("speeding in the winter, good luck on the snow, oh wait...")

            return 'death'

        elif speed == "don't speed":
            print("you've made the responsbile choice!")

            return 'ski'

        else:
            print("You\'ve broke Space Time")

            return 'death'

class Ski(Scene):

    def enter(self):
        print(dedent("""
            You hit the mountain safe and sound, and my goodness what
            a beautiful day to go skiing. As you're speeding down,
            you see a blue, green, or black, at a three way fork.
            Which route do you choose
        """))

        route = input("blue, black, or green: > ")

        if route == "blue":
            print('a strong conservative choie, you make it down ok')
            return 'bar'

        elif route == 'black':
            print(''''Way too dangerous, but ok. But wait, a tree, split second decision,
            do you go left (1), or right (2), at that tree!''')

            choice = f"{randint(1,2)}"
            right_choice = input('1 (left), or 2 (right)')
            guesses = 0

            if right_choice != choice:
                print("Hello random snowboarder!")
                return 'death'

            else:
                print('woo close call but you made it')
                return 'bar'

        else:
            print('Way too tame, you don\'t deserve this day')
            return 'death'

class Bar(Scene):

    def enter(self):
        print(dedent("""
            Well after a long day of skiing, you've earned the right to the
            time-honored tradition of a hard Lake Placid boozefest. God speed soldier.
        """))

        print(dedent(""""
            You start making the rounds, and stumble into a bar. After many hours of
            boozing, you leave the bar, but are faced with a three-way intersection.
            It's a little chilly, and you think you remember where your hotel was, but who knows.
            Do you go left (1), right (2), or straight (3)?
        """))

        good_dir = randint(1,3)
        guess = input('1, 2 or 3?> ')

        if int(guess) != good_dir:
            print(dedent("""
            You chose poorly buddy, and will freeze to death this night.

            """))
            return 'death'

        else:
            print(dedent("""
        Against all odds, you see the hotel in the distance on your street you
        chose. Good job friend.

        """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You wake up in a haze in a gutter behind the hotel, but you made it. Time to gather your friends, and drive home! Good Job")
        return 'finished'

class Map(object):

    scenes = {
        'death': Death(),
        'snowday': SnowDay(),
        'travel': Travel(),
        'ski': Ski(),
        'bar': Bar(),
        'finished': Finished(),
        }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('snowday')
a_game = Engine(a_map)
a_game.play()
