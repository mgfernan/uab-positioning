# AMI Presentation Scaffold

A Quarto Reveal.js presentation scaffold for UAB coursework.

## Structure

- `ami_presentation.qmd`: presentation entry point.
- `slides/sections/`: reusable slide sections, including references.
- `docs/references.bib`: project-wide bibliography.
- `assets/`: neutral presentation styling and static assets.
- `_extensions/`: vendored `quiz` and `acronyms` Quarto extensions.

## Commands

- Render: `quarto render ami_presentation.qmd`
- Preview: `quarto preview ami_presentation.qmd --no-browser`

Output is written to `dist/`. Use **Dev Containers: Reopen in Container** in VS Code to get the complete Quarto and Python environment. GitHub Actions publishes rendered slides to GitHub Pages after pushes to `main`.