import pytest
import requests
import cerberus


schema = {
    "message": {"type": "string", "required": True},
    "status": {"type": "string", "required": True},
}

schema_sub_breeds = {
    "message": {"type": "string", "required": True},
    "afghan": {"type": "string", "required": True},
    "basset": {"type": "string", "required": True},
    "blood": {"type": "string", "required": True},
    "english": {"type": "string", "required": True},
    "ibizan": {"type": "string", "required": True},
    "plott": {"type": "string", "required": True},
    "walker": {"type": "string", "required": True},
    "status": {"type": "string", "required": True},
}

class TestClassBreeds:
    # 1 тест
    @pytest.mark.parametrize("message", ["australian"])
    @pytest.mark.parametrize("message2", ["collie"])
    @pytest.mark.parametrize("message3", ["affenpinscher"])
    def test_LIST_ALL_BREEDS(self, api_client, message, message2, message3):
        res = requests.get('https://dog.ceo/api/breeds/list/all')
        js = res.json()
        assert res.status_code == 200
        assert js["status"] == "success"
        assert js["message"][message] == ["shepherd"]
        assert js["message"][message2] == ["border"]
        assert js["message"][message3] == []

    # 2 тест
    @pytest.mark.parametrize("random", ["https://dog.ceo/api/breeds/image/random",
                                        "https://dog.ceo/api/breeds/image/random/3"])
    def test_Random_image(self, random):
        res = requests.get(random)
        js = res.json()
        assert js["status"] == "success"
        if random == "https://dog.ceo/api/breeds/image/random":
            assert str(js).count("https://images.dog.ceo") == 1
            v = cerberus.Validator()
            assert v.validate(js, schema)
        if random == "https://dog.ceo/api/breeds/image/random/3":
            assert str(js).count("https://images.dog.ceo") == 3

    # 3 тест
    @pytest.mark.parametrize("images", ['https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg',
                                        'https://images.dog.ceo/breeds/hound-afghan/n02088094_1150.jpg'])
    def test_BY_BREED(self, images):
        res = requests.get('https://dog.ceo/api/breed/hound/images')
        js = res.json()
        assert res.apparent_encoding == 'ascii'
        assert res.status_code == 200
        for k, v in js.items():
            assert images or 'success' in v

    # 4 тест
    def test_LIST_ALL_SUB_BREEDS(self):
        res = requests.get("https://dog.ceo/api/breed/hound/list")
        js = res.json()
        assert js["message"] == ["afghan",
                                    "basset",
                                    "blood",
                                    "english",
                                    "ibizan",
                                    "plott",
                                    "walker"]
        res_random = requests.get('https://dog.ceo/api/breed/hound/afghan/images/random')
        js_random = res_random.json()
        res_images = requests.get('https://dog.ceo/api/breed/hound/afghan/images')
        js_images = res_images.json()
        for v in js_images.values():
            for va in js_random.values():
                assert va or 'success' in v

    # 5 тест
    @pytest.mark.parametrize("dog", ["affenpinscher", "african"])
    def test_BREEDS_LIST(self, dog):
        res = requests.get(f'https://dog.ceo/api/breed/{dog}/images/random')
        js = res.json()
        res_images = requests.get('https://dog.ceo/api/breed/hound/afghan/images')
        js_images = res_images.json()
        for v in js_images.values():
            for va in js.values():
                assert va or 'success' in v