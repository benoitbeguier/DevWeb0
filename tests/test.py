from flask import Flask

from app import app

def test_user_template():
    client = app.test_client()
    response = client.get("/user/adrien")
    template = app.jinja_env.get_template('user.html')
    assert template.render(name="adrien") == response.get_data(as_text=True)