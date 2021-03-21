# python-brainfuck

Brainfuck interpreter written in Python.

[![Unit Tests](https://github.com/aminnairi/python-brainfuck/actions/workflows/unit_tests.yaml/badge.svg)](https://github.com/aminnairi/python-brainfuck/actions/workflows/unit_tests.yaml) [![Integration Tests](https://github.com/aminnairi/python-brainfuck/actions/workflows/integration_tests.yaml/badge.svg)](https://github.com/aminnairi/python-brainfuck/actions/workflows/integration_tests.yaml)

## Requirements

- UNIX-like operating system
- Git
- Python

## Local installation

### HTTPS

```console
$ git clone https://github.com/aminnairi/python-brainfuck
$ cd python-brainfuck
```

### SSH

```console
$ git clone git@github.com:aminnairi/python-brainfuck
$ cd python-brainfuck
```

## Local usage

```console
$ python main.py helloworld.bf
Hello world!
```

## Global installation

```console
$ echo $PATH | grep /usr/local/bin
$ sudo cp main.py /usr/local/bin/brainfuck
$ sudo chmod +x /usr/local/bin/brainfuck
```

## Global usage

```console
$ brainfuck helloworld.bf
Hello world!
```

## Global update

```console
$ echo $PATH | grep /usr/local/bin
$ git pull
$ sudo rm /usr/local/bin/brainfuck
$ sudo cp main.py /usr/local/bin/brainfuck
$ sudo chmod +x /usr/local/bin/brainfuck
```

## Global uninstallation

```console
$ sudo rm /usr/local/bin/brainfuck
```

## Program exit statuses

### 0

Exited without any errors

### 1

No arguments have been provided (expected one)

### 2

Too much arguments have been provided (expected one)

### 3

Argument provided is not a readable file

### 4

Keyboard interruption (`CTRL-C`)

### 5

Unknown error with its message

## Issues

See [issues](../../issues).

## Changelog

See [`CHANGELOG.md`](./CHANGELOG.md).

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## License

See [`LICENSE`](./LICENSE).
