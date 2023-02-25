# Unit 3. Expenses Tracker App for Ms. Emmy Abella 


# Criteria A: Planning
## Problem Definition

Emmy Abella Domingues is an 18-year-old IB Year 1 student from Brazil. As an international & boarding student in UWC ISAK Japan, money management is a major aspect of her life. Although Emmy easily keep tracks of her income or cash inflow, she finds it hard to keep track of her expenses. Specifically, she finds it difficult to note what, when, and how much she spends on. In addition, she finds it hard to visualize how large her purchases are since she spends in a currency (Japanese Yen - ¥) different to what she's used to (Brazilian Real - R$). The client, Emmy Domingues, is in need of an app that keeps track of her expenses. In addition, the client requires the app to be encrypted through a login system, for the data to be stored in a database, and for the user interface to be clear, concise, and most importantly attractive by using the client's favorite color, pink.


## // Rationale for Proposed Solution
- The rationale behind the choice of the proposed product must be in extended writing justifying how the choice of proposed product must be in extended writing justifying how the choice of this particular product is an effective solution.
- Why is an app needed?
- What are included in the app?
- What are used in the development in the app



## Success Criteria
1. The solution is an application that provides a presentation of the user's expenses in a tabular format.
2. The application is able to add, edit, or delete entries to the app's database and present these changes.
3. The application is kept secure by embedding a log in system and a registration system to add users.
4. The user's data of expenses are stored in a SQLLite database.
5. The application is up to the user's visual standard by using only shades of the user's favorite color, pink.
6. The user's expenses are categorized into Food, Transportation, Emergency & Healthcare, Leisure, and Miscellaneous. 
7. The app logs the date of purchase based on user input, and allows the user to write a 20-character note about that expense as an option.


# Criteria B: Design
## Record of Tasks
| Task No | Planned Action                                                               | Planned Outcome                                                                                                                                                                                             | Time estimate | Target completion date | Criterion |
|---------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Identify & interview the client                                              |                                                                                                                                                                                                             | 6 min         | Feb 9                  | A         |
| 2       | Write the problem context                                                    | Establish the problem identified in a clear and concise manner. The problem definition must include who the client is, what the client wants, and indicate a possible solution.                             | 15 min        | Feb 9                  | A         |
| 3       | Write the Design Statement                                                   | Explain in a concise and clear manner the purpose of the project to the client                                                                                                                              | 5 min         | Feb 9                  | A         | 
| 4       | Draw a system diagram                                                        |                                                                                                                                                                                                             | 10 min        | Feb 10                 | A         |
| 5       | Draw a UML Diagram                                                           |                                                                                                                                                                                                             | 20 min        | Feb 10                 | A         |
| 6       | Draw Wireframes                                                              |                                                                                                                                                                                                             | 45 min        | Feb 10                 | B         |
| 7       | Coding Part 1. User Interface                                                |                                                                                                                                                                                                             | 3 hours       | Feb 11                 | C         |
| 8       | Coding Part 2. Embed Database & functionalities of the log in screen.        |                                                                                                                                                                                                             | 45 min        | Feb 11                 | C         |
| 9       | Coding Part 3. Embed Database & functionalities of the sign up screen.       |                                                                                                                                                                                                             |               | Feb 12-14              | C         |
| 10      | Coding Part 4. Embed & present database in a tabular form in the main screen |                                                                                                                                                                                                             |               |                        | C         |
| 11      | Coding Part 5. Additional functionalities of the main screen                 | The program should be able to allow the user to add, edit, and delete entries. These entries must meet success criteria #6 and #7.                                                                          |               |                        | C         |
| 12      | Beta Testing                                                                 | Gauge the app's functionaly, security, and visual layout by having the client, Emmy Abella, test the app. Take notes of certain comments, suggestions, and concerns and present app amendments to the user. |               |                        | C         |
| 13      | Beta Development       | Code changes into the app based on feedback given by client from the previous step.                                                                                                                         |               |                        | C         |


## Test Plan
| Test No | Test Type                                                                                            | Date   | Procedure                                                                                                                                  | Expected Outcome                                                                                                                                                                                                                                                                                    |
|---------|------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| 1       | Functional: Test  whether the SignUp screen succesfully registers new user if all entries are valid. | Feb 18 | Run python file (spentio.py). Go to sign up screen and enter the following values: <br/>- email: bob@isak<br/>- username: bob<br/>-password: bob123 | When the database, spentio.db is checked, a new row of data can be seen. This row shows the entered email, username, and password encrypted using a certain hash.                                                                                                                                   |  
| 2       | Functional: Test sign up screen when data inputted by user is invalid                                | Feb 18 | Run spentio.py. Navigate to the SignUp Screen. Enter the following values:<br/>-  email: bob@isak<br/>- username: bob2<br/>-password: bob123 | Once the sign up button is clicked and the user input is queried into the database, the application shows a dialog box that tells the user the exact error. In this case, since the email already exists due to the prior test step, the dialog will show "Email already exists. Please try again". |
| 3       | Functional: Data registered from a new user is stored securely in an SQLite Database.                | Feb 18 | After Test step 1 and 2, open the sqllite database console and view the users table.                                                       | The users table must have the email, username, and a hashed password.                                                                                                                                                                                                                               |
| 4       | Functional: Test Login screen with valid input.                                                      | Feb 20 | Input the username and password registered during test step 1.                                                                             | Once the login button is clicked, the app transitions to the Main Screen                                                                                                                                                                                                                            |
| 5       | Functional: Test login screen with invalid input (username that hasn't been registered prior).       | Feb 20 | Input a random username and password that haven't been registered to the application prior.                                                | The application shows a dialog box stating that the 'User does not exist'.                                                                                                                                                                                                                          |
| 6       | Functional: Test login screen with invalid input (existing username but wrong password)              | Feb 20 | Input a previously registered username ('bob') or email ('bob@isak') and input a wrong or random password ('12345').                       | The appplication's password textfield turns red.                                                                                                                                                                                                                                                    |
| 7       | Non-functional: Test the application's graphic interface with the client.                            | Feb 21 | Communicate with the client, Emmy Abella Domingues da Silva during Computer Science class.                                                 | The client approves of the color scheme, layout, and features of the application.                                                                                                                                                                                                                   |
| 8       |                                                                                                      |        |                                                                                                                                            |                                                                                                                                                                                                                                                                                                     |




## Diagrams
### System Diagrams
### UML Diagram
### Wireframes
### Flowcharts
# Criteria C: Development
## Existing Tools
## Techniques Applied
## Sources
## Computational Thinking 
# Criteria D: Functionality
## Video

