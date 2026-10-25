# PrintEase Services

## Project Description

PrintEase Services is a simple and interactive printing services website developed using HTML, CSS, Python, and PyScript.

The website is designed to help students, teachers, and office workers easily check printing prices and calculate the total cost of their printing needs.

This project demonstrates how Python can be integrated into a website using PyScript and how event-driven programming can make a website interactive.

## Project Objectives

The objectives of this project are:

1. To create a simple and user-friendly business website.
2. To provide information about available printing services.
3. To develop an interactive printing price calculator.
4. To demonstrate event-driven programming using Python and PyScript.
5. To practice version control using Git and GitHub.

## Technologies Used

- **HTML** – Used to create the website's structure and content.
- **CSS** – Used to design the website and improve its appearance.
- **Python** – Used to implement the website's interactive functions.
- **PyScript** – Used to run Python code inside the web browser.
- **Git** – Used to track changes made during development.
- **GitHub** – Used to store and manage the project repository.
- **Visual Studio Code** – Used to write and edit the project files.

## Website Features

### 1. Homepage
Displays the business name, welcome message, and introduction to PrintEase Services.

### 2. Printing Services
Provides information about the available printing services and their prices.

| Service | Price per Page |
|---|---|
| Black and White Printing | ₱2.00 |
| Colored Printing | ₱5.00 |
| Photocopying | ₱1.00 |

### 3. Printing Price Calculator
Allows users to select a printing service, enter the number of pages, and calculate the total printing cost.

For example:

**10 pages × ₱2.00 = ₱20.00**

The calculation is performed using Python and PyScript.

### 4. Sample Order Form
Allows users to enter their name and the number of pages they want to print.

After submitting the form, the website displays a confirmation message.

**Note:** This is a demonstration form. It does not process or save actual customer orders.

### 5. Input Validation
Checks the information entered by users to help prevent invalid page quantities.

## Event-Driven Programming

This project uses event-driven programming through Python and PyScript.

Two main events are implemented:

**Click Event:** When the user clicks the Calculate Price button, Python calculates the total printing cost and displays the result.

**Submit Event:** When the user submits the sample order form, Python validates the input and displays a confirmation message.

These events allow users to interact with the website without manually refreshing the page.

## Project Files

- `index.html` – Contains the website structure and content.
- `style.css` – Contains the website design and styling.
- `main.py` – Contains the Python code for the interactive features.
- `README.md` – Contains the project documentation.

## How to Run the Project

1. Download or clone the GitHub repository.
2. Open the project folder in Visual Studio Code.
3. Make sure Python is installed.
4. Open the terminal.
5. Run the following command:

   ```bash
   python -m http.server 8000
   ```

6. Open a web browser.
7. Visit `http://localhost:8000`.
8. Test the printing calculator and sample order form.

**Note:** An internet connection is required to load PyScript.

## Developer

**Wency Alampayan**

Individual Project

## Project Purpose

This project was created as an academic requirement to demonstrate the practical application of Python, PyScript, event-driven programming, and GitHub version control in developing an interactive business website.