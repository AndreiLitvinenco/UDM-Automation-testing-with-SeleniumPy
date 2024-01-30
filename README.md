# Udemy-course-automation-testing-with-Seleniumpy
This repository contains a few automated tests made with selenium webdriver and python along with some other exercises performed within the udemy course.
## Installation
To run the test scripts locally, you need to have Python3 and pip installed on your machine. Follow these steps to get started:
1. Go to `https://www.python.org/downloads/` and install the newest LTS version available.
2. Clone the repository: `git clone https://github.com/AndreiLitvinenco/UDM-Automation-testing-with-SeleniumPy.git`.
3. Change into the project directory: `cd UDM-Automation-testing-with-SeleniumPy`.
4. Install the project dependencies: `pip install -U selenium` and `pip install assertpy`.

## Running the tests
To run the test scripts on your machine follow the next steps:
1. Open a terminal window and change into the project directory: `cd UDM-Automation-testing-with-SeleniumPy`.
2. Run the command `python -m unittest discover`.

## Test catalog
* On the home page of emag.ro verify if the logo is present on the page.
* ^ verify that the title of the page is equal or contains the word "emag"
* On the about page of emag.ro verify that the title tag is equal or contains the word "emag".
* ^ verify that the navbar elements contain the right text.
