def mutate_string(string, position, character):
    # change immutable str into mutable list & then change list[position in list] to character 
    s_mutable = list(string)
    s_mutable[position] = character

    new_string = "".join(s_mutable)
    return new_string

def alt_mutate_string(string, position, character):
    new_string = string[:position] + character + string[position + 1:]
    return new_string

string = 'abracadabra'
position = 5
character = 'k'
result = mutate_string(string, position, character)
print(result)
alt_result = alt_mutate_string(string, position, character)
print(alt_result)