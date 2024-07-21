# Audio file transcript Generator

A web application that transcribes audio files into text using AssemblyAI and Django.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- Upload and transcribe music files to generate lyrics.
- View, edit, and delete generated transcripts.
- User authentication (registration, login, logout).
- Responsive design using javascript and TailwindCSS.

## Requirements

- Python 3.8+
- Django 3.0+
- AssemblyAI API Key

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/fasasimayokun/Webstack---Portfolio-Project.git
    cd audio_lyrics
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory of your project and add your API keys:

    ```env
    ASSEMBLYAI_KEY=your_assemblyai_api_key
    ```

5. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Register a new user account or log in with your superuser account.
3. Upload a music file and generate its transcript.
4. View, edit, or delete the generated transcripts.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.