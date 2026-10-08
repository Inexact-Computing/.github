# Inexact Computing Lab

Open **inexact and approximate computing research**, **arithmetic hardware architectures**, and a **curated map of 600+ research papers** — accelerating the transition to energy-efficient, error-resilient computing for edge AI, DSP, and domain-specific accelerators.

[![GitHub Pages](https://img.shields.io/badge/Pages-Inexact%20Paper%20Map-181717?logo=github)](https://inexact-computing.github.io/.github/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](https://creativecommons.org/licenses/by/4.0/)
[![Corpus: 600+ Papers](https://img.shields.io/badge/Corpus-600%2B%20Papers-blue)](https://github.com/Inexact-Computing/inexact-computing-lab)
[![Org Followers](https://img.shields.io/github/followers/inexact-computing?label=followers&logo=github)](https://github.com/inexact-computing)

---

## Start Here

- **[Interactive Inexact Paper Map](https://inexact-computing.github.io/.github/)** — Search, filter by research domain, and sort across 600+ curated papers with direct publisher links.
- **[Inexact Computing Lab Workspace](https://github.com/Inexact-Computing/inexact-computing-lab)** — Central research repository containing literature analyses, Python golden models, RTL packages, and PDK benchmark flows.

---

## Repository Structure & Synchronization

This organization profile repository is synchronized from the monorepo [Inexact-Computing/inexact-computing-lab](https://github.com/Inexact-Computing/inexact-computing-lab):
- `profile/README.md`: This landing page (generated from corpus analysis).
- `docs/index.html`: Interactive Paper Map web app deployed to GitHub Pages.
- `docs/papers.json`: Machine-readable catalog metadata.
- `.github/workflows/deploy-pages.yml`: Automated GitHub Pages deployment pipeline.

To refresh the catalog, run `python scripts/sync_papers_json.py` in `inexact-computing-lab`.

---

## License

This catalog and organization profile documentation are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Publisher metadata, DOIs, and paper citations remain under the copyright of their respective publishers (IEEE, ACM, Elsevier, Springer). This repository does not host copyright-restricted PDFs.
