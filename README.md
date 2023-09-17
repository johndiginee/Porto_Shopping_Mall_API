# Porto Shopping Mall API 
Porto Shopping Mall API is an eCommerce store API that allows different software applications to communicate and interact with their platform. This API enables the exchange of data and functionality (such as product, inventory, cart, and customer management, order processing, etc) between their store and other systems, such as mobile apps, third-party software, payment gateways, and more.

## API Features

### User Authentication
* Register user
* Login user
* Change password
* Password reset request
* Password reset confirmation
* Refresh token
* Logout user

### User Profile
* Current user profile
* Update user profile

### Product
* Create product
* Upload product image
* Delete product
* Update product
* List all products
* Get single product

### Order
* Create order
* Get all orders
* Get single order
* Delete order
* Make payment
* Process order

### Review
* Create product review
* Update product review
* Delete product review

## Technologies Used
 * Django
 * Django Rest Framework
 * JWT Authentication
 * Mailtrap
 * Stripe
 * Amazon S3
 * Postgres
 * Github Actions (Continuous Integration/Continuous Deployment)
 * Digital Ocean
 * DRF-YASG (API Documentation)
 * Insomnia

## API Documentation


## Installation on local machine

```bash
git clone https://github.com/johndiginee/Porto_Shopping_Mall_API.git
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
Set DEBUG = True in settings.py
```
```bash
python3 manage.py makemigrations
```
```bash
python3 manage.py migrate
```
```bash
python3 manage.py runserver
```

Create a .env file and set:
```bash
SECRET_KEY =
DEBUG =

AWS_ACCESS_KEY_ID =
AWS_SECRET_ACCESS_KEY =
AWS_STORAGE_BUCKET_NAME =
AWS_S3_REGION_NAME =

EMAIL_HOST = 
EMAIL_HOST_USER = 
EMAIL_HOST_PASSWORD =
EMAIL_PORT = 

STRIPE_PUBLIC_KEY =
STRIPE_PRIVATE_KEY =
STRIPE_WEBHOOK =
```

## Author
John Diginee - [LinkedIn](https://www.linkedin.com/in/johndiginee/) / [X](http://x.com/johndiginee) / [Person Site](https://johndiginee.com)

## Acknowledgements
[Holberton School](https://www.holbertonschool.com/), [ALX Africa](https://www.alxafrica.com/) (Mentors, Staff and Students) & [Mastercard Foundation](https://mastercardfdn.org/)