from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

def suggest_fix(error_log):
    prompt = f"Test error: {error_log[:120]}\nFix:"
    try:
        result = generator(prompt, max_length=60, num_return_sequences=1, do_sample=True)
        suggestion = result[0]['generated_text'].split("Fix:")[-1].strip()

        # Clean up junk output
        suggestion = suggestion.replace("<", "").replace(">", "").split("\n")[0].strip()

        # Fallback if too short or looks broken
        if len(suggestion) < 10 or suggestion.startswith("@") or "http" in suggestion:
            return fallback_suggestion(error_log)

        return suggestion
    except Exception as e:
        return fallback_suggestion(error_log)


def fallback_suggestion(error_log):
    if "TimeoutException" in error_log:
        return "Try increasing wait time or use explicit waits."
    elif "NoSuchElementException" in error_log:
        return "Ensure the element ID/class is correct and the element is visible."
    elif "ElementClickInterceptedException" in error_log:
        return "Wait for overlays or popups to disappear before clicking."
    else:
        return "Check the full stack trace and inspect UI load conditions."
