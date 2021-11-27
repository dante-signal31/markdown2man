""" Library module for markdown2man functions

This library should be enough to take a GitHub README.md file strip any GitHub
badge and convert it to a valid manpage.
"""


def remove_badges(text: str) -> str:
    """ Remove Github badges.

    :param text: Original text.
    :return: Text with Github badges removed.
    """
    raise NotImplementedError


def add_man_header(text: str, name, section, title) -> str:
    """ Add a header string to markdown that can be converted by Pandoc to a man page header.

    :param text: Original text..
    :param name: Name for this manpage.
    :param section: Man pages section for this page.
    :param title: Title for this page.
    :return: Text with header added.
    """
    # % cifra(1) | cifra usage documentation
    raise NotImplementedError


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
    raise NotImplementedError


def convert_file(source_file: str, output_name: str, manpage_section: str) -> str:
    """ Convert source file to a manpage file.

    Conversion is performed using pandoc.

    Be aware that resulting manpage won't be compressed yet.

    :param source_file: Markdown to convert. You'd better use here preprocesss_source_file() output.
    :param output_name: Name for resulting manpage.
    :param manpage_section: Manpage section to add as extension.
    :return: Pathname to resulting manpage.
    """
    raise NotImplementedError


def compress_manpage(file_to_compress) -> str:
    """ Compress given manpage to a .gz file.

    :param file_to_compress: Manpage file to compress.
    :return: Resulting compressed file pathname.
    """
    raise NotImplementedError


def copy_manpage(source_file: str, destination_folder: str) -> None:
    """ Copy generated manpage to its final folder.

    :param source_file: Current manpage pathname.
    :param destination_folder: Folder to copy on source_file.
    """
    raise NotImplementedError
