# Blockers

Items the build could not resolve autonomously. Per the build directive, nothing here stopped
the run — each item was documented, skipped or worked around, and the build continued.

## Open

- **GitHub authentication not completed at build time.** `gh` CLI was installed (v2.96.0) but
  `gh auth login` had not been run when the build started. All milestones are committed locally
  on `main`. If pushes were still failing at the end of the build, the final report includes the
  exact commands to create the remote and push. *Workaround: none needed for the build itself;
  publication only.* (This entry is removed if auth succeeded mid-build.)

## Resolved

*(none yet)*
