import media
import fresh_tomatoes

inception = media.Movie('Inception',
                        'A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.',
                        'https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg',
                        'https://www.youtube.com/watch?v=8hP9D6kZseM')

matrix = media.Movie('The Matrix',
                     'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
                     'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg',
                     'https://www.youtube.com/watch?v=m8e-FF8MsqU')

school_of_rock = media.Movie('School of Rock',
                             'After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.',
                             'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                             'https://www.youtube.com/watch?v=XCwy6lW5Ixc')

godfather = media.Movie('The Godfather',
                        'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                        'https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg',
                        'https://www.youtube.com/watch?v=sY1S34973zA')

movies = [inception, matrix, school_of_rock, godfather]
print media.Movie.VALID_RATINGS
#fresh_tomatoes.open_movies_page(movies)
