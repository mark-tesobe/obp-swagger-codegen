## OBP Python Swagger Codegen

#### Pre-requesites
* Python 3.9^
* Poetry 1.2.2

#### Installing dependency
```
> poetry install --without test
```

#### Running
```
make run
```
or
```
> poetry run generate -h //Display command line options.
> poetry run generate //Run with default options.
```

#### Development
```
> make format //Run linter and formatter.
> make test //Run tests.
```

#### Other Make Targets
```
> make codegen //Direct command for swagger codegen (Optional `source` argument for location of swagger spec).
> make setup_install //Install generated Python SDK to local Python virtual environment.
> make setup_distribution //Generate Python distribution archives.
> make setup_twine //Upload generated SDK to pypi (Optional `twinerepo` argument).
```
