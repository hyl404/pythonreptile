import curses
import random

s = curses.initscr()
curses.curs_set(0)
sh,sw = s.getmaxyx()
w = curses.newwin(sh,sw,0,0)
w.keypad(1)
w.timeout(100)


snake_x=int(sw / 4)
snake_y=int(sh / 2)
snake = [
    [snake_y,snake_x],
    [snake_y,snake_x - 1],
    [snake_y,snake_x - 2],
]


food = [int(sh / 2),int(sw / 2)]
w.addch(food[0],food[1],curses.ACS_PI)

kr = curses.KEY_RIGHT
kl = curses.KEY_LEFT
ku = curses.KEY_UP
kd = curses.KEY_DOWN
key = kr
while True:
    next_key = w.getch()
    if next_key in [kr,kl,ku,kd]:
        if (key == kr and next_key != kl) or\
           (key == kl and next_key != kr) or\
           (key == ku and next_key != kd) or\
           (key == kd and next_key != ku):
           key = next_key

    if snake[0] in snake[1:] or snake[0][0] in [0,sh] or snake[0][1] in [0,sw]:
        curses.endwin()
        quit()

    new_head = [snake[0][0],snake[0][1]]
    if key == kl:
        new_head[1] -= 1
    if key == kr:
        new_head[1] += 1
    if key == ku:
        new_head[0] -= 1
    if key == kd:
        new_head[0] += 1
    snake.insert(0,new_head)

    if snake[0] == food:
        food =None
        while food is None:
            nf = [
                random.randint(1,sh - 1 ),
                random.randint(1,sw - 1),
                ]
            food = nf if nf not in snake else None
        w.addch(food[0],food[1],curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0],tail[1],' ')
    w.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD)
