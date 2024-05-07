# exactly-api

This is a FastAPI application for receiving, saving and sending images of cats and dogs. General steps of the application:
1. To receive pictures from a third-party service, we use celery beat, scheduled for retrieving the image every 2 minutes.
2. After receiving an image, it goes through a recognition process into one of three categories: `cat`, `dog`, `not recognized`. Recognition occurs using a `local pre-trained ML model VGG16`.
3. Then it saves the image in `Minio storage` and stores the bucket path in the corresponding entry in the PostgreSQL database.
4. `<host>:<port>/images/` endpoint returns the last 10 images with the following structure:

```
[
    {
        "id": 1,
        "type": "CAT",
        "file_path": <file_path>,
        "created_at": "2024-05-06T17:18:56.087145Z",
        "url": <minio_url>
    },
    ...
]
```

## Installation

1. Clone the repository
2. Install requirements with dev requirements via pipenv `pipenv sync`.
3. Fill `.env` file based on `.env.example`
4. Activate pipenv environment `pipenv shell`
5. Create PostgreSQL database and fill according DB fields in .env file.
6. Run migrations via `alembic upgrade head`
7. Run API (FastAPI) server by typing `pipenv run server`
8. Run celery worker on another terminal tab with command `pipenv run celery_worker`
9. Run celery beat on another terminal tab with command `pipenv run celery_beat`

### Minio file storage info
1. Minio is used as storage for files.
2. You need to download the Minio here: https://dl.min.io/server/minio/release/
3. You can use minio.conf file in the root of the project or create the new one:

```
MacOS getting config example:
cd /some_folder
mkdir minio && cd minio
curl -O https://dl.min.io/server/minio/release/darwin-arm64/minio && chmod +x ./minio
nano minio.conf - example of config file: https://min.io/docs/minio/macos/operations/install-deploy-manage/deploy-minio-single-node-single-drive.html#id4
```
5. And run
```
export MINIO_CONFIG_ENV_FILE=/some_folder/minio/minio.conf
./minio server :9000
```
6. Fill the all needed info in .env based on .env.example file.
