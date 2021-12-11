![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/dante-signal31/markdown2man)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![GitHub issues](https://img.shields.io/github/issues/dante-signal31/markdown2man)](https://github.com/dante-signal31/markdown2man/issues)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/y/dante-signal31/markdown2man)](https://github.com/dante-signal31/markdown2man/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/dante-signal31/markdown2man)](https://github.com/dante-signal31/markdown2man/commits/main)

# markdown2man

A GitHub Action to convert a markdown document into a man page.

This way you only have to keep updated your README.md and generate your application
man page from it with this action.

Be aware that to keep things visually coherent with text structure expected for
a man page your README.md should have every section expected in a man page and 
you should avoid some text structures not easily convertable to man page format.
You'd better read [this article](https://www.dlab.ninja/2021/10/how-to-write-manpages-with-markdown-and.html)
about this method of man page generation. This action uses the basics explained 
in that article. 

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
 - name: Create a man page from current README.md.
   uses: dante-signal31/markdown2man@v1.0.0
   with:
     markdown_file: src/tests/resources/README.md
     manpage_name: cifra
     manpage_section: 2
     manpage_folder: man/
     manpage_title: "How to use cifra"
```

With that configuration a man file called cifra.2.gz should be created at man folder.
If manpage_folder does not exist then markdown2man creates it for you.
