# Mateo Trucco — Portfolio

A dependency-free bilingual portfolio presenting nine intentionally distinct projects. Repeated exercises were consolidated into stronger systems with clear workflows, testable logic and honest platform boundaries.

[![Portfolio home](screenshots/portfolio-home.png)](https://mateotrucco.github.io/)

**[Visit the portfolio](https://mateotrucco.github.io/)** · [Browse the GitHub profile](https://github.com/MateoTrucco)

## Experience

- Five selected projects with larger editorial cards
- Searchable and filterable index for nine focused repositories
- Code-native symbolic project visuals instead of brittle screenshots
- Hand-written English/Spanish content with device-language detection
- Shared, persistent light/dark preference across portfolio and demos
- Rotating hero copy, terminal messages, counters, capability chart and reveal animations
- Responsive layout with skip navigation and semantic landmarks
- Central project metadata in `static/js/projects.js`

## Live-project strategy

- Native HTML/CSS/JavaScript projects run directly.
- Pure Python logic runs in the browser through versioned Pyodide **314.0.4**.
- The consolidated system workbench uses transparent, portable snapshots because a browser cannot inspect host processes safely.
- The Django project exposes its main workflow as an interactive simulator; the real authenticated backend remains in its repository.

## Local development

Serve the workspace from its parent directory so project links resolve exactly as they do on GitHub Pages:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000/mateotrucco.github.io/`.

```bash
npm test
```

Node **24.x** is pinned through `.nvmrc`, `package.json` and GitHub Actions.
