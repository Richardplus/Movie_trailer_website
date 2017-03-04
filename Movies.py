import media
import fresh_tomatoes

‘‘‘create some instances of movie class
6 movies created
’’’ 

# movie Titanic
Titanic = media.Movie("Titanic",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SY1000_CR0,0,671,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=cMVi953awHQ")

# movie the shawshak redemption
the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                                       "https://www.youtube.com/watch?v=K_tLp7T6U1c")

# movie forrest gump
forrest_gump = media.Movie("Forrest Gump",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=uPIEn0M8su0")

# movie Schindler's List
Schindler_s_List= media.Movie("Schindler's List",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                              "https://www.youtube.com/watch?v=M5FpB6qDGAE")

# movie fight club
Fight_club = media.Movie("Fight Club",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

# movie la la land
La_La_Land = media.Movie("La La Land",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_SY1000_SX675_AL_.jpg",
                "https://www.youtube.com/watch?v=0pdqf4P9MB8")

# group the movie instances
movies = [Titanic, the_shawshank_redemption, forrest_gump,
            Schindler_s_List, Fight_club, La_La_Land]

# call the open page method in fresh tomatoes
fresh_tomatoes.open_movies_page(movies)

