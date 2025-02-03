import pgzrun

WIDTH=1000
HEIGHT=590

enemies = []

galaga = Actor ("galaga")
for i in range(8):
    bug = Actor ("bug")
    enemies.append(bug)
    enemies[-1].x = 50 + 70 * i
    enemies[-1].y = 50

galaga.pos = (500,525)

def draw():
    screen.fill("#060736")
    galaga.draw()
    for enemy in enemies:
        enemy.draw()

def update():
    if keyboard.left:
        galaga.x=galaga.x-2
        if galaga.x <= 50:
            galaga.x=50
    if keyboard.right:
        galaga.x=galaga.x+2
        if galaga.x >= 950:
            galaga.x=950

pgzrun.go()