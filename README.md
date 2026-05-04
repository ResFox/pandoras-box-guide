# Pandora's Box — Documentation Site

A pinkish-purple, MkDocs-Material-powered documentation site, designed to look like a polished GitBook page and host itself for free on **GitHub Pages**.

This README is your end-to-end guide: from cloning, to running it locally, to publishing it live in ~10 minutes.

---

## 0. What's in this folder?

```
Guida page/
├─ mkdocs.yml                 # Site configuration (theme, nav, extensions)
├─ requirements.txt           # Python deps (mkdocs + material + extensions)
├─ .gitignore
├─ .github/
│  └─ workflows/
│     └─ deploy.yml           # Auto-deploy to GitHub Pages on every push
├─ docs/                      # All your content lives here
│  ├─ index.md                # Home page (hero + cards grid)
│  ├─ stylesheets/
│  │  └─ extra.css            # Custom pinkish-purple theme
│  ├─ assets/
│  │  └─ logopandora.gif      # Your logo
│  └─ pages/
│     ├─ valorant.md
│     ├─ universal.md
│     ├─ fortnite.md
│     ├─ rust.md
│     ├─ apex.md
│     ├─ bo7-wz.md            # Fully populated example
│     ├─ arc-raiders.md
│     ├─ marvel-rivals.md
│     ├─ cs2.md
│     ├─ controller-guide.md
│     └─ pc-environment.md
└─ README.md                  # ← you are here
```

---

## 1. One-time setup (Windows / PowerShell)

### 1.1 Install Python (if you don't have it)

Open **PowerShell** and run:

```powershell
python --version
```

If you see something like `Python 3.10+`, you're good. If you get *"Python was not found"*, install it from <https://www.python.org/downloads/> — make sure to **check "Add Python to PATH"** during install.

### 1.2 Install Git (if you don't have it)

```powershell
git --version
```

If missing, get it from <https://git-scm.com/download/win>.

### 1.3 Install the docs dependencies

From inside the `Guida page` folder:

```powershell
cd "C:\Users\Res\Downloads\Guida page"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

This installs `mkdocs`, the **Material** theme, and the markdown extensions used by `mkdocs.yml`.

---

## 2. Run the site locally

```powershell
mkdocs serve
```

Open <http://127.0.0.1:8000> in your browser. Edit any `.md` file in `docs/` and the page **auto-reloads** as you type. This is your authoring loop.

To build the static HTML once (without serving):

```powershell
mkdocs build
```

Output goes to `./site/` (it's gitignored).

---

## 3. Publish it on GitHub Pages

You only do this once. After it's set up, every `git push` to `main` rebuilds and redeploys the site automatically (~30 seconds).

### 3.1 Create a GitHub repo

1. Go to <https://github.com/new>.
2. Name it whatever you want — e.g. `pandoras-box-docs`.
3. **Public** (Pages requires public, *or* a paid GitHub Pro plan for private).
4. Do **not** initialize with a README (we already have one).
5. Click **Create repository**.

GitHub will show you a page with a `git remote add origin ...` URL — copy it.

### 3.2 Update the repo URL in `mkdocs.yml`

Open `mkdocs.yml` and replace the placeholders at the top:

```yaml
site_url: https://YOUR-USERNAME.github.io/REPO-NAME/
repo_name: YOUR-USERNAME/REPO-NAME
repo_url:  https://github.com/YOUR-USERNAME/REPO-NAME
```

For example, if your username is `acme` and your repo is `pandoras-box-docs`:

```yaml
site_url: https://acme.github.io/pandoras-box-docs/
repo_name: acme/pandoras-box-docs
repo_url:  https://github.com/acme/pandoras-box-docs
```

### 3.3 Push the project to GitHub

In PowerShell, from the `Guida page` folder:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial commit: Pandora's Box docs site"
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git
git push -u origin main
```

### 3.4 Enable GitHub Pages

1. Go to your repo on github.com.
2. **Settings → Pages** (left sidebar).
3. Under **Build and deployment → Source**, choose **GitHub Actions**.
4. Save.

