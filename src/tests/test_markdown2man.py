""" Test for markdown2man launcher."""
import gzip
import os
import sys
import tempfile

import test_common.fs.ops as test_ops
from test_common.fs.temp import temp_dir

sys.path.append("src")
import src.markdown2man as markdown2man


def test_launcher_all_options_given(temp_dir):
    # Setup test.
    temporal_markdown_file = os.path.join(temp_dir, "README.md")
    test_ops.copy_file("src/tests/resources/README.md", temporal_markdown_file)
    command_args = [f"{temporal_markdown_file}", "cifra", "-s", "1", "-t",
                    "cifra usage documentation"]
    expected_output_file = os.path.join(temp_dir, "cifra.1.gz")
    recovered_content = ""
    expected_content = ""
    with open("src/tests/resources/cifra.1") as manpage:
        expected_content = manpage.read()

    # Perform test.
    assert not os.path.exists(expected_output_file)
    markdown2man.main(command_args)
    assert os.path.exists(expected_output_file)
    with gzip.open(expected_output_file) as output_file:
        recovered_content = "".join(line.decode() for line in output_file.readlines())
    assert recovered_content == expected_content


def test_launcher_section_changed(temp_dir):
    # Setup test.
    temporal_markdown_file = os.path.join(temp_dir, "README.md")
    test_ops.copy_file("src/tests/resources/README.md", temporal_markdown_file)
    command_args = [f"{temporal_markdown_file}", "cifra", "-s", "2", "-t",
                    "cifra usage documentation"]
    expected_output_file = os.path.join(temp_dir, "cifra.2.gz")
    recovered_content = ""
    expected_content = ""
    with open("src/tests/resources/cifra.1") as manpage:
        expected_content = manpage.read()
    expected_content = expected_content.replace(".TH \"cifra\" \"1\"",
                                                ".TH \"cifra\" \"2\"")

    # Perform test.
    assert not os.path.exists(expected_output_file)
    markdown2man.main(command_args)
    assert os.path.exists(expected_output_file)
    with gzip.open(expected_output_file) as output_file:
        recovered_content = "".join(line.decode() for line in output_file.readlines())
    assert recovered_content == expected_content


def test_launcher_section_omitted(temp_dir):
    # Setup test.
    temporal_markdown_file = os.path.join(temp_dir, "README.md")
    test_ops.copy_file("src/tests/resources/README.md", temporal_markdown_file)
    command_args = [f"{temporal_markdown_file}", "cifra", "-t",
                    "cifra usage documentation"]
    expected_output_file = os.path.join(temp_dir, "cifra.1.gz")
    recovered_content = ""
    expected_content = ""
    with open("src/tests/resources/cifra.1") as manpage:
        expected_content = manpage.read()

    # Perform test.
    assert not os.path.exists(expected_output_file)
    markdown2man.main(command_args)
    assert os.path.exists(expected_output_file)
    with gzip.open(expected_output_file) as output_file:
        recovered_content = "".join(line.decode() for line in output_file.readlines())
    assert recovered_content == expected_content


def test_launcher_title_omitted(temp_dir):
    # Setup test.
    temporal_markdown_file = os.path.join(temp_dir, "README.md")
    test_ops.copy_file("src/tests/resources/README.md", temporal_markdown_file)
    command_args = [f"{temporal_markdown_file}", "cifra"]
    expected_output_file = os.path.join(temp_dir, "cifra.1.gz")
    recovered_content = ""
    expected_line = ".TH \"cifra\" \"1\" \"\" \"\" \"cifra\"\n"
    with open("src/tests/resources/cifra.1") as manpage:
        expected_content = manpage.read()

    # Perform test.
    assert not os.path.exists(expected_output_file)
    markdown2man.main(command_args)
    assert os.path.exists(expected_output_file)
    with gzip.open(expected_output_file) as output_file:
        recovered_content = [line.decode() for line in output_file.readlines()]
    assert expected_line in recovered_content


def test_launcher_uncompressed(temp_dir):
    # Setup test.
    temporal_markdown_file = os.path.join(temp_dir, "README.md")
    test_ops.copy_file("src/tests/resources/README.md", temporal_markdown_file)
    command_args = [f"{temporal_markdown_file}", "cifra", "-s", "1", "-t",
                    "cifra usage documentation", "-u"]
    expected_output_file = os.path.join(temp_dir, "cifra.1")
    recovered_content = ""
    expected_content = ""
    with open("src/tests/resources/cifra.1") as manpage:
        expected_content = manpage.read()

    # Perform test.
    assert not os.path.exists(expected_output_file)
    markdown2man.main(command_args)
    assert os.path.exists(expected_output_file)
    with open(expected_output_file) as output_file:
        recovered_content = output_file.read()
    assert recovered_content == expected_content


def test_launcher_different_output_folder(temp_dir):
    with tempfile.TemporaryDirectory() as temp_output_folder:
        # Setup test.
        temporal_markdown_file = os.path.join(temp_dir, "README.md")
        test_ops.copy_file("src/tests/resources/README.md", temporal_markdown_file)
        command_args = [f"{temporal_markdown_file}", "cifra", "-s", "1", "-t",
                        "cifra usage documentation", "-f", f"{temp_output_folder}"]
        expected_output_file = os.path.join(temp_output_folder, "cifra.1.gz")
        recovered_content = ""
        expected_content = ""
        with open("src/tests/resources/cifra.1") as manpage:
            expected_content = manpage.read()

        # Perform test.
        assert not os.path.exists(expected_output_file)
        markdown2man.main(command_args)
        assert os.path.exists(expected_output_file)
        with gzip.open(expected_output_file) as output_file:
            recovered_content = "".join(line.decode() for line in output_file.readlines())
        assert recovered_content == expected_content