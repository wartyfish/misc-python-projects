import random

def pull_from_hat(participants: list, excluded_pairs: dict = None) -> dict:
    derangement_factor = random.randrange(1, len(participants))
    participants_deranged = []
    for i in range(len(participants)):
        j = (i + derangement_factor) % len(participants)
        print(participants[j])
    print(derangement_factor)
    print(participants_deranged)
        
def define_groups(my_list) -> list:
    random.shuffle(my_list)
    groups = []
    groups_index = 0
    item_count = 0
    groups.append([my_list[0]])
    
    for item in my_list:
        if item != my_list[0]:
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

def group_size_frequencies(list, iterations) -> dict:
    number_of_groups_count = {}
    [number_of_groups_count.setdefault(n, 0) for n in range(len(list) // 2 + 1)]

    for i in range(iterations):
        number_of_groups_count[len(define_groups(list))] += 1

    return number_of_groups_count

def print_distribution(my_list, iterations) -> None:
    distribution = group_size_frequencies(my_list, iterations)
    print(distribution)
    for n in distribution:
        print(f"Group size {n:2}: {"x"*int(round((int(distribution[n])/100)))}")




participants = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Gabriel", "Hannah", "Imogen", "Jamie", "Kate",
                "Liam", "Max", "Nick", "Olivia", "Peter", "Quentin", "Racheal", "Simon", "Tina", "Uma", "Velma", "Wilson",
                "Xanvier", "Yorik", "Zack"]

disallowed = {}
disallowed["Alice"] = ["Bob", "David"]
disallowed["Bob"]   = ["Alice", "David"]
disallowed["David"] = ["Alice", "Bob"]

group_size = 3
participants = participants[:group_size]

pull_from_hat(participants)

iterations = 10000
distribution = group_size_frequencies(participants, iterations)


