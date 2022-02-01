import map, player

w = map.Map(3, 3, fill='🟩')
p = player.Player('🛸', w.world, '🟩')

x = 0
y = 0
while True:
    p.teleport(x,y)
    w.out()