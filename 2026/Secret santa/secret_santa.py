import random

def pull_from_hat(participants: list, excluded_pairs: dict = None) -> dict:
    if excluded_pairs is None:
        excluded_pairs = {}
    
    for name in participants:
        excluded_pairs.setdefault(name, [])

    gifters = [name for name in participants]
    receivers = [name for name in participants]

    paired = {}
    for name in gifters:
        other_names = [n for n in receivers if n != name and n not in excluded_pairs[name]]
        chosen = other_names[random.randrange(len(other_names))]
        paired[name] = chosen
        receivers.remove(chosen)

        print(f"{name:10} is gifting {chosen}")
        
def define_groups(my_list):
    random.shuffle(my_list)
    groups = []
    groups_index = 0
    item_count = 0
    groups.append([my_list[0]])
    
    for item in my_list:
        item_count += 1
        # make sure group size is at least 2
        if len(groups[groups_index]) == 1 or len(my_list) - item_count <= 1:
            groups[groups_index].append(item)
        # if allowed, each successive item has 50% change of joining group
        else:
            if random.randrange(2) == 0:
                groups[groups_index].append(item)
            else:
                groups_index += 1
                groups.append([item])
    
    return groups

def group_distributions(list, iterations):
    number_of_groups_count = {}
    [number_of_groups_count.setdefault(n, 0) for n in range(len(list) // 2 + 1)]

    for i in range(iterations):
        number_of_groups_count[len(define_groups(list))] += 1

    return number_of_groups_count



participants = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Gabriel", "Hannah", "Imogen", "Jamie"]

disallowed = {}
disallowed["Alice"] = ["Bob", "David"]
disallowed["Bob"]   = ["Alice", "David"]
disallowed["David"] = ["Alice", "Bob"]

iterations = 10000

distribution = group_distributions(participants, iterations)

for n in distribution:
    