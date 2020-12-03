

def test_radio_button_yes(py):
    py.visit('https://demoqa.com/radio-button')
    py.get('#yesRadio').click(force=True)
    assert py.get('.text-success').should().have_text('Yes')


def test_radio_button_impressive(py):
    py.visit('https://demoqa.com/radio-button')
    checkbox = py.get('#impressiveRadio')
    checkbox.click(force=True)
    assert checkbox.is_selected()


def test_radio_button_no(py):
    py.visit('https://demoqa.com/radio-button')
    no_radio_button = py.get('#noRadio')
    py.execute_script('arguments[0].disabled= false', no_radio_button.webelement)
    no_radio_button.click(force=True)
    assert no_radio_button.is_selected()