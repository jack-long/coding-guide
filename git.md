# Git tips

## gitignore

When you specify a folder or file **pattern** in the `.gitignore` file, 
Git will ignore matching files or directories wherever they occur within the repository.

You can place a `.gitignore` file in a subfolder of your project. 
It will work and apply the ignore rules specifically to that subfolder and its contents.

The `.gitignore` file only affects untracked files or new files that haven't been added to the repository yet.
If you have already added a file to `.gitignore` 
but it still shows up in the "Changes not staged for commit" section, 
it means that the file was previously committed to the repository and is still being tracked by Git.

## remove tracked files

`git rm --cached <file_pattern>`

