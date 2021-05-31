####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Project 3
# Due Date: 03 JUN 2021
####################################################

def main():
    movies = {}
    infile = open('tv_shows.txt', 'r')
    title = infile.readline().rstrip('\n')
    while title != '':
        movie_info  = [0, 0, 0, 0, 0, 0, 0]
        title = title.upper()
        movie_code = infile.readline().rstrip('\n')  # movie code
        first_yr = int(movie_code[0:2])
        if first_yr >= 0 and first_yr < 19:
            first_yr += 2000
        else:
            first_yr += 1900
        last_yr = int(movie_code[2:4]) + first_yr
        network = int(movie_code[4])
        if network == 1:
            networkName = 'ABC'
        elif network == 2:
            networkName = 'CBS'
        elif network == 3:
            networkName = 'NBC'
        elif network == 4:
            networkName = 'FOX'

        movie_info[0] = first_yr
        movie_info[1] = last_yr
        movie_info[2] = networkName
        movie_info[3] = infile.readline().rstrip('\n')  # star1
        movie_info[4] = infile.readline().rstrip('\n')  # star2
        movie_info[5] = infile.readline().rstrip('\n')  # star3
        movie_info[6] = infile.readline().rstrip('\n')  # star4

        movies[title] = movie_info

        title = str(infile.readline().rstrip('\n'))
    
    infile.close()

    for key in movies:
        print(f'\n{key} aired from {movies[key][0]} to {movies[key][1]} on {movies[key][2]}')
        print(f'It starred {movies[key][3]}, {movies[key][4]}, {movies[key][5]}, and {movies[key][6]}')

main()