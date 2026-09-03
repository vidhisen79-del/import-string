# ==========================================
# Project 4: The General Knowledge Quiz
# Architecture: IPOS + Question Block Micro-Architecture
# Standard: 'Above the API' - All Checks Included
# ==========================================

# --- State Management and the Score Vault ---
# Type Integrity + State Initialization
score = 0
storage = []
total = 5

print("=== The Cognitive Engine: Engineering The Testing Effect ===")
name = input("Enter your name: ").strip()
print(f"\nWelcome {name}! Starting Retrieval Practice...\n")

# --- Synthesis: The Question Block Micro-Architecture ---

# BLOCK 1: Capital Question
# Step 1: Ask & Capture
raw_q1 = input("Q1. What is the capital of France? ")
# Step 2: Sanitize - Data Normalization + Whitespace Audit
q1 = raw_q1.strip().lower()
# Step 3: Evaluate - Booleans Power the Backend (==)
# Step 4: Execute - If-Else Gate
if q1 == "paris":  # Operator: Equality
    score += 1
    storage.append("Q1-Correct")
    print(f"✅ Correct! Score: {score:>2}/{total}")
else:
    # Sustaining State - else block me score pe koi operation nahi
    print(f"❌ Wrong! Correct is Paris. Score: {score:>2}/{total}")

# BLOCK 2: Math Question - Threshold Authorization (>)
q2 = input("\nQ2. What is 2+2? ").strip().lower()
if q2 == "4" or q2 == "four": # Operator: Equality
    score += 1
    storage.append("Q2-Correct")
    print(f"✅ Correct! Score: {score:>2}/{total}")
else:
    print(f"❌ Wrong! Score: {score:>2}/{total}")

# BLOCK 3: Planet Question
q3 = input("\nQ3. Which planet is Red Planet? ").strip().lower()
if q3 == "mars":
    score += 1
    storage.append("Q3-Correct")
    print(f"✅ Correct! Score: {score:>2}/{total}")
else:
    print(f"❌ Wrong! Score: {score:>2}/{total}")

# BLOCK 4: Prevents Empty Check / Null Prevention (!=)
q4 = input("\nQ4. Who invented Python? ").strip().lower()
if q4 != "": # Operator: Inequality
    if q4 == "guido van rossum":
        score += 1
        storage.append("Q4-Correct")
        print(f"✅ Correct! Score: {score:>2}/{total}")
    else:
        print(f"❌ Wrong! Correct is Guido van Rossum. Score: {score:>2}/{total}")
else:
    print(f"❌ Empty input not allowed. Score: {score:>2}/{total}")

# BLOCK 5: Threshold Authorization
q5 = input("\nQ5. How many continents? ").strip().lower()
# Operational Mapping - Real world example
if q5 == "7" or q5 == "seven":
    score += 1
    storage.append("Q5-Correct")
    print(f"✅ Correct! Score: {score:>2}/{total}")
else:
    print(f"❌ Wrong! Score: {score:>2}/{total}")

# --- Delivering Results: The F-String Injector ---
# Runtime Evaluation + Precision Formatting
# Professional CLIs require clean alignment - f'{score:>2}'
print("\n==========================================")
print("          FINAL REPORT - Score Vault      ")
print("==========================================")
print(f"Player           : {name}")
print(f"Final Score      : {score:>2} out of {total}")
print(f"Percentage       : {(score/total)*100:.0f}%")
print(f"Storage Vault    : {storage}")

# Rule Engine - Differentiated Learning
if score >= 4:
    print(f"Result           : Excellent {name}! Ready for Global Grading Engine!")
elif score >= 2:
    print(f"Result           : Good job {name}! Keep doing Retrieval Practice.")
else:
    print(f"Result           : Keep Learning {name}! Scaffolding & Feedback needed.")

print("==========================================")-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
