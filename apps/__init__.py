from dependency_injector import containers, providers

from db.containers import DBContainer
from apps.image.containers import Container as ImageContainer


db_container = DBContainer()
db_container.wire(packages=[__name__])


class RootContainer(containers.DeclarativeContainer):
    image_app = providers.Container(ImageContainer)


root_container = RootContainer()
root_container.wire(packages=[__name__])
root_container.image_app.wire(packages=[__name__])
