# Django Chat Application

This project is a Django-based real-time chat application where users can register, log in, and chat with other registered users. It is designed for simplicity and functionality, providing a seamless chatting experience.

---

## Features

- **User Authentication**: Register and log in securely.
- **Real-Time Chat**: Users can send and receive messages in real time.
- **User List**: Displays all registered users in the application.
- **Message History**: Stores and retrieves chat messages from the database.
- **Responsive UI**: User-friendly design using Bootstrap.

---

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap)
- **Database**: SQLite (default Django database)
- **Hosting Platform**: PythonAnywhere

---

## Prerequisites

To set up and run the project locally, ensure the following are installed on your system:

- Python 3.9 or higher
- pip (Python package manager)
- A virtual environment tool (optional but recommended)

---

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone <https://github.com/Fahmithasirin/Chat.git>
   cd chat_project
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   - Open a browser and visit `http://127.0.0.1:8000`.

---

## Usage

1. Register a new account or log in with an existing account.
2. View the list of registered users.
3. Click on a username to start a chat.
4. Send messages in real time and view chat history.

---

## Deployment

The application is hosted on **PythonAnywhere**. You can access it using the following link:

[Live App on PythonAnywhere](https://fahmithasirin.pythonanywhere.com/)

---

## Project Structure

```
chat_project/
|-- call/               # Django app folder
|   |-- migrations/      # Database migrations
|   |-- templates/       # HTML templates
|   |-- views.py         # Application logic
|   |-- models.py        # Database models
|   |-- forms.py         # Forms for user input
|
|-- chat_project/       # Main Django project folder
|   |-- __init__.py
|   |-- settings.py      # Project settings
|   |-- urls.py          # URL routing
|   |-- wsgi.py          # WSGI configuration for deployment
|
|-- manage.py           # Django project management script
|-- requirements.txt    # Python dependencies
|-- README.md           # Project documentation
```

---

## Future Enhancements

- **Group Chat**: Enable group conversations.
- **WebSocket Integration**: Use WebSockets for true real-time messaging.
- **File Sharing**: Add functionality to share files and images.
- **User Profiles**: Enhance user profiles with additional details.

---


## Author

Developed by Fahmitha Sirin.

For inquiries or suggestions, feel free to contact: [fahmithasirin@gmail.com](mailto:fahmithasirin@gmail.com)

