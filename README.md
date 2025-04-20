# Smart-Test-Analyzer
AI Based Testcase failure analyzer Dashboard 

**Overview** 
- Smart Test Analyzer is a plug-and-play tool that automatically classifies test failures, detects the root cause, and provides fix suggestions using Machine Learning and NLP.
- It supports Selenium (Java + TestNG) and Playwright (JavaScript/TypeScript).

**Features of smart-test-analyzer**
- Auto-detects failure causes (e.g., Timeout, NoSuchElement, ClickIntercepted, etc.)
- Provides rule-based and AI-based suggestions (via Hugging Face GPT)
- Dashboard view for triage-friendly summaries
- Works with both Java (TestNG) and Playwright

**Tech Stack**  
- Selenium + TestNG  
- Python, Flask, Pandas
- HuggingFace Transformers (optional AI-based suggestions)
- ML model (sklearn-based classifier on test logs)

**Setup Instructions**  
Clone the repo      
**Step 1:** 📦 Install Python Dependencies   
1. cd ml-analyzer  
2. python -m venv venv   
3. venv\Scripts\activate     # Or: source venv/bin/activate (Linux/macOS)   
4. pip install -r requirements.txt   
Note : If transformers or torch error   
Run: pip install transformers torch pandas joblib flask   

**Step 2:** 🧪 Run Java Tests (Selenium + TestNG)   
File: LoginTest.java   

- Make sure your @AfterMethod in LoginTest.java logs errors like this:  

  TEST: testLoginFail  
  ERROR: org.openqa.selenium.NoSuchElementException  
  CLASS: tests.LoginTest   
  METHOD: testLoginFail  
  LINE: 25  

- File will be saved in: testng-scripts/logs/failed_logs.txt   

**Step 3:** Run the tests:      

1. cd testng-scripts  
2. mvn clean test
   
Run Classifier (Python)  
1. cd ../ml-analyzer  
2. python classify_failure.py  
➡ Output: output/classified_results.csv  

**Step 4:** Launch the Dashboard  

1. cd ../testng-scripts  
2. python dashboard_app.py  
3. Then go to your browser and visit:  
**http://127.0.0.1:5000/**

**Dashboard Screenshot**  

![image](https://github.com/user-attachments/assets/ce96a5a9-f195-4850-b2b0-107da821a74f)

