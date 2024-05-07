import io
import numpy as np

from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions


class ImageClassificationService:
    model = VGG16(weights='imagenet')

    def predict(self, img_bytes: bytes, categories: list[str], breeds_catalog: dict):
        preds_categories = self._classify_image(img_bytes)

        return self._match_categories(categories, preds_categories, breeds_catalog)

    def _classify_image(self, img_bytes: bytes) -> list:
        img_stream = io.BytesIO(img_bytes)
        img = image.load_img(img_stream, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)

        preds = self.model.predict(img)
        decoded_preds = decode_predictions(preds, top=3)[0]

        return [pred[1] for pred in decoded_preds]

    @staticmethod
    def _match_categories(categories: list, preds_categories: list[str], breeds_catalog: dict) -> str | None:
        for category in categories:
            for preds_category in preds_categories:
                if category.value.lower() in preds_category.lower():
                    return category

                for key_word in breeds_catalog[category]:
                    if key_word in preds_category.lower():
                        return category

        return None
