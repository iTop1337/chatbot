@echo off
call python manage.py runserver
docker-compose up -d
python -m streamlit run chatbot/chatbot_streamlit.py
