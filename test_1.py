import requests
import pytest

# API url
base_url = "https://jsonplaceholder.typicode.com"


# Submit a GET request to https://jsonplaceholder.typicode.com/posts
# Positive case of get the posts
def test_case_1():
    response = requests.get(base_url + "/posts")
    response_body = response.json()
    print(response.status_code)


# Submit a GET request to https://jsonplaceholder.typicode.com/posts
# Negative case of get the posts
def test_case_2():
    response = requests.get(base_url + "/posts")
    response_body = response.json()
    # Access to list items
    index = response_body[1]
    # Access to dictionary items
    access = index.get("email")
    print(access)
    print(response.status_code)


# Submit a GET request to https://jsonplaceholder.typicode.com/posts/1
# Positive case of get the posts_1
def test_case_3():
    response = requests.get(base_url + "/posts")
    response_body = response.json()
    # Access to list items
    index = response_body[0]
    # Access to dictionary items
    access = index.get("userId")
    print(access)
    print(response.status_code)


# Submit a GET request to https://jsonplaceholder.typicode.com/posts/1
# negative case of get the posts/1
def test_case_4():
    response = requests.get(base_url + "/posts")
    response_body = response.json()
    # Access to list items
    index = response_body[0]
    # Access to dictionary items
    access = index.get("name")
    print(access)
    print(response.status_code)


# Submit a GET request to https://jsonplaceholder.typicode.com/comments?postId=1
# Positive case of get comments postid = 1
def test_case_5():
    response = requests.get(base_url + "/comments")
    response_body = response.json()
    # Access to list items
    index = response_body[0]
    # Access to dictionary items
    access = index.get("postId")
    print(access)
    print(response.status_code)


# Submit a GET request to https://jsonplaceholder.typicode.com/comments?postId=1
# Negative case of get comments post id = 1
def test_case_6():
    response = requests.get(base_url + "/comments")
    response_body = response.json()
    # Access to list items
    index = response_body[0]
    # Access to dictionary items
    access = index.get("title")
    print(access)
    print(response.status_code)


# Submit a POST request to https://jsonplaceholder.typicode.com/posts
# to create a new post with a title, body and associated user ID (1-10)
# Check that the response status code equals HTTP 201 (Created)
def test_case_7():
    new_post = {
        "title": "My new post title",
        "body": "My new post body",
        "userId": 1
    }
    response = requests.post(base_url + "/posts", json=new_post)
    response_body = response.json()
    print(response.status_code)


# Negative case of create a new post in posts
def test_case_8():
    new_post = {
        "title": "new post title",
        "body": " new post body",
        "userId": 2
    }
    response = requests.post(base_url + "//posts//id")
    response_body = response.json()
    print(response.status_code)


# Positive case of delete the posts/1
def test_case_9():
    response = requests.delete(base_url + "/posts/1")
    print(response.status_code)


# Negative case of delete the posts/1
def test_case_10():
    response = requests.delete(base_url + "//posts")
    response_body = response.json()
    print(response.status_code)


