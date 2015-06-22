# Uploading files to S3 from the browser

This is the example project for the post in (here)[TODO].

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py bower install`

if you would like to test it on localhost set `S3_DEBUG` to `True` in your `settings.py` and create a file called `.env` with the following content:
```bash
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
AWS_STORAGE_BUCKET_NAME=''
```
Make sure your bucket's CORS is set like the example on our blog post [here](TODO).
