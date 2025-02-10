# Simple Social Network (Student Project)

## Introduction
This project is a simple social network implemented using object-oriented programming (OOP) in Python. It was developed as a student project for an advanced programming course. The primary goal was to create a basic social media system where users can:
- Create accounts
- Log in
- Send friend requests
- Send and view messages
- Create and view posts

## Motivation
This was my first programming project, as our introductory programming course did not include a project. Initially, I had no experience with handling file storage in Python, so this project was a great learning experience in working with CSV files to store user data, messages, and friend requests.

## Features
- **User Registration**: Users can create an account with their name, birthdate, city, gender, username, and password.
- **Login System**: Users can log in with their credentials.
- **Friend Requests**: Users can send and receive friend requests.
- **Messaging System**: Users can send messages to their friends.
- **Post Creation**: Users can create posts that are stored and viewed later.
- **Admin Panel**: An admin account can log in to view all messages and friendships.

## Funny Bug Story 🐞
On the day of my project presentation, everything worked perfectly at home. However, in front of my professor, nothing worked! There were no errors or warnings from the compiler. It felt like I had perfectly wired an entire building but forgot to install electrical outlets.

After debugging, I realized that I had defined the `show_menu` function inside the class but never instantiated an object for it. As a result, the function was never executed in the terminal, making it impossible to interact with the system. Lesson learned: Always check object instantiation before running the program! 😅

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/simple-social-network.git
   ```
2. Navigate to the project directory:
   ```bash
   cd simple-social-network
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## Technologies Used
- Python
- CSV for data storage

## Future Improvements
- Use a database instead of CSV files
- Add a graphical user interface (GUI)
- Improve security (e.g., password hashing)

## Conclusion
This project was a great introduction to object-oriented programming and file handling in Python. It was also a valuable lesson in debugging and making sure the program is properly executed. 🚀

