from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Collapse(Scene):

    collapses = [
        "TMD (tyrannical mercurial destabilising-dust) takes root in all your waterpipes and they dissolve into a thousand ",
         "global warming reaches and then sits at a temperature at which, unbeknownst to all of humans, bricks start to vibrate into the audiosphere. One night, you hear yourself vibrate to ""death"".",
         "boom!"

    ]

    def enter(self):
        print(Collapse.collapses[randint(0, len(self.collapses)-1)])
        exit(1)

class Kali(Scene):

    end = "Kali twists a meridian line and the realms of man are collapsed into each other, bringint time to it's knees and triggering the fault line beneath your $@%$%&^"

    def enter(self):
        print(Kali.end)
        exit(1)

class Dirt(Scene):

    def enter(self):
        print(dedent("""
             TYHWB // this would be the opening section - where you start. lets begin with only two rooms.
             in this instance, you must complete the rooms sequentially to "win".
             """))

        action = input("> ")

        if action == "room one":
            print(dedent("""
                  TYHWB // what happens AFTER you choose ROOM ONE but BEFORE you enter it?
                  """))
            return 'room_one'

        elif action == "room two":
            print(dedent("""
                  TYHWB // what happens AFTER you choose ROOM TWO but BEFORE you enter it?
                  """))
            return 'room_two'

        else:
            print("try choosing \"room one\" or \"room two\"!")
            return 'dirt'

class RoomOne(Scene):

    def enter(self):
        print(dedent("""
              TYHWB // this is what you are faced with upon entering room one. let's say you have to either attach a copper pipe to the left fixture or the right...
              """))

        action = input("> ")

        if action == "left":
            print(dedent("""
                  TYHWB // attaching the pipe to the left fixture collapses the architecture
                  """))
            return 'collapse'

        elif action == "right":
            print(dedent("""
                  TYHWB // attaching the right lets you move to the next room.
                  """))
            return 'room_two'

        else:
            print("huh? maybe you mean \"left\" or \"right\"?")
            return "room_one"


class RoomTwo(Scene):

    def enter(self):
        print(dedent("""
              TYHWB // this is what you are faced with upon entering room two. let's say you have to either paint the cupboards red or green (( there is so much more we could do with this but let me just get this simple version working for you))...
              """))

        action = input("> ")

        if action == "red":
            print(dedent("""
                  TYHWB // red - there were redbugs in the paint. termination imminent
                  """))
            return 'collapse'

        elif action == "green":
            print(dedent("""
                  TYHWB // green - 
                  """))
            return 'kali'

        elif action == "turquoise":
            print(dedent("""
                  TYHWB // whaa?? this colour is perfect, you can go to room three. all we need to do is create room thrree...
                  """))
            return 'room_three'

        else:
            print("huh? maybe you mean \"red\" or \"green\"? or perhaps... you notice a turquoise quality in the leaded glass of the window...")
            return "room_two"

class Finished(Scene):

    def enter(self):
        print("You have fixed all the sadnesses in your architecture. You attain no enlightenment. Futility was within you all along.")
        return 'finished'

class Map(object):

    scenes = {
        'dirt': Dirt(),
        'room_one': RoomOne(),
        'room_two': RoomTwo(),
        'collapse': Collapse(),
        'kali': Kali(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('dirt')
a_game = Engine(a_map)
a_game.play()