lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}
type(collection_of_coins)
type(lucky_number)
type(marks)
type(my_favourite_films)
type(name)
type(one_is_a_prime_number)
type(pi)
type(profile_info)
# і так далі...
for var in ['collection_of_coins', 'lucky_number', 'marks', 'my_favourite_films', 'name', 'one_is_a_prime_number', 'pi', 'profile_info']:
    print(var, type(globals()[var]))
sorted_variables = {
    "mutable": [collection_of_coins, marks, my_favourite_films],
    "immutable": [lucky_number, pi, one_is_a_prime_number, name, profile_info]
}

print(sorted_variables)

# write your code here
