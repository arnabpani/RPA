*** Settings ***
Documentation       Google using an already open Chrome browser.

Library             RPA.Browser.Selenium


*** Tasks ***
Attach to running Chrome Browser and execute Google search
    Attach Chrome Browser    9222
    Go To    https://www.google.com/?hl=en
    Input Text    name:q    Dinosaur
    Press Keys    name:q    ENTER