
**Types of git commit messages**

| Type       | Used for                 | Example                             |
| ---------- | ------------------------ | ----------------------------------- |
| `feat`     | New feature              | `feat: add AI agent memory support` |
| `fix`      | Bug fix                  | `fix: handle empty API response`    |
| `chore`    | Maintenance tasks        | `chore: update dependencies`        |
| `docs`     | Documentation            | `docs: add setup instructions`      |
| `refactor` | Code restructuring       | `refactor: simplify agent workflow` |
| `test`     | Adding/updating tests    | `test: add API endpoint tests`      |
| `style`    | Formatting changes       | `style: format Python files`        |
| `perf`     | Performance improvements | `perf: optimize vector search`      |


chore: add pnpm workspace configuration and Turbo tasks
- Created pnpm-workspace.yaml to define package structure for apps and packages.
- Added turbo.json to configure build, dev, lint, test, format, and clean tasks with dependencies and caching settings.