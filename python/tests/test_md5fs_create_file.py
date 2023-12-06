import hashlib
import os
import json
from md5fs import MD5FileHandler

def test_is_content_file_created():
    expected_content = b"\x00\x01\x02"
    filename = "/directory/file.ext"
    root_path = "./test_root_path"
    depth = 5
    expected_md5_hash = hashlib.md5(expected_content).hexdigest() # Should be b95f67f61ebb03619622d798f45fc2d3
    file_handler = MD5FileHandler(root_path = root_path, depth = depth)
    generated_hash = file_handler.create_file(filename = filename, content = expected_content, content_type = "application/octet-stream")
    assert generated_hash == expected_md5_hash
    expected_path_parts = list(expected_md5_hash)[:depth]
    expected_content_file_path = os.path.join(root_path, *expected_path_parts, expected_md5_hash)
    assert os.path.exists(expected_content_file_path)
    created_content_file = open(expected_content_file_path, "rb")
    created_content_file_content = created_content_file.read()
    assert created_content_file_content == expected_content

def test_is_metadata_file_created():
    expected_content = b"\x00\x01\x02"
    expected_filename = "/directory/file.ext"
    expected_content_type = "application/octet-stream"
    root_path = "./test_root_path"
    depth = 5
    expected_md5_hash = hashlib.md5(expected_content).hexdigest() # Should be b95f67f61ebb03619622d798f45fc2d3
    file_handler = MD5FileHandler(root_path = root_path, depth = depth)
    generated_hash = file_handler.create_file(filename = expected_filename, content = expected_content, content_type = expected_content_type)
    assert generated_hash == expected_md5_hash
    expected_path_parts = list(expected_md5_hash)[:depth]
    expected_metadata_file_path = os.path.join(root_path, *expected_path_parts, expected_md5_hash + ".json")
    assert os.path.exists(expected_metadata_file_path)
    created_metadata_file = open(expected_metadata_file_path, "r")
    created_metadata_file_content = json.load(created_metadata_file)
    assert created_metadata_file_content["filename"] == expected_filename
    assert created_metadata_file_content["contenttype"] == expected_content_type
