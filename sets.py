# Elimina los duplicados de una lista
# [1, 1, 2, 3, 4]  -> [1, 2, 4]

def remove_duplicates(some_list):
    wiout_duplicates = []
    for element in some_list:
        if element not in wiout_duplicates:
            wiout_duplicates.append(element)
    return wiout_duplicates

def run():
    random_list = [1, 1, 2, 2, 4]

    # eliminar repetidos con for
    print(remove_duplicates(random_list))

    # eliminar repetidos cono sets.
    random_list = set(random_list)
    print(random_list)

if __name__ == '__main__':
    run()
