# NodeJS implementation

## Examples

### Create a file and obtain its MD5 hash

```python
# Import module and define root path for the file structure
from md5fs import MD5FileHandler
file_handler = MD5FileHandler(root_folder="./data")

# Prepare file content
filename = "/this/is/where/my/file/was/located/helloworld.txt"
content = "Hello World" # Can also be binary content
content_type = "text/plain"

# Create file and return MD5 hash
md5_hash = file_handler.create_file(filename, content, content_type)
```

This example calculates a MD5 hash for the file (e.g. `7e716d0e702df0505fc72e2b89467910`) and stores it in a directory structure below the given **root_path** `./data/7/e/7/1/6/7e716d0e702df0505fc72e2b89467910`. Additionally a metadata file gets stored in `./data/7/e/7/1/6/7e716d0e702df0505fc72e2b89467910.json`.

### Fetch the content of a file

```python
content = file_handler.get_file_content(md5_hash)
```

### Fetch the metadata of a file

```python
metadata = file_handler.get_file_metadata(md5_hash)
```
