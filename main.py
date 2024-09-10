import art
import game_data
import random



def get_data(comp):
    return f"{comp['name']}, a {comp['description']}, from {comp['country']}."
def get_follower(person):
    return person['follower_count']

print(art.logo)
cont=True
score = 0
while cont:
    data_lst = game_data.data
    comp1 = random.choice(data_lst)
    comp2 = random.choice(data_lst)
    if comp1==comp2:
        comp2=random.choice(data_lst)
    print(f"Compare A: {get_data(comp1)}")
    print(art.vs)
    print(f"Compare B: {get_data(comp2)} ")
    ans=input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n"*20)
    print(art.logo)
    if get_follower(comp1)>get_follower(comp2) and ans=='a' or get_follower(comp1)<get_follower(comp2) and ans=='b':
        score += 1
        print(f"You got it right. Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        cont=False
