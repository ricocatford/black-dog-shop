[# Testing

## 1. Functionality

I've performed regular manual tests throughout development for the usability and performance of the website. Below you
can find all tests performed to the different elements and features. All tests were carried out in Chrome browser which
is
my preferred one and the most used nowadays. Also, I've performed some of these tests in Microsoft Edge, Mozilla Firefox
and Safari to
ensure it's working as expected in other browsers.

### Navbar

| **Element / Feature**       |  **Test performed**   | **Result**                                                             | **Pass / Fail** |
|:----------------------------|:---------------------:|:-----------------------------------------------------------------------|:---------------:|
| **Brand logo**              |        Clicked        | Goes to Home page                                                      |    **Pass**     |
| **All products link**       |        Clicked        | Goes to Products catalog page                                          |    **Pass**     |
| **Clothing link**           |        Clicked        | Opens up dropdown list with corresponding categories                   |    **Pass**     |
| **Skateboards link**        |        Clicked        | Opens up dropdown list with corresponding categories                   |    **Pass**     |
| **Categories links**        |        Clicked        | Goes to Products catalog page filtering only for the selected category |    **Pass**     |
| **Product management link** |        Clicked        | Goes to Add a Product page (shows only for Admin/Superusers)           |    **Pass**     |
| **My Profile link**         |        Clicked        | Goes to User's Profile page (shows only for Registered users)          |    **Pass**     |
| **Shopping Bag link**       |        Clicked        | Goes to Shopping Bag page                                              |    **Pass**     |
| **Register link**           |        Clicked        | Goes to Sign up page                                                   |    **Pass**     |
| **Login link**              |        Clicked        | Goes to Sign in page                                                   |    **Pass**     |
| **Logout link**             |        Clicked        | Goes to Sign out page                                                  |    **Pass**     |
| **Search bar**              | Searched for 'Volcom' | Shows all products containing 'Volcom' in name and/or description      |    **Pass**     |

### Footer

| **Element / Feature** |     **Test performed**     | **Result**                                                             | **Pass / Fail** |
|:----------------------|:--------------------------:|:-----------------------------------------------------------------------|:---------------:|
| **Home link**         |          Clicked           | Goes to Home page                                                      |    **Pass**     |
| **All products link** |          Clicked           | Goes to Products catalog page                                          |    **Pass**     |
| **My Profile link**   |          Clicked           | Goes to User's Profile page (only for Registered users)                |    **Pass**     |
| **Shopping Bag link** |          Clicked           | Goes to Shopping Bag page                                              |    **Pass**     |
| **Register link**     |          Clicked           | Goes to Sign up page                                                   |    **Pass**     |
| **Login link**        |          Clicked           | Goes to Sign in page                                                   |    **Pass**     |
| **Logout link**       |          Clicked           | Goes to Sign out page                                                  |    **Pass**     |
| **Instagram link**    |          Clicked           | Goes to Instagram website                                              |    **Pass**     |
| **Facebook link**     |          Clicked           | Goes to Facebook website                                               |    **Pass**     |
| **Twitter link**      |          Clicked           | Goes to Twitter website                                                |    **Pass**     |
| **Search bar**        | Searched for 'Independent' | Shows all products containing 'Independent' in name and/or description |    **Pass**     |

### Register page

| **Element / Feature**             |         **Test performed**         | **Result**                                                        | **Pass / Fail** |
|:----------------------------------|:----------------------------------:|:------------------------------------------------------------------|:---------------:|
| **Form**                          | Filled up with new account details | Works as expected                                                 |    **Pass**     |
| **Already have an account? link** |              Clicked               | Goes to Sign in page                                              |    **Pass**     |
| **New account**                   |        Created new account         | Creates new account and redirects to Email verification sent page |    **Pass**     |
| **Email verification link**       |              Clicked               | Activates the account and redirects to Confirm email page         |    **Pass**     |

### Confirm email page

| **Element / Feature** | **Test performed** | **Result**                                   | **Pass / Fail** |
|:----------------------|:------------------:|:---------------------------------------------|:---------------:|
| **Confirm button**    |      Clicked       | Confirms email and redirects to Sign in page |    **Pass**     |

### Sign in page

| **Element / Feature**     |       **Test performed**       | **Result**                             | **Pass / Fail** |
|:--------------------------|:------------------------------:|:---------------------------------------|:---------------:|
| **Form**                  | Filled up with account details | Works as expected                      |    **Pass**     |
| **Sign In button**        |            Clicked             | Logs you in and redirects to Home page |    **Pass**     |
| **Forgot password? link** |            Clicked             | Goes to Password reset page            |    **Pass**     |

### Sign out page

| **Element / Feature** | **Test performed** | **Result**                               | **Pass / Fail** |
|:----------------------|:------------------:|:-----------------------------------------|:---------------:|
| **Sign out button**   |      Clicked       | Signs you out and redirects to Home page |    **Pass**     |

### Password reset page

| **Element / Feature**     |           **Test performed**            | **Result**                                                                                                      | **Pass / Fail** |
|:--------------------------|:---------------------------------------:|:----------------------------------------------------------------------------------------------------------------|:---------------:|
| **Form**                  | Filled up with associated email address | Works as expected                                                                                               |    **Pass**     |
| **Password reset button** |                 Clicked                 | Sends email with password reset link and redirects to confirmation page stating the email was sent successfully |    **Pass**     |
| **Password reset link**   |                 Clicked                 | Redirects to New password page                                                                                  |    **Pass**     |

### New password page

| **Element / Feature**      |     **Test performed**      | **Result**                                                                                                 | **Pass / Fail** |
|:---------------------------|:---------------------------:|:-----------------------------------------------------------------------------------------------------------|:---------------:|
| **Form**                   | Filled up with new password | Works as expected                                                                                          |    **Pass**     |
| **Change password button** |           Clicked           | Sets account new password and redirects to confirmation page stating the password was changed successfully |    **Pass**     |

### Change password page

| **Element / Feature**      |            **Test performed**            | **Result**                                              | **Pass / Fail** |
|:---------------------------|:----------------------------------------:|:--------------------------------------------------------|:---------------:|
| **Form**                   | Filled up with current and new passwords | Works as expected                                       |    **Pass**     |
| **Change password button** |                 Clicked                  | Changes account password and redirects to the same page |    **Pass**     |

### Home page

| **Element / Feature** |      **Test performed**      | **Result**                                   | **Pass / Fail** |
|:----------------------|:----------------------------:|:---------------------------------------------|:---------------:|
| **Background Image**  | Visited page, resized screen | It covers all of the background in Home page |    **Pass**     |
| **Shop now link**     |           Clicked            | Goes to Products catalog page                |    **Pass**     |

### Products catalog page

| **Element / Feature**                                       |               **Test performed**               | **Result**                                                                         | **Pass / Fail** |
|:------------------------------------------------------------|:----------------------------------------------:|:-----------------------------------------------------------------------------------|:---------------:|
| **Products grid**                                           | Visited page, resized screen, clicked products | Page renders OK, is responsive and redirects to corresponding product when clicked |    **Pass**     |
| **Sort by price link**                                      |                    Clicked                     | Opens up dropdown list with filtering options: Low to High and High to Low         |    **Pass**     |
| **Sort by price: Low to High**                              |                    Clicked                     | Filters all products starting from lowest to highest prices                        |    **Pass**     |
| **Sort by price: High to Low**                              |                    Clicked                     | Filters all products starting from highest to lowest prices                        |    **Pass**     |
| **Sort by price: Low to High (while selecting a category)** |                    Clicked                     | Filters current category products starting from lowest to highest prices           |    **Pass**     |
| **Sort by price: High to Low (while selecting a category)** |                    Clicked                     | Filters current category products starting from highest to lowest prices           |    **Pass**     |

### Product details page

| **Element / Feature** |           **Test performed**            | **Result**                                                                            | **Pass / Fail** |
|:----------------------|:---------------------------------------:|:--------------------------------------------------------------------------------------|:---------------:|
| **Page**              |      Visited page, resized screen       | Page renders OK, is responsive and shows corresponding product                        |    **Pass**     |
| **Three dots button** |                 Clicked                 | Opens up dropdown list with Edit and Delete options (shows only for Admin/Superusers) |    **Pass**     |
| **Edit link**         |                 Clicked                 | Goes to Edit product page for the selected product (shows only for Admin/Superusers)  |    **Pass**     |
| **Delete link**       |                 Clicked                 | Deletes current selected product (shows only for Admin/Superusers)                    |    **Pass**     |
| **Form**              | Selected different sizes and quantities | Works as expected                                                                     |    **Pass**     |
| **Add to Bag button** |                 Clicked                 | Adds item with correct size and quantity to the Shopping bag                          |    **Pass**     |

### Shopping bag page

| **Element / Feature**   |                             **Test performed**                              | **Result**                                                                                         | **Pass / Fail** |
|:------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------|:---------------:|
| **Page**                |                        Visited page, resized screen                         | Page renders OK, is responsive and shows all products in the bag                                   |    **Pass**     |
| **Product name**        |                                   Clicked                                   | Goes to the corresponding Product details page                                                     |    **Pass**     |
| **Update link**         |                                   Clicked                                   | Shows form for updating the product, when clicked a second time it hides the form                  |    **Pass**     |
| **Remove link**         |                                   Clicked                                   | Removes product from the bag                                                                       |    **Pass**     |
| **Update product form** |                        Changed sizes and quantities                         | Works as expected                                                                                  |    **Pass**     |
| **Confirm button**      |                                   Clicked                                   | Updates product with new size and/or quantity                                                      |    **Pass**     |
| **Bag total**           |                          Added or removed products                          | Updates bag total amount with correct total                                                        |    **Pass**     |
| **Delivery cost**       | Added product under £50 total, added more products for going over threshold | Shows correct amount of delivery cost (10%), if it's over £50 worth of products delivery cost is 0 |    **Pass**     |
| **Grand Total**         |                          Added or removed products                          | Updates Grand Total with correct amount (bag total + delivery cost if there is any)                |    **Pass**     |
| **Go checkout link**    |                                   Clicked                                   | Goes to Checkout page with current product(s) in the bag                                           |    **Pass**     |

### Checkout page

| **Element / Feature**    |                                                               **Test performed**                                                                | **Result**                                                                                                                                                 | **Pass / Fail** |
|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------:|
| **Page**                 |                                                          Visited page, resized screen                                                           | Page renders OK, is responsive and shows all selected products for the order                                                                               |    **Pass**     |
| **Form**                 |                                                       Filled up with all required details                                                       | Works as expected, does autofocus to Full Name input, shows Save info checkbox (only for Registered users)                                                 |    **Pass**     |
| **Save info checkbox**   |                                                                     Clicked                                                                     | Saves current form info into User's Profile                                                                                                                |    **Pass**     |
| **Stripe payment input** | Filled up with valid credit card number, filled up with test card that prompts further authorization, filled up with invalid credit card number | Validates card number, prompts further authorization upon placing order, display errors if invalid credit card number or if the expiry date is in the past |    **Pass**     |
| **Place order button**   |                                                                     Clicked                                                                     | Places order in the database and creates Stripe payment intent, displays overlay with loading spinner and redirects to Checkout success page               |    **Pass**     |

### Checkout success page

| **Element / Feature** |       **Test performed**        | **Result**                                                                    | **Pass / Fail** |
|:----------------------|:-------------------------------:|:------------------------------------------------------------------------------|:---------------:|
| **Page**              |  Visited page, resized screen   | Page renders OK, is responsive and shows all products for the order placed    |    **Pass**     |
| **Order details**     | Visited page upon placing order | Shows order number, date and delivery information (full name and address)     |    **Pass**     |
| **Order summary**     | Visited page upon placing order | Shows all the products for the order placed with its corresponding total cost |    **Pass**     |

### User's Profile page

| **Element / Feature**         |      **Test performed**      | **Result**                                                                                                                             | **Pass / Fail** |
|:------------------------------|:----------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------|:---------------:|
| **Page**                      | Visited page, resized screen | Page renders OK, is responsive and shows all as expected                                                                               |    **Pass**     |
| **Delivery information form** |  Filled up with new details  | Works as expected                                                                                                                      |    **Pass**     |
| **Save changes button**       |           Clicked            | Saves information in the current form, when placing new order all details are updated correctly                                        |    **Pass**     |
| **Changed password link**     |           Clicked            | Goes to Change password page                                                                                                           |    **Pass**     |
| **Order history table**       |         Visited page         | Shows all orders placed with associated profile                                                                                        |    **Pass**     |
| **Order link**                |           Clicked            | Goes to Checkout success page for the selected order, it does not show green box with confirmation text and shows Back to profile link |    **Pass**     |

### Add a product page

| **Element / Feature**               |                              **Test performed**                              | **Result**                                                                                                     | **Pass / Fail** |
|:------------------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------|:---------------:|
| **Page**                            |                         Visited page, resized screen                         | Page renders OK and is responsive (shows only for Admin/Superusers)                                            |    **Pass**     |
| **Form**                            | Filled up with correct details, also with incorrect or missing details/image | Works as expected, if there is any missing required field or incorrect field it doesn't allow you to submit it |    **Pass**     |
| **Add product button**              |                                   Clicked                                    | Adds product to the shop, goes to new added product details page                                               |    **Pass**     |
| **Image input: Choose file button** |                                   Clicked                                    | Opens up window for selecting the image to add, upon form submission it attaches selected image to the product |    **Pass**     |

### Edit product page

| **Element / Feature**               |                   **Test performed**                    | **Result**                                                                                                                                                          | **Pass / Fail** |
|:------------------------------------|:-------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------:|
| **Page**                            |              Visited page, resized screen               | Page renders OK and is responsive (shows only for Admin/Superusers)                                                                                                 |    **Pass**     |
| **Form**                            | Changed details, also with incorrect or missing details | Works as expected, its filled up with current product details by default                                                                                            |    **Pass**     |
| **Update product button**           |                         Clicked                         | Edits product in the shop if there is any change, goes to edited product details page, if there is any missing or incorrect field it doesn't allow you to submit it |    **Pass**     |
| **Clear checkbox**                  |                         Clicked                         | Deletes current image and replaces it with new one, if there is any                                                                                                 |    **Pass**     |
| **Image input: Choose file button** |                         Clicked                         | Opens up window for selecting the image to add, upon form submission it attaches selected image to the product                                                      |    **Pass**     |

## 2. Security

I've performed several critical tests to ensure security across the website. Below you can find all security tests as **Anonymous** or **Registered User** (without *Superuser* permissions):

| **Element / Feature**           |                                     **Test performed**                                      | **Result**                                                                            | **Pass / Fail** |
|:--------------------------------|:-------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------|:---------------:|
| **Add a product endpoint**      |   Visited page by typing in the URL bar: https://blackdogshop.herokuapp.com/products/add/   | Redirects to Sign in page                                                             |    **Pass**     |
| **Edit product endpoint**       |  Visited page by typing in the URL bar: https://blackdogshop.herokuapp.com/products/edit/2  | Redirects to Sign in page                                                             |    **Pass**     |
| **Delete product endpoint**     | Visited page by typing in the URL bar: https://blackdogshop.herokuapp.com/products/delete/2 | Redirects to Sign in page                                                             |    **Pass**     |
| **Django administration panel** |       Visited page by typing in the URL bar: https://blackdogshop.herokuapp.com/admin       | Says you are authenticated as {username} and does not allow you to log into the panel |    **Pass**     |

## 3. Code Validation
### HTML files
I've validated all HTML files using 