# Professional Software Development Workflow

> Reference: What a professional programmer does from idea to production and beyond. Tools, alternatives, and how each fits into the lifecycle.

---

## Lifecycle Overview

```
Idea → Requirements → Design → Environment Setup → Code → Test → Review → CI/CD → Deploy → Monitor → Maintain
```

Every professional team follows some version of this. The tools change; the phases don't.

---

## 1. Ideation & Requirements

**What professionals do:**
- Define what the product should do (features, user stories)
- Prioritize features (MoSCoW, sprint planning)
- Document requirements (user stories, acceptance criteria)
- Track work (backlog, sprints, tickets)

**Tools (industry standard):**

| Tool | Purpose | Cost |
|------|---------|------|
| Jira | Project management, sprint planning, ticket tracking | Paid (free for ≤10 users) |
| Confluence | Documentation, wikis, meeting notes | Paid |
| Miro | Brainstorming, whiteboarding, flowcharts | Paid (free tier limited) |
| Figma | UI/UX design, wireframes, prototypes | Paid (free tier generous) |
| Slack | Team communication | Paid (free tier limited) |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| GitHub Issues + Projects | Jira | Free, built into GitHub. Kanban boards, milestones, labels |
| GitHub Wiki | Confluence | Free, lives in your repo |
| Notion | Confluence + Miro | Free tier for individuals, very flexible |
| Excalidraw | Miro | Free, open source, hand-drawn style diagrams |
| Penpot | Figma | Free, open source, Figma alternative |
| Discord | Slack | Free, voice + text channels, bots |
| Trello | Jira | Free tier, simple Kanban |

---

## 2. Planning & Design

**What professionals do:**
- System design: architecture, data flow, API contracts
- UI/UX design: wireframes, mockups, user flows
- Database design: schema, ER diagrams, migrations
- Technical design documents (RFCs, ADRs)

**Tools (industry standard):**

| Tool | Purpose | Cost |
|------|---------|------|
| Figma | UI design, component libraries, design systems | Paid |
| Lucidchart | System diagrams, ER diagrams, flowcharts | Paid |
| Draw.io (diagrams.net) | General diagrams | Free |
| Swagger/OpenAPI | API design, documentation | Free (open source) |
| dbdiagram.io | Database schema visualization | Free tier |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| Excalidraw | Lucidchart | Open source, runs in browser |
| draw.io | Lucidchart | Free, desktop app available, integrates with VS Code |
| Penpot | Figma | Open source, browser-based |
| Mermaid | Draw.io (for diagrams in code) | Free, Markdown-based diagrams, renders in GitHub |
| DBML + dbdiagram.io | dbdiagram.io | Free tier, code-first schema |

---

## 3. Development Environment Setup

**What professionals do:**
- Choose an OS (macOS, Linux, or Windows with WSL)
- Install a package manager
- Set up terminal + shell
- Install runtime (Node, Python, Go, etc.)
- Set up containerization (Docker)
- Configure editor/IDE

**Tools (industry standard):**

| Tool | Purpose | Platform |
|------|---------|----------|
| macOS / Ubuntu Linux | Primary development OS | macOS, Linux |
| Homebrew | Package manager (macOS/Linux) | macOS, Linux |
| apt / yum | Package manager (Linux) | Linux |
| Windows Terminal | Terminal (Windows) | Windows |
| WSL2 | Linux on Windows | Windows |
| Docker Desktop | Containerization | All |
| OrbStack | Docker alternative (macOS) | macOS |
| nvm / pyenv / rbenv | Version managers (Node/Python/Ruby) | All |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| Scoop / winget | Homebrew (Windows) | Free, Windows-native package managers |
| Podman | Docker Desktop | Free, open source, rootless containers |
| Volta | nvm | Free, fast Node version manager |
| mise (formerly rtx) | pyenv + nvm + rbenv | Free, single tool for multiple runtimes |

---

## 4. Code Editing & Development

**What professionals do:**
- Write code in an IDE with language support (LSP, linting, formatting)
- Use AI assistants for code completion and suggestions
- Debug with breakpoints and inspectors
- Use REPL for experimentation

**Tools (industry standard):**

