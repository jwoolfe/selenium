Feature: Costco Shopping Cart

Scenario: Shopping Cart presence on Costco home Page
    Given launch chrome browser
    When  open Costco homepage
    Then  verify the cart is present on the Page
    And   close browser

