# Sustainability reporting portfolio

Professional portfolio covering sustainability reporting, ESG data, reporting controls and assurance readiness.

Website: https://marinaesg.github.io/

## Local preview

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory site
```

## Edit and validate

Edit page content in `scripts/build_site.py`, design in `site/assets/styles.css`, and navigation behaviour in `site/assets/main.js`.

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
```

## Publication

GitHub Pages uses the manual **Publish approved portfolio** workflow. It uploads only `site/` and requires the owner to approve the preview before entering the publication confirmation. There is no automatic push trigger.

Case studies label independent work and document their evidence boundaries. No client records or research corpus are included.
