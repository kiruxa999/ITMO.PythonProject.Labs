import PythonLab5Module

print('Введите имя первого игрока')
igrok1 = PythonLab5Module.enter_name()
print('Введите имя второго игрока')
igrok2 = PythonLab5Module.enter_name()

score1 = 0
score2 = 0
PythonLab5Module.result_game(PythonLab5Module.thr_game(igrok1, score1),
                            PythonLab5Module.thr_game(igrok2, score2), igrok1, igrok2)
