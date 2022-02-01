import os, msvcrt, threading
import random

# local
import src.map, src.player


w = src.map.Map(3, 3, fill='🟦')

p = src.player.Player('🛸', w.world, '🟦')
e = src.player.Player('🚁', w.world, '🟦')

clear = lambda: os.system('cls')

# player
pS = 0.01

pX = 0
pY = 0
# enemy
eX = random.randint(0, len(w.world[pY])-1)
eY = random.randint(0, len(w.world)-1)


key = ''
def movement():
    global key, pX, pY

    while True:
        key = msvcrt.getch()
        
        if key == b'q':
            clear()
            print('The game has been stopped.')
            break

        if key == b'w':
            if pX != 0:
                pY -= 1
        
        if key == b's':
            if pY != len(w.world)-1:
                pY+=1
        
def main():
    global pX, pY, eX, eY, pS

    w.out()
    while True:

        if key == b'q':
            break
        
        if int(pX)>len(w.world[pY])-1:
            pX = 0
            
            pS += 0.0005

            eX = random.randint(0, len(w.world[pY])-1)
            eY = random.randint(0, len(w.world)-1)

        e.teleport(eX, eY)
        if (int(pX), pY) != (eX, eY): p.teleport(int(pX), pY)
        else: 
            clear()
            print('The game has been stopped. Press Q to exit.')
            break


        pX += pS

        w.out()
        clear()

if __name__ == '__main__':
    # load threads
    threading.Thread(target=movement).start()
    # load main
    main()