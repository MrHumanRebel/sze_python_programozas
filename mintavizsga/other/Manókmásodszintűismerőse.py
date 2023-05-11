#Az A , B , C , ..., Z betűk embereket jelölnek, a friends lista pedig megadja azokat párokat,
# akik ismerik egymást. Készítsünk programot, amely kiírja, hogy melyik embernek van a legtöbb
# olyan másodszintű ismerőse, aki nem elsőszintű ismerős! Elsőszintű ismerősöknek az ismerősöket,
# másodszintű ismerősöknek az ismerősök ismerőseit nevezzük. Holtverseny esetén elég egy ember nevét kiírni.
# A program ne csak a megadott friends listára működjön, hanem tetszőleges, ugyanilyen formátumú bemenetre is!
import itertools
friends = [ 'I-N', 'L-W', 'F-R', 'F-Z', 'B-D', 'L-Q', 'I-U', 'A-N', 'E-F', 'A-I',
 'S-T', 'B-S', 'B-E', 'F-P', 'D-V', 'C-V', 'J-S', 'G-I', 'A-C', 'N-X',
 'K-N', 'Q-Y', 'A-U', 'O-Z', 'S-U', 'E-L', 'B-V', 'Y-Z', 'H-O', 'D-U',
 'A-K', 'F-W', 'N-T', 'H-T', 'R-T']

people = {}
for pair in friends:
    a, b = pair.split('-')
    if a not in people:
        people[a] = set()
    if b not in people:
        people[b] = set()
    people[a].add(b)
    people[b].add(a)


def get_second_level_friends(name):
    second_level_friends = set()
    for friend in people[name]:
        for second_level_friend in people[friend]:
            if second_level_friend != name and second_level_friend not in people[name]:
                second_level_friends.add(second_level_friend)
    return second_level_friends

max_second_level_friends = 0
person_with_most_second_level_friends = None
for person in people:
    second_level_friends = get_second_level_friends(person)
    num_second_level_friends = len(second_level_friends)
    if num_second_level_friends > max_second_level_friends:
        max_second_level_friends = num_second_level_friends
        person_with_most_second_level_friends = person

print(person_with_most_second_level_friends)

