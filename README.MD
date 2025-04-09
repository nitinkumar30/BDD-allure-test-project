### **1. Project Setup:**

#### 1.1. **Create a Virtual Environment (Optional if using Pycharm but Recommended)**

It’s a good practice to create a virtual environment for your project to isolate the dependencies.

- **Windows**:

```bash
python -m venv venv
```

- **Mac/Linux**:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **Windows**:

```bash
.\venv\Scripts\activate
```

- **Mac/Linux**:

```bash
source venv/bin/activate
```

#### 1.2. **Install Dependencies (Behave, Selenium, WebDriver, etc.)**

Use `pip` to install the necessary packages.

```bash
pip install selenium behave
```

If you want to use **Allure** for reports, you can install the **Allure Behave** plugin:

```bash
pip install allure-behave
```

Additionally, you may need to install the appropriate **WebDriver** for your browser (e.g., ChromeDriver for Chrome):

- **For Chrome**: [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- **For Firefox**: [Download GeckoDriver](https://github.com/mozilla/geckodriver/releases)

#### 1.3. **Install Other Dependencies (if required)**

If you are using other dependencies for API testing or additional features, install them as well. For example, if you need **Requests** for API testing:

```bash
pip install requests
```

---

### **2. Project Structure:**

Here’s the basic folder structure for your project:

```
.\
│
├── config\
│   └── configreader.py
│
├── features\
│   ├── login.feature
│   └── loginAgain.feature
│
├── screenshots\
│   ├── 1.png
│   ├── 2.png
│   └── 3.png
│
├── steps\
│   ├── test_steps.py
│   └── utils.py
│
├── xpaths\
│   └── loginPage.properties
│
├── config.properties
└── runSpecificFeature.py
```

---

### **3. Running Tests:**

#### 3.1. **Run Behave Tests (Basic)**

To run the Behave tests:

```bash
behave
```

This will search for `.feature` files and execute the scenarios defined inside them.

#### 3.2. **Running Tests with Specific Feature File**

If you want to run a specific feature file:

```bash
behave features/login.feature
```

#### 3.3. **Run Tests with Tags**

You can also run tests using **tags** defined in your feature file:

Example of tagging in `login.feature`:

```gherkin
@smoke
Feature: User login functionality
```

To run tests with a specific tag:

```bash
behave -t @smoke
```

To run tests without a specific tag:

```bash
behave -t ~@smoke
```

#### 3.4. **Run Tests with Multiple Formats (HTML, JSON, JUnit)**

To generate detailed reports (HTML, JSON, JUnit):

```bash
behave --format html --outfile reports/report.html --format json --outfile reports/report.json --format junit --outfile reports/result.xml
```

#### 3.5. **Run Tests with Allure Formatter**

To run the tests with **Allure** formatter and generate results for Allure reports:

```bash
behave features/loginAgain.feature -f allure_behave.formatter:AllureFormatter -o allure-results
```

- **`features/loginAgain.feature`**: Specifies the feature file you want to run (in this case, `loginAgain.feature`).
- **`-f allure_behave.formatter:AllureFormatter`**: Tells Behave to use the Allure formatter to generate the report results in Allure-compatible format.
- **`-o allure-results`**: Specifies the output directory (`allure-results`) where the results will be stored.

#### 3.6. **Serve Allure Report**

After running your tests with Allure, you can **serve the Allure report** to view the detailed test results in your browser:

```bash
allure serve allure-results
```

This command will:
- Generate the Allure report from the `allure-results` folder.
- Automatically open the report in your default web browser so you can visually inspect the test results and trends.

---

### **4. Debugging Behave Tests:**

#### 4.1. **Running Tests with Logging**

You can enable logging to get more detailed output about the tests:

```bash
behave -D loglevel=DEBUG
```

This will show additional debug information during the test run.

#### 4.2. **Running Tests in Verbose Mode**

Use the `--verbose` flag to display each step’s output:

```bash
behave --verbose
```

#### 4.4. **Using Browser Developer Tools**

You can inspect the webpage and troubleshoot element locators using the browser's Developer Tools (`F12` or `Ctrl+Shift+I`).

- **Elements Tab:** Inspect and get the exact XPath or CSS selector.
- **Console Tab:** Check for JavaScript errors or log output from the page.

---

### **5. Clean Up & Maintenance:**

#### 5.1. **Deactivate the Virtual Environment**

Once you’re done working on your project, deactivate the virtual environment:

```bash
deactivate
```

#### 5.2. **Remove Unused Dependencies**

If you need to uninstall any Python packages, use `pip uninstall`:

```bash
pip uninstall selenium
pip uninstall behave
```

---

### **6. CI/CD Integration (Optional)**

For **CI/CD** (Jenkins, GitLab CI, CircleCI, etc.), you can integrate Behave tests and the reports generated (e.g., JUnit report) to visualize test results in your pipeline.

#### Example for Jenkins:

In your Jenkinsfile:

```bash
stage('Run Tests') {
    steps {
        sh 'behave --format junit --outfile result.xml'
        junit '**/result.xml'  # Jenkins will publish the JUnit test results
    }
}
```

---

### **Summary of Useful Commands:**


| **Action**                              | **Command**                                                    |
|-----------------------------------------|---------------------------------------------------------------|
| Create a virtual environment            | `python -m venv venv`                                          |
| Activate virtual environment            | `source venv/bin/activate` (Mac/Linux), `.\venv\Scripts\activate` (Windows) |
| Install dependencies                    | `pip install selenium behave`                                  |
| Run tests                               | `behave`                                                       |
| Run specific feature file               | `behave features/login.feature`                                |
| Run tests with tags                     | `behave -t @smoke`                                             |
| Run tests with multiple formats         | `behave --format html --outfile reports/report.html --format json --outfile reports/report.json` |
| Enable verbose logging                  | `behave --verbose`                                             |
| Enable debugging                        | `behave -D loglevel=DEBUG`                                     |
| Pause on failure (manual debugging)     | `time.sleep(10)` or `pdb.set_trace()`                          |
| Take screenshot on failure              | `context.driver.save_screenshot('path/to/screenshot.png')`     |
| Run tests with Allure formatter         | `behave features/loginAgain.feature -f allure_behave.formatter:AllureFormatter -o allure-results` |
| Serve Allure report                     | `allure serve allure-results`                                  |


