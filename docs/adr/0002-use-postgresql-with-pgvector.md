# 0002. Use PostgreSQL with pgvector

- **Status:** Accepted
- **Date:** 2026-10-23

## Context

Hiboo needs to store the embeddings of the user's profile (CV and past projects)
and find the ones closest to each requirement of a job offer. These vectors must
be stored persistently, next to relational data such as applications and offers.
The expected volume is small: a few thousand text chunks at most.

## Options considered

- **In-memory search with NumPy**  simplest option, no extra service, but
  embeddings must be recomputed or reloaded at each start, and nothing links them
  to the relational data.
- **PostgreSQL with pgvector**  a single database for relational and vector data;
  both can be combined in one SQL query. Less optimized than a dedicated engine
  for very large volumes.
- **Qdrant**  a dedicated vector database, fast and feature-rich at scale, but a
  second service to run and keep in sync with the relational data.

## Decision

Use **PostgreSQL with the pgvector extension** as the single database for
relational data and embeddings. Similarity scoring is done separately in NumPy,
so the database is only responsible for storage and retrieval.

## Consequences

- One service to run, back up and migrate.
- Vector search and relational filters in the same SQL query.
- Strengthens SQL skills, which are useful across any data or AI role.
- Not designed for very large vector volumes; irrelevant at Hiboo's scale.
- If needs grow, migrating to a dedicated engine such as Qdrant remains possible
  and will be documented in a new ADR.