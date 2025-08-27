*** Settings ***
Resource    ../config/librarys.resource

*** Tasks ***
Clear Report
    Remove Directory    path=${CURDIR}${/}..${/}report    recursive=True