quiz_system = True

user_scores = {}
questions = {}

while quiz_system:
    print("\n==== Quiz System ====")
    print("1. Admin Login")
    print("2. User Login")
    print("3. View Highest Scores")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        admin_id = 4477
        pwd = 9876
        admin = int(input('Enter admin ID: '))
        admin_pwd = int(input('Enter password: '))
        if admin == admin_id and admin_pwd == pwd:
            print('Admin login successfully')

            while True:
                print("\n--- Admin Menu ---")
                print("1. Add Question")
                print("2. Modify Question")
                print("3. Delete Question")
                print("4. View All Questions")
                print("5. View All User Details")
                print("6. Logout")

                choice = input("Choose one option: ")

                if choice == "1":
                    tech = input("Enter Technology :")
                    q = input("Enter question: ")
                    op1 = input("Enter option A: ")
                    op2 = input("Enter option B: ")
                    op3 = input("Enter option C: ")
                    op4 = input("Enter option D: ")
                    a = input("Enter correct answer: ")

                    
                    if tech not in questions:
                        questions[tech] = []

                    questions[tech].append({"questions": f"{q} a){op1} b){op2} c){op3} d){op4}","answer": a})
                    print("Question Added successfully.")

                elif choice == "2":
                    tech = input("Enter technology: ")
                    if tech in questions and questions[tech]:

                        num = int(input("Enter question number to modify: ")) - 1
                        if 0 <= num < len(questions[tech]):
                            new_q = input("Enter new question: ")
                            op1 = input("Enter option A: ")
                            op2 = input("Enter option B: ")
                            op3 = input("Enter option C: ")
                            op4 = input("Enter option D: ")
                            new_a = input("Enter new answer: ")

                            questions[tech][num] = {"questions": f"{new_q} a){op1} b){op2} c){op3} d){op4}","answer": new_a}
                            print("Question modified successfully.")
                        else:
                            print("Invalid question number.")
                    else:
                        print("No questions available for this technology.")

                elif choice == "3":
                    tech = input("Enter technology: ")
                    if tech in questions and questions[tech]:
                        num = int(input("Enter question number to delete: ")) - 1
                        if 0 <= num < len(questions[tech]):
                            del questions[tech][num]
                            print("Deleted question successfully.")
                        else:
                            print("Invalid question number.")
                    else:
                        print("No questions to delete.")

                elif choice == "4":
                    tech = input("Enter technology: ")
                    if tech in questions:
                        for i, ques in enumerate(questions[tech], 1):
                            print(f"{i}. {ques['questions']}")

                    else:
                        print("Technology not found.")

                elif choice == "5":
                    if user_scores:
                        for user, details in user_scores.items():
                            print(f"\nUser: {user}")
                            print(f"Mobile: {details['mobile']}, Score: {details['score']}")
                    else:
                        print("*"*5, "Users can't be login","*"*5)

                elif choice == "6":
                    print("Logout .")
                    break

                else:
                    print("Choose correct option.")
        else:
            print("Invalid login.")

    elif ch == "2":
        user_name = input("Enter user name: ")
        mobile_no = input("Enter mobile number: ")
        if len(mobile_no) != 10 or not mobile_no.isdigit():
            print("Invalid mobile number.")
            continue
        print(f'Welcome {user_name}! Let\'s take the quiz.')
        
        

        tech = input("Choose technology : ")
        if tech in questions and questions[tech]:
            score = 0
            for q in questions[tech]:
                print("\n" + q["questions"])
                ans = input("Your answer: ")
                if ans == q["answer"]:
                    score += 1

            
            print(f"\nYour Score: {score}/{len(questions[tech])}")
            user_scores[user_name] = {"mobile": mobile_no,"score": score}
        else:
            print("Technology not found or no questions available.")

    elif ch == "3":
        if user_scores:
            sorted_users = sorted(user_scores.items(), key=lambda item: item[1]["score"], reverse=True)
            print("\nTop 3 Highest Scores:")
            for i, (user, details) in enumerate(sorted_users[:3], start=1):
                print(f"{i}. User: {user}, Score: {details['score']}, Mobile: {details['mobile']}")
        else:
            print("No user has taken the quiz yet.")

    elif ch == "4":
        print("Exiting")
        break

    else:
        print("Choose a correct option.")
