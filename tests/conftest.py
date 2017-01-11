import pytest

from vc.main import create_app
from vc.database import db

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
    return app
