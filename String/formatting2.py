movies = ['Dhol','Bahubali','Jab tak hai jaan', 'Pk', 'Golmal2' ]
stars = ['🌟🌟🌟🌟', '🌟🌟🌟🌟','🌟🌟🌟','🌟🌟🌟','🌟🌟']
for movie, star in zip (movies, stars):
    print(f'{movie:<20},{star:>20}')