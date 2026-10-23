---
name: saudi-olympiad-data
description: Answer questions about Saudi olympiad teams, participants, awards, exams, and selection results; help maintain their JSON data and contribute to the shared WebsiteBuilder websites.
---

# Saudi Olympiad Websites

Use this self-contained guide across the websites below. Read detailed documentation and source files only as needed. Answer in the user's language; retain code identifiers and recorded personal names.

## Choose the scope

- Identify the subject from the request or established conversation. If it remains unspecified or ambiguous, ask which subject the user means: informatics, mathematics, physics, AI, biology, or chemistry. Do not choose a subject merely because this file was fetched from that website.
- Honor explicit requests covering several subjects or all six teams. Check dataset meanings and identity conventions before combining records.
- For a shared builder question, inspect WebsiteBuilder directly; ask for a subject only when a site-specific setting or result matters.

## Website and repository directory

| Subject | Website | Source repository |
| --- | --- | --- |
| Informatics | [sainformatics.org](https://sainformatics.org/) | [informatics-website](https://github.com/informatics-sa/informatics-website) |
| Mathematics | [mathsa.org](https://mathsa.org/) | [math-website](https://github.com/informatics-sa/math-website) |
| Physics | [physics.sainformatics.org](https://physics.sainformatics.org/) | [physics-website](https://github.com/informatics-sa/physics-website) |
| AI | [ai.sainformatics.org](https://ai.sainformatics.org/) | [ai-website](https://github.com/informatics-sa/ai-website) |
| Biology | [bio.sainformatics.org](https://bio.sainformatics.org/) | [biology-website](https://github.com/informatics-sa/biology-website) |
| Chemistry | [chem.sainformatics.org](https://chem.sainformatics.org/) | [chemistry-website](https://github.com/informatics-sa/chemistry-website) |

- Use [WebsiteBuilder](https://github.com/informatics-sa/WebsiteBuilder) for shared generation code, libraries, and layouts.
- Use [WebsiteTemplate](https://github.com/informatics-sa/WebsiteTemplate) and its [example site](https://template.sainformatics.org/) for implementation examples. Exclude template records from real team statistics.
- Start with the selected site's `/data/` documentation and `/data/dev` developer guide when available. Use the [shared data guide](https://sainformatics.org/data/) and [developer guide](https://sainformatics.org/data/dev) as fallbacks; check compatibility with the selected site.

## Find the relevant files

Look for public JSON at `<site-origin>/data/<filename>`. In the team repository, inspect `root/data/`. Verify availability; files and enabled features vary by site. A missing file or failed request does not establish an empty dataset.

| File | Purpose |
| --- | --- |
| `settings.json` | Builder selection, ID mode, feature switches |
| `people.json` | People, bilingual names, identifiers |
| `olympiads.json` | Competition definitions |
| `participations.json` | Competition editions, participants, awards, optional scores |
| `exams.json` | Exam definitions and per-task scores |
| `tsts.json` | Selection exams, weights, eligibility settings |
| `images.json` | Image metadata |
| `contact.json` | Contact roles and person references |
| `countries.json` | Country metadata |
| `translations.json` | Interface translations |

Read `settings.json` before interpreting IDs or optional features. Check `website_builder` or legacy `version` before inspecting implementation behavior; a site may use a release, branch, or commit other than the latest `main`.

Use a person's numeric `iid` by default. When `settings.old_id_system` is true, use the legacy string `id` instead. Verify references against the selected dataset and active implementation.

## Answer data questions

1. Establish the subject, competition, year range, and requested measure. Clarify distinctions that change the answer, such as unique people versus participation entries.
2. Retrieve current JSON from the selected website. If unavailable, use the corresponding repository files and label that source; repository data may differ from the deployed site. Record retrieval date and repository revision when available.
3. Load only needed files. Join participation `name` to olympiad `id`; resolve person references using the configured ID mode. Match numeric IDs to JSON object keys carefully, since object keys are strings. Never join different teams by matching local IDs alone.
4. Calculate numerical answers from retrieved records, using code for substantial aggregation. State the filters, counting unit, and relevant formula. Keep gold, silver, bronze, and `hm` separate; distinguish medals from awards that include honorable mentions.
5. Preserve the difference between zero, null, absent, and unavailable. Interpret explicit null awards according to the schema; do not infer an award from a missing record. Filter competition editions by `year`, which may differ from the calendar year of their dates.
6. For exam and selection calculations, inspect the configured builder's implementation and actual JSON. Apply task sums, weights, eligibility rules, exclusions, team size, and tie handling as relevant. Distinguish a calculated ranking from confirmed team participation.
7. Link the JSON sources and relevant human-readable pages. Verify page URLs through navigation or generated routes. Report material gaps or disagreements with rendered summaries; do not substitute remembered totals.

If browsing or file access is unavailable, request the relevant JSON or explain what could not be verified. Never manufacture current results.

## Contribute to a website

1. Inspect repository instructions, README, workflow, and current files. Use the team repository for its data and settings, WebsiteBuilder for shared behavior and layouts, and WebsiteTemplate when starting another site.
2. Trace the build: `prebuild.py` obtains WebsiteBuilder, `build.py` generates page data/front matter, and Jekyll renders the website. Check the actual workflow and selected builder revision before changing this flow.
3. Edit maintained source rather than generated pages. Preserve IDs, JSON types, bilingual fields, date formats, and existing conventions. Use supplied or verified personal names; do not invent name variants.
4. Check JSON syntax, unique identifiers, cross-file references, task arrays, weights, and affected translations. Change relevant records and explain unresolved source conflicts.
5. Resolve documentation/code differences explicitly. Verify spellings such as `execluded` versus `excluded`, `_general_execluded` versus `_general_excluded`, and `participants_count` versus `participations_count` against active code. Do not silently rename keys or assume aliases exist.
6. Follow repository build instructions and run relevant checks. A common sequence from the team repository root is:

   ```bash
   python3 prebuild.py
   bundle install
   python3 build.py
   bundle exec jekyll build --source ./root --destination ./_site
   ```

   For shared changes, use `python3 prebuild.py --path ../WebsiteBuilder` when supported, adjusting the local path. Prebuild copies builder files into the checkout; inspect the diff before including generated or copied files in a contribution.
7. Inspect affected Arabic and English pages, links, and calculated results. Summarize changes, behavior, checks, and limitations. Separate a prepared contribution from an actually published change.

## English–Arabic glossary

Use these plain-language defaults. Prefer the selected site's existing translations and recorded competition names. Keep JSON keys, IDs, URLs, and acronyms unchanged.

| English | Arabic |
| --- | --- |
| Informatics | المعلوماتية |
| Mathematics | الرياضيات |
| Physics | الفيزياء |
| Artificial intelligence (AI) | الذكاء الاصطناعي |
| Biology | الأحياء |
| Chemistry | الكيمياء |
| Olympiad | أولمبياد |
| Participant | مشارك / مشاركة |
| Participation | مشاركة |
| Gold / silver / bronze medal | ميدالية ذهبية / فضية / برونزية |
| Honorable mention (`hm`) | شهادة تقدير |
| Score | درجة |
| Team selection tests (TSTs) | اختبارات اختيار الفريق |
| Eligibility | الأهلية |
| Maintainer / developer | مسؤول صيانة / مطوّر |

## Example requests

- “Who won gold at IOI?” Use informatics, clarify the year range if needed, filter awards, and resolve names.
- “How many medals did we win in 2025?” Ask which subject; count gold, silver, and bronze from current records, with `hm` listed separately.
- “Compare mathematics and physics results for 2024.” Retrieve both datasets and compare a defined measure without merging local person IDs.
- “Add this student's exam result.” Establish the subject and exam, validate the supplied person reference and task scores, and check affected pages.
- “Fix a layout shared by all sites.” Inspect WebsiteBuilder and test the shared change with representative team configurations.