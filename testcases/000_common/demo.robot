*** Settings ***
Resource    ../../config/librarys.resource

*** Test Cases ***
Robot Run Script Normal 
    [Tags]    extra
    ${num}    Evaluate    random.randint(0,2)    random
    Should be equal as strings    1    ${num}    #检查bin下的run脚本中的rerun功能(报告生成，报告合并等)。

Custom Library Test
    ${res}    Add    1    2
    Should Be Equal As Integers    ${res}    3




