from fasthtml_extn.utils import create_app


def test_create_app():
    app, rt = create_app(live=False)
    assert app is not None
    assert rt is not None
    assert rt.app is app
    assert rt.live is False
    assert rt.debug is False
