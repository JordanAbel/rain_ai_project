# This is the basic structure of how we can extract keywords from a serializable JSON response
def extract_keywords(data):
    data_dict = {}
    keywords = ["knee", "shoulder", "elbow", "wrist", "hand", "hip", "foot", "ankle", "multiple myeloma", "myopathy",
                "tumour + subtractions, vit e marker", "mortons neuroma", "hand", "fingers", "achilles tendon",
                "humerus", "forearm", "femur", "tib/fib", "sternum", "tumour with gad and subtractions", "sacrum",
                "l-spine", "l-spine and Sacrum", "bilateral", "review with radiologist", "scapula", "thumb", "toes"]

    data_words = list(data.split(" "))

    for data_word in data_words:
        data_word.lower()

        if data_word in keywords:

            if data_dict.get(data_word):
                data_dict[data_word] += 1
            else:
                data_dict[data_word] = 1

    return data_dict
