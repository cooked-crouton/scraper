# cc\_scraper

## Build the project

```py
pip install -e .
```

Some distro will need the `--break-system-packages` argument.

## Run the project

```py
python3 -m cc_scraper
```

## Embeddings

After scraping, each recipe is vectorized locally with `sentence-transformers` (`paraphrase-multilingual-MiniLM-L12-v2`, 384 dimensions, normalized) and the vector is stored in `Recipe.embedding`. The model is downloaded on first run, then works offline.