### 3.5 Wait ~30 seconds, then open your site

- Go to the **Actions** tab of your repo. You should see the *"Deploy Pandora's Box docs"* workflow running.
- When it turns green, your site is live at:

```
https://YOUR-USERNAME.github.io/REPO-NAME/
```

That's it. From now on, just edit any `.md` file, then:

```powershell
git add .
git commit -m "Update BO7/WZ guide"
git push
```

…and the site updates itself.

---

## 4. How to author content

Everything lives in `docs/`. Each `.md` file is a page. The **left sidebar** is generated from the `nav:` section of `mkdocs.yml` — add a new entry there to add a new page.

### Common patterns used in this site

**Hint boxes (admonitions):**

````markdown
!!! info
    This is an info box.

!!! warning
    This is a yellow warning.

!!! danger
    This is a red danger box.

!!! success
    This is a green success box.
````

**Highlighted text** (the yellow `<mark>` style on the original site):

```markdown
==This text is highlighted==
```

**Buttons:**

```markdown
[Click me](https://example.com){ .md-button }
[Primary button](https://example.com){ .md-button .md-button--primary }
```

**Cards grid** (used on the home page) — wrap a block in `<div class="pb-grid">` and use `<a class="pb-card">` for each card. See `docs/index.md` for an example.

**Code blocks:**

````markdown
```python
print("hello")
```
````

**Tables:**

```markdown
| Column A | Column B |
|----------|----------|
| Row 1    | Value 1  |
| Row 2    | Value 2  |
```

---

## 5. Customizing the look

All theme overrides live in **`docs/stylesheets/extra.css`**. The pinkish-purple palette is defined at the top:

```css
--pb-pink:        #ff4fb1;
--pb-purple:      #9d4edd;
--pb-magenta:     #c026d3;
```

Change those values to retune the entire site. `mkdocs serve` reloads instantly when you save the CSS.

To change the **logo**, replace `docs/assets/logopandora.gif` with any image (PNG / JPG / GIF / SVG) and keep the same filename — or update `theme.logo` in `mkdocs.yml`.

---

## 6. Custom domain (optional)

If you own a domain (e.g. `pandoras-box.io`):

1. Create a file `docs/CNAME` with one line: `pandoras-box.io`.
2. In your DNS provider, add a `CNAME` record pointing your domain (or subdomain) to `YOUR-USERNAME.github.io`.
3. In your GitHub repo: **Settings → Pages → Custom domain** → enter your domain, save, tick **Enforce HTTPS** once it's ready.

---

## 7. Troubleshooting

| Problem | Fix |
|---|---|
| `mkdocs: command not found` | Run `python -m mkdocs serve` instead, or restart PowerShell after installing. |
| `mkdocs build --strict` fails in CI | Run it locally too — the `--strict` flag fails on broken links / unknown nav entries. Fix the warnings shown. |
| Logo doesn't show | Make sure the file is in `docs/assets/` and `theme.logo` in `mkdocs.yml` points to `assets/<filename>`. |
| Site loads but CSS is broken on GitHub Pages | `site_url` in `mkdocs.yml` must match your real URL (`https://USER.github.io/REPO/`). |
| Workflow fails on first run | Open the failed job in the **Actions** tab; usually it's the `site_url` mismatch above, or the repo isn't public (GitHub Pages needs Public on the free plan). |

---

## 8. What you should do right now

1. ✅ Open this README — done.
2. ⬜ Run `python -m pip install -r requirements.txt`.
3. ⬜ Run `mkdocs serve` and visit <http://127.0.0.1:8000>.
4. ⬜ Edit `docs/pages/bo7-wz.md` to fine-tune the BO7 page.
5. ⬜ Update `mkdocs.yml` with your real GitHub repo info (section 3.2).
6. ⬜ Create the GitHub repo and push (section 3.3).
7. ⬜ Enable Pages = "GitHub Actions" (section 3.4).
8. ⬜ Open your live URL.

That's the full path from zero to a live, polished docs site that auto-deploys.
