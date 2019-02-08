# Bash
Snippets of [GNU Bash][bash] code to do simple but helpful things.

- `find ./* -exec sed -i -e 's/foo/bar/g' {} \;` Find & Replace "foo" with "bar" in all files under this directory tree.
- `find ./ -name __pycache__ | xargs rm -rf` Find and delete all directories with the name `__pycache__`.

[bash]: https://www.gnu.org/software/bash/
