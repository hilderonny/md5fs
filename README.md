# md5fs
File storage system for large amount of files: Uses md5 hashes for file names and a deep directory structure.

There are two implementations, one for [NodeJS](nodejs/) and one for [Python](python/).

## Concept

The main idea came from the requirement to store a very large amount of files on a server. To speed up the access to the filesystem and to prevent to get into file count per directory issues all files are stored in a special way.

When a file gets stored, its MD5 hash gets calculated, for example `7e716d0e702df0505fc72e2b89467910`.

Then a directory structure for the first five digits in the hash is created and the file ist stored in the last leaf. In the example this would be the file `7/e/7/1/6/7e716d0e702df0505fc72e2b89467910`.

Additionally there is a JSON file stored containing the metadata of the original file.

```JSON
{
    "filename" : "original/path/and/filename.ext",
    "contenttype" : "application/zip"
}
```

The JSON file gets the MD5 hash and the extension ".json" as file name. So you get two files belonging together.

```
7/e/7/1/6/7e716d0e702df0505fc72e2b89467910
7/e/7/1/6/7e716d0e702df0505fc72e2b89467910.json
```

## Usage

Please have a look into the language dependent documentation for [NodeJS](nodejs/) and [Python](python/).