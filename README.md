
# Little Lemon Backend Project with Django

This project implements the backend functionality for **Little Lemon**, a restaurant management system. It includes features for managing menu items, user authentication, and API endpoints, along with comprehensive unit testing.

## Features

1. **Menu Management**
   - CRUD operations for menu items.
   - String representation of menu items in the format: `"<title> - $<price> (<inventory> in stock)"`.

2. **User Authentication**
   - Supports token-based authentication using Django REST Framework (DRF).
   - Djoser library for easy user management and authentication endpoints.

3. **API Endpoints**
   - Provides a browsable API for CRUD operations on menu items.

4. **Unit Testing**
   - Automated testing for models and views.
   - Ensures API responses match expected data.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/little-lemon-backend.git
   cd little-lemon-backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Testing

Run the test suite using the following command:
```bash
python manage.py test
```

### Example Test Structure

#### `test-models.py`
Tests the string representation of the `Menu` model:
```python
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream - $80.00 (100 in stock)")
```

#### `test-views.py`
Tests the API endpoints for `Menu`:
```python
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Pasta", price=90, inventory=30)

    def test_get_all(self):
        response = self.client.get("/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
```

## Authentication Endpoints (Djoser)

| Endpoint          | Description                |
|-------------------|----------------------------|
| `/token/login/`   | User login with token.     |
| `/users/me/`      | Retrieve user information. |


## Contribution Guidelines

1. Fork the repository and create a feature branch.
2. Write tests for new features.
3. Ensure all tests pass before submitting a pull request.


