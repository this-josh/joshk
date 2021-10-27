# joshk
 
## CLI

### `python -m joshk --bibtex "your bibtex"

To insert a bibtex entry in a your notion database there are a few things required

1. Install this package
2. Get your notion key and database ID by following the [Getting started](https://developers.notion.com/docs/getting-started#getting-started), this will only take a few minutes.
3. Find a paper on your Mendely, right click and "Copy BibTeX entry"
4. Run `python -m joshk --bibtex "{paste}"

Hey presto, you're done!

**Further usage**

Having to activate the appropriate Python env and type out the full command name may become annoying, if on unix you can add this function to you `.bashrc`/`.zshrc`

```
paper() {
    export NOTION_KEY={your notion key}
    export NOTION_DATABASE_ID=d957d986760c4b5dad0081d781f8e78d
    if [[ "$CONDA_DEFAULT_ENV" == "{your conda env}" ]]; then
        python -m bibtex_to_notion --bibtex "${@}"
    else
        export current_env=$CONDA_DEFAULT_ENV
        conda activate {your conda env}
        python -m bibtex_to_notion --bibtex "${@}"
        conda activate $current_env
    fi
}
```