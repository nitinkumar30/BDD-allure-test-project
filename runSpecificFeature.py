import os
from datetime import datetime
import subprocess

# Get the current date and time to create a unique report folder
current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Define the report directory using the current date-time
report_directory = f"reports/allure-results_{current_datetime}"

feature_file = os.path.abspath('features/loginAgain.feature')

# Run Behave with the custom output directory
subprocess.run([
    'python', '-m', 'behave',
    # 'features/loginAgain.feature',
    feature_file,
    '--format', 'allure_behave.formatter:AllureFormatter',
    '--outfile', report_directory
])

print(report_directory, "\n\n\n\n")

# Generate the Allure report with the custom directory
subprocess.run([
    'allure',
    'generate',
    report_directory,
    '--output', f"reports/allure-report_{current_datetime}"
])

# Open the Allure report in a browser
subprocess.run(['allure', 'open', f"reports/allure-report_{current_datetime}"])





#
