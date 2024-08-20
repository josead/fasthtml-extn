# FastHTML-Extn

FastHTML-Extn is a small and opinionated framework for building web applications. It provides a simple and intuitive way to create dynamic HTML pages using [FastHTML](https://github.com/AnswerDotAI/fasthtml).

It's inspired by [Next.js](https://nextjs.org) App approach.

## Usage

```python
from fasthtml_extn import create_app, serve

app, rt = create_app(live=False)

serve()
```

```




## Features

- Autogeneration of routes based on folder structure.
- Layouts ...
- Pages ...

## TODO:

- [x] Route pages like `app/**/*/page.py`
- [x] Route layouts like `app/**/*/layout.py`
- [x] Route expected errors like `app/**/*/except.py`
- [] Route not found like `app/**/*/not_found.py`
- [] Route apis like `app/**/*/router.py`
- [] Add more tests

## Ideas:

- App Seeding with ootb working apps (similar to react-create-app)
- Add more components as helpers. Maybe those should be on it's own library _help needed here_
- Auto creation of folders: ask user from CLI
- Create a CLI for adding pages or routes

## Contributing

We welcome contributions from the community! If you have any bug reports, feature requests, or pull requests, please submit them to our [GitHub repository](https://github.com/josead/fasthtml-extn).

## License

FastHTML-Next is released under the MIT License. See the [LICENSE](https://github.com/josead/fasthtml-extn/LICENSE) file for more information.
```
