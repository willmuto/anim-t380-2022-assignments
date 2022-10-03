# Assignment 3

 Using a shell of your choice (Windows Command Prompt, Git Bash, etc):
 * Make an alias that sets an environment variable named asset and store that in a file called `etc/.aliases`
 * Make a script (shell or python) that uses the environment variable to make a directory `assets/$asset/maya/scenes`
 * Make a script in python that create an empty group in a Maya scene with that asset name (use an environment variable or you can pass the asset name as an argument)

When creating the directory, there are a couple of different ways you could approach it:

* Python: https://docs.python.org/3/library/os.html#os.makedirs
* Bash: https://stackoverflow.com/questions/1731767/how-can-i-create-nonexistent-subdirectories-recursively-using-bash
* Windows Command Prompt: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mkdir
* Powershell: https://stackoverflow.com/questions/47357135/powershell-equivalent-of-linux-mkdir-p

When creating the empty group in Maya, look at the usage of:
https://help.autodesk.com/cloudhelp/2018/CHS/Maya-Tech-Docs/CommandsPython/group.html

 ## Code Examples

 ### Aliases

**Git Bash/zsh**

```bash
# This is an example comment
alias testprint='echo Hello world'
```

**Windows Command Prompt**
```bat
DOSKEY testprint=echo "Hello world"
```

**Powershell**

Note: Powershell aliases do not allow you to use default arguments, so you'll need to create a function.
```powershell
New-Alias -Name testprint -Value 'echo'  
```

### Environment Variables

**Git Bash/zsh**

```bash
export asset=raptor
echo $asset
```

**Windows Command Prompt**
```bat
set asset=raptor
echo %asset%
```

**Powershell**
```Powershell
$env:asset='trex'
echo $env:asset
```

**Python**
```python
>>> import os
>>> os.getenv('asset')
'raptor'
```

### Batch Scripts

**Git Bash/zsh**

Note: Name your file with the `.sh` extension
```bash
# This is a comment
echo "Hello world"
```

**Windows Command Prompt**

Note: Name your file with the `.bat` extension
```bat
@echo off
REM This is a comment
echo "Hello world"
```

**Powershell**

Note: Name your file with the `.ps1` extension
```Powershell
# This is a comment
Write-Output "Hello world"
```
