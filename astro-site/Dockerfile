# Multi-stage build for Astro server mode
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source files
COPY . .

# Copy view_counts.txt from project root (one level up)
COPY ../view_counts.txt /app/view_counts.txt

# Build the site for server mode
RUN npm run build

# Production stage - run with Node.js
FROM node:20-alpine AS runtime

WORKDIR /app

# Copy built files from builder
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

# Copy view_counts.txt
COPY --from=builder /app/view_counts.txt ../view_counts.txt

# Set environment to production
ENV NODE_ENV=production
ENV HOST=0.0.0.0
ENV PORT=4321

# Expose port
EXPOSE 4321

# Start the Astro server
CMD ["node", "./dist/server/entry.mjs"]
