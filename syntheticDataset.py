import pandas as pd
import numpy as np

def generate_dataset(n_without=30, n_with=30):
    np.random.seed(42)

    def generate_data(n, scenario):
        data = []

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