**To get an HTML report using Pytest, you need to follow these steps:**
1. Install Pytest and Pytest HTML

Pytest is a testing framework for Python that allows you to write test codes. Pytest HTML is a plugin for Pytest that generates HTML reports for test results. To install both, you need to run the following command in your terminal:

pip install pytest pytest-html

2. Run Pytest with HTML Report Option:

Once Pytest and the HTML plugin are installed, you can run your tests and generate an HTML report. Use the command below, replacing `DEC/4_DEC_2023/test_labapi005.py` with the path to your test file:

pytest DEC/4_DEC_2023/test_labapi005.py --html=report.html

This command will execute the tests in `test_labapi005.py` and generate an HTML report named `report.html`.

3. View the HTML Report:

After running the tests, you can find the `report.html` file in your project directory. Open this file in a web browser to view the test results in a formatted HTML report.

**For generating Allure reports, follow these steps:**

1. Install Allure Report:

Allure is another framework for test reporting. Before you can generate reports with Allure, you need to install it. Allure can be installed via npm (Node Package Manager). First, ensure that you have Node.js and npm installed on your system. Then run the following command:

npm install -g allure-commandline

2. Install Allure Pytest Plugin:

To integrate Allure with Pytest, install the Allure Pytest plugin. You can do this by running the following command:

pip install allure-pytest

3. Run Pytest with Allure Report Option:

After installing the Allure commandline and the Allure Pytest plugin, you can generate Allure reports from your tests. Use the command below, replacing `DEC/4_DEC_2023/test_labapi005.py` with the path to your test file:

pytest DEC/4_DEC_2023/test_labapi005.py --alluredir=reports

This will run the tests and store the results in the `reports` directory.

4. Generate and View the Allure Report:

To view the reports, you need to generate them using the Allure commandline tool. Run the following command:

allure serve reports

This command will process the files in the `reports` directory and start a web server to display the results. Your default web browser should automatically open and display the Allure report.

Remember to replace `DEC/4_DEC_2023/test_labapi005.py` with the actual path to your test file.