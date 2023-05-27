*** Settings ***
Documentation       Inhuman insurance, Inc. Artificial Intelligence System Robot.
...                 produces traffic data work items.
Library             RPA.HTTP
Library             RPA.JSON
Library             RPA.Tables
Library             Collections
Library             RPA.RobotLogListener
Library             OperatingSystem
Library             RPA.Robocorp.WorkItems
Resource            shared.robot


*** Variables ***
${TRAFFIC_JSON_FILE_PATH}=    ${OUTPUT_DIR}${/}traffic.json
#JSON data keys:
${COUNTRY_KEY}=                 SpatialDim
${GENDER_KEY}=                  Dim1
${RATE_KEY}=                    NumericValue
${YEAR_KEY}=                    TimeDim

*** Tasks ***
Produce traffic data work items
    # Empty Required Directory
    Download traffic data
    ${traffic_data}=    Load traffic data as table
    ${filtered_data}=    Filter and sort traffic data    ${traffic_data}
    ${filtered_data}=    Get latest data by country    ${traffic_data}
    ${payloads}=    Create wok item payloads    ${filtered_data}
    Save work item payloads    ${payloads}

*** Keywords ***
# Empty Required Directory
#     Empty Directory    ${OUTPUT_DIR}
Download traffic data
    Download    https://github.com/robocorp/inhuman-insurance-inc/raw/main/RS_198.json
    ...         ${OUTPUT_DIR}${/}traffic.json
    ...         overwrite=True

Load traffic data as table
    ${json}=    Load JSON from file    ${OUTPUT_DIR}${/}traffic.json
    ${table}=    Create Table    ${json}[value]
    #Write Table To Csv    ${table}    test.csv
    RETURN    ${table}

Filter and sort traffic data
    [Arguments]    ${table}
    
    ${max_rate}=    Set Variable    ${5.0}
    ${rate_key}=    Set Variable    NumericValue
    ${gender_key}=    Set Variable    Dim1
    ${both_genders}=    Set Variable    BTSX
    ${year_key}=    Set Variable    TimeDim

    Filter Table By Column    ${table}    ${rate_key}    <    ${max_rate}
    Filter Table By Column    ${table}    ${gender_key}    ==    ${both_genders}
    Sort Table By Column    ${table}    ${year_key}    False
    RETURN    ${table}

Get latest data by country
    [Arguments]    ${table}
    ${country_key}=    Set Variable    SpatialDim
    ${table}=    Group Table By Column    ${table}    ${country_key}
    ${latest_data_by_country}=    Create List
    FOR    ${group}    IN    @{table}
        Log To Console    ${group}
        ${first_row}=    Pop Table Row    ${group}
        Append To List    ${latest_data_by_country}    ${first_row}
    END
    RETURN    ${latest_data_by_country}

Create wok item payloads
    [Arguments]    ${traffic_data}
    ${payloads}=    Create List
    FOR    ${row}    IN    @{traffic_data}
        ${payload}=
        ...    Create Dictionary
        ...    country=${row}[${COUNTRY_KEY}]
        ...    year=${row}[${YEAR_KEY}]
        ...    date=${row}[${RATE_KEY}]
        Append To List    ${payloads}    ${payload}
    END
    RETURN    ${payloads}

Save work item payloads
    [Arguments]    ${payloads}
    FOR    ${payload}    IN    @{payloads}
        Save work item payload    ${payload}
    END

Save work item payload
    [Arguments]    ${payload}
    ${variables}=    Create Dictionary    traffic_data=${payload}
    Create Output Work Item    variables=${variables}    save=True