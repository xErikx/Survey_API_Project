# Django API for user surveys purpose
Current API is developed to gather and manage users surveys in the system

# Project environment
- Python 3.9.6
- Django 2.2.10
- django-extensions 3.1.0
- djangorestframework 3.12.2
## To install requirements use the following command:
```
pip3 install -r requirements.txt
```

# System Admin Functions
- authorization in the system 
- add / change / delete polls. 
- Survey attributes: title, start date, end date, description. After creation, the field "start date" for the survey cannot be changed
- adding / changing / deleting questions in the survey. 
- Question attributes: question text, question type (text answer, single choice answer, multiple choice answer)

# System User Functions
- getting a list of active surveys
- taking a survey: surveys can be completed anonymously, a numeric ID is passed to the API as a user identifier, by which the user's answers to questions are stored; one user can participate in any number of surveys
- getting the surveys completed by the user with details on the answers (what is selected) by the unique user ID

# Login description
## To login as superuser use the following options:
- Default Admin username: Admin_user
- Default Admin password: password123
```
curl --location --request GET 'http://localhost:8000/api/login/' \
--form 'username=%username' \
--form 'password=%password'
```
If you want to create new superuser, use following command:
```
python manage.py createsuperuser
```

# API Documentation

## Get User's token:
* Request method: GET
* URL: http://localhost:8000/api/login/
* Body: 
    * username: 
    * password: 
* Sample:
```
curl --location --request GET 'http://localhost:8000/api/login/' \
--form 'username=%username' \
--form 'password=%password'
```
## Create Survey:
* Request method: POST
* URL: http://localhost:8000/api/apiApp/survey/create/
* Header:
   *  Authorization: Token user_token
* Body:
    * survey_name: name of survey
    * pub_date: publication date can be set only when survey is created
    * end_date: survey end date
    * survey_description: description of survey
* Sample: 
```
curl --location --request POST 'http://localhost:8000/api/apiApp/survey/create/' \
--header 'Authorization: Token %user_token' \
--form 'survey_name=%survey_name' \
--form 'pub_date=%pub_date' \
--form 'end_date=%end_date \
--form 'survey_description=%survey_description'
```

## Delete Survey:
* Request method: DELETE
* URL: http://localhost:8000/api/apiApp/delete/[survey_id]
* Header:
    * Authorization: Token user_token
* Param:
    * survey_id
* Sample:
```
curl --location --request DELETE 'http://localhost:8000/api/apiApp/update/[survey_id]/' \
--header 'Authorization: Token %user_token'
```

## Update Survey:
* Request method: PATCH
* URL: http://localhost:8000/api/apiApp/update/[srv_id]/
* Header:
    * Authorization: Token user_token
* Param:
    * survey_id 
* Body:
    * survey_name: name of survey
    * end_date: survey end date
    * survey_description: description of survey
* Sample:
```
curl --location --request PATCH 'http://localhost:8000/api/apiApp/update/[survey_id]/' \
--header 'Authorization: Token %user_token' \
--form 'survey_name=%srv_name' \
--form 'end_date=%end_date \
--form 'survey_description=%srv_description'
```

## Overview Surveys:
* Request method: GET
* URL: http://localhost:8000/api/apiApp/survey/view/
* Header:
    * Authorization: Token user_token
* Sample:
```
curl --location --request GET 'http://localhost:8000/api/apiApp/survey/view/' \
--header 'Authorization: Token %user_token'
```

## View active surveys:
* Request method: GET
* URL: http://localhost:8000/api/apiApp/view/active/
* Header:
    * Authorization: Token user_token
* Sample:
```
curl --location --request GET 'http://localhost:8000/api/apiApp/view/active/' \
--header 'Authorization: Token %user_token'
```

## Create Question:
* Request method: POST
* URL: http://localhost:8000/api/apiApp/question/create/
* Header:
    * Authorization: Token user_oken
* Body:
    * survey_id: id of survey 
    * question_text: 
    * question_type: can be only 'one', 'multiple' or 'text'
* Sample:
```
curl --location --request POST 'http://localhost:8000/api/apiApp/question/create/' \
--header 'Authorization: Token %user_token' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

## Delete Question:
* Request method: DELETE
* URL: http://localhost:8000/api/apiApp/question/update/[question_id]/
* Header:
    * Authorization: Token user_token
* Param:
    * question_id
* Sample:
```
curl --location --request DELETE 'http://localhost:8000/api/apiApp/question/update/[question_id]/' 
```

## Update Question:
* Request method: PATCH
* URL: http://localhost:8000/api/apiApp/question/update/[question_id]/
* Header:
    * Authorization: Token user_token
* Param:
    * question_id
* Body:
    * survey: id of survey 
    * question_text: question
    * question_type: can be only `one`, `multiple` or `text`
* Sample:
```
curl --location --request PATCH 'http://localhost:8000/api/apiApp/question/update/[question_id]/' \
--header 'Authorization: Token %user_token' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

## Create Choice:
* Request method: POST
* URL: http://localhost:8000/api/choice/create_choice/
* Header:
    * Authorization: Token user_token
* Body:
    * question_id: id of question
    * choice_text: choice
* Sample:
```
curl --location --request POST 'http://localhost:8000/api/apiApp/choice/create/' \
--header 'Authorization: Token %user_token' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

## Delete Choice:
* Request method: DELETE
* URL: http://localhost:8000/api/apiApp/choice/update/[choice_id]/
* Header:
    * Authorization: Token user_token
* Param:
    * choice_id
* Sample:
```
curl --location --request DELETE 'http://localhost:8000/api/choice/delete_choice/[choice_id]/'
```

## Update Choice:
* Request method: PATCH
* URL: http://localhost:8000/api/apiApp/choice/update/[choice_id]/
* Header:
    * Authorization: Token user_token
* Param:
    * choice_id
* Body:
    * question: id of question
    * choice_text: choice
* Sample:
```
curl --location --request PATCH 'http://localhost:8000/api/apiApp/choice/update/[choice_id]/' \
--header 'Authorization: Token %user_token' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

## Create Answer:
* Request method: POST
* URL: http://localhost:8000/api/apiApp/answer/create/
* Header:
    * Authorization: Token user_token
* Body:
    * survey_id: id of survey
    * question_id: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Sample:
```
curl --location --request POST 'http://localhost:8000/api/apiApp/answer/create/' \
--header 'Authorization: Token %user_token' \
--form 'survey=%survey' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

## Delete Answer:
* Request method: DELETE
* URL: http://localhost:8000/api/apiApp/answer/update/[answer_id]/
* Header:
    * Authorization: Token user_token
* Param:
    * answer_id
* Sample:
```
curl --location --request DELETE 'http://localhost:8000/api/apiApp/answer/update/[answer_id]' \
--header 'Authorization: Token %user_token'
```

## Update Answer:
* Request method: PATCH
* URL: http://localhost:8000/api/apiApp/answer/update/[answer_id]/
* Header:
    * Authorization: Token user_token
* Param:
    * answer_id
* Body:
    * survey: id of survey
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Sample:
```
curl --location --request PATCH 'http://localhost:8000/api/apiApp/answer/update/[answer_id]' \
--header 'Authorization: Token %user_token' \
--form 'survey=%survey' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

## View User's Answer:
* Request method: GET
* URL: http://localhost:8000/api/apiApp/answer/view/[user_id]/
* Param:
    * user_id
* Header:
    * Authorization: Token user_token
* Sample:
```
curl --location --request GET 'http://localhost:8000/api/apiApp/answer/view/[user_id]' \
--header 'Authorization: Token %user_token'
