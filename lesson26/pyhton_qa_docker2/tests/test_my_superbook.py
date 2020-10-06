import time


def test_add_contact(browserm):
    name_input = browserm.find_element_by_css_selector("input[name='name']")
    phone_input = browserm.find_element_by_css_selector("input[name='phone']")
    name_input.send_keys("Hello")
    phone_input.send_keys("89992323224")
    browserm.find_element_by_css_selector("form[id='record']").submit()
    time.sleep(2)


def test_remove_contact(browserm):
    before_remove = len(browserm.find_elements_by_css_selector("tr[attr='contact']"))
    browserm.find_element_by_css_selector("#remove-button").click()
    after_remove = len(browserm.find_elements_by_css_selector("tr[attr='contact']"))
    assert before_remove == after_remove + 1
    time.sleep(2)
