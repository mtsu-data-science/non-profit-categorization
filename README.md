# Non-Profit Categorization

This repository is meant for the collaboration around producing meaningful categorizations for non-profits using their tax descriptions.

## Overview

In the United States, there are over 1.5 million non-profit organizations, ranging in services from homeless shelters to professional organizations. Though they all offer much needed services, most of them are difficult to locate and go largely unnoticed by those who need them. Additionally, very few of them work together to offer a suite of services, that if offered, would provide a person with the support, skills training, and connections necessary to help them. [Project Maslow](https://www.projectmaslow.org/) is connecting the non-profit network and making their services available for anyone who seeks assistance or growth. And by connecting non-profit services thoughtfully, we are using data analytics and AI, we will be able to help individuals plot a path to anywhere they wish to go. Project Maslow's mission is to connect people, resources, and community to create endless opportunity.

For this project, since non-profit organizations operate using mission statements and they don’t have the published service categories that are needed, we will be helping determine what services are offered using tax data from the IRS for all non-profits that have applied for non-profit status in the US over the last 7 years. The data set is large and in free-form text, describing multiple non-profit businesses. Since Project Maslow will require knowing what services are offered by the non-profits in the non-profit network, we will use natural language processing and any other tools at your disposal to categorize these great organizations using their descriptions and you will plot them geographically based on their locations. Project Maslow will use the results to launch their first functioning prototype.

## Onboarding

### Environment

Modeling in this project will be done in Python with the environment being managed with [python-poetry](https://python-poetry.org/).

Initially, if working in Windows, you will need to use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about) to install and set up the environment.  Down the road we can explore working natively in Windows but for now, this project will be initially built out in MacOS/Linux.

### Code Tooling

The following tools will be used to help ensure code quality:

* Black - This is a code formatting tool that ensures all code is formatting consistently. This only applies to *.py files.
* flake8 - This is a code linting tool that takes care of the code following standards
* isort - This takes care of ensuring script imports are sorted consistently
* precommit - This is a utility that will run a series of checks prior to each commit.

A suggested IDE will be [VS Code](https://code.visualstudio.com/) but this is optional.

### Environment Setup

Prior to running the python setup commands, the following needs to be done:

* Install a Python version consistent with ">=3.10,<3.11"
* Install poetry and pre-commit `pip install poetry pre-commit`
* Once the above criteria are met, run `make get-started`


### Exploring SageMaker Studio Lab Support

[SageMaker Studio Lab](https://studiolab.sagemaker.aws/) is a free service provided by AWS which gives access to an online notebook service for working in Python Jupyter Notebooks.  We are exploring this as an option for folks to either start with as they are getting onboarded to the project or in situations where someone does not have a powerful enough of a computer, can use this as a permanent option.  Initially this will only be intended for working in notebooks since the necessary development tools for running black, isort, pre-commit, and pytest have not yet been added.
