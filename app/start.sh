flask db init && \
flask db migrate && \
flask db upgrade && \
gunicorn personalWebsiteFlask.app:create_app\(\) -b 0.0.0.0:5000 -w 3