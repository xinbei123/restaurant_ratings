"""Restaurant rating lister."""


# put your code here
file_open = open("scores.txt")

def restaurant_rating(file):
    rest_dict = {}

    for line in file_open:

        line = line.rstrip() 
        restaurant, rating = line.split(':')
        
        rest_dict[restaurant] = int(rating)

    for item, num in sorted(rest_dict.items()):
        print(f"{item} is rated at {num}")

restaurant_rating(file_open)