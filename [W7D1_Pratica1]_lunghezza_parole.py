input_list = ["pc", "coding", "kali", "beatrice", "epicode", "cybersecurity"]

def lunghezza_parola(input_list):
    lenght_list = []
    for input_list in input_list:
        lenght_list.append(len(input_list))
    return lenght_list

print(lunghezza_parola(input_list))