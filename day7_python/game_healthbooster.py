def main():
    print("Healing...")
    health = int(input("Enter the health from 1 to 100: "))
    check_healed = heal(health)
    if check_healed == "healed":
        print("Healing successful")
    elif check_healed == None:
        print("Player already at full health")

def heal(health):
    if health >= 100:
        return None
    else:
        return "healed" 

main()