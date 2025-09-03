movies = [
    ("the social network", 20000000),
    ("the fight club", 9000000),
    ("final destination", 4500000),
    ("fantastic 4", 379000000),
    ("superman", 365000000),
    ("Avengers: Endgame", 356000000),
    ("john wick", 200000000)
]
print("Do you want to add more movies? (yes/no)")
ans = input().strip().lower()
if ans == "yes":
    how_many = int(input("How many movies do you want to add? "))
    for i in range(how_many):
        print(f"Movie {i+1}:")
        title = input("Enter movie name: ")
        cost = int(input("Enter movie budget: "))
        movies.append((title, cost))
total = 0
for m in movies:
    total += m[1]
avg = total / len(movies)
print(f"\nAverage movie budget: ${avg}")
above = []
for m in movies:
    if m[1] > avg:
        gap = m[1] - avg
        above.append((m[0], gap))
        print(f"\n{m[0]} is above average by ${gap}")
print(f"\nTotal movies above average: {len(above)}")
