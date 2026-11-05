# Public Data Catalogue

An offline Python CLI for validating, searching and summarizing dataset metadata. It supports keyword, category and license filtering, rejects duplicate IDs, and validates required fields and HTTP(S) URLs.

## Usage

```bash
python catalogue.py examples/datasets.json
python catalogue.py examples/datasets.json --query school --category Education
python catalogue.py examples/datasets.json --license CC0
```

Each JSON record must include `id`, `title`, `description`, `category`, `license`, and `url`.

## Tests

```bash
python -m unittest discover -s tests -v
```

Eight tests run through GitHub Actions on Python 3.10, 3.12, and 3.13.

## Data disclaimer

The sample records are fictional and their example.org URLs are placeholders. This catalogue does not fetch, verify, endorse, or license real datasets. Always verify source URLs, metadata and licensing before publication.
