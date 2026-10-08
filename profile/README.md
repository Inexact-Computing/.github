# Inexact Computing Lab

Open **inexact and approximate computing research**, **arithmetic hardware architectures**, and a **curated map of 600+ research papers** — accelerating energy-efficient, error-resilient computing for edge AI, DSP, and domain-specific accelerators.

[![GitHub Pages](https://img.shields.io/badge/Pages-Inexact%20Paper%20Map-181717?logo=github)](https://inexact-computing.github.io/.github/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](https://creativecommons.org/licenses/by/4.0/)
[![Corpus: 600+ Papers](https://img.shields.io/badge/Corpus-600%2B%20Papers-blue)](https://inexact-computing.github.io/.github/)
[![Org Repositories](https://img.shields.io/badge/Repositories-Inexact--Computing-informational?logo=github)](https://github.com/Inexact-Computing)

---

## Start Here

- **[Interactive Paper Map & Explorer](https://inexact-computing.github.io/.github/)**: Search, filter, and explore 600+ curated research papers on approximate multipliers, adders, CORDIC, and error-tolerant computing.
- **[Inexact Computing Lab Monorepo](https://github.com/Inexact-Computing/inexact-computing-lab)**: Research repository containing literature analyses, Python golden models, RTL packages, and PDK benchmark flows.

---

## Research Domains

```
+-----------------------------------------------------------------------------------------+
|                               INEXACT COMPUTING TAXONOMY                                |
+-----------------------------------------------------------------------------------------+
| [1. Primitive Circuits]   | [2. Multipliers & Adders]   | [3. Algorithms & Systems]     |
| - Approximate Compressors | - Dynamic Range Truncation  | - Runtime-Adaptive CORDIC     |
| - Broken-Carry Logic      | - Approximate Booth (R4/R8) | - Error-Resilient DNN / Edge  |
| - Speculative Prefix Cells| - Encoded Partial Products  | - Rate-Distortion Compilation |
+-----------------------------------------------------------------------------------------+
```

| Research Domain | Core Focus Areas | Description |
| :--- | :--- | :--- |
| **Approximate Multipliers** | Truncation (DRUM, LETAM), Compressors (4:2, 5:2), Booth | Trading partial product generation and accumulation accuracy for power and area savings. |
| **Adders & Dividers** | Broken-carry adders, speculative prefix, piecewise dividers | Low-latency carry-propagation truncation and speculative error recovery schemes. |
| **CORDIC & Non-Linear** | Adaptive iteration count, scaling-free, angle unbiasing | Hardware-efficient trigonometric, vector rotation, and coordinate transformation units. |
| **Quality-Configurable** | Dynamic error-budget control, voltage/frequency scaling | Systems that dynamically scale arithmetic precision based on runtime QoS constraints. |
| **Domain Applications** | Image/Video DSP (PSNR/SSIM), Deep Learning (CNNs/Transformers) | Downstream evaluation of inexact arithmetic in noise-tolerant application workloads. |

---

## Curated Catalog & Tooling

The [`docs/`](docs/) directory in this repository powers a live, zero-dependency **Paper Map** hosted on GitHub Pages:
- **Instant Search**: Real-time filtering across titles, authors, venues, years, and categories.
- **Structured Database**: Machine-readable [`docs/papers.json`](docs/papers.json) containing metadata and DOIs.
- **Citation Export**: 1-click BibTeX generation for all indexed papers.

---

## Citation & License

This workspace and literature catalog are curated by the **SJTU Yongfu Research Group** under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
