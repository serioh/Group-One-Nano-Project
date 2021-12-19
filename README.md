# Group-One-Nano-Project
README file as of 19 Dec 2021

File run order:

In the config.py file in the database directory, enter in your MySql login info.

Then run the main.py file which will show the login page.

Click on register and fill in the registration form. Once filled in, this will redirect you to the login page.

Enter your details in the login form, and the game will start! There will be 10 questions testing your Python skills.

If you have already registered, there is no need to register again. Have fun!

Info on files and directories:

main.py - The main file to play the game!

requirements.txt - What you may need to add or import to run the file.

backend - Containing question.py adn snake_brain, these are the files that select the questions and presents them, and our quiz brain mainframe respectively.

database - Containing config.py, create_database.py, create_database.sql and sql_python_connection.py, these files facilitate the creation and connection of our database which holds questions and user login info.

Tests - Containing init.py, test_main.py, test_question.py, test_snake_brain.py, test_sql_python_connection.py, this contains all of our test files for the game. If you want to run the unit tests, type in "pytest" into your terminal.

user_interface - Containing our background images, login.py, register.py and snake_charmer_ui.py, this is our Tkinter UI in all of its attractive glory.
