Feature: Login functionality validation using credentials

  Scenario Outline: Successful login with provided credentials
    Given User is on login page
    When User provides valid login credentials as <username> and <password>
    Then User will be displayed with a current page title

    Examples: Valid
      | username | password |
      | nitin    | kumar    |
      | black    | eagle    |

    Examples: Invalid
      | username | password |
      | nitin    | nitin    |
