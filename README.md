# Watchme

## Monitor changes on files in a directory and automatically re-run the server when a file is changed (re-running server broke in testing but you can re-run a file xD)

### Only works on `Linus/Unix`

- To use, add json and python file to the directory you are working in
- Update the extensions, PORT and script in `config.json` file
- Run `watchme.py`

### `config.json` file format

```bash
{
  "extensions": [],
  "script": " ",
  "PORT": " "
}
```
