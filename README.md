# Url Shortner


This url shortner is implemented by using a hashing technique such that every requested url to short is stored in a RDBMS table sequentially. Then I converted the primary key (int) to a hash code using base 62 conversion(More in base 62 conversion is explained below). This hash is used in shorten url. I have implemented another base 10 conversion method that will take a hash code as input and then it will convert it to a integer/long number. This base 10 converted number is the primary key of that table using which we can get the main url that was shorten.

## What is base 62 conversion

This is called base 62 because we use 0-9 integers, A-Z capital alphabets and a-z small alphabets which when combined returns us 62. This means we can get a total of 2^62 combinations i.e. 4611686018427387904 times we can use before coming acroes any collisions.

---

# FAQ

#### 1: Will it handle collisions?
As we know it is based on a hash conversion of base 62, i.e 4611686018427387904 combinations possible hence we don't need to handle collsions

#### 2: Will the shortend url ever expire?
No

#### 3: Can we use other shorten url methods like bit.ly or tiny.url instead of what is being provided in this codebase?
Yes. I have followed a design pattern OOP concept which will allow to use whatever type of concrete class you want to use

#### 4: Does this API given in the code base support user based token authentication?
No, not yet

---

# Installation and demo
    # Python 3 is required
    git clone git@github.com:am1tyadava/url_shortner.git
    cd url_shortner
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver


