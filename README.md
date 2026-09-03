# Fiecare Voce

The official source repository for the [Fiecare Voce](https://fiecarevoce.com) web platform.

<p align="center">
  <img src="docs/images/preview.gif" alt="Fiecare Voce Platform Preview" width="800">
</p>

## Overview

Fiecare Voce is an independent student-led media and advocacy platform based in Romania. The platform publishes investigative journalism, student rights guides, educational analyses, opinion pieces, and community projects.

This repository contains the full source code, content architecture, custom layouts, and automated CI/CD pipelines powering the live static website.

## Tech Stack

- Static Site Generator: Hugo Extended
- Base Theme: Blowfish (managed via Git submodule)
- Design System: Custom Neo-Brutalist UI built with Tailwind CSS
- Data & Content: Markdown (with YAML/TOML frontmatter) and YAML data stores
- Media Pipeline: Python (Pillow) automated WebP conversion
- Preview Automation: [Websnap](https://github.com/danielpos178/websnap)
- CI/CD & Auditing: GitHub Actions (Lighthouse CI, Lychee Link Checker, Image Optimizer, Preview Generator)
- Hosting & CDN: Cloudflare Pages / CDN

## Project Structure

```
.
├── archetypes/           # Content scaffolding templates (default frontmatter)
├── assets/               # CSS, JS, and global asset pipeline
├── config/               # Hugo configuration files (_default/config.toml, params.toml, menus.ro.toml)
├── content/              # Editorial content
│   ├── authors/          # Author profiles and biographies
│   ├── categories/       # Taxonomy pages
│   └── posts/            # Published articles organized by date
├── data/                 # Structured YAML data (homepage, founders, team, testimonials)
├── docs/                 # Documentation assets and preview media
├── layouts/              # Custom HTML layout templates and partials
├── static/               # Unprocessed static assets (images, fonts, manifests)
├── themes/blowfish/      # Blowfish theme submodule
└── .github/workflows/    # CI/CD automation pipelines
```

## Getting Started

### Prerequisites

- Hugo Extended v0.120.0 or later
- Git 2.25 or later
- Python 3.10+ (optional, for running local image optimization scripts)

### Installation

1. Clone the repository with submodules:

   ```bash
   git clone --recurse-submodules https://github.com/danielpos178/fiecarevoce.git
   cd fiecarevoce
   ```

   If you cloned without `--recurse-submodules`, initialize the theme submodule manually:

   ```bash
   git submodule update --init --recursive
   ```

2. Start the local development server:

   ```bash
   hugo server -D
   ```

   The local preview will be available at `http://localhost:1313/`.

3. Build for production:

   ```bash
   hugo --minify --gc
   ```

   The generated static site will be output to the `public/` directory.

## Content Management

### Creating a New Article

Articles are located under `content/posts/` and can be organized by publication year and month.

Create a new draft using Hugo archetypes:

```bash
hugo new posts/2026/08/article-title.md
```

### Frontmatter Specification

Every article requires the following metadata in its header:

```yaml
---
title: "Article Title"
slug: "article-title"
date: 2026-08-26
draft: false
summary: "Short 1-2 sentence overview for home cards and search summaries."
description: "SEO description (140-160 characters) for search engines."
author: "Redactia Fiecare Voce"
authors: ["Author Name"]
categories: ["Educatie"]
tags: ["drepturile elevilor", "bacalaureat"]
image: "/images/posts/article-cover.webp"
photo_credit: "Arhiva Fiecare Voce"
featured: false
---
```

### Author Profiles

Author information is managed in `content/authors/<author-slug>/_index.md`. Include biographical notes, social links, and profile photos to associate authors with their publications.

## Automated Workflows

The repository uses GitHub Actions for continuous integration, quality assurance, and asset management:

- **Lighthouse Audit (`.github/workflows/lighthouse.yml`)**: Executes on pull requests to ensure performance, accessibility, best practices, and SEO scores meet project thresholds.
- **Link Checker (`.github/workflows/link-checker.yml`)**: Scans built HTML output weekly and on PRs via Lychee to detect broken external or internal links.
- **Image Optimization (`.github/workflows/optimize-images.yml`)**: Automatically converts and resizes images committed under `static/images/posts/` into optimized WebP formats using Pillow.
- **Website Preview (`.github/workflows/preview.yml`)**: Uses [Websnap](https://github.com/danielpos178/websnap) to periodically capture full-page scrolling GIF animations of the live website for documentation.

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). See the [LICENSE](LICENSE) file for details.
