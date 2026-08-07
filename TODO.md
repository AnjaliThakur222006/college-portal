# Task: Fix models.py errors

## Steps

- [x] 1. Create TODO.md to track progress
- [x] 2. Fix `myproject/student/models.py`:
  - Remove leading space before `class course`
  - Rename `course` → `Course`
  - Fix indentation to consistent 4 spaces
  - Add `Enrollment` through-model
  - Add `__str__` to `Student` model
- [x] 3. Update `myproject/student/admin.py` — Register `Course` and `Enrollment`
- [x] 4. Run `makemigrations` and `migrate` — **Done** ✅

# Task: Fix GitHub upload error

## Steps

- [x] 1. Diagnose the upload issue:
  - Root repo remote: `college-portal.git`
  - Nested `myproject/.git` (separate repo) → caused conflicts
  - `db.sqlite3` + `__pycache__` files were tracked but ignored by `.gitignore`
- [x] 2. Remove nested `myproject/.git` so the whole project is ONE repo
- [x] 3. `git rm --cached` database files and `__pycache__` files (keep them on disk)
- [x] 4. Stage all real code (forms.py, templates, migrations, models, views)
- [x] 5. Commit: `Fix GitHub upload: remove nested .git, untrack pycache/db files, add course & student features`
- [x] 6. Push to `origin/main` — **Done** ✅ (`0a999ce..5756d6d`)

