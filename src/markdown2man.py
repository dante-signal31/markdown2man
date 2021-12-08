#!/usr/bin/env python3
import argparse
import os
import sys
from typing import List, Dict

import lib.m2mlib as m2mlib

DEFAULT_MANPAGE_SECTION = 1


def _check_file_exists(file: str) -> str:
    """ Check given file actually exists.

    :param file: File to check.
    :return: Given string if it is actually a file.
    """
    if os.path.exists(file):
        return file
    else:
        raise argparse.ArgumentTypeError(f"Given file {file} does not exists.")


def _get_folder_path_prefix() -> str:
    """ Check if we are running inside a Github Action and returns the real path
    were application files are actually stored.

    If we aren't running inside Github Action an empty string is returned.

    :return: Prefix for application folder.
    """
    return os.getenv("GITHUB_WORKSPACE", "")


def _prepend_path_prefix(args: Dict[str, str])-> Dict[str, str]:
    """ If we are running inside a GitHub Action prepend its real path where
    application is actually stored.

    :param args: User arguments as output by parse_arguments()
    :return: The same arguments with prefix prepended in arguments where a path is provided.
    """
    path_arguments = {"markdown_file", "manpage_folder"}
    if (prefix := _get_folder_path_prefix() != ""):
        for key in path_arguments:
            args[key] = os.path.join(prefix, args[key])
    return args


def parse_args(args: List[str]) -> Dict[str, str]:
    """ Parse given arguments

    :param args: Program arguments.
    :returns: A Dictionary with given arguments as keys and its respective values.
    """
    parser = argparse.ArgumentParser(
        description="Console command to convert a markdown document into a man page.",
        epilog="Follow this tool development at: "
               "<https://github.com/dante-signal31/markdown2man"
    )
    parser.add_argument("markdown_file",
                        type=_check_file_exists,
                        help="Path to markdown file to convert.",
                        metavar="MARKDOWN_FILE")
    parser.add_argument("manpage_name",
                        type=str,
                        help="Name for resulting manpage file. Do not add extension.",
                        metavar="MANPAGE_NAME")
    parser.add_argument("-s", "--manpage_section",
                        type=str,
                        default=str(DEFAULT_MANPAGE_SECTION),
                        help=f"Section for resulting manpage. Defaults to "
                             f"{DEFAULT_MANPAGE_SECTION}",
                        metavar="MANPAGE_SECTION")
    parser.add_argument("-t", "--manpage_title",
                        type=str,
                        help="Title for resulting manpage. Defaults to manpage_name.",
                        metavar="MANPAGE_TITLE")
    parser.add_argument("-u", "--uncompressed",
                        action="store_true",
                        default=False,
                        help="Do not compress resulting manpage. Defaults to False")
    parser.add_argument("-f", "--manpage_folder",
                        type=str,
                        help="Folder to place resulting manpage. Defaults to the "
                             "same as markdown file.",
                        metavar="MANPAGE_FOLDER")
    parsed_arguments = vars(parser.parse_args(args))
    filtered_parser_arguments = {key: value
                                 for key, value in parsed_arguments.items()
                                 if value is not None}
    return filtered_parser_arguments


def main(args=sys.argv[1:]) -> None:
    """ Main execution.

    Taken to its own function to ease testing.

    :param args: Application arguments. Only explicitly set at tests. Usually you'll
    leave it empty and it will populated with sys.argv values.
    """
    arguments: Dict[str, str] = parse_args(args)
    # arguments = _prepend_path_prefix(arguments)
    source_file_preprocessed = m2mlib.preprocess_source_file(
        source_file=arguments["markdown_file"],
        manpage_name=arguments["manpage_name"],
        manpage_section=int(arguments["manpage_section"]),
        manpage_title=arguments.get("manpage_title", arguments["manpage_name"]))
    print(f"Output name: _{arguments['manpage_name']}.{arguments['manpage_section']}_")
    manpage = m2mlib.convert_file(
        source_file=source_file_preprocessed,
        output_name=arguments["manpage_name"],
        manpage_section=arguments["manpage_section"])
    if not arguments["uncompressed"]:
        manpage = m2mlib.compress_manpage(manpage)
    m2mlib.copy_manpage(
        source_file=manpage,
        destination_folder=arguments.get("manpage_folder", os.path.dirname(arguments["markdown_file"])))
    # print(f"Default manpage folder: {os.path.dirname(arguments['markdown_file'])}")
    # print(os.listdir("/work/src/tests/resources/"))


if __name__ == "__main__":
    main()
