<h1 align="center" >E-Library Web Site <a style="color: red;" href="https://www.github.com/shyamkumaryadav/E_library" target="_blank" >&copy;</a></h1>

![version](https://img.shields.io/github/v/release/shyamkumaryadav/E_library?style=for-the-badge) ![Star](https://img.shields.io/github/stars/shyamkumaryadav/E_library?style=for-the-badge) ![Licence](https://img.shields.io/apm/l/vim-mode?style=for-the-badge) ![last-commit](https://img.shields.io/github/last-commit/shyamkumaryadav/E_library?style=for-the-badge) ![twitter](https://img.shields.io/twitter/follow/shyamkumaryada?logo=Twitter&style=for-the-badge) ![Size Repo](https://img.shields.io/github/repo-size/shyamkumaryadav/E_library?style=for-the-badge)

### *Requirements*
#####    ```python programming (Django)```
#####     ```PostgreSQL (From Heroku) or SQlite```
#####     ```HTML CSS JavaScript```
#####     ```GIT```

### *About*
##### ```This web project is a E-library system with all the basic as well as some innovative features for managing a library. It consists of a large database of various books available in the library. It also lists various books issued to respective readers.If the reader needs a book, he can order the book request for home delivery by just submitting an online form.```

### *Installation*
#####    ```git clone https://github.com/shyamkumaryadav/E_library.git```  
#####     ```cd E_library```  
#####     ```pipenv shell or https://duckduckgo.com/?q=python+make+virtual+environment```  
#####     ```pipenv install or (venv)$ pip install -r requirements.txt```  
#####     ```pipenv run server or (venv)$ python src/manage.py runserver```  

### *Data Link*
#### [Book Author](Data/BookAuthor.json)
#### [Book Publisher](Data/Bookpublish.json)
#### [Book](Data/Book.json)

### *Detail*
     0. Admin login -- Admin can add or remove books from the system and also maintains records of the book available and issued in the library.
     1. User login -- User has to first create an account in the system to gain access.
     3. Tracking the user record -- The system can track the period for which the book has been issued to user and calculates fine if the book is not returned on time.
     4. Quantity Update -- The quantity is updated by the system depending on the quantity ordered.
     5. Fine calculation -- If the user is unable to return the book, the system automatically calculates the fine that the user has to pay for subsequent days.
     6. View date info -- The user can view the date when he has issued the book as well as the expiry date of the book and can view fine to be paid that is calculated by the system.
     7. Online search and order form -- The user may order the book online.


#### *Live At*    [https://shyamkumaryadav.herokuapp.com/](https://shyamkumaryadav.herokuapp.com/)
