#!/usr/bin/env python3
import sys
podcast = ['Castle Super Beast', 'Fall of Civilizations','The Deprogram','Scam Goddess','For All Nerds Show']
print("BATTLE WITH THE SLIME")

your_dam = 0
print("While walking to the next town, you run into a slime. AHHHHHHHH! ")
print("""
        1: Hit it with a stick
        2: Throw a rock
        3: Run Away
        4: Stare
        """)
ans1 = input(">")
ans1 = ans1.strip()
while ans1 not in ("1","2","3","4"):
    print("Please select from the choices above")
    ans1 = input(">")

your_dam += int(ans1)

if your_dam == 3:
    print("Wow, you ran from a slime...")
    print("The End")
    sys.exit()

# Question 2
print("Its just standing there... ")
print("""
        1. Hit with a stick again
        2. Spray it with some water
        3. Check your bag for a spellbook
        4. Stare
        """)
ans2 = input(">")
ans2 = ans2.strip()
while ans2 not in ("1","2","3","4"):
    print("Please select from the choices above")
    ans2 = input(">")
your_dam += int(ans2)

# Question 3
print("OH! Maybe that worked! The slime seems...angry though...")
print("""
        1. Hit it one more time
        2. Chuck the spray bottle at it
        3. Cast Zettaflare
        4. Stare
        """)
ans3 = input(">")
ans3=ans3.strip()
while ans3 not in ("1","2","3","4"):
    print("Please select from the choices above")
    ans3 = input(">")
your_dam += int(ans3)

# Finale
if your_dam <= 4:
    print("The slime got annoyed with your hitting with a stick, so it exploded. RIP")
elif your_dam > 5 and your_dam < 12:
    print("Somehow, everything you did missed. The slime shook its head(?) and walked away. But hey, you tried.")
elif your_dam == 12:
    print("All you did was stare. The slime though your were weird and ran away. HOORAY")
