import { defineCollection, z } from 'astro:content';

const notes = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    date: z.coerce.date().optional(),
    tags: z.array(z.string()).optional(),
    draft: z.boolean().default(false),
  }),
});

const projects = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    date: z.coerce.date().optional(),
    tags: z.array(z.string()).optional(),
    company: z.string().optional(),
    role: z.string().optional(),
    technologies: z.array(z.string()).optional(),
    draft: z.boolean().default(false),
  }),
});

const interviews = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    date: z.coerce.date().optional(),
    tags: z.array(z.string()).optional(),
    category: z.string().optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = {
  notes,
  projects,
  interviews,
};
