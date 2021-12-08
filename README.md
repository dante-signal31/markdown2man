[![GitHub release (latest by date)](https://img.shields.io/github/v/release/dante-signal31/markdown2man)](https://github.com/dante-signal31/markdown2man)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![GitHub issues](https://img.shields.io/github/issues/dante-signal31/markdown2man)](https://github.com/dante-signal31/markdown2man/issues)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/y/dante-signal31/markdown2man)](https://github.com/dante-signal31/markdown2man/commits/master)
[![GitHub last commit](https://img.shields.io/github/last-commit/dante-signal31/markdown2man)](https://github.com/dante-signal31/markdown2man/commits/master)

# markdown2man

A GitHub Action to convert a markdown document into a man page.

## Inputs

**Required:**
* *markdown_file*: Markdown file pathname to convert, relative to repository root.
* *manpage_name*: Man page name for converted document.

**Optional:**
* *manpage_section*: Section for converted man page. Defaults to "1".
* *manpage_folder*: Output folder for converted man page. Defaults to the same 
folder as markdown_file.
* *manpage_title*: Title for converted manpage. Defaults to "Usage documentation".

## Usage

```yaml
 uses: dante-signal31/markdown2man@main
    with:
        markdown_file: src/tests/resources/README.md
        manpage_name: cifra
        manpage_section: 2
        manpage_folder: man/
```

With that configuration a man file called cifra.2.gz should be created at man folder.
If manpage_folder does not exist then markdown2man creates it for you.
