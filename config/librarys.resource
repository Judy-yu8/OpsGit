*** Settings ***
# rf内置库导入
Library    String
Library    DateTime
Library    OperatingSystem

# 第三方库导入
Library    ../library/demo.py
Library    Browser

# 项目关键字库
Resource    settings.resource
Resource    ../keywords/000_common/000_common_keyword.robot
Resource    ../keywords/001_document/001_document_userguide_keyword.robot
Resource    ../testdata/selector/docs/001_docs_dashboard_selector.resource
Resource    ../testdata/data/001_docs_testdata.resource

