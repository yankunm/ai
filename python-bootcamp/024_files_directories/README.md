# Files, Directories, and Paths

## Files

### Open

```with open(file_name, mode) as whatever_name:```

`mode` = 
* `r` read
* `w` write
* `a` append

if `file_name` doesn't exist it'll create it for you in the `!pwd` (present working directory).

### Reading

```file.read()```

### Writing

```file.write(text)```

## Paths

### Absolute File Path

Always start from `/`.

### Relative File Path

Always start from `!pwd` or `./`.

## Pathlib

Comes from Python version 3.4
