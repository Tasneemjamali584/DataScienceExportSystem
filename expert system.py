
print("========================================")
print(" DATA SCIENCE CAREER EXPERT SYSTEM")
print("========================================")

print("\nAnswer each question with yes or no.")

excel = input("\n1. Do you like Excel and data analysis? ").lower()
python = input("2. Are you interested in Python programming? ").lower()
maths = input("3. Do you like mathematics and statistics? ").lower()
ai = input("4. Are you interested in AI and Machine Learning? ").lower()
bi = input("5. Do you like dashboards and data visualization? ").lower()

scores = {
    "Data Analyst": 0,
    "Data Scientist": 0,
    "Machine Learning Engineer": 0,
    "Business Intelligence Analyst": 0
}

# Knowledge Base: IF-THEN rules

if excel == "yes":
    scores["Data Analyst"] += 2
    scores["Business Intelligence Analyst"] += 1

if python == "yes":
    scores["Data Scientist"] += 2
    scores["Machine Learning Engineer"] += 2

if maths == "yes":
    scores["Data Scientist"] += 2
    scores["Machine Learning Engineer"] += 1

if ai == "yes":
    scores["Machine Learning Engineer"] += 3
    scores["Data Scientist"] += 1

if bi == "yes":
    scores["Business Intelligence Analyst"] += 3
    scores["Data Analyst"] += 1

# Inference Engine: Find the best matching career

best_score = max(scores.values())

if best_score == 0:
    print("\nRecommendation: Explore Data Science basics first.")
    print("Learn Excel, Python, statistics and visualization.")
else:
    print("\n========== EXPERT SYSTEM RESULT ==========")

    for career, score in scores.items():
        if score == best_score:
            print("\nRecommended Career:", career)
            print("Matching Score:", score)
            
            if career == "Data Analyst":
                print("Learning Path: Excel, SQL, Power BI and statistics.")

            elif career == "Data Scientist":
                print("Learning Path: Python, SQL, statistics and Machine Learning.")

            elif career == "Machine Learning Engineer":
                print("Learning Path: Python, mathematics, ML and model deployment.")

            elif career == "Business Intelligence Analyst":
                print("Learning Path: Excel, SQL, Power BI and dashboards.")

print("\nNote: This is a learning recommendation,")
print("not a final decision about your career.")
print("\nThank you for using the Expert System!")