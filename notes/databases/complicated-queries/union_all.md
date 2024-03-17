# UNION ALL

## Case Study

- I have four relational tables: User, Post, Hotspot, Hotspot_media, and Media.

```mermeid
erDiagram
    User ||--o{ Post: contains
    User {
        uuid id
    }
    Post ||--o{ Hotspot: contains
    Post ||--o| Media: has
    Post {
        uuid id
        uuid image_id
        uuid author_id
    }
    Hotspot ||--o{ HotspotMedia: contains
    Hotspot {
        uuid id
    }
    HotspotMedia ||--o| Media: has
    HotspotMedia {
        uuid id
        uuid hotspot_id
        uuid media_id
    }
    Media {
        uuid id
        int file_size
    }
```

The requirements are as follows:

- Calculate the file_size of media linked to hotspot media based on media type per post per user.
- Calculate the file_size of media linked to post based on media type per post per user.
- Aggregate the results into one response.

### First Approach

- The SQL query involves selecting data from the User table and left joining it with the Post table.
- Subsequently, left joins are applied to the Hotspot, HotspotMedia, and Media tables. Additionally, there is a left join between the Post and Media tables.
- The query looks like this:

```sql
SELECT * FROM "user"
LEFT JOIN post ON "user".id = post.author_id
LEFT JOIN hotspot ON post.id = hotspot.post_id
LEFT JOIN hotspot_media ON hotspot.id = hotspot_media.hotspot_id
LEFT JOIN media ON hotspot_media.media_id = media.id OR post.media_id = media.id
```

In this approach, an issue arises where media linked to a post gets duplicated.
For example, if there is one post with one hotspot and two hotspot media items (A, B), each linked to media items (C, D), and one media item (E) linked directly to the post, the result will include duplicate entries for each hotspot media. Specifically, (A <- C, B <- D) will appear twice. Additionally, media item (E) will be associated with each hotspot media, resulting in entries like (post <- A <- E) and (post <- B <- E).

The desired outcome is to display media items (C, D, and E) only once in the result set.

### Second Approach (using UNION ALL)

In this approach, we leverage the UNION ALL operator to achieve the desired result. The strategy involves two distinct queries:

The first query retrieves media linked directly to posts.
The second query fetches all media linked to their respective hotspot media entries.
Subsequently, we use the UNION ALL operator to combine the results. This allows us to calculate the total media file size based on the aggregated information.

The final SQL query is structured as follows:

```sql
WITH combined_media AS (SELECT u.id         as user_id,
                               p.image_id   as p_media_id,
                               m.id         as media_id,
                               m.type       as media_type,
                               p.id         as post_id,
                               p.media_type as post_media_type,
                               m.file_size,
                               m.status,
                               NULL         as hm_media_id
                        FROM "user" u
                                 LEFT OUTER JOIN post p ON u.id = p.author_id
                                 LEFT OUTER JOIN media m ON m.id = p.image_id

                        UNION ALL

                        SELECT u.id         as user_id,
                               p.image_id   as p_media_id,
                               m.id         as media_id,
                               m.type       as media_type,
                               p.id         as post_id,
                               p.media_type as post_media_type,
                               m.file_size,
                               m.status,
                               hm.media_id  as hm_media_id
                        FROM "user" u
                                 LEFT OUTER JOIN post p ON u.id = p.author_id
                                 LEFT OUTER JOIN hotspot h ON h.post_id = p.id
                                 LEFT OUTER JOIN hotspot_media hm ON hm.hotspot_id = h.id
                                 LEFT OUTER JOIN media m ON m.id = hm.media_id
						)
select user_id,
       post_id,
       sum(CASE
               WHEN (
                   post_media_type = 1::INTEGER AND media_id = hm_media_id AND media_type = 1 OR
                   post_media_type = 1::INTEGER AND media_id = p_media_id AND media_type = 1::INTEGER)
                   THEN file_size
               ELSE 0::INTEGER END) AS image_size,
       SUM(CASE
               WHEN (p_media_id = media_id) THEN file_size
               ELSE 0::INTEGER
           END)                     AS primary_file_size
from combined_media
GROUP BY user_id, post_id
ORDER BY post_id IS NOT NULL DESC, user_id;
```
