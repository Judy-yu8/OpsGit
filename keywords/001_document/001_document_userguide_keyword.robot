*** Settings ***
Resource    ../../config/librarys.resource

*** Keywords ***
Go To User Guide Page
    [Documentation]    进入User Guide页面
    Log To Console     \n进入User Guide页面
    Click    ${user_guide_link_a}
  
Verify User Guide Page Normal
    [Documentation]    检查User Guide页面正常打开
    Log To Console     \n检查User Guide页面正常打开

    ${previous}    Switch Page    NEW
    ${url_expect}=    Get Url    #检查用户指导页的URL
    Should Be Equal As Strings    ${url_expect}    ${user_guide_page_url}
    ${text_expect}=    Get Text    ${usre_guide_page_title_h1}    #检查用户指导页的title是否出现
    Should Be Equal As Strings    ${text_expect}    ${user_guide_page_title}
    Switch Page    ${previous}  
