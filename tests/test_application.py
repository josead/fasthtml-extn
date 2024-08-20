def test_application_should_work():
    from fasthtml_extn import create_app

    app, rt = create_app()

    assert app is not None
    assert app.routes == rt
