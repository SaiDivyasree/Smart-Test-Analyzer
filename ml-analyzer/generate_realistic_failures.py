import random
import csv

# Define realistic failure types for Selenium
errors_by_cause = {
    "locator_issue": [
        "NoSuchElementException: Cannot locate element with id '{id}'",
        "InvalidSelectorException: The given selector '##{id}' is not valid",
        "StaleElementReferenceException: The element with id '{id}' is no longer attached to the DOM"
    ],
    "wait_issue": [
        "TimeoutException: Waiting for visibility of element '{id}' timed out",
        "ElementNotVisibleException: Element '{id}' is not visible after wait",
        "TimeoutException: Script execution exceeded 10s"
    ],
    "flaky": [
        "ElementClickInterceptedException: Element click intercepted by another element",
        "ElementNotInteractableException: Element '{id}' could not be interacted with",
        "UnknownError: Random JavaScript failure occurred"
    ],
    "env_issue": [
        "WebDriverException: chrome not reachable",
        "SessionNotCreatedException: session ID is null",
        "500 Internal Server Error: GET /api/v{num}/data",
        "JavascriptException: error executing script in browser"
    ],
    "navigation_issue": [
        "NoSuchWindowException: Tried switching to a non-existent window",
        "UnhandledAlertException: Unexpected alert open",
        "NavigationTimeoutException: Page load timed out"
    ]
}

ids = ['loginBtn', 'submit', 'username', 'searchBox', 'logout', 'email']
dataset = []

# Generate ~60 logs per category
for cause, templates in errors_by_cause.items():
    for _ in range(60):  # 60 logs × 5 causes = 300 total
        template = random.choice(templates)
        log = template.format(
            id=random.choice(ids),
            num=random.randint(1, 5)
        )
        dataset.append((log, cause))

# Shuffle results
random.shuffle(dataset)

# Save to training file
with open("dataset/errors_dataset.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["error_log_text", "root_cause"])
    writer.writerows(dataset)

# Save same logs (without labels) for prediction
with open("../testng-scripts/logs/failed_logs.txt", "w", encoding='utf-8') as f:
    for row in dataset:
        f.write(row[0] + "\n")

print("✅ Generated 300 diverse error logs and labeled training set")
