import pgzrun

WIDTH=1000
HEIGHT=590

score = 0
gameover = False
enemies = []
bullets = []

galaga = Actor ("galaga")
for j in range(7):
    for i in range(8):
        bug = Actor ("bug")
        enemies.append(bug)
        enemies[-1].x = 50 + 70 * i
        enemies[-1].y = 50*j

galaga.pos = (500,525)

def draw():
    screen.fill("#060736")
    galaga.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    screen.draw.text(str(score),(20,20), fontsize=40)
    if gameover:
        screen.fill("#060736")
        screen.draw.text("GAME\nOVER",(175,50), fontsize=300)
        screen.draw.text("score= " + str(score),(350,500), fontsize=75)

def update():
    global score, gameover
    if keyboard.left:
        galaga.x=galaga.x-2
        if galaga.x <= 50:
            galaga.x=50
    if keyboard.right:
        galaga.x=galaga.x+2
        if galaga.x >= 950:
            galaga.x=950

    for bullet in bullets:
        bullet.y -= 10
    
    for enemy in enemies:
        for bullet in bullets:
            if enemy.colliderect(bullet):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score = score + 1

    for enemy in enemies:
        enemy.y += 1
        if enemy.y > 590:
            enemies.remove(enemy)
    if len(enemies) == 0:
        gameover = True

def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor ("bullet")
        bullets.append(bullet)
        bullets[-1].x = galaga.x-0.1
        bullets[-1].y = galaga.y-40

pgzrun.go()