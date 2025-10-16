# Harry Dang Portfolio - Astro Version

This is the Astro-powered version of my personal portfolio and knowledge base website, migrated from FastAPI + Jinja2.

## Tech Stack

- **Framework**: [Astro](https://astro.build/) 5.14+
- **Content**: MDX with Content Collections
- **Styling**: Bootstrap 5 + Custom CSS
- **Deployment**: Docker + Nginx
- **CI/CD**: GitHub Actions

## Project Structure

```
astro-site/
├── src/
│   ├── components/       # Reusable Astro components
│   │   └── Header.astro
│   ├── content/          # Content collections (symlinked)
│   │   ├── config.ts     # Content schema definitions
│   │   ├── notes/        → ../../../notes
│   │   ├── projects/     → ../../../projects
│   │   └── interviews/   → ../../../interviews
│   ├── layouts/          # Page layouts
│   │   ├── BaseLayout.astro
│   │   └── PageLayout.astro
│   └── pages/            # File-based routing
│       ├── index.astro   # Homepage
│       ├── notes/
│       │   ├── index.astro
│       │   └── [...slug].astro
│       └── projects/
│           ├── index.astro
│           └── [...slug].astro
├── public/               # Static assets
│   ├── note.css
│   ├── project.css
│   ├── task.css
│   └── page_detail.css
├── astro.config.mjs      # Astro configuration
├── Dockerfile            # Multi-stage Docker build
├── nginx.conf            # Nginx configuration
└── package.json
```

## Features

### Implemented

- Static site generation with Astro
- Content collections for notes, projects, and interviews
- File-based routing for pages
- Markdown with frontmatter support
- Search functionality for notes
- Tag filtering
- Responsive Bootstrap UI
- Docker deployment with Nginx
- GitHub Actions CI/CD pipeline

### Migration Notes

The following features were successfully migrated from the FastAPI version:

1. **Content Structure**: All markdown files now use YAML frontmatter instead of HTML comments
2. **Routing**: Dynamic routes using Astro's `[...slug].astro` pattern
3. **Layouts**: Jinja2 templates converted to Astro components
4. **Styling**: CSS files copied to public directory
5. **Search**: Implemented client-side search for notes

### Not Yet Implemented

The following features from the original FastAPI version are not included:

- **Task Management**: The Slack bot integration and SCHEDULE.md task system (this was backend-specific)
- **View Count Tracking**: Currently removed (can be re-implemented with an API or analytics)
- **Dynamic Features**: Any server-side processing that required Python/FastAPI

## Development

### Prerequisites

- Node.js 20+
- npm or pnpm

### Local Development

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

### Content Management

#### Adding a New Note

1. Create a markdown file in the `notes/` directory (in the parent repo)
2. Add frontmatter at the top:

```markdown
---
title: "Your Note Title"
description: "Optional description"
date: 2025-01-16
tags: ["backend", "database"]
---

Your content here...
```

#### Adding a New Project

1. Create a markdown file in the `projects/` directory (in the parent repo)
2. Add frontmatter:

```markdown
---
title: "Project Name"
description: "Project description"
date: 2025-01-16
role: "Backend Developer"
company: "Company Name"
technologies: ["Python", "FastAPI", "PostgreSQL"]
---

Project details...
```

## Deployment

### Docker Build

```bash
# Build image
docker build -t portfolio-astro .

# Run container
docker run -p 80:80 portfolio-astro
```

### CI/CD

The GitHub Actions workflow (`.github/workflows/astro.yaml`) automatically:

1. Builds the Docker image on push to master
2. Pushes to ECR (AWS Elastic Container Registry)
3. Deploys to production server via SSH
4. Restarts the service with the new image

## Migration from FastAPI

This project was migrated from a FastAPI + Jinja2 application. Key changes:

### Before (FastAPI)
- Server-side rendering with Jinja2
- Python-based routing and services
- Metadata in HTML comments
- Dynamic view count tracking
- Integrated Slack bot for tasks

### After (Astro)
- Static site generation
- File-based routing
- YAML frontmatter for metadata
- Faster performance (no server required)
- Simplified deployment

### Migration Script

The `migrate_frontmatter.py` script in the parent directory was used to convert all markdown files from HTML comment metadata to YAML frontmatter.

## Performance Benefits

Migrating to Astro provides:

- **Faster Load Times**: Static HTML, no server processing
- **Better SEO**: Pre-rendered pages
- **Lower Costs**: Can be hosted on static hosting (Netlify, Vercel, S3, etc.)
- **Improved DX**: Hot module reloading, TypeScript support
- **Modern Tooling**: Built-in optimization, image processing

## Future Enhancements

Potential improvements:

1. Add pagination for notes (currently shows all)
2. Implement client-side search with Pagefind or Fuse.js
3. Add syntax highlighting for code blocks
4. Create a custom 404 page
5. Add RSS feed generation
6. Implement view tracking with a lightweight analytics solution
7. Consider adding the Slack bot as a separate microservice

## License

Personal project - see parent repository for details.

## Author

Harry Dang
- GitHub: [@harrylowkey](https://github.com/harrylowkey)
- Email: harrydang.tech@gmail.com
- Website: https://harrylowkey.dev
