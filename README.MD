![](https://github.com/DamianPyCoder/DamianPyCoder/blob/main/icons/python.png)

# PYTHON LESSONS

## 1. Getting started 
#### 1.1 - Python Installation

:computer: Windows

- Go to the official Python website, https://www.python.org/downloads/, and download the latest Python installer for Windows.
- Run the installer, and select the "Add Python to PATH" option. This will ensure that you can run Python from any directory in the command prompt.
- Choose the installation directory, and click on "Install Now".
- Wait for the installation to finish. This may take a few minutes.
- Once the installation is complete, open the command prompt and type "python" to verify that Python has been installed correctly.

:computer: Linux

- Open a terminal window.
- Update the package list with the command "sudo apt-get update".
- Install Python by typing "sudo apt-get install python3" (or "python" if you prefer Python 2).
- Wait for the installation to finish. This may take a few minutes.
- Once the installation is complete, type "python3" (or "python" if you installed Python 2) in the terminal window to verify that Python has been installed correctly.

```
Note: 
  The above instructions assume that you are using a Debian-based Linux distribution such as Ubuntu.
  If you are using a different distribution, the commands may vary slightly.
```


#### 1.2 - Git & Github

- Create a project on GITHUB and copy the link

- Create a folder on your system, open a terminal and situate inside the folder. Attention, in this folder we will put all the code that we want to upload.

- In the terminal type the command ```GIT CLONE``` +"address of the repository"

- To know what state the files are in and see if they are still to be uploaded, we will put in command: 
```diff 
GIT STATUS
```

- In case we want to upload a file we will use the command: ``` GIT ADD ``` "file name"

- If you want to upload ALL the files, the name is replaced by a period: 
```diff 
GIT ADD .
```

- We add a commit that specifies that we have uploaded, for example we will call it First Commit: 
``` diff
GIT COMMIT -m "First Commit" 
```

- We upload the files: 
```diff 
GIT PUSH
```



##

## 2. Exercices
#### Basic exercises from exchange variables without auxiliary variable to Rome cipher.

:blue_book: Ask the user for a number and display on the screen the multiplication table of this number in the format (Number x i = Result...).

- :clipboard: [Solved exercise](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/2_Exercises/taula_mult.py)

:blue_book: Write a program that asks the user for three numbers and displays the average, the largest and the smallest.

- :clipboard: [Solved exercise](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/2_Exercises/mitjana.py)

:blue_book: Ask the user for 2 numbers and show which one is closest to 100.

- :clipboard: [Solved exercise](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/2_Exercises/aprop100.py)

:blue_book: Calculate the numbers of the Fibonacci series, bearing in mind that a1=1, a2=1 y que an=an-1+an-2.. It asks the user how many numbers to calculate

- :clipboard: [Solved exercise](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/2_Exercises/fibonacci.py)

:green_book: Make a program that calculates the area and perimeter of a triangle. Two functions must be defined that calculate the area and the perimeter of the triangle.

:green_book: Write a program that asks for a year and writes whether it is a transfer or not. Remember that leap years are multiples of 4, but multiples of 100 are not, although multiples of 400 are.
Here are some examples of possible answers: 2012 is a carryover, 2010 is not a carryover, 2000 is a carryover, 1900 is not a carryover.

:green_book: Section radars consist of placing two cameras at two points away from a road to be able to check how long it took the car to travel that section. If the average speed exceeds the maximum speed allowed, we will be able to know (even if we have not seen it) that at some point on the journey it has exceeded this speed.
The program will ask to SPECIFY three integers: the first will be the distance (in meters) that separates the two cameras, the second will indicate the maximum speed allowed in this entire section (in km / h), and the third number will indicate the number of seconds that it took the car to travel the stretch.
The output will display "OK" if the car did not exceed the maximum speed, "fine" if this speed was exceeded by less than 20% of the maximum speed allowed, and "POINTS" if the speed was exceeded by 20% or more of that speed; in this case, in addition to the fine, points will be deducted from the card.

:closed_book: Make a program that counts the number of vowels in a string written in Spanish.

:closed_book: Write a program that prompts the user to enter a sentence at the console and a vowel, and then displays the same sentence on the screen but with the vowel entered in uppercase.

:closed_book: Ask the user to enter a text or number. Show on screen whether or not the entered text is a palindrome. A palindrome is a word, number or phrase that can be read forwards as well as backwards (if it is a number, it is called a capicua). Therefore, neither spaces nor upper/lowercase letters should be present. A single-letter or single-number text is considered a palindrome. To do this problem you don't need to be aware of the accents.

:closed_book: Make a program that checks if a registration is valid according to the format established from the year 2000 in Spain.
A valid license plate consists of four numbers followed by three capital letters of the Spanish alphabet, except for the vowels “A”, “E”, “I”, “O”, “U” and the consonants “Ñ” and “ Q".

:orange_book: A certain telephone company charges 10 cents to establish a telephone connection and from that point on, 5 cents per minute. If we ask the user for the time of a call in HH, MM and SS format (that is, if he tells us how many hours, minutes and seconds he has been on a call), show the corresponding amount in euros and cents.

:orange_book: Load by keyboard and store in a list of integers. Delete the elements greater than or equal to 10 and generate a new list with these values. Print both lists.

:orange_book: Write a program that allows you to create two lists of words, and then write another list that includes all the words from the previous two lists without repetition.) I also wrote the ordered list and the inverted list.

