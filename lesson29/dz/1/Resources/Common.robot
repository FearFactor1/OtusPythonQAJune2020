*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${SERVER}         demo.opencart.com/admin/
${BROWSER}        Chrome
${DELAY}          0
${LOGIN URL}      http://${SERVER}/
${CATEGORIES}     Cameras
${OrderID}        10250

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}


Go To Login Page
    Go To    ${LOGIN URL}
    Title Should Be    Administration


Submit Credentials
    Click Button    Login


Submit Logout
    Click Element    //span[contains(text(),'Logout')]


Welcome Page Should Be Open
    Title Should Be    Dashboard


Current Page Categories
    Title Should Be    Categories


Go To Catalog
    Click Element  css=li[id=menu-catalog]


Go To Sales Orders
    Click Element  xpath=//a[contains(text(),' Sales')]
    Click Element  xpath=//a[contains(text(),'Orders')]


Go To Profile
    Click Element  xpath=//a[contains(text(),'demo demo ')]
    Click Element  xpath=//a[contains(text(),' Your Profile')]


Go To Categories
    Click Element  xpath=//a[contains(text(),'Categories')]


Search Categories
    Wait Until Page Contains Element  xpath=//td[contains(text(),'${CATEGORIES}')]


Search Fields
    Wait Until Page Contains Element  xpath=//label[contains(text(),'Username')]
    Wait Until Page Contains Element  xpath=//label[contains(text(),'First Name')]
    Wait Until Page Contains Element  xpath=//label[contains(text(),'Last Name')]
    Wait Until Page Contains Element  xpath=//label[contains(text(),'E-Mail')]
    Wait Until Page Contains Element  xpath=//label[contains(text(),'Image')]
    Wait Until Page Contains Element  xpath=//label[contains(text(),'Password')]
    Wait Until Page Contains Element  xpath=//label[contains(text(),'Confirm')]


Search Order ID
    Input Text  xpath=//input[@id='input-order-id']  ${OrderID}
    Click Element  xpath=//button[contains(text(),' Filter')]
    Wait Until Page Contains Element  xpath=//td[contains(text(),'${OrderID}')]