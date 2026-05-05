Feature: login functionality

    Scenario Outline:  Login with multiple user
        Given I open the login page
        When I login with "<username>" and "<password>"
        Then I should see the home page

        Examples:
            | username        | password     |
            | standard_user   | secret_sauce |
            | locked_out_user | secret_sauce |
            | problem_user    | secret_sauce |