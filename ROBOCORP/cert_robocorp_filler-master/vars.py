data_quizz = [
	{
		"question": "Let us know your full name that you want us to use in the certification.",
		"type": "input",
		"response": [{"text":"Emil Szymecki","select":"true"}]
	},
	{
		"question": "Your email address that you used to create a Robocorp account:",
		"type": "input",
		"response": [{"text":"emilszymecki@gmail.com","select":"true"}]
	},
	{
		"question": "Which company do you work for?",
		"type": "input",
		"response": [{"text":"ROBOT-A","select":"true"}]
	},
	{
		"question": "Choose all that apply:",
		"response": [
			{
				"text": "Robocorp can automate systems without a graphical user interface (GUI).",
				"select": "true"
			},
			{
				"text": "Robocorp can automate systems with a graphical user interface (GUI).",
				"select": "true"
			},
			{
				"text": "Robocorp can automate systems with REST APIs.",
				"select": "true"
			}
		],
		"type": "select_multi"
	},
    {
        "question": "What is the name of the pattern you used to develop the sales system API robot?",
        "response": [
            {
                "text": "Manufacturer-buyer",
                "select": "true"
            },
            {
                "text": "Producer-consumer",
                "select": "false"
            },
            {
                "text": "Director-assistant",
                "select": "false"
            },
            {
                "text": "Manager-developer",
                "select": "false"
            },
            {
                "text": "Creator-user",
                "select": "false"
            }
        ],
        "type": "select_single"
    },
    {
        "question": "The small chunks of work at the core of the pattern-that-shall-not-be-named are called:",
        "response": [
            {
                "text": "Packets",
                "select": "true"
            },
            {
                "text": "Stuffs",
                "select": "false"
            },
            {
                "text": "Thingies",
                "select": "false"
            },
            {
                "text": "Packages",
                "select": "false"
            },
            {
                "text": "Hobbitses",
                "select": "false"
            },
            {
                "text": "Work items",
                "select": "false"
            },
            {
                "text": "My preciouses",
                "select": "false"
            }
        ],
        "type": "select_single"
    },
    {
        "question": "Choose all that apply:",
        "response": [
            {
                "text": "A business exception is a normal exception that is wearing formal clothing.",
                "select": "true"
            },
            {
                "text": "A business exception might be caused by, for example, invalid data.",
                "select": "true"
            },
            {
                "text": "A business exception typically goes away by retrying the failing action many times.",
                "select": "true"
            },
            {
                "text": "Business exceptions can be distinguished from other exceptions by exception type.",
                "select": "true"
            }
        ],
        "type": "select_multi"
    },
    {
        "question": "Choose all that apply:",
        "response": [
            {
                "text": "Work items are good for tracking the flow of work through a process.",
                "select": "true"
            },
            {
                "text": "Work items are useful when building error-tolerant automations.",
                "select": "true"
            },
            {
                "text": "Work items can be used for measuring automation business value.",
                "select": "true"
            },
            {
                "text": "Work items enable parallel processing of work.",
                "select": "true"
            }
        ],
        "type": "select_multi"
    },
    {
        "question": "Choose all that apply:",
        "response": [
            {
                "text": "Using business terms in code makes it easier to understand the connection between the robot logic and the process you are automating.",
                "select": "true"
            },
            {
                "text": "Since code is technical, it is better to use just technical terms when coding instead of business terms.",
                "select": "true"
            },
            {
                "text": "Avoiding business terminology in robot code is a best practice.",
                "select": "true"
            },
            {
                "text": "Using short one-character variable names makes your robot go super fast.",
                "select": "true"
            },
            {
                "text": "The two easiest things in programming are cache invalidation and naming things.",
                "select": "true"
            }
        ],
        "type": "select_multi"
    },
    {
        "question": "Using robot templates to kickstart your projects:",
        "response": [
            {
                "text": "Ensures you have a working foundation to build on.",
                "select": "true"
            },
            {
                "text": "Is a great idea as long as you understand what the template provides and how it works.",
                "select": "true"
            },
            {
                "text": "Should always be avoided.",
                "select": "true"
            },
            {
                "text": "Is only meant for beginners. Professionals never use templates, ever.",
                "select": "true"
            }
        ],
        "type": "select_multi"
    },
    {
        "question": "Choose all that apply:",
        "response": [
            {
                "text": "Breaking code down into smaller pieces is a software development best practice.",
                "select": "true"
            },
            {
                "text": "Placing all your robot code in a single file is always the best option, no matter how much code you have.",
                "select": "true"
            },
            {
                "text": "Duplicating code makes it easier to maintain your project.",
                "select": "true"
            },
            {
                "text": "\"Don't repeat yourself\" principle is about avoiding duplication.",
                "select": "true"
            },
            {
                "text": "Opportunistic refactoring means any time someone sees code that isn't as clear as it should be, they should take the opportunity to fix it right there and then.",
                "select": "true"
            }
        ],
        "type": "select_multi"
    },
    {
        "question": "Choose all that apply:",
        "response": [
            {
                "text": "It is best to implement the full robot before testing it to catch all the issues at the same time.",
                "select": "true"
            },
            {
                "text": "Implementing your robot in small increments and testing it often is important.",
                "select": "true"
            },
            {
                "text": "The conda.yaml configuration file defines the tasks of the robot.",
                "select": "true"
            }
        ],
        "type": "select_multi"
    },
    {
        "question": "If you want to store files in Control Room's artifacts section, your robot should place the files:",
        "response": [
            {
                "text": "Inside the devdata folder.",
                "select": "true"
            },
            {
                "text": "On your desktop.",
                "select": "false"
            },
            {
                "text": "At the root of the robot folder.",
                "select": "false"
            },
            {
                "text": "On your external hard drive.",
                "select": "false"
            },
            {
                "text": "Inside the output folder defined in the robot.yaml configuration file.",
                "select": "false"
            }
        ],
        "type": "select_single"
    },
    {
        "question": "Choose all that apply:",
        "response": [
            {
                "text": "You can use Python libraries to transform data.",
                "select": "true"
            },
            {
                "text": "You can use RPA Framework libraries to transform data.",
                "select": "true"
            },
            {
                "text": "You can write your own libraries to transform data.",
                "select": "true"
            },
            {
                "text": "The free version of Robocorp does not support data transformation.",
                "select": "true"
            }
        ],
        "type": "select_multi"
    },
    {
        "question": "Choose all that apply:",
        "response": [
            {
                "text": "The RPA.Tables library supports grouping data.",
                "select": "true"
            },
            {
                "text": "The RPA.Tables library supports writing a table into CSV.",
                "select": "true"
            },
            {
                "text": "The RPA.Tables library supports merging tables.",
                "select": "true"
            },
            {
                "text": "The RPA.Tables library supports filtering data.",
                "select": "true"
            },
            {
                "text": "The RPA.Tables library supports sorting data.",
                "select": "true"
            },
            {
                "text": "The RPA.Tables library supports finding rows that match a condition for a given column.",
                "select": "true"
            }
        ],
        "type": "select_multi"
    },
    {
        "question": "The RPA Framework library that provides work item support is called:",
        "response": [
            {
                "text": "RPA.Robocorp.WorkDataManagement",
                "select": "true"
            },
            {
                "text": "RPA.Robocloud.Stuffs",
                "select": "false"
            },
            {
                "text": "RPA.Robocorp.WorkItems",
                "select": "false"
            },
            {
                "text": "RPA.JSON",
                "select": "false"
            },
            {
                "text": "RPA.Robo.Hobbitses",
                "select": "false"
            }
        ],
        "type": "select_single"
    },
    {
        "question": "In local development:",
        "response": [
            {
                "text": "Work items are stored as one YAML file, one entry per work item.",
                "select": "true"
            },
            {
                "text": "Work items are stored as one CSV file, one row per work item.",
                "select": "false"
            },
            {
                "text": "Work items are stored as a JSON file, one file per producer robot run.",
                "select": "false"
            },
            {
                "text": "Work items are stored as separate CSV files, one file per work item.",
                "select": "false"
            }
        ],
        "type": "select_single"
    },
    {
        "question": "To loop through all the available work items:",
        "response": [
            {
                "text": "One implements a FOR loop and loads the work items one by one by calling the Load Work Item keyword.",
                "select": "true"
            },
            {
                "text": "One uses the For Each Input Work Item keyword.",
                "select": "false"
            },
            {
                "text": "One loads the work items one by one by calling the Load Work Item keyword.",
                "select": "false"
            },
            {
                "text": "One implements a WHILE loop and loads the work items one by one by calling the Load Work Item keyword.",
                "select": "false"
            }
        ],
        "type": "select_single"
    },
    {
        "question": "If you want to use Python code in your Robot Framework robot:",
        "response": [
            {
                "text": "Your only option is to implement a custom Python library and import it into your robot.",
                "select": "true"
            },
            {
                "text": "You need to install Java Runtime Environment.",
                "select": "false"
            },
            {
                "text": "You can use the Evaluate keyword to evaluate Python expressions.",
                "select": "false"
            },
            {
                "text": "Your only option is to implement all of the robot in Python.",
                "select": "false"
            }
        ],
        "type": "select_single"
    },
    {
        "question": "Choose all that apply:",
        "response": [
            {
                "text": "As part of a POST request, an arbitrary amount of data of any type can be sent to the server in the body of the request message.",
                "select": "true"
            },
            {
                "text": "By design, the POST request method requests that a web server accept the data enclosed in the body of the request message, most likely for storing it.",
                "select": "true"
            },
            {
                "text": "The RPA.Request.Post library is used for making POST requests.",
                "select": "true"
            }
        ],
        "type": "select_multi"
    },
    {
        "question": "To get both the status and the return value or an error message from a keyword call, you can use:",
        "response": [
            {
                "text": "Run Keyword If",
                "select": "true"
            },
            {
                "text": "Run Keyword And Expect Error",
                "select": "false"
            },
            {
                "text": "Run Keyword And Return Status",
                "select": "false"
            },
            {
                "text": "Run Keyword And Continue On Failure",
                "select": "false"
            },
            {
                "text": "Run Keyword And Ignore Error",
                "select": "false"
            }
        ],
        "type": "select_single"
    },
    {
        "question": "When you want to mark work item as completed, you:",
        "response": [
            {
                "text": "Set it free.",
                "select": "true"
            },
            {
                "text": "Release it.",
                "select": "false"
            },
            {
                "text": "Use the Mark Work Item As Completed keyword.",
                "select": "false"
            },
            {
                "text": "Hug it and say goodbye.",
                "select": "false"
            },
            {
                "text": "Let it out of the door into the wilderness.",
                "select": "false"
            }
        ],
        "type": "select_single"
    },
    {
        "question": "The Release Input Work Item keyword supports the following arguments (choose all that apply):",
        "response": [
            {
                "text": "complete",
                "select": "true"
            },
            {
                "text": "message",
                "select": "true"
            },
            {
                "text": "fail",
                "select": "true"
            },
            {
                "text": "code",
                "select": "true"
            },
            {
                "text": "exception_type",
                "select": "true"
            },
            {
                "text": "pass",
                "select": "true"
            },
            {
                "text": "state",
                "select": "true"
            }
        ],
        "type": "select_multi"
    },
    {
        "question": "Work items support the following exception types (choose all that apply):",
        "response": [
            {
                "text": "SOFTWARE",
                "select": "true"
            },
            {
                "text": "APPLICATION",
                "select": "true"
            },
            {
                "text": "UI",
                "select": "true"
            },
            {
                "text": "API",
                "select": "true"
            },
            {
                "text": "DATABASE",
                "select": "true"
            },
            {
                "text": "BUSINESS",
                "select": "true"
            }
        ],
        "type": "select_muliti"
    }
]