from pico2d import *

from grass import Grass1, Grass2

from boy import Boy

import game_world
# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global running
    global world
    global boy

    running = True
    world = []

    grass = Grass1()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    grass = Grass2()
    game_world.add_object(grass, 2)


def update_world():
    game_world.update( )


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
