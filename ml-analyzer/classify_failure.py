import joblib
import pandas as pd
import os
import re
from suggest_fix import suggest_fix

# Load the trained ML model
model = joblib.load("failure_classifier.pkl")

# Path to the structured failed logs file
log_path = os.path.join("..", "testng-scripts", "logs", "failed_logs.txt")

# Read and split logs using '-----' as a block separator
with open(log_path, "r") as f:
    blocks = f.read().split("-----\n")

results = []

for block in blocks:
    if not block.strip():
        continue

    try:
        # Default values
        test_name = "UnknownTest"
        error_msg = ""
        class_name = "UnknownClass"
        method_name = "UnknownMethod"
        line_number = "N/A"

        # Extract values line by line
        for line in block.strip().split("\n"):
            if line.startswith("TEST:"):
                test_name = line.split("TEST:")[1].strip()
            elif line.startswith("ERROR:"):
                error_msg = line.split("ERROR:")[1].strip()
            elif line.startswith("CLASS:"):
                class_name = line.split("CLASS:")[1].strip()
            elif line.startswith("METHOD:"):
                method_name = line.split("METHOD:")[1].strip()
            elif line.startswith("LINE:"):
                line_number = line.split("LINE:")[1].strip()

        # Combine location for dashboard display
        location = f"{class_name}.{method_name}:{line_number}"

        # Predict cause and suggest fix
        predicted_cause = model.predict([error_msg])[0]
        suggestion = suggest_fix(error_msg)

        # Append to result list
        results.append((test_name, error_msg, location, predicted_cause, suggestion))

    except Exception as e:
        print(f"⚠️ Error parsing block:\n{block}\nReason: {e}")

# Write output to CSV for the dashboard
output_path = os.path.join("..", "output", "classified_results.csv")
df = pd.DataFrame(results, columns=["test_name", "error_log", "location", "predicted_cause", "suggestion"])
df.to_csv(output_path, index=False, na_rep="N/A")

print(f"✅ Analysis complete. Output written to {output_path}")
