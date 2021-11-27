""" Library module for markdown2man functions

This library should be enough to take a GitHub README.md file strip any GitHub
badge and convert it to a valid manpage.
"""
import gzip
import os
import pypandoc
import shutil
import tempfile


def remove_badges(text: str) -> str:
    """ Remove Github badges.

    :param text: Original text.
    :return: Text with Github badges removed.
    """
    new_text = "\n".join((line for line in text.splitlines() if "![" not in line))
    return new_text


def add_man_header(text: str, name, section, title) -> str:
    """ Add a header string to markdown that can be converted by Pandoc to a man page header.

    :param text: Original text..
    :param name: Name for this manpage.
    :param section: Man pages section for this page.
    :param title: Title for this page.
    :return: Text with header added.
    """
    # % cifra(1) | cifra usage documentation
    header = f"% {name}({section}) | {title}"
    new_text = "\n".join([header, text])
    return new_text


def preprocess_source_file(source_file: str, manpage_name: str, manpage_section: int, manpage_title: str) -> str:
    """ Remove Github Badges and add a proper manpage header.
    
    This function does not touch original source_file. It does copy it to a temporal 
    file instead and modifies it.
    
    :param source_file: Markdown file to modify.
    :param manpage_name: Manpage name to set at header.
    :param manpage_section: Manpage section to set at header.
    :param manpage_title: Manpage title to set at header.
    :return: Pathname to modified file at its temporal location.
    """
    # I don't use TemporaryDirectory() context manager because we need created temporal folder
    # persists until modified_markdown_file is retrieved from outside of this function.
    temp_dir = tempfile.mkdtemp()
    with open(source_file) as markdown_file:
        markdown_content = markdown_file.read()
        markdown_content = remove_badges(markdown_content)
        markdown_content = add_man_header(markdown_content, manpage_name, manpage_section, manpage_title)
        modified_markdown_file_pathname = os.path.join(temp_dir, os.path.basename(source_file))
        with open(modified_markdown_file_pathname, "wt+") as modified_markdown_file:
            modified_markdown_file.write(markdown_content)
        return modified_markdown_file_pathname


def convert_file(source_file: str, output_name: str, manpage_section: str) -> str:
    """ Convert source file to a manpage file.

    Conversion is performed using pandoc.

    Be aware that resulting manpage won't be compressed yet and will be located at the same folder
    than source_file.

    :param source_file: Markdown to convert. You'd better use here preprocesss_source_file() output.
    :param output_name: Name for resulting manpage.
    :param manpage_section: Manpage section to add as extension.
    :return: Pathname to resulting manpage.
    """
    output_file_pathname = os.path.join(os.path.dirname(source_file), f"{output_name}.{manpage_section}")
    pypandoc.convert(source_file, "man", outputfile=output_file_pathname, extra_args=["--standalone"])
    return output_file_pathname


def compress_manpage(file_to_compress) -> str:
    """ Compress given manpage to a .gz file.

    Resulting compressed file will be located at the same folder than file_to_compress.

    :param file_to_compress: Manpage file to compress.
    :return: Resulting compressed file pathname.
    """
    compressed_file_pathname = os.path.join(os.path.dirname(file_to_compress),
                                            f"{os.path.basename(file_to_compress)}.gz")
    with open(file_to_compress, 'rb') as f_in:
        with gzip.open(compressed_file_pathname, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return compressed_file_pathname


def copy_manpage(source_file: str, destination_folder: str) -> None:
    """ Copy generated manpage to its final folder.

    :param source_file: Current manpage pathname.
    :param destination_folder: Folder to copy on source_file.
    """
    shutil.copy(source_file, destination_folder)
