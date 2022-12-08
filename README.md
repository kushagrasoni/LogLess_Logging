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

## Setup

TODO - Describe cloning repository, virtual env setup, and installing dependencies.

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

## Application Testing

TODO - Describe how to test each example application (appX) that is in this repository.

## Citations

The following open-source projects are referenced for this project:
- https://github.com/cool-RR/PySnooper
