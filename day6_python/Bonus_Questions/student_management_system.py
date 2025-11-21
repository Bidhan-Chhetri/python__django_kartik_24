data = {
        101: ["reading", "cycling"],
        102: ["gaming"],
        103: ["swimming", "cycling"]
        }

count = 0

for id, hobby in data.items():
    if len(hobby) > 1:
        print(f"The student {id} of the student who have more than one hobby.")
    if "cycling" in hobby:
        print(f"The student id {id} of the student who have cycling hobby.")



unique_hobbies =  set(data[101]) | set(data[102]) | set(data[103])
print(f"The unique hobbies of the students {unique_hobbies}")