:orange_book: Load by keyboard and store in a list the heights of several people (float values)
Obtain the average of the heights. Count how many people are taller than average and how many are shorter.

:orange_book: Write a program that asks the user for a fruit, a number of kilos and displays on the screen the price of that number of kilos of fruit. The program will store in a dictionary the data from the following table:
Fruit Price
Banana 2.35
Apple 2.80
Pear 1.85
Orange 1.70
If the fruit is not in the dictionary, a message should be displayed informing about it.

:ledger: Write a program that contains two functions, the first function will receive a sentence and return a list with each word it contains and its frequency. The second function will take the list generated with the previous function and return a dictionary with the most repeated word and its frequency.

:ledger: Write a program that creates a Spanish-English translation dictionary. The user will enter the words in Spanish and English separated by colons, and each pair <word>:<translation> separated by commas. The program must create a dictionary with the words and translations. It will then ask for a sentence in Spanish and use the dictionary to translate it word for word. If a word is not in the dictionary, it must be left untranslated.

:ledger: Create a class called Account that has the following attributes: owner and balance (can have decimals). It will have two methods:
deposit: an amount is added to the account balance, if the amount entered is negative, nothing will be done.
withdraw: an amount is subtracted from the account balance. If the remainder gives a negative number, the balance becomes 0.
Add and withdraw money from the account and show how the balance is updated.

:ledger: Make a class called Person with the following methods and attributes:
Attributes: name, age, weight, height and sex (H, M).
Methods:
esMajorDeEdat(): indicates if he is of legal age, returns a boolean.
calculateBMI(): Calculates weight in kg divided by height in meters squared. If this formula returns a value less than 20, the function returns 'INFRAPES', if it returns a number between 20 and 25 (inclusive) the function returns 'PES_IDEAL' and if it returns a value greater than 25 it returns 'OVERSEE'.
The program will ask for the people's data by keyboard and will indicate for each person their BMI and whether they are of legal age.

:ledger: We add the Company class to the previous program. The Company class has a method that indicates whether a person can be hired as a worker. This method allows hiring people under 50 years of age and who are not overweight.
We have four candidates who want to join the company, they are:
Person('Pepe','Lopez','H',34,80,1.70)
Person('Juan','Perez','H',55,72,1.74)
Person('Luisa','Romero','M',48,55,1.60)
Person('Ramon','Bilbao','H',25,60,1.80)
The program will indicate whether or not these candidates can be hired.

:ledger: To the Person class we add the greet method that displays a greeting on the screen: "Hello! I'm in {name}".
The Professor class inherits from the Person class and has a subject attribute. It also has a dismiss method that displays a dismissal: "Bye {name} {surnames}. Your subject is {subject}"
Write a program that prompts for information to create a teacher object, creates the object, and calls the greet and dismiss methods.

##

## 2.1. Advanced exercices

:blue_book: Password generator with libraries like colorama, random and pyperclip.

- :clipboard: [Solved exercise](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/2_Exercises/generarPasswords.py)
   :paperclip: [Interesting tools](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/2_Exercises/jugandoConLibreriasDeTerminal.py)

##

## 3. Data base
#### 3.1 - SQLITE
#### 3.2 - SQLAlchemy

##

## 4. Data Access & Big Data
#### 4.1 - Regex with Python
#### 4.1 - Web scraping Amazon

##

## 5. Basic games
#### :video_game: [TicTacToe using colorama](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/Games/TRES_EN_RAYA.py)
![](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/Games/IMAGES/TRESENRAYA.png)
#### :video_game: [Hangman](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/Games/HANGMAN.py)
![](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/Games/IMAGES/HANGMAN.png)
#### :video_game: [Checkers](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/Games/checkers.py)
![](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/Games/IMAGES/CHECKERS.png)
#### :video_game: [Couples game with Tkinter](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/Games/PAREJAS_TKINTER.py)
![](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/Games/IMAGES/PAREJAS_TK.png)
#### :video_game: [Paint with Tkinter](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/Games/dibujarConColores.py)
![](https://github.com/DamianPyCoder/Python__TEACHING_in_Youtube/blob/main/Games/IMAGES/paintPython50.png)
   
##

## 6. NLP
#### 6.1 - Text classification
#### 6.2 - Sentiment analysis
#### 6.3 - Chatbot
#### 6.4 - Speech recognition and synthesis

##

## 7. Machine learning
#### 7.1 - Numpy
#### 7.2 - Pandas & Matplotlib
#### 7.3 - Tensorflow
#### 7.4 - Pytorch
#### 7.5 - NLTK
#### 7.6 - Pillow library 

##

## 8. Create api and call it
#### 8.1 - ...


