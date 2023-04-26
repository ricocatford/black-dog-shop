# Testing

## 1. Functionality

I've performed regular manual tests throughout development for the usability and performance of the website. Below you
can find all tests performed to the different elements and features. All tests were carried out in Chrome browser which
is
my preferred one and the most used nowadays. Also, I've performed some of these tests in Microsoft Edge and Safari to
ensure it's working as expected in other browsers.

### Navbar

| **Element / Feature**       |  **Test performed**   | **Result**                                                             | **Pass / Fail** |
|:----------------------------|:---------------------:|:-----------------------------------------------------------------------|:---------------:|
| **Brand logo**              |        Clicked        | Goes to Home page                                                      |    **Pass**     |
| **All products link**       |        Clicked        | Goes to Products catalog page                                          |    **Pass**     |
| **Clothing link**           |        Clicked        | Opens up dropdown list with corresponding categories                   |    **Pass**     |
| **Skateboards link**        |        Clicked        | Opens up dropdown list with corresponding categories                   |    **Pass**     |
| **Categories links**        |        Clicked        | Goes to Products catalog page filtering only for the selected category |    **Pass**     |
| **Product management link** |        Clicked        | Goes to Add a Product page (only for Admin/Superusers)                 |    **Pass**     |
| **My Profile link**         |        Clicked        | Goes to User's Profile page (only for Registered users)                |    **Pass**     |
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
| **Inputs**                        | Filled up with new account details | Works as expected                                                 |    **Pass**     |
| **Already have an account? link** |              Clicked               | Goes to Sign in page                                              |    **Pass**     |
| **New account**                   |        Created new account         | Creates new account and redirects to Email verification sent page |    **Pass**     |
| **Email verification link**       |              Clicked               | Activates the account and redirects to Confirm email page         |    **Pass**     |

### Confirm email page

| **Element / Feature** | **Test performed** | **Result**                                   | **Pass / Fail** |
|:----------------------|:------------------:|:---------------------------------------------|:---------------:|
| **Confirm button**    |      Clicked       | Confirms email and redirects to Sign in page |    **Pass**     |

### Sign in page

| **Element / Feature**     |                  **Test performed**                  | **Result**                             | **Pass / Fail** |
|:--------------------------|:----------------------------------------------------:|:---------------------------------------|:---------------:|
| **Inputs**                |            Filled up with account details            | Works as expected                      |    **Pass**     |
| **Sign In button**        | Clicked after filling up inputs with correct details | Logs you in and redirects to Home page |    **Pass**     |
| **Forgot password? link** |                       Clicked                        | Goes to Password reset page            |    **Pass**     |

### Password reset page

| **Element / Feature**   |           **Test performed**            | **Result**                                                                                                      | **Pass / Fail** |
|:------------------------|:---------------------------------------:|:----------------------------------------------------------------------------------------------------------------|:---------------:|
| **Email input**         | Filled up with associated email address | Sends email with password reset link and redirects to confirmation page stating the email was sent successfully |    **Pass**     |
| **Password reset link** |                 Clicked                 | Redirects to New password page                                                                                  |    **Pass**     |





