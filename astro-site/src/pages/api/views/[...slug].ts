import type { APIRoute } from 'astro';
import { getViewCount, updateViewCount } from '../../../utils/viewCount';

// Disable prerendering for this API route
export const prerender = false;

// GET: Retrieve view count for a specific page
export const GET: APIRoute = async ({ params }) => {
  const slug = params.slug || '';

  const count = getViewCount(slug);

  return new Response(JSON.stringify({ page: slug, views: count }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};

// POST: Increment view count for a specific page
export const POST: APIRoute = async ({ params }) => {
  const slug = params.slug || '';

  updateViewCount(slug);
  const count = getViewCount(slug);

  return new Response(JSON.stringify({ page: slug, views: count }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};
