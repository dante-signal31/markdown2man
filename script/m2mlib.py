""" Library module for markdown2man functions

This library should be enough to take a GitHub README.md file strip any GitHub
badge and convert it to a valid manpage.
"""


def add_man_header(file_handle, name, section, title) -> None:
    """ Add a header string to markdown that can be converted by Pandoc to a man page header.

    :param file: Markdown temporal file.
    :param name: Name for this manpage.
    :param section: Man pages section for this page.
    :param title: Title for this page.
    """
    raise NotImplementedError