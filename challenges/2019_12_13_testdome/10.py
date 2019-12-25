def find_all_hobbyists(hobby, hobbies):
    return [i for i in hobbies if hobby in hobbies[i]] 
    
hobbies = { 
    "Steve": ['Fashion', 'Piano', 'Reading'],
    "Patty": ['Drama', 'Magic', 'Pets'],
    "Chad": ['Puzzles', 'Pets', 'Yoga']
}

print(find_all_hobbyists('Yoga', hobbies))