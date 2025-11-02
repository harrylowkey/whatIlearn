import fs from 'fs';
import path from 'path';

const VIEW_COUNT_FILE = path.join(process.cwd(), '..', 'view_counts.txt');

/**
 * Read view counts from file
 * Returns an object with page paths as keys and counts as values
 */
export function readViewCounts(): Record<string, number> {
  try {
    const data = fs.readFileSync(VIEW_COUNT_FILE, 'utf-8');
    const viewCounts: Record<string, number> = {};

    const lines = data.trim().split('\n');
    for (const line of lines) {
      if (line.trim()) {
        const [page, count] = line.split(':');
        viewCounts[page] = parseInt(count, 10);
      }
    }

    return viewCounts;
  } catch (error) {
    // File doesn't exist or can't be read, return empty object
    return {};
  }
}

/**
 * Write view counts to file
 */
export function writeViewCounts(viewCounts: Record<string, number>): void {
  const lines = Object.entries(viewCounts)
    .map(([page, count]) => `${page}:${count}`)
    .join('\n');

  fs.writeFileSync(VIEW_COUNT_FILE, lines + '\n', 'utf-8');
}

/**
 * Update (increment) view count for a page
 */
export function updateViewCount(page: string): void {
  const viewCounts = readViewCounts();
  viewCounts[page] = (viewCounts[page] || 0) + 1;
  writeViewCounts(viewCounts);
}

/**
 * Get view count for a specific page
 */
export function getViewCount(page: string): number {
  const viewCounts = readViewCounts();
  return viewCounts[page] || 0;
}
