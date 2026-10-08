# Inexact Computing Lab

Open **inexact and approximate computing research**, **reproducible arithmetic RTL packages**, **design-space exploration (DSE) frameworks**, and a **curated map of 600+ research papers** — accelerating energy-efficient, error-resilient hardware for edge AI, DSP, and domain-specific accelerators.

[![GitHub Pages: Paper Map](https://img.shields.io/badge/Pages-Inexact%20Paper%20Map-181717?logo=github)](https://inexact-computing.github.io/.github/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](https://creativecommons.org/licenses/by/4.0/)
[![Corpus: 600+ Papers](https://img.shields.io/badge/Corpus-600%2B%20Papers-blue)](https://github.com/Inexact-Computing/inexact-computing-lab/blob/main/docs/PAPERS.md)
[![Work Packages: 500+ Baselines](https://img.shields.io/badge/Baselines-500%2B%20RTL-orange)](https://github.com/Inexact-Computing/inexact-computing-lab/tree/main/work)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-3776ab.svg)](https://www.python.org/downloads/)

---

## Quick Navigation

- **[Interactive Paper Map & Explorer](https://inexact-computing.github.io/.github/)**: Live search, filter by domain, error bounds, and reproducible RTL status across 600+ papers.
- **[Research Directions Roadmap (`docs/DIRECTION.md`)](https://github.com/Inexact-Computing/inexact-computing-lab/blob/main/docs/DIRECTION.md)**: Layered synthesis across modeling $\to$ circuit $\to$ architecture $\to$ system.
- **[Multiplier Taxonomy & DSE (`docs/MULTIPLIER.md`)](https://github.com/Inexact-Computing/inexact-computing-lab/blob/main/docs/MULTIPLIER.md)**: Deep dive into approximate multiplier microarchitectures, compressors, and Booth encoding.
- **[Design-Space Opportunity Tracker (`docs/DESIGN_SPACE.md`)](https://github.com/Inexact-Computing/inexact-computing-lab/blob/main/docs/DESIGN_SPACE.md)**: Active exploration branches (O1–O15) closing unmapped design-space coordinates.
- **[Published Reproductions (`work/`)](https://github.com/Inexact-Computing/inexact-computing-lab/tree/main/work/)**: 500+ executable work packages with bit-accurate Python goldens and Verilog RTL.

---

## Architectural Pillars

```
+-------------------------------------------------------------------------------+
|                      INEXACT COMPUTING RESEARCH ECOSYSTEM                     |
+-------------------------------------------------------------------------------+
|  1. Literature Ingestion   |  2. Baseline Reproduction |  3. Design-Space DSE |
|     (papers/, docs/)       |     (work/ packages)      |     (wip/ O1–O15)    |
+----------------------------+---------------------------+----------------------+
|  4. Multi-PDK Synthesis & STA Engine (pdk/, scripts/synth_registry.py)        |
+-------------------------------------------------------------------------------+
|  5. Automated Verification & Quality Gates (CI, scripts/finish_paper_gates.sh)|
+-------------------------------------------------------------------------------+
```

1. **Literature & Synthesis**: Closed-loop tracking from paper index $\to$ PDF dossier $\to$ figure extraction $\to$ cross-paper taxonomy.
2. **Reproducible Work Packages (`work/`)**: 100% executable testbenches, Python goldens, and RTL models matching published claims.
3. **Hypothesis & DSE Tracks (`wip/`)**: Systematic closure of design-space gaps (O1–O15) under a unified benchmark harness (O14).
4. **Standardized PPA & PDK Engine**: Uniform multi-corner PPA extraction (ASAP7 7nm, FreePDK45, Sky130) paired with exact error metrics ($\text{MED}, \text{MRED}, \text{WCE}$).
5. **Interactive Web Dissemination**: Zero-dependency living paper map hosted via GitHub Pages.

---

## Research Tracks

| Research Domain | Core Focus Areas | Key Literature & Dossiers |
| :--- | :--- | :--- |
| **Approximate Multipliers** | Dual-CDM disregards, dynamic range truncation (DRUM, LETAM), approximate 4:2 compressors, Radix-4/8 Booth | [`docs/MULTIPLIER.md`](https://github.com/Inexact-Computing/inexact-computing-lab/blob/main/docs/MULTIPLIER.md) |
| **CORDIC & Trigonometry** | Runtime-adaptive rotations, speculative adders, angle unbiasing, hyperbolic functions | [`papers/`](https://github.com/Inexact-Computing/inexact-computing-lab/tree/main/papers) |
| **Adders & Dividers** | Broken-carry adders, speculative prefix adders, piecewise floating-point dividers | [`docs/PAPERS.md`](https://github.com/Inexact-Computing/inexact-computing-lab/blob/main/docs/PAPERS.md) |
| **Adaptive & Quality-Configurable** | Dynamic error-budget controllers, voltage/frequency scaling, learned unbiasing | [`wip/`](https://github.com/Inexact-Computing/inexact-computing-lab/tree/main/wip) |

---

## Citation & License

This workspace and catalog are curated by the **SJTU Yongfu Research Group** under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Individual third-party papers remain under the copyright of their respective publishers and authors.
