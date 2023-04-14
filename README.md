# Watchme

## Monitor changes on files in a directory and automatically re-run the server when a file is changed

### Only works on `Linux/Unix`

- To use, add json and python file to the directory you are working in
- Update the extensions, PORT and script in `config.json` file
- Run `watchme.py`

### `config.json` file format

```bash
{
  "extensions": [],
  "script": " ",
  "PORT": " ",
  "Ignore Directories" = []
}
```
