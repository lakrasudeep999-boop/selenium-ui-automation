Selenium UI Automation Framework





OVERVIEW:

This project is a UI automation framework built using Python, Selenium WebDriver, and Pytest.

It follows industry best practices like Page Object Model (POM) and pytest fixtures to create a clean, scalable, and maintainable test framework.



The framework automates an end-to-end user journey on the SauceDemo application:

Login → Inventory → Cart → Checkout → Order Completion



TECH STACK:

Python

Selenium WebDriver

Pytest

Page Object Model (POM)



KEY FEATURES:

Page Object Model (POM) design

Pytest fixtures for setup and chaining

End-to-End (E2E) test flow

Explicit waits for stable execution

Screenshot capture on test failure

Logging support for debugging





PROJECT STRUCTURE:



project/

│

├── pages/ # Page Object Classes

│ ├── login\_page.py

│ ├── inventory\_page.py

│ ├── cart\_page.py

│ ├── checkout\_page.py

│ ├── checkout\_overview\_page.py

│

├── tests/ # Test Files

│ ├── test\_login.py

│ ├── test\_cart.py

│ ├── test\_checkout.py

│ ├── test\_e2e.py

|      test\_checkout\_negative.py

|      test\_overview.py

│

├── screenshots/ # Failure screenshots

├── conftest.py # Fixtures (driver, login, flow)

├── config.py # Test configuration

├── requirements.txt

├── README.md



FRAMEWORK DESIGN:

Page Object Model (POM)



Each page contains:

Locators

Actions (click, type)

Waits for UI changes

Navigation to next page



FIXTURES:



Fixtures are used to:



Initialize WebDriver

Perform login

Chain navigation (Login → Inventory → Cart)



Example:

driver → login → add\_to\_cart → checkout



TESTS:



Tests are:



Clean and readable

Focused only on assertions

Free from setup logic



How to Run

&#x20;-Install dependencies

pip install -r requirements.txt



Run all tests

pytest -v



Run specific test

pytest tests/test\_cart.py -v



Screenshot on Failure:

If a test fails, a screenshot is automatically captured and stored in the screenshots/ folder.



TEST COVERAGE:

Login functionality

Product selection and cart validation

Checkout form validation

Price and total verification

Order completion flow





Best Practices Implemented:

Explicit waits instead of sleep

Separation of concerns (POM, fixtures, tests)

Reusable and scalable architecture

Clean test design (no driver calls in tests)



Learning Outcomes:

UI automation using Selenium

Designing scalable test frameworks

Handling dynamic UI with waits

Using pytest fixtures and hooks

Debugging and stabilizing flaky tests



Author:

Sudeep Lakra

