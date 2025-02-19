## Installation and Setup


1. **Clone the repository:**
    ```bash
    git clone https://github.com/s-nishad/pathao_assessment
    cd pathao_assessment
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate   # Windows
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
   
4. **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```
   
## END points are:
  
Post request to create user: http://localhost:8000/users/

Get request with id to get a user: http://localhost:8000/users/1

Post request to add tag with user id, tag name and expiry: http://localhost:8000/users/1/tags
[use swagger to input tag]

Get user by tag: http://localhost:8000/user/?tags=abc,xyz

## Swagger link for all api: http://localhost:8000/docs/
