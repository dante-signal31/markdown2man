""" Test for m2mlib module. """
import os.path

import test_common.fs.ops as test_ops
from test_common.fs.temp import temp_dir

import script.m2mlib as m2mlib


def test_remove_badges():
    # Test setup.
    original_text = ""
    with open("tests/resources/README.md") as original_file:
        original_text = original_file.read()
    expected_text = ""
    with open("tests/resources/README_no_badge.md") as expected_file:
        expected_file = expected_file.read()
    # Perform test.
    recovered_text = m2mlib.remove_badges(original_text)
    assert expected_text == recovered_text


def test_add_man_header():
    # Test setup.
    original_text = ""
    with open("tests/resources/README_no_badge.md") as original_file:
        original_text = original_file.read()
    expected_text = ""
    with open("tests/resources/README_no_badge_with_header.md") as expected_file:
        expected_file = expected_file.read()
    # Perform test.
    recovered_text = m2mlib.add_man_header(original_text, "cifra", "1",
                                          "cifra usage documentation")
    assert expected_text == recovered_text


def test_preprocess_source_file():
    # Test setup.
    original_text = ""
    with open("tests/resources/README.md") as original_file:
        original_text = original_file.read()
    expected_text = ""
    with open("tests/resources/README_no_badge_with_header.md") as expected_file:
        expected_file = expected_file.read()
    # Perform test.
    converted_file = m2mlib.preprocess_source_file("tests/resources/README.md", "cifra", "1", "cifra usage documentation")
    recovered_text = ""
    with open(converted_file) as file:
        recovered_text = file.read()
    assert expected_text == recovered_text


def test_convert_file(temp_dir):
    # Test setup.
    expected_text = ""
    with open("tests/resources/cifra.1") as manpage:
        expected_text = manpage.read()
    temp_pathname = os.path.join(temp_dir, "README.md")
    test_ops.copy_file("tests/resources/README.md", temp_pathname)
    # Perform text.
    converted_pathname = m2mlib.convert_file(temp_pathname, "cifra", "1")
    with open(converted_pathname) as converted_file:
        recovered_text = converted_file.read()
    assert expected_text == recovered_text


def test_compress_manpage(temp_dir):
    # Test setup.
    temp_pathname = os.path.join(temp_dir, "cifra.1")
    test_ops.copy_file("tests/resources/cifra.1", temp_pathname)
    # Perform text.
    m2mlib.compress_manpage(temp_pathname)
    assert os.path.exists(os.path.join(temp_dir, "cifra.1.gz"))


def test_copy_manpage(temp_dir):
    destination_pathname = os.path.join(temp_dir, "cifra.1")
    m2mlib.copy_manpage("tests/resources/cifra.1", destination_pathname)
    assert os.path.exists(destination_pathname)
