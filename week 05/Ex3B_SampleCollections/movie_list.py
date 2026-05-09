# Favorite movies

movies = ["life is beautiful", "lala land", "shutter island", ]
print (len(movies))

print(f"The list movies included my top {len(movies)} favorite movies")
print(movies)

#sorting

print(sorted(movies))
#displays in alphabetical order

movies.sort()
print(movies)
#sorted = temporary sorting
#.sort = permanent sorting

movies.append("avatar")
print(movies)
print(f"The list movies included my top {len(movies)} favorite movies")