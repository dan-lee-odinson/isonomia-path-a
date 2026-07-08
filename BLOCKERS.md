# Blockers

Items the build could not resolve autonomously. Per the build directive, nothing here stopped
the run — each item was documented, worked around, and the build continued.

## Open

- **GitHub authentication was not completed during the build.** The GitHub CLI was installed
  (v2.96.0) but `gh auth login` had not been run by the time the build finished, so the repo
  exists locally with the full milestone commit history and could not be pushed. To publish:

  ```powershell
  & "C:\Program Files\GitHub CLI\gh.exe" auth login --hostname github.com --git-protocol https --web
  cd C:\Users\wolfe\projects\agora-path-a
  & "C:\Program Files\GitHub CLI\gh.exe" repo create agora-path-a --public --source . --push --description "Agent-based simulation of the AGORA Tier-1 launch economics (Path A)"
  ```

  Optionally mirror PLAN.md as issue #1 afterwards:

  ```powershell
  & "C:\Program Files\GitHub CLI\gh.exe" issue create --title "Implementation plan (PLAN.md)" --body-file PLAN.md
  ```

## Resolved

- *(none — every other item in the build ran to completion; interpretation calls went to
  DECISIONS.md rather than blocking.)*
