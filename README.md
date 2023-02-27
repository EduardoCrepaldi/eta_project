# eta_project

# ETA

## Resultado
<table class="index" data-sortable>
        <thead>
            <tr class="tablehead" title="Click to sort">
                <th class="name left" aria-sort="none" data-shortcut="n">Module</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="s">statements</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="m">missing</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="x">excluded</th>
                <th class="right" aria-sort="none" data-shortcut="c">coverage</th>
            </tr>
        </thead>
        <tbody>
            <tr class="file">
                <td class="name left"><a href="src/models/ice_cream_stand.py">src/models/ice_cream_stand.py</a></td>
                <td>24</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="24 24">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="src/models/restaurant.py">src/models/restaurant.py</a></td>
                <td>34</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="34 34">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="test/models/test_ice_cream_stand.py">test/models/test_ice_cream_stand.py</a></td>
                <td>66</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="66 66">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="test/models/test_restaurant.py">test/models/test_restaurant.py</a></td>
                <td>75</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="75 75">100%</td>
            </tr>
        </tbody>
        <tfoot>
            <tr class="total">
                <td class="name left">Total</td>
                <td>199</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="199 199">100%</td>
            </tr>
        </tfoot>
    </table>

## Setup

```bash
pip install -r requirements.txt
```


## Pytest

```bash
pytest .
```

## Test Coverage

- `coverage` and `pytest-cov` packages are required
- Add `pragma: no cover` to exclude code from coverage report

### With `pytest`

Terminal report:

 ```bash
pytest --cov-report term-missing --cov .
 ```

HTML report:

```bash
pytest --cov-report html --cov .
```

```bash
 pytest ./test/models --cov . --cov-report html 
 ```

### With `unittest`

To generate report:

```bash
python -m coverage run -m unittest
```

To view report in terminal:

```bash
python -m coverage report
```

To view report in HTML:

```bash
python -m coverage html
```