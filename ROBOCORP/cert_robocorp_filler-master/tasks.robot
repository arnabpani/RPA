*** Settings ***
Documentation       Playwright template.
Library             Collections
Library             RPA.Browser.Playwright
Library             libs.py
Library             RPA.Tables

*** Settings ***
Variables         vars.py


*** Test Cases ***
Minimal task
    Starting a browser
    Start Typeform
    Result Checker


*** Keywords ***
Wait And Get Question Title
    Wait For Elements State    [data-qa-focused="true"]
    Sleep    1s
    ${q_title}=    Evaluate JavaScript
    ...    [data-qa-focused="true"]
    ...    (element, arg) => element.querySelector('[data-qa^="block-title"]').innerText
    @{q_texts}=    Evaluate Javascript
    ...    body
    ...    (element, arg) => [...document.querySelectorAll('[data-qa-focused="true"] div.TextWrapper-sc-__sc-1f8vz90-0.kULmuD')].map(x => x.innerText)
    ...    all_elements=True
    RETURN    ${q_title}    ${q_texts}

Get Quiz Data
    [Arguments]    ${q_title}    ${q_texts}
    &{q_data}=    get_quizz_data    ${q_title}    ${q_texts}    ${data_quizz}
    RETURN    ${q_data}

Fill Quizz
    [Arguments]    ${q_data}
    ${type}=    Get From Dictionary    ${q_data}    type
    ${response}=    Get From Dictionary    ${q_data}    response
    FOR    ${question}    IN    @{response}
         ${q_txt}=    Get From Dictionary    ${question}    text
         ${q_select}=    Get From Dictionary    ${question}    select
         IF    "${q_select}" == "true"
            IF    "${type}" == "input"
                Keyboard Input    type    ${q_txt}
            ELSE
                Click    [data-qa-focused="true"] div[class^="TextWrapper-"] >> text=${q_txt}    delay=300ms
            END
         END
    END
    IF    "${type}" != "select_single"
        Click OK
    END

Click OK
    Click    [data-qa-focused="true"] button    delay=1s

Eval Qestion
    ${q_title}    ${q_texts}=    Wait And Get Question Title
    ${q_data}=    Get Quiz Data    ${q_title}    ${q_texts}
    Fill Quizz    ${q_data}

Starting a browser
    New Browser    chromium    headless=false
    Set Browser Timeout    5s
    ${context_desktop}=    New Context    viewport={'width': 1920, 'height': 1080}
    Switch Context    ${context_desktop}

Start Typeform
    ${data_len}=    Get Length    ${data_quizz}
    New Page    https://robocorp.typeform.com/to/ig9496MD
    Click    [data-qa="start-button"]
    FOR    ${element}    IN    @{data_quizz}
        Eval Qestion
    END

Result Checker
    ${status}=    Run Keyword And Return Status    Wait For Elements State    text=Good try!    timeout=2 s
    Sleep    15s
    IF    ${status}
        Log To Console    Try Again!
        Fail    Try Again!
    ELSE
        Log To Console    Sucess!!
    END
