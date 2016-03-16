# BRS - Books Review System

Project training how to use django

## Installation

* [Environment](http://askubuntu.com/questions/244641/how-to-set-up-and-use-a-virtual-python-environment-in-ubuntu)

## Usage

1. Create virtualenv
	* mkvirtualenv name_virtualenv
	* workon name_virtualenv
2. Install environment with requirements.txt
	* pip install requirements.txt
3. Migrate database
	* python manage.py migrate
4. Create superuser
	* python manage.py createsuperuser (user login admin)
5. Copy file and folder in folder data_test to folder root.
6. Dumpdata and loaddata
	* python manage.py dumpdata > [name.json]
	* python manage.py loaddata [name.json]
7. Run
	* python manage.py runserver [port] (default: 8000)

## Task Admin
	1. Login
		1. Signin, Signout
	2. Profile
		1. Change profile
		2. Change password
	3. User
		1. List all user register
		2. Delete user
		3. View detail user
	4. Book
		1. List all book
		2. View detail book
		3. Add, edit, delete book
	5. Request
		1. List all request
		2. View detail request
		3. Update, delete request

## Task User
	1. Can register for app 
	2. Can signin, signout
	3. Can see the list of all books
	4. Can search books by title, category, rating, favorite, etc.
	5. Can rate and write a review for book (also can edit, delete it)
	6. Can comment to a review (also can edit, delete it)
	7. Can mark a book as reading, read, favorite
	8. Can see reading history
	9. Can follow/unfollow other users
	10. Can send admin a request to buy a new book (also can cancel it)
	11. Can see the list of the requests he/she sent

## License

MIT
