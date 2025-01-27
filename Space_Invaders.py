import pgzrun

WIDTH=1000
HEIGHT=600

galaga = Actor ("galaga")
bug = Actor ("bug")

galaga.pos = (500,525)

def draw():
    screen.fill("#060736")
    galaga.draw()

pgzrun.go()