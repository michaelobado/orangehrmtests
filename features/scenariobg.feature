Feature: OrangeHRM Login

  Background: Common steps
    Given I launch browser
    When I open application
    And Enter valid username and password
    And Click on login

  Scenario: Login to HRM Application
    Then User must login to the Dashboard page

  Scenario: Search user
    When navigate to search page
    Then search page should display
   Scenario: Advanced Search user
    When navigate to advanced search page
    Then advanced search page should display