# 3️⃣5️⃣ Day - 35
## Pytest Markers

### Topics Covered
Parameterization, Markers, Custom markers, pytest.ini file

#### Folder Structure
Day_35/
├── tests/
│   ├── test_login_creds.py
│   ├── test_product_cart.py
│   └── test_checkout_validation.py
├── marker_tests/
│   ├── test_smoke_login.py
│   ├── test_smoke_add_product.py
│   └── test_smoke_checkout.py
├── regression_tests/
│   ├── test_regression_login.py
│   ├── test_regression_add_product.py
│   └── test_regression_checkout.py
├── conftest.py
├── pytest.ini

#### Tasks
- Parameterize the valid login
- Parameterize the invalid login
- Parameterize the product validation
- Use smoke and regression