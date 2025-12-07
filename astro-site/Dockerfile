# Multi-stage build for Astro server mode
# Build from root directory to include notes/, projects/, interviews/
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package files from astro-site
COPY astro-site/package*.json ./

# Install dependencies
RUN npm ci

# Copy astro-site source files
COPY astro-site/ ./

# Copy content folders (notes, projects, interviews) to parent directory
# This matches the symlink structure: src/content/notes -> ../../../notes
COPY notes/ ../notes/
COPY projects/ ../projects/
COPY interviews/ ../interviews/

# Build the site for server mode
RUN npm run build

# Production stage - run with Node.js
FROM node:20-alpine AS runtime

WORKDIR /app

# Copy built files from builder
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

# Copy content folders for runtime access (needed for SSR)
COPY --from=builder /notes ../notes
COPY --from=builder /projects ../projects
COPY --from=builder /interviews ../interviews

# Set environment to production
ENV NODE_ENV=production
ENV HOST=0.0.0.0
ENV PORT=4321

# Expose port
EXPOSE 4321

# Start the Astro server
CMD ["node", "./dist/server/entry.mjs"]
