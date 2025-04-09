Feature: Login functionality
Scenario: Successful login with valid credentials
  Given User is on login page
  When User provides valid login credentials
  Then User will be logged into website

