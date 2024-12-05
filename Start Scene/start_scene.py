name = input("Name? ")
username_list = []
username_list.append(name)
username = username_list[0]

def welcome(welcoming):
    return f"Hi {username} vaknar i en främmande värld med huvudverk. {username} vaknar i en säng med en främmande tjej (Sara) som byter ut en  varm handduk på din panna. Sara blir förvånad att {username} vaknar och hälsar på han “Äntligen är du vaken, trodde du va död en sekund där” 1. “Vem e du?” 2. “Var e jag?” 3. Skrik!"

result = welcome(username)
print(result)