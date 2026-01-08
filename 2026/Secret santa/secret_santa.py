import random

def derange_group(my_list: list) -> dict:
    derangement_factor = random.randrange(1, len(my_list))
    participants_deranged = []
    for i in range(len(my_list)):
        j = (i + derangement_factor) % len(my_list)
        participants_deranged.append(my_list[j])

    return dict(zip(my_list, participants_deranged))
        
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


###

def pull_from_hat(participants: list) -> dict:
    groups = define_groups(participants)
    draw = {}

    def merge_two_dicts(x, y):
        z = x.copy()
        z.update(y)
        return z

    for group in groups:
        group_paired = derange_group(define_groups(group))
        
        merge_two_dicts(draw, group_paired)

    return draw

###


participants = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Gabriel", "Hannah", "Imogen", "Jamie", "Kate",
                "Liam", "Max", "Nick", "Olivia", "Peter", "Quentin", "Racheal", "Simon", "Tina", "Uma", "Velma", "Wilson",
                "Xanvier", "Yorik", "Zack"]

disallowed = {}
disallowed["Alice"] = ["Bob", "David"]
disallowed["Bob"]   = ["Alice", "David"]
disallowed["David"] = ["Alice", "Bob"]

group_size = 10
participants = participants[:group_size]

print(pull_from_hat(participants))