| Tool | Purpose | Cost |
|------|---------|------|
| VS Code | IDE | Free (open source) |
| JetBrains IDEs (IntelliJ, PyCharm, WebStorm) | Language-specific IDEs | Paid (free for students/open source) |
| Vim / Neovim | Terminal-based editor | Free (open source) |
| Sublime Text | Lightweight editor | Paid (unlimited free trial) |
| GitHub Copilot | AI code completion | Paid (free for students) |
| Cursor | AI-native IDE | Paid (free tier) |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| VS Code | JetBrains (for most use cases) | Free, massive extension ecosystem |
| Continue | GitHub Copilot | Free, open source, local LLM support |
| Tabnine | GitHub Copilot | Free tier, runs locally |
| Aider | Cursor | Free, open source, CLI AI coding |
| Zed | VS Code | Free, open source, fast, AI features built-in |

**Essential VS Code extensions:**
- Language packs (Python, Go, Rust, etc.)
- Pylint / ESLint (linting)
- Black / Prettier (formatting)
- GitLens (Git blame, history)
- Docker (container management)
- Remote SSH (develop on remote servers)
- Thunder Client (API testing, like Postman inside VS Code)

---

## 5. Version Control

**What professionals do:**
- Track every change in Git
- Use branches for features, fixes, experiments
- Write meaningful commit messages (conventional commits)
- Code review via pull/merge requests
- Protect main branch (CI must pass before merge)

**Tools (industry standard):**

| Tool | Purpose | Cost |
|------|---------|------|
| Git | Version control | Free (open source) |
| GitHub | Remote hosting, code review, CI/CD | Free (public repos) |
| GitLab | Remote hosting, CI/CD, DevOps | Free tier |
| Bitbucket | Remote hosting (Atlassian ecosystem) | Free (≤5 users) |
| GitKraken | Git GUI client | Paid (free tier) |
| GitHub Desktop | Git GUI client | Free |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| GitHub (free tier) | GitHub (paid) | Free for public and private repos |
| SourceTree | GitKraken | Free, full-featured Git GUI |
| Lazygit | SourceTree/GitKraken | Free, terminal-based Git GUI |
| GitHub CLI (gh) | GitHub web interface | Free, do everything from terminal |

**Branching strategies (how professionals organize work):**

| Strategy | Description | Best for |
|----------|-------------|----------|
| GitHub Flow | `main` + feature branches, PR to merge | Small teams, continuous deployment |
| Git Flow | `main` + `develop` + `release` + `hotfix` branches | Release-based products |
| Trunk-based | Everyone commits to `main`, short-lived branches | Mature teams, CI/CD heavy |

---

## 6. Testing

**What professionals do:**
- Write tests at every level (unit → integration → E2E)
- Test before and after code changes
- Run tests in CI automatically
- Track code coverage
- Test edge cases, failures, security

**Testing pyramid:**
```
        /  E2E  \        (few, slow, expensive)
       / Integration \   (some, moderate)
      /    Unit Tests   \ (many, fast, cheap)
```

**Tools (industry standard):**

| Tool | Purpose | Language |
|------|---------|----------|
| pytest | Unit/integration testing | Python |
| Jest | Unit/integration testing | JavaScript |
| JUnit | Unit testing | Java |
| Playwright | E2E browser testing | All |
| Cypress | E2E browser testing | JavaScript |
| Selenium | E2E browser testing | All |
| Postman | API testing | All |
| k6 | Load/performance testing | All |
| Locust | Load testing | Python |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| pytest | JUnit (for Python) | Free, plugins ecosystem |
| Vitest | Jest | Free, faster than Jest |
| Playwright | Selenium | Free, Microsoft, faster than Selenium |
| httpx / requests + pytest | Postman (programmatic API testing) | Free, scriptable |
| k6 | JMeter | Free, modern load testing |
| coverage.py | Commercial coverage tools | Free, Python coverage |

---

## 7. Code Quality & Review

**What professionals do:**
- Lint code (catch style and logic errors automatically)
- Format code (consistent style across team)
- Static analysis (find bugs without running code)
- Code review (human + automated review before merge)
- Pre-commit hooks (enforce quality before commit)

**Tools (industry standard):**

| Tool | Purpose | Language |
|------|---------|----------|
| ESLint | Linting | JavaScript/TypeScript |
| Pylint / Flake8 | Linting | Python |
| Ruff | Linting + formatting (fast) | Python |
| Black | Code formatting | Python |
| Prettier | Code formatting | JavaScript/HTML/CSS |
| SonarQube | Static analysis, security, quality | All |
| RuboCop | Linting + formatting | Ruby |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| Ruff | Pylint + Flake8 + Black (all-in-one) | Free, extremely fast |
| ESLint + Prettier | SonarQube (for JS linting/formatting) | Free, industry standard |
| pre-commit | Manual quality checks | Free, Git hook framework |
| Bandit | SonarQube (security for Python) | Free, finds common security issues |
| mypy / Pyright | SonarQube (type checking) | Free, catches type errors |

