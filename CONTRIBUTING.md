# Contributing to AI Engineer Workbench

Thank you for your interest in contributing to AI Engineer Workbench.

We welcome contributions that improve the project, fix bugs, enhance documentation, or introduce new production AI engineering features.

---

# Getting Started

1. Fork the repository.

2. Clone your fork.

```bash
git clone https://github.com/<your-username>/ai-engineer-workbench.git
```

3. Create a new branch.

```bash
git checkout -b feature/my-feature
```

4. Install project dependencies.

Backend

```bash
cd backend

python -m venv .venv

source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

Frontend

```bash
cd frontend

npm install
```

---

# Development Guidelines

Please follow these principles when contributing:

- Keep pull requests focused on a single change.
- Write clear commit messages.
- Follow the existing project structure.
- Keep code modular and readable.
- Prefer descriptive variable and function names.
- Add tests where appropriate.
- Update documentation when introducing new functionality.

---

# Commit Message Style

Examples:

```
feat(api): add trace filtering
fix(frontend): improve dashboard loading
docs: update architecture documentation
refactor(db): simplify repository layer
```

---

# Pull Requests

Before opening a pull request, ensure:

- Code builds successfully.
- Tests pass.
- Documentation is updated.
- No unnecessary files are included.

---

# Reporting Issues

When reporting a bug, include:

- Description
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment information

---

# Questions

If you have questions or suggestions, feel free to open an issue.

Thank you for helping improve AI Engineer Workbench.