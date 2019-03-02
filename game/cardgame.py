import random

#Probably need some kind of random seed

Clubs = ["Ac", "Kc", "Qc", "Jc", "10c ", "9c", "8c", "7c", "6c", "5c", "4c", "3c", "2c"];
Spades = ["As", "Ks", "Qs", "Js", "10s", "9s", "8s", "7s", "6s", "5s", "4s", "3s", "2s", "1s"];
Diamonds = ["Ad", "Kd", "Qd", "Jd", "10d", "9d", "8d", "7d", "6d", "5d", "4d", "3d", "2d", "1d"];
Hearts = ["Ah", "Kh", "Qh", "Jh", "10h", "9h", "8h", "7h", "6h", "5h", "4h", "3h", "2h", "1h"];

deck = [Clubs, Spades, Diamonds, Hearts];

def rungame():
    print("Welcome to our cool game");
    print("Time to play!")
    for i in range(1,5):
        draw();

def draw():
    draw = input("Enter any key to draw");
    print("You drew", deck[random.randint(1,4)-1][random.randint(1,13)-1]);
    
