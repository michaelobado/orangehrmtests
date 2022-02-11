Feature: OrangeHRM Login
    Scenario: Login to orangeHRM with valid parameters
        Given I launch chrome browser
        When I open orange hrm homepage
        And Enter username "admin" and password "admin123"
        And Click on login button
        Then User must successfully login to the Dashboard page

    Scenario Outline: Login to orangeHRM with Multiple parameters
        Given I launch chrome browser
        When I open orange hrm homepage
        And Enter username "<username>" and password "<password>"
        And Click on login button
        Then User must successfully login to the Dashboard page

        Examples:
            | username | password |
            | admin | admin123 |
            | admin123 | admin |
            | adminxyz | admin123 |
            | admin | adminxyz |