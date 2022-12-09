# LogLess

**LogLess** is an automated and hassle-free logging mechanism that generates logs of serverless applications for developers.
 
There automated logs can be used by developers for tracking the execution workflow and debugging without writing any logging statements manually.

### For Serverless Platforms
Current logging mechanisms in serverless platforms can sometimes become cumbersome for developers. 
In case of any failures or debugging, spotting the issues can become difficult due to inadequate logging. 

Additionally, the auto-generated system-wide logs, by cloud platforms, are not descriptive enough to help debug an application error. 
There are indeed some logging tools and utilities available in the market, which can be configured to an application’s needs. 
However, they still need developers to write the logging statements apart from the code.

### Serverless & Beyond...
Apart from Serverless application, LogLess can be conveniently used for logging any Python based application.

## Requirements
This project requires the following installations:
```
Python 3.7+
```

## Setup
Follow these steps for project setup:

1. Clone the repository
```
git clone https://github.com/kushagrasoni/LogLess_Logging.git
```
2. Set up a virtual environment after switching into the project repository
```
cd LogLess_Logging
python3 -m venv venv
```
3. Activate the virtual environment
```
source venv/bin/activate
```
4. Install requirements
```
pip3 install -r requirements.txt
```

## LogLess Usage

LogLess provides a set of sample lambda applications that can be tested locally. Each application has been applied with the the logless decorator and predefined configurations. In order to the test the existing applications without custom configurations, follow the steps below:

1. Change directory into the application of interest
```
cd {appX}
```
- Substitute {appX} with the name of an application directory (For example: ```app1``` to test the application in the app1 directory)

2. Run the following command
```
python-lambda-local -f {name_of_function} {name_of_app_file} {name_of_event_file}
```
- Substitute {name_of_function} with the name of the application function in that directory (For example: ```lambda_handler```)

- Substitute {name_of_app_file} with the name of the application file (For example: ```sample_app1.py```)

- Substitute {name_of_event_file} with the name of the event json file (For example: ```event.json```)

If you want to customize the configurations for an application under test, the decorator can be updated to accept from a set of arguments. Reference the decorator function for the details on the arguments.

## Automated Testing

Execute the testing suite.
```
pytest -v
```

## Code Coverage

1. Run the testing suite under coverage.
```
coverage run -m pytest -v tests
```
2. Report the results in an HTML page.
```
coverage html
```
3. Open the `htmlcov/index.html` file in a browser to view the results.

## Citations

The following open-source projects are referenced for this project:
- https://github.com/cool-RR/PySnooper
