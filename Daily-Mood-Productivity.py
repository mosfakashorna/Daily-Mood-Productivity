
mood_list = []
productivity_list = []


print("""
*****************************************
      Daily Mood & Productivity         
*****************************************
1. Log today's mood.
2. View mood history.
3. Average mood and productivity score.
4. Exit.
----------------------------------------          
""")

while True:

    choice = input("\nChoose an option: ")

    if choice == "1":
        mood = int(input("\nHow was your mood today? (1 - 10): "))
        productivity = int(input("How productive were you today? (1 - 10): "))

        mood_list.append(mood)
        productivity_list.append(productivity)

    elif choice == "2":
        if len(mood_list) == 0:
            print("No history.")
        else:
            for x in range(len(mood_list)):
                print(
                    f"Day {x + 1} Mood: {mood_list[x]} | Productivity: {productivity_list[x]} ")

    elif choice == "3":
        if len(mood_list) == 0:
            print("""
Record your mood & productivity evryday 
to find the average of mood & productivity.
                  """)
        else:
            total_mood = 0
            total_productivity = 0

            for mood in mood_list:
                total_mood += mood
                average_mood = total_mood / len(mood_list)

            for productive in productivity_list:
                total_productivity += productive
                average_productivity = total_productivity / \
                    len(productivity_list)

            print(f"Your average mood: {average_mood}")
            print(f"Your average productivity: {average_productivity}")

    elif choice == "4":
        print("\nHave a Wonderful rest of your day.")
        break

    else:
        print("""
Sorry, invalid entry. 
To record today's log mood or any other menu choose between (1 - 4).
              """)
