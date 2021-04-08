# Restful Toys

This is an experimental project to test Django Rest Framework. This application offers a rich API for collecting Toys.

## API

| HTTP verb | Scope              | url        | Semantics                                                                               |
| --------- | ------------------ | ---------- | --------------------------------------------------------------------------------------- |
| GET       | Toy                | /toys/<id> | Retrieve a single toy                                                                   |
| GET       | Collection of toys | /toys/     | Retrieve all the stored toys in the collection, sorted by their name in ascending order |
| POST      | Collection of toys | /toys/     | Create a new toy in the collection                                                      |
| PUT       | Toy                | /toys/<id> | Update an existing toy                                                                  |
| DELETE    | Toy                | /toys<id>  | Delete an existing toy                                                                  |

## The Database Model

#### Data Feilds
* `name`
* `description`
* `category`
* `release_date`

Additionally feild named `Created` would store the date and time at wich a particular data object is created.

#### Database Structure

| Feild        | Type     | Size | Required |
| ------------ | -------- | ---- | -------- |
| name         | Char     | 150  | Yes      |
| description  | Char     | 250  | No       |
| category     | Char     | 200  | Yes      |
| release_date | dateTime |      | No       |
| created      | dateTime |      | Auto     |



## Project Setup

### Project Requirements

`Python 3.x`

### Setup

1. Install all requirements from `requirements.txt` file with the command
    ```
    pip install -r requirements.txt
    ```
2. Start the Django development server with the command
    ```
    python manage.py runserver
    ```
