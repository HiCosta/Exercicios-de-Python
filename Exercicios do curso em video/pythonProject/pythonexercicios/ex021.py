from pygame import mixer
mixer.init()
mixer.music.load('ex021.wav')
mixer.music.play()
enc = input('Tecle algo para encerrar: ')
