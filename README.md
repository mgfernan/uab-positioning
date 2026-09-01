[![Publish Quarto Slides](https://github.com/mgfernan/uab-positioning/actions/workflows/publish-slides.yml/badge.svg)](https://github.com/mgfernan/uab-positioning/actions/workflows/publish-slides.yml)


# GNSS Positioning Systems

Course presentation for *Multidisciplinary Applications*, part of the Master's Degree in Telecommunication Engineering at UAB. The slides introduce Global Navigation Satellite Systems (GNSS) as a multidisciplinary technology spanning satellite-system design, radio reception, signal processing, positioning algorithms, and real-world services.

## Course Scope

The preliminary material establishes the course roadmap:

- GNSS motivation, history, system architecture, and applications.
- Positioning principles, including trilateration, Time of Arrival (ToA), Time Difference of Arrival (TDoA), pseudorange, carrier phase, Doppler, and navigation equations.
- Accuracy, error sources, mitigation techniques, differential positioning, and augmentation systems.
- GNSS signal structure, spectrum modulation, navigation messages, and modernized signals.
- Receiver architecture: antenna, front end, acquisition, tracking, demodulation, and measurements.
- Applications, positioning-market requirements, and the appropriate accuracy for each scenario.
- Added-value services such as integrity, continuity, and availability, together with GNSS threats, vulnerabilities, and future developments.

By the end of the course, students should be able to explain GNSS architecture and signals, solve navigation equations, understand accurate-positioning principles, describe receiver operation, and assess GNSS applications.

## Project Layout

- `ami_presentation.qmd`: presentation entry point that assembles the sections.
- `slides/sections/introduction.qmd`: introductory material, learning goals, and course roadmap.
- `slides/sections/references.qmd`: bibliography slide container.
- `slides/sections/acronyms.qmd`: definitions for GNSS, GPS, ToA, and TDoA.
- `docs/references.bib`: shared bibliography, rendered with Chicago author-date citations.
- `assets/`: presentation stylesheet and GNSS system/receiver figures.
- `_extensions/`: vendored Quarto `quiz` and `acronyms` extensions.

## Build And Preview

Render the presentation:

```bash
quarto render ami_presentation.qmd
```

Preview it locally while editing:

```bash
quarto preview ami_presentation.qmd --no-browser
```

Rendered files are written to `dist/`. The project configuration enables Reveal.js slide numbers, a chalkboard, automatic preview links, and the UAB footer. Use **Dev Containers: Reopen in Container** in VS Code to obtain the Quarto and Python environment expected by the project.

## Publishing

The GitHub Actions workflow publishes the rendered slides to GitHub Pages after pushes to `main`.

## License

The presentation is distributed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).