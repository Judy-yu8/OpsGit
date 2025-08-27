*** Settings ***
Resource          ../../config/librarys.resource
Suite Setup       Open Browser With Chrome
Suite Teardown    Clear Environment   

*** Test Cases ***
User Guide Page Normal
    [Tags]    WEB
    Go To User Guide Page
    Verify User Guide Page Normal
    