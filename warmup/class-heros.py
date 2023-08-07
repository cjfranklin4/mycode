#!/usr/bin/env python3
import classinfo

heroes = classinfo.classinfo

def main():
    print('Part 1')
    print(f"{heroes['all'][2]['Name']}")

    print('\nPart 2')

    print(f"""My name is {heroes['all'][2]['Name']} and my spirit animal is {heroes['all'][2]['Spirit Animal']}.
My name is {heroes['all'][2]['Name']} and my skills are {heroes['all'][2]['Skill Level']}.
My name is {heroes['all'][2]['Name']} and my super power is {heroes['all'][2]['Super Power']}.""")

    print('\nPart 3')
    for hero in heroes["all"]:
        name = hero['Name']
        skill = hero['Skill Level'].lower()
        animal = hero['Spirit Animal'].lower()
        power = hero['Super Power'].lower()
        #print(name)
        print(f"{name}, a {skill} {animal} of a programmer, possesses a {power} factor for moonlighting as a superhero!\n")

if __name__ == "__main__":
    main()