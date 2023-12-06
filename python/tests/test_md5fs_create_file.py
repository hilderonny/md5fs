import hashlib
import os
from md5fs import MD5FileHandler

def test_is_content_file_created():
    content = b"\x00\x01\x02"
    filename = "/directory/file.ext"
    expected_md5_hash = hashlib.md5(content).hexdigest() # Should be b95f67f61ebb03619622d798f45fc2d3
    file_handler = MD5FileHandler(root_path = "./testdata", depth = 5)
    generated_hash = file_handler.create_file(filename = filename, content = content, content_type = "application/octet-stream")
    assert generated_hash == expected_md5_hash
    expected_path_parts = list(expected_md5_hash)[:5]
    expected_content_file_path = os.path.join(*expected_path_parts, expected_md5_hash)
    assert os.path.exists(expected_content_file_path)
