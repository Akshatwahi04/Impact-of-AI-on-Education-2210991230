import pandas as pd
import numpy as np

def generate_dataset(n_without=30, n_with=30):
    np.random.seed(42)

    def generate_data(n, scenario):
        data = []
import pandas as pd
import matplotlib.pyplot as plt


USE_SYNTHETIC = True   #  Change to False if you want to use CSV

# data_generator

if USE_SYNTHETIC:
    # Import generator
    from synthetic_data_generator import generate_dataset

    df = generate_dataset()
    print("Synthetic Dataset Generated\n")

else:
    try:
        df = pd.read_csv("../Dataset/ai_impact_dataset.csv")
        print("Dataset Loaded Successfully\n")
    except FileNotFoundError:
        print("Error: Dataset file not found.")
        exit()

print(df.head())


# Ensure only numeric columns are used for calculations
numeric_cols = df.select_dtypes(include='number').columns

# Group by scenario
summary = df.groupby("Scenario")[numeric_cols].mean().round(2)

print("\n===== Average Impact Analysis =====")
print(summary)

# Calculate percentage improvement
improvement = (
    (summary.loc["With_AI"] - summary.loc["Without_AI"])
    / summary.loc["Without_AI"]
) * 100

improvement = improvement.round(2)

print("\n===== Percentage Improvement =====")
print(improvement)



summary["Efficiency_Score"] = (
    summary["Concept_Score"] * 0.25 +
    summary["Completion_Rate"] * 0.25 +
    summary["Retention"] * 0.2 +
    summary["Engagement"] * 0.1 -
    summary["Study_Time"] * 0.1 -
    summary["Teacher_Time"] * 0.1
).round(2)

print("\n===== Efficiency Score =====")
print(summary["Efficiency_Score"])



# 1. Learning Outcomes
plt.figure()
summary[["Concept_Score", "Completion_Rate", "Retention"]].T.plot(kind="bar")
plt.title("Learning Outcomes: With vs Without AI")
plt.ylabel("Score (%)")
plt.xlabel("Metrics")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 2. Time Reduction
plt.figure()
summary[["Study_Time", "Teacher_Time"]].T.plot(kind="bar")
plt.title("Time Reduction Due to AI")
plt.ylabel("Time")
plt.xlabel("Metrics")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 3. Engagement
plt.figure()
summary["Engagement"].plot(kind="bar")
plt.title("Student Engagement Comparison")
plt.ylabel("Engagement Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 4. Efficiency Score
plt.figure()
summary["Efficiency_Score"].plot(kind="bar")
plt.title("Overall Educational Efficiency")
plt.ylabel("Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# fina result

if summary.loc["With_AI", "Efficiency_Score"] > summary.loc["Without_AI", "Efficiency_Score"]:
    print("\nConclusion: AI significantly improves overall educational efficiency.")
else:
    print("\nConclusion: AI shows limited impact.")
        for _ in range(n):
            if scenario == "Without_AI":
                concept = np.random.randint(59, 69)
                completion = concept + np.random.randint(5, 7)
                study = np.random.randint(47, 55)
                retention = concept - np.random.randint(3, 5)
                engagement = round(np.random.uniform(2.2, 3.1), 1)
                teacher = round(np.random.uniform(5.4, 6.7), 1)
                feedback = np.random.randint(45, 55)

            else:  # With_AI
                concept = np.random.randint(77, 87)
                completion = concept + np.random.randint(10, 12)
                study = np.random.randint(24, 33)
                retention = concept - np.random.randint(3, 5)
                engagement = round(np.random.uniform(3.8, 4.7), 1)
                teacher = round(np.random.uniform(1.5, 2.4), 1)
                feedback = np.random.randint(2, 7)

            data.append([
                scenario, concept, completion, study,
                retention, engagement, teacher, feedback
            ])

        return data

    without_ai = generate_data(n_without, "Without_AI")
    with_ai = generate_data(n_with, "With_AI")

    columns = [
        "Scenario", "Concept_Score", "Completion_Rate",
        "Study_Time", "Retention", "Engagement",
        "Teacher_Time", "Feedback_Speed"
    ]

    df = pd.DataFrame(without_ai + with_ai, columns=columns)

    return df