**Pre-commit hook example:**
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    hooks:
      - id: ruff
      - id: ruff-format
  - repo: https://github.com/pre-commit/pre-commit-hooks
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
```

---

## 8. CI/CD (Continuous Integration / Continuous Deployment)

**What professionals do:**
- Every push triggers automated tests
- Code must pass linting, formatting, tests before merge
- Deploy to staging automatically on merge to main
- Deploy to production on release tag or manual approval
- Rollback if deployment fails

**Pipeline stages:**
```
Push → Lint → Test → Build → Deploy to Staging → Deploy to Production
```

**Tools (industry standard):**

| Tool | Purpose | Cost |
|------|---------|------|
| GitHub Actions | CI/CD (built into GitHub) | Free (2000 min/month) |
| GitLab CI/CD | CI/CD (built into GitLab) | Free (400 min/month) |
| Jenkins | CI/CD server | Free (open source) |
| CircleCI | CI/CD | Free tier (6000 min/month) |
| Travis CI | CI/CD | Free for open source |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| GitHub Actions | Jenkins (for most projects) | Free, YAML config, huge marketplace |
| Dagger | Custom CI scripts | Free, test pipelines locally |
| Earthly | Jenkins complex pipelines | Free, combines Docker + Make |

**GitHub Actions example (Python project):**
```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: ruff check .
      - run: pytest
