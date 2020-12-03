

def test_submit_form(py):
    py.visit('https://demoqa.com/text-box')
    py.get("#userName").type('John Doe')
    py.get("#userEmail").type('johndoe@pc.com')
    py.get("#currentAddress").type('123 Main Street, Midvale, Utah 84095')
    py.get("#permanentAddress").type(py.fake.address())
    py.get("#submit").click()
    assert py.get('p[id="name"]').should().contain_text('John Doe')
    assert py.get('p[id="email"]').should().contain_text('johndoe@pc.com')
    assert py.get('p[id="currentAddress"]').should().contain_text('123 Main Street, Midvale, Utah 84095')


