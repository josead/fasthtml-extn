from fasthtml_extn import create_app, serve

app, rt = create_app(live=False)

serve()
