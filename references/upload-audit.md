# Upload Audit

## Use this file when

- the paper is close to submission;
- the source ZIP, main PDF, supplement, checklist, or code/data archive will be uploaded;
- the wording changed late and you need to know whether old hashes, manifests, or portal expectations are now stale.

## Three-layer final audit

1. Source archive audit
   Verify unique relative paths, no caches, no absolute local paths, no prompt/tool transcripts, and no stale auxiliary files.
   Prefer a minimal anonymous source ZIP rather than a dump of the full project tree.
2. Read-only PDF audit
   Inspect the already-built PDFs without recompiling them.
   Check page counts, reference-page placement, page size, embedded fonts, metadata anonymity, and visually sensitive figures or tables.
3. Portal preview audit
   After upload, compare the platform preview against a short checklist of fragile pages, figures, and layout assumptions.
   Treat this as distinct from local PDF validation because portal rendering can substitute fonts, blur vectors, or mis-handle supplement slots.

## Reuse rule

If the payload is frozen, document exactly what changed and what stayed byte-identical.

Useful forms include:

- member-level SHA comparison against a prior validated archive;
- synchronized-mirror counts for manuscript copies inside larger code/data packages;
- explicit statement that no solver, bootstrap, fit, or stress-test job was rerun.

## Minimum checks worth keeping

- archive paths are unique, relative, and safe;
- forbidden files are absent;
- required files are present;
- checksum tables match the archive members they claim to describe;
- `title.txt`, `abstract.txt`, `keywords.txt`, `tldr.txt`, and `openreview_registration.txt` stay synchronized when those fields exist;
- main-paper technical content stays inside the venue page budget;
- supplement is not accidentally appended to the main paper in the portal;
- figure text is not clipped, blurred, or font-substituted in portal previews.

## Typical stale-record failures

- local checklist still mentions an old page rule or old runtime total;
- portal title or abstract diverges from the frozen metadata files;
- updated text changed ZIP bytes but the hash manifest was not regenerated;
- a README or mirror manuscript changed in one package but not its synchronized counterpart elsewhere.

## Preferred outputs

- `package_validation.md`
- `SHA256SUMS.csv` or equivalent manifest
- `upload_checklist.md`
- `portal_preview_checklist.md`
- `pdf_readonly_final_audit.md`
