# Mateo Trucco — Portfolio

Live site: **https://mateotrucco.github.io/**

This repository contains only the portfolio site. Each project has its own repository and GitHub Pages demo.

## Live demo strategy

- Native HTML/CSS/JavaScript projects run directly.
- Pure Python project logic runs in-browser through versioned Pyodide **314.0.4**.
- OS-bound tools use safe sample data because browsers cannot access the host process list, Windows Registry or `.lnk` COM APIs.
- The Django project includes a frontend workflow simulator; the actual Django backend remains in its repository.

## Node.js

Portfolio test tooling is pinned to Node **24.x** (`.nvmrc`, `package.json`, GitHub Actions).
