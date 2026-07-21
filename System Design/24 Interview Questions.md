# 24 Common Interview Questions

## Why this topic matters
The best way to prepare for a System Design interview is to solve actual problems. While the concepts (Caching, LB, Sharding) are the building blocks, the "Case Studies" are where you learn how to put them together.

## Learning Objectives
- Master the "Short Answer" theoretical questions.
- Learn how to approach "Scenario-based" design questions.
- Build a mental library of common architecture patterns.

## Intuition
Think of this as a **Cheat Sheet**. You've learned how the engine works (the previous 23 notes), now you're learning how to drive the car in different weather conditions.

## Detailed Explanation

### Part 1: High-Frequency Theory Questions
These are often used as "Warm-up" questions in interviews for service-based companies (TCS, Infosys, etc.).

| Question | Key Points for Answer | Related Topic |
| :--- | :--- | :--- |
| **What is a Load Balancer?** | Traffic cop, prevents overloading, Horizontal Scaling. | [[07 Load Balancer]] |
| **SQL vs NoSQL?** | Structured/ACID vs Flexible/Scalable. | [[10 Database Basics]] |
| **What is Caching?** | Store in RAM, reduce latency, Cache Hit/Miss. | [[09 Caching]] |
| **What is CAP Theorem?** | Consistency, Availability, Partition Tolerance. Pick 2. | [[06 CAP Theorem]] |
| **What is a CDN?** | Geographically distributed servers for static assets. | [[16 CDN]] |
| **Explain Microservices.** | Small independent services, decoupled, scalable. | [[19 Microservices vs Monolith]] |
| **What is an API?** | Contract between client/server, REST principles. | [[17 API Design & REST]] |
| **What is Sharding?** | Splitting one big DB into smaller chunks. | [[12 Replication & Sharding]] |

### Part 2: Common Design Scenarios (Case Studies)
For mid-sized product companies (Oracle, Cisco, SAP), you will be asked to design a system. Use the [[20 HLD Process]].

#### 1. Design a URL Shortener (TinyURL)
- **Key Challenge**: Generating a unique short ID.
- **Tech Stack**: NoSQL (Key-Value) for fast lookups, Redis for caching popular links.
- **Core Logic**: Base62 encoding of a unique ID.

#### 2. Design a Pastebin (Text Storage)
- **Key Challenge**: Handling large amounts of text and expiration dates.
- **Tech Stack**: Object Store (S3) for text files, SQL for metadata.
- **Core Logic**: Hashing the content to avoid duplicates.

#### 3. Design a Chat System (WhatsApp/Messenger)
- **Key Challenge**: Real-time delivery and "Online" status.
- **Tech Stack**: WebSockets (for bi-directional communication), NoSQL (Cassandra) for message history.
- **Core Logic**: Message Queue for asynchronous delivery.

#### 4. Design a News Feed (Facebook/Twitter)
- **Key Challenge**: "Fan-out" for celebrities with millions of followers.
- **Tech Stack**: Redis for pre-computed feeds, NoSQL for tweets.
- **Core Logic**: Pre-computing the feed when a user posts.

#### 5. Design a Parking Lot (The Classic LLD/HLD Mix)
- **Key Challenge**: Managing slots and vehicle types.
- **Tech Stack**: Simple SQL DB.
- **Core Logic**: Classes for Vehicle, Slot, and Ticket.

## Real-world Example
In a real interview, if you are asked to design a **Payment System**, the interviewer is testing your knowledge of **Consistency**. You should focus on:
1. **ACID Transactions** (SQL).
2. **Idempotency** (Ensuring a user isn't charged twice if they click "Pay" twice).
3. **Retries with Exponential Backoff** (Using [[14 Message Queues]]).

## Advantages of Case Studies
- Builds confidence.
- Teaches you to spot patterns (e.g., "Whenever there is a feed, I need a Cache").
- Improves your diagramming speed.

## Disadvantages
- **Rote Memorization**: If you just memorize the answer and the interviewer changes one requirement, you will fail. Always apply the *first principles*.

## Common Interview Questions (Scenario-Based)
- *"How would you handle a sudden spike in traffic on Black Friday?"* $\rightarrow$ Talk about [[07 Load Balancer]], [[03 Scalability]], and [[15 Rate Limiting]].
- *"What happens if your cache is too small for the data?"* $\rightarrow$ Talk about [[09 Caching]] eviction policies (LRU).
- *"Your DB is slow for reads but fast for writes. What do you do?"* $\rightarrow$ Talk about [[12 Replication & Sharding]] (Read Replicas).

### Interview Answer Tips
- **Ask "Why" before "What"**. Don't just say "I'll use MongoDB." Say "Because our data is unstructured and we need to scale horizontally, I'll use MongoDB."
- **Draw and Talk**. Never draw a box without explaining what it does.

## Common Mistakes
- **Over-designing**: Adding Kafka to a parking lot design.
- **Ignoring the Bottleneck**: Designing a perfect API but forgetting that the database will crash under the load.

## Summary
The final step of preparation is applying concepts to scenarios. Master the theory, follow the HLD process, and use the right tool for the right problem.

## Practice Questions
1. Design a system to count the number of views on a YouTube video in real-time.
2. How would you design a "Top 10 Trending" list for a news site?
3. Design a simplified version of Dropbox.
4. What are the trade-offs between a SQL and NoSQL database for a Social Media app?
5. How would you ensure that a "Like" on a post is reflected for all users eventually?

## Further Reading
- [[20 HLD Process]]
- [[23 Interview Strategy]]
- All previous topics 01-22.

#system-design #placements #interview #case-studies #preparation
