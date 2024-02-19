import mp3

ipod = mp3.Player()

s1 = mp3.Music('Shoot Out', 'MONSTA X', 8)
s2 = mp3.Music('Alligator', 'MONSTA X', 2)
s3 = mp3.Music('FANTASIA', 'MONSTA X', 9)
s4 = mp3.Music('Love Killa', 'MONSTA X', 5)
s5 = mp3.Music('GAMBLER', 'MONSTA X', 1)

ipod.addSong(s1)
ipod.addSong(s2)
ipod.addSong(s3)
ipod.addSong(s4)
ipod.addSong(s5)

ipod.setIsLoop(False)
ipod.shuffle()
ipod.play()