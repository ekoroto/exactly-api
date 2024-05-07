import enum


class ImageTypes(str, enum.Enum):
    CAT = 'CAT'
    DOG = 'DOG'
    NOT_RECOGNIZED = 'NOT_RECOGNIZED'
