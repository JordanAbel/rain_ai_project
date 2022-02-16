from mock_data import mock_input


def extract_keywords():
    data = mock_input["entry_1"]["data"]
    data_dict = {}
    keywords = ["knee", "shoulder", "elbow", "wrist", "hand", "hip", "foot", "ankle", "multiple myeloma", "myopathy",
                "tumour + subtractions, vit e marker", "mortons neuroma", "hand", "fingers", "achilles tendon",
                "humerus", "forearm", "femur", "tib/fib", "sternum", "tumour with gad and subtractions", "sacrum",
                "l-spine", "l-spine and Sacrum", "bilateral", "review with radiologist", "scapula", "thumb", "toes"]

    data_words = list(data.split(" "))

    for data_word in data_words:
        count = 0
        data_word.lower()

        if data_word in keywords:
            count += 1
            data_dict[data_word] = count

    return data_dict
