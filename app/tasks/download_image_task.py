from celery_app import app


@app.task(name='download_image')
def download_image():
    #TODO: call download service
    pass
