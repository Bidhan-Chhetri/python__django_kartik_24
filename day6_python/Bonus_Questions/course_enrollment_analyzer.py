enroll = {
        "arjun": ["math", "english", "science"],
        "bishal": ["nepali"],
        "chandni": ["math", "computer"],
        "deepa": ["science", "math"],
        "ekta": ["computer", "english"]
        }

count = 0
change_to_set = {}
for name in enroll.keys():
    if "math" in enroll[name] and "science" in enroll[name]:
        print(f'The student {name} studied both math and science.')
print()

for subjects in enroll.values():
    if len(subjects) == 1:
        print(f'Changing the data list of enroll to tuple {name} {tuple(subjects)}\n')
       
    
    change_to_set[name] = set(subjects)

print(f'The set of all the student is \n{change_to_set}\n') 

    
remove = enroll["ekta"].remove("english")
print(f"The removed verison of ekta is \n{enroll}\n")