import PythonLab5Module

print('Введите имя первого игрока')
igrok1 = PythonLab5Module.enterName()
print('Введите имя второго игрока')
igrok2 = PythonLab5Module.enterName()

score1 = 0
score2 = 0
PythonLab5Module.resultGame(PythonLab5Module.thrGame(igrok1, score1), PythonLab5Module.thrGame(igrok2, score2), igrok1, igrok2)
