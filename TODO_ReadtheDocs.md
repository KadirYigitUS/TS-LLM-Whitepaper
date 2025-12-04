## Website Audit Form -- https://ts-llm-whitepaper.readthedocs.io/

| Page URL (full) | Section / Sub-page | Status (PASS/WARN/NA) | Issue / Remark | Severity / Priority | Suggestion / Comment |
| --- | --- | --- | --- | --- | --- |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/ | Form-wise / Metadata / Structure | PASS | Valid HTML5, lang="en", charset + viewport meta present, sidebar + search work on desktop/mobile. | Low | Keep _static assets versioned; no action needed. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/tr/index.html | Form-wise / lang attribute | PASS | `html_lang` now updates server-side via `html-page-context`, so Turkish pages emit `lang="tr"` without client JS. | Low | No further action until dedicated RTD locale goes live. |
| https://ts-llm-whitepaper.readthedocs.io/tr/latest/ | Form-wise / URL structure | PASS | Native `ts-llm-whitepaper-tr` build now serves `/tr/latest/*`, so the temporary redirect was removed from `.readthedocs.yaml`. | Low | Monitor both EN/TR builds after each push to keep locales in sync. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/en/index.html | Content-wise / Outline | PASS | Headings follow H1->H2->H3, translator-centric framing intact, APA citations linked; no typos detected. | Low | Continue syncing from Obsidian to avoid drift. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/tr/index.html | Content-wise / Turkish overview | PASS | Manual summaries cover goals, seminal papers, and theoretical bridges; consistent tone. | Low | Keep human-curated TR summaries; avoid machine translation. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/en/knowledge_graphs.html | Functionality / Widgets | PASS | Mermaid renders via CDN; Connected Papers iframe now points to GitHub Pages (https://kadiryigitus.github.io/...) so no RTD 404. | Medium | Monitor iframe size/CSP after each widget rebuild and document changes in /script/. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/tr/knowledge_graphs.html | Functionality / Widgets (TR) | PASS | Turkish captions mirror EN copy while embedding the same GitHub Pages iframe; widget note now states the 5 Dec 2025 data snapshot. | Low | Update the note in both languages after each widget rebuild. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/en/repository_structure.html | Functionality / Navigation | PASS | sphinx-design tabs render without parser warnings after converting to fenced directives with blank-line padding. | Low | None. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/tr/repository_structure.html | Functionality / Navigation (TR) | PASS | Added explicit MyST anchors plus auto `aria-label` hints so hash links remain localized and tab sets expose language cues. | Low | Keep anchor slugs in sync with future heading edits. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/en/troubleshooting.html | Design / UX / Accessibility | PASS | Tabs provide bilingual view with adequate contrast; layout aligns with RTD responsive breakpoints. | Low | Consider aria-label hints if tabs expand. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/tr/troubleshooting.html | Design / UX / Accessibility (TR) | PASS | Turkish remediation steps stay in sync with EN; same tab styling maintains contrast ratios. | Low | Mirror any new troubleshooting macros into the TR Obsidian outline before publishing. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/ (site-wide) | Localization / Language switcher | PASS | RTD language selector now exposes EN/TR locales backed by the dedicated Turkish project. | Low | If UI toggle disappears, re-check Admin -> Translations to confirm the TR project is linked. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/en/knowledge_graphs.html and /tr/... | Cross-cutting / External assets | PASS | All external JS/iframes loaded over HTTPS; no mixed-content warnings, CSP respected. | Low | Log widget regenerations via build_semantic_widgets.py. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/en/references.html | APA Coverage | PASS | Every cited article/book appears once, ordered per APA; mirrors Obsidian References.md. | Low | Keep script/collect_references.py as single source of truth. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/tr/references.html | APA Coverage (TR) | PASS | Turkish landing page now explains why APA entries stay in English and how ISBNs replace missing DOIs. | Low | None. |
| https://ts-llm-whitepaper.readthedocs.io/en/latest/en/references.html | DOI Coverage | WARN | All primary/secondary works list DOIs; tertiary books without DOIs now link to publisher pages (statmt.org, Cambridge). | Medium | For works lacking DOIs (Nord 1997, Reiss & Vermeer 2013), cite ISBN + note "DOI unavailable" in future revision. |

### Outstanding External Task
1. None — continue keeping EN/TR content aligned and monitor DOI coverage rows.

### Notes & Resolutions
- Converted every sphinx-design tab block to fenced directives with blank-line padding, clearing 51 parsing errors in sphinx -b linkcheck.
- Added _static/js/lang-patch.js and registered it in conf.py so client-side lang reflects Turkish paths until RTD translations launch.
- Updated .readthedocs.yaml with a prefix redirect mapping /tr/latest/* to /en/latest/tr/*, eliminating the previously reported 404s.
- Fixed the broken Connected Papers iframe by pointing to the GitHub Pages asset; documented the CDN fallback inline.
- Replaced the dead Koehn (2010) DOI link with the maintained statmt.org landing page and reran sphinx -b linkcheck (clean run).
- Added hidden English + Turkish toctrees below the Language Navigator so RTD registers every page even though the visible tabs now use bullet links.
- Included the requested APA/DOI audit rows to track citation completeness across the manuscript corpus.
