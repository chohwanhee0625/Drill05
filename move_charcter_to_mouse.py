from pico2d import *
from random import *

open_canvas()

TUK_WHIDTH, TUK_HEIGHT = 1280, 860
open_canvas(TUK_WHIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            running = False

def draw_line(p1, p2):
    global t, x, y

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    t += 4
    x = (1 - t / 100) * x1 + t / 100 * x2
    y = (1 - t / 100) * y1 + t / 100 * y2



running = True
x, y = TUK_WHIDTH // 2, TUK_HEIGHT // 2
p_c = [x, y]
p_h = [randint(0, TUK_WHIDTH), randint(0, TUK_HEIGHT)]
frame = 0
t = 0

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WHIDTH // 2, TUK_HEIGHT // 2)

    if x == p_h[0] and y == p_h[1]:
        p_h[0], p_h[1] = randint(0, TUK_WHIDTH), randint(0, TUK_HEIGHT)
        p_c = [x, y]
        t = 0

    arrow.draw(p_h[0], p_h[1])

    if p_c[0] <= p_h[0]:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)  # right
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)  # left

    draw_line(p_c, p_h)

    update_canvas()
    handle_events()

    frame = (frame + 1) % 8

    delay(0.05)

close_canvas()
