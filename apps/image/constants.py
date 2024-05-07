from .types import ImageTypes


# Popular Dog Breeds
DOG_BREEDS_KEY_WORDS = [
    "golden" ,"retriever", "labrador", "french", "bulldog",
    "german", "shepherd", "poodle", "beagle", "yorkshire", "terrier",
    "pomeranian", "dachshund"
]

# Popular Cat Breeds
CAT_BREEDS_KEY_WORDS = [
    "persian", "siamese", "maine", "coon", "ragdoll", "blue",
    "sphynx", "abyssinian", "fold", "shorthair",
    "bengal"
]

BREEDS_CATALOG = {
    ImageTypes.CAT: CAT_BREEDS_KEY_WORDS,
    ImageTypes.DOG: DOG_BREEDS_KEY_WORDS,
}
