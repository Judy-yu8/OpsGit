*** Settings ***
Resource    ../../config/librarys.resource

*** Keywords ***
Open Browser With Chrome
    Log To Console    打开浏览器\n

    Set Browser Timeout    30s
    New browser    headless=False
    New Page    ${url_test}

Clear Environment
    Close Browser    ALL


    