```

---

## 9. Deployment & Hosting

**What professionals do:**
- Deploy to cloud infrastructure
- Use containers for consistency
- Set up domains and SSL
- Configure environment variables (secrets)
- Set up databases and backups

**Tools (industry standard):**

| Tool | Purpose | Cost |
|------|---------|------|
| AWS (EC2, ECS, Lambda, RDS) | Cloud infrastructure | Paid |
| Google Cloud (GCE, Cloud Run, Cloud SQL) | Cloud infrastructure | Paid |
| Azure (App Service, Functions) | Cloud infrastructure | Paid |
| Heroku | Platform as a Service (PaaS) | Paid |
| Vercel | Frontend/serverless deployment | Free tier |
| Netlify | Static sites + serverless | Free tier |
| Cloudflare | CDN, DNS, Workers, Pages | Free tier |
| DigitalOcean | VPS, databases, managed services | Paid |
| Fly.io | Containers as a Service | Free tier |
| Railway | PaaS | Free tier |
| Render | PaaS | Free tier |

**Free alternatives for personal/small projects:**

| Tool | Purpose | Notes |
|------|---------|-------|
| Vercel | Frontend + API routes | Free for personal projects, deploys from Git |
| Netlify | Static sites + forms + functions | Free tier, auto-deploys from Git |
| Cloudflare Pages | Static sites | Free, unlimited bandwidth |
| Fly.io | Container hosting | Free tier, run Docker containers |
| Railway | Full-stack apps | Free tier, databases included |
| Render | Web services + databases | Free tier (with limitations) |
| GitHub Pages | Static sites | Free, auto-deploys from Git |

**Infrastructure as Code (IaC):**
| Tool | Purpose | Cost |
|------|---------|------|
| Terraform | Cloud infrastructure as code | Free (open source) |
| Pulumi | Cloud infrastructure as code | Free (open source) |
| Ansible | Configuration management | Free (open source) |

---

## 10. Databases & Data

**What professionals do:**
- Choose database type (SQL vs NoSQL vs cache)
- Design schema, run migrations
- Manage database versions (migrations)
- Back up data
- Monitor performance

**Tools (industry standard):**

| Tool | Purpose | Type | Cost |
|------|---------|------|------|
| PostgreSQL | Relational database | SQL | Free (open source) |
| MySQL | Relational database | SQL | Free (open source) |
| MongoDB | Document database | NoSQL | Free tier (Atlas) |
| Redis | Cache / key-value store | Cache | Free (open source) |
| Supabase | PostgreSQL + auth + storage | BaaS | Free tier |
| PlanetScale | Serverless MySQL | SQL | Free tier |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| SQLite | PostgreSQL (for small projects) | Free, zero-config, single file |
| Supabase | Firebase | Free tier, open source, real-time |
| Turso | PlanetScale | Free tier, SQLite at the edge |
| DuckDB | Snowflake (for analytics) | Free, embedded analytics DB |

**Migration tools:**
| Tool | Purpose | Language |
|------|---------|----------|
| Alembic | Database migrations | Python |
| Flyway | Database migrations | Java/All |
| dbmate | Database migrations | Go/All |
| Prisma | ORM + migrations | JavaScript |

---

## 11. Monitoring & Observability

**What professionals do:**
- Track errors in production (error tracking)
- Monitor uptime (is the app alive?)
- Log structured events
- Track performance (latency, throughput)
- Alert on failures

**Three pillars of observability:**
1. **Logs** — what happened
2. **Metrics** — how much / how fast
3. **Traces** — where time was spent

**Tools (industry standard):**

| Tool | Purpose | Cost |
|------|---------|------|
| Datadog | Monitoring, APM, logging | Paid (expensive) |
| New Relic | APM, monitoring | Paid (free tier) |
| PagerDuty | Incident management, on-call | Paid |
| Grafana + Prometheus | Metrics + dashboards | Free (open source) |
| ELK Stack (Elasticsearch, Logstash, Kibana) | Log aggregation | Free (open source) |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| Sentry | Datadog error tracking | Free tier, excellent error tracking |
| Grafana Cloud | Datadog (basic) | Free tier (10K metrics, 50GB logs) |
| UptimeRobot | PagerDuty (uptime) | Free tier, 50 monitors |
| Better Stack | UptimeRobot + logging | Free tier, modern UI |
| Loki + Grafana | ELK Stack | Free, lightweight log aggregation |
| OpenTelemetry | Vendor-specific APM | Free, open standard for traces/metrics/logs |

---

## 12. Documentation

**What professionals do:**
- Write README with setup instructions, usage, architecture
- Document API endpoints (Swagger/OpenAPI)
- Write inline code comments (why, not what)
- Maintain a changelog
- Write ADRs (Architecture Decision Records)
- Keep docs close to code (not in a separate silo)

**Tools (industry standard):**

| Tool | Purpose | Cost |
|------|---------|------|
| Confluence | Team wiki, documentation | Paid |
| Notion | Docs, wikis, project notes | Paid (free tier) |
| Docusaurus | Documentation sites | Free (open source) |
| GitBook | Technical documentation | Free tier |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| GitHub Wiki + README | Confluence | Free, lives with code |
| Notion (free tier) | Confluence | Free for individuals, very flexible |
| Docusaurus | GitBook | Free, Markdown-based, deploys anywhere |
| MkDocs + Material theme | Docusaurus | Free, Python-based, great for API docs |
| Swagger UI + OpenAPI spec | Postman collection docs | Free, auto-generates from API spec |

---

## 13. Collaboration & Communication

**What professionals do:**
- Daily standups (what did I do, what will I do, blockers)
- Sprint planning and retrospectives
- Async communication for distributed teams
- Code review discussions (in PRs)
- Incident response communication

**Tools (industry standard):**

| Tool | Purpose | Cost |
|------|---------|------|
| Slack | Team chat | Paid (free tier limited) |
| Microsoft Teams | Team chat + video | Paid |
| Zoom | Video meetings | Paid (free tier limited) |
| Google Workspace | Docs + email + video | Paid |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| Discord | Slack | Free, voice + text, bots, threads |
| Google Meet | Zoom | Free (with Google account) |
| Zulip | Slack | Free, open source, threaded chat |
| Mattermost | Slack | Free, open source, self-hostable |

---

## 14. Security

**What professionals do:**
- Scan dependencies for vulnerabilities (SCA)
- Scan code for security issues (SAST)
- Never commit secrets (use .gitignore + env vars)
- Use secrets managers
- Enable 2FA everywhere
- Regular security audits

**Tools (industry standard):**

| Tool | Purpose | Cost |
|------|---------|------|
| Snyk | Dependency scanning, SAST | Paid (free tier) |
| SonarQube | Code quality + security | Free (community edition) |
| GitHub Advanced Security | Code scanning, secret scanning | Paid (free for public repos) |
| Vault (HashiCorp) | Secrets management | Free (open source) |

**Free alternatives:**

| Tool | Replaces | Notes |
|------|----------|-------|
| Dependabot | Snyk (dependency updates) | Free, built into GitHub |
| Bandit | SonarQube (Python security) | Free, finds common Python security issues |
| TruffleHog | GitHub secret scanning | Free, scans for leaked secrets |
| .env + python-dotenv | Vault (for small projects) | Free, simple secrets in .env files |
| gitleaks | TruffleHog | Free, fast secret scanning |

---

## The Full Professional Workflow (Step by Step)

Here's what a professional programmer actually does when building a feature or project, start to finish:

### Phase 1: Before Writing Code

```
1. Understand the requirement (user story, bug report, or feature idea)
2. Break it into small tasks (tickets/issues)
3. Design the solution (architecture, data model, API contract)
4. Get design reviewed (tech lead or peer feedback)
5. Set up the environment (branch, dependencies, tools)
```

### Phase 2: Development

```
6. Write code (one task at a time)
7. Write tests alongside code (not after)
8. Run locally after every change
9. Commit with meaningful message (one commit per logical change)
10. Push to remote branch
11. Open pull/merge request (even for solo work — forces review habit)
```

### Phase 3: Review & Quality

```
12. CI runs automatically (lint + test + build)
13. Self-review the diff before requesting review
14. Peer review (if team) — someone else reads the code
15. Address feedback, push again
16. Merge when CI passes and reviewer approves
```

### Phase 4: Deployment

```
17. CI/CD deploys to staging automatically
18. Verify on staging (manual or automated E2E tests)
19. Deploy to production (manual approval or auto on release)
20. Monitor for errors (Sentry, logs, metrics)
21. Rollback if something breaks
```

### Phase 5: After Deployment

```
22. Update documentation (README, changelog, API docs)
23. Monitor for issues (uptime, errors, performance)
24. Gather feedback (users, analytics)
25. Plan next iteration (backlog refinement, sprint planning)
26. Retrospective (what went well, what to improve)
```

---

## Individual Developer Toolkit (All Free)

If you're a solo developer / student building projects, here's the minimum viable toolchain:

| Need | Tool | Why |
|------|------|-----|
| Editor | VS Code | Free, extensions, AI assist |
| Version control | Git + GitHub | Free, industry standard |
| Terminal | Windows Terminal / iTerm2 | Free, modern |
| Package manager | Homebrew (macOS) / apt (Linux) / winget (Windows) | Free |
| Runtime | Python / Node.js / Go | Free, depending on project |
| Containerization | Docker Desktop (free for personal) | Free, consistent environments |
| Linting + formatting | Ruff (Python) / ESLint+Prettier (JS) | Free, catches errors |
| Testing | pytest (Python) / Vitest (JS) | Free, essential |
| CI/CD | GitHub Actions | Free (2000 min/month) |
| Hosting (frontend) | Vercel / Cloudflare Pages | Free |
| Hosting (full-stack) | Railway / Render / Fly.io | Free tier |
| Database | SQLite (local) / Supabase (cloud) | Free |
| Error tracking | Sentry | Free tier |
| Uptime monitoring | UptimeRobot | Free tier |
| Documentation | README + GitHub Wiki | Free |
| API testing | Thunder Client (VS Code) / httpx (Python) | Free |
| Secrets | .env + python-dotenv | Free |
| AI coding assist | Continue (open source) | Free |
| Collaboration | Discord + GitHub | Free |

---

## How This Applies to Project 1 (Expense Tracker)

For your current project, the professional workflow looks like this:

| Phase | What you'll do | Tools |
|-------|----------------|-------|
| Planning | SPEC.md already written ✓ | Markdown |
| Setup | Create project dir, init Git, set up .gitignore | Git, terminal |
| Code v0.1 | main.py (menu, add, list, summary, JSON persistence) | VS Code, Python |
| Test v0.1 | Run manually, test edge cases | Terminal |
| Commit v0.1 | `git add -A && git commit -m "feat: v0.1 core loop"` | Git |
| Refactor v0.2 | Split into modules (main/models/storage/reports) | VS Code |
| Test v0.2 | Add category filter, monthly summary | Terminal |
| CI/CD (optional) | Add GitHub Actions for linting/testing | GitHub Actions |
| Document | README with usage, decisions, AI disclosure | Markdown |
| Review Day 2 | AI-free cumulative review | Terminal |

You don't need all the tools yet. But knowing the full landscape means when you encounter any of them, you'll recognize where they fit.

---

*Last updated: 2026-08-29*
