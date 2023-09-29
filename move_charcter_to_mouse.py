from pico2d import *

open_canvas()

TUK_WHIDTH, TUK_HEIGHT = 1280, 860
open_canvas(TUK_WHIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            running = False
    pass


running = True
x, y = TUK_WHIDTH // 2, TUK_HEIGHT // 2
frame = 0

while (running):
    clear_canvas()

    tuk_ground.draw(TUK_WHIDTH // 2, TUK_HEIGHT // 2)
    
    character.clip_draw(frame * 100, 100, 100, 100, x, y)   # right

    # character.clip_draw(frame * 100, 0, 100, 100, x, y)   # left

    update_canvas()
    handle_events()


    frame = (frame + 1) % 8

    delay(0.05)

close_canvas()
