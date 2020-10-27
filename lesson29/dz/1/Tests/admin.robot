*** Settings ***
Documentation     dz
Resource          ../Resources/Common.robot

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser


Search Categories
    Open Browser To Login Page
    Submit Credentials
    Go To Catalog
    Go To Categories
    Current Page Categories
    Search Categories
    [Teardown]    Close Browser


Login And Logout
    Open Browser To Login Page
    Submit Credentials
    Welcome Page Should Be Open
    Submit Logout
    Go To Login Page
    [Teardown]    Close Browser


Check Profile
    Open Browser To Login Page
    Submit Credentials
    Go To Profile
    Search Fields
    [Teardown]    Close Browser


Search Order ID
    Open Browser To Login Page
    Submit Credentials
    Go To Sales Orders
    Search Order ID
    [Teardown]    Close Browser