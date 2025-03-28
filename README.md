# Text-Smilarity-API
## Setup Instructions
1. **Set Up Virtual Environment**:
   ```bash
   python -m venv chatenv
   
   chatenv\Scripts\activate

2. **Install Dependencies**:
   ```bash
   pip install -r requirement.txt


3. **Add Database Models**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate


4. **Run python**:
   ```bash
   python manage.py runserver


5. **Open the browser and go to:**:
   ```bash
   (http://127.0.0.1:8000)
