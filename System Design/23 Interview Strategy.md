# 23 Interview Strategy

## Why this topic matters
You can be the best coder in the world, but if you freeze during a System Design interview or start drawing random boxes without explaining why, you will fail. System Design is a **communication test**, not a coding test.

## Learning Objectives
- Learn the "Psychology" of a System Design interview.
- Master the "Think Aloud" technique.
- Understand how to handle "Curveball" questions.

## Intuition
Imagine you are being interviewed to be a **Project Manager**.
The interviewer doesn't want you to just give the "Correct Answer" (because in system design, there is no single correct answer). They want to see:
- Can you handle ambiguity?
- Can you make a decision and justify it?
- Do you understand the trade-offs?
- Can you listen to feedback and pivot?

It's a **collaboration**, not a presentation.

## Detailed Explanation

### 1. The "Think Aloud" Technique
Never be silent for more than 30 seconds. If you are thinking, say: *"I am currently thinking about whether to use a SQL or NoSQL database. SQL gives us better consistency, but NoSQL would scale better for our volume of data..."*
**Why?** If you are silent and your final answer is wrong, the interviewer knows nothing. If you think aloud and your logic is good but your final answer is slightly off, they will often guide you to the right answer.

### 2. The "Trade-off" Mindset
Every choice in System Design has a cost. Whenever you suggest a tool, mention the downside.
- ❌ "I will use a Cache to make it fast."
- ✅ "I will use a Cache to reduce latency. The trade-off is that we'll have to manage cache invalidation to avoid stale data."
**This is what separates a Fresher from a Staff Engineer.**

### 3. Handling "Curveballs"
The interviewer might say: *"What if we suddenly have 100x more users?"* or *"What if the database is read-only?"*
- **Don't panic**. 
- **Don't defend your design blindly**.
- **Acknowledge and Pivot**: *"That's an interesting constraint. In that case, my current single-node DB would become a bottleneck. I would introduce Sharding to distribute the load."*

### The Ideal Interview Flow
| Time | Phase | Your Goal |
| :--- | :--- | :--- |
| **0-5m** | Clarification | Ask questions. Define FRs and NFRs. Set the scope. |
| **5-10m** | Estimation | Do a quick back-of-the-envelope calculation. |
| **10-15m** | API/Data Model | Define the contract (REST) and the DB schema. |
| **15-30m** | High-Level Design | Draw the boxes. Explain the flow of a request. |
| **30-45m** | Deep Dive | Discuss scaling, bottlenecks, and trade-offs. |

## Real-world Example
**Bad Candidate**:
Interviewer: "Design Twitter."
Candidate: (Draws a box for Server, a box for DB). "The user sends a tweet, it goes to the server, then to the DB. Done."
(Result: Fail. No requirements, no scale, no reasoning).

**Good Candidate**:
Interviewer: "Design Twitter."
Candidate: "First, let me clarify the scope. Are we focusing on the posting and timeline part? I'm assuming we need high availability for reads since most people just browse. For 100M users, a single DB won't work, so I'll suggest a NoSQL store for tweets and a Cache for the home timeline..."
(Result: Pass. Shows process, considers scale, suggests tools with reason).

## Advantages of this Strategy
- Reduces anxiety by providing a "Script" to follow.
- Builds a rapport with the interviewer.
- Guarantees you don't miss the basics (Requirements).

## Common Mistakes
- **The "Correct Answer" Trap**: Trying to remember how "Uber actually does it" instead of designing a system that works.
- **Over-engineering**: Adding a Message Queue to a system that only has 100 users.
- **Ignoring the Interviewer**: Not asking for feedback (e.g., *"Does this approach make sense to you, or should I explore another option?"*).

## Summary
The System Design interview is a conversation about trade-offs. By following a structured framework, thinking aloud, and acknowledging the downsides of your choices, you demonstrate the maturity of a senior engineer.

## Practice Questions
1. How do you react when an interviewer tells you your proposed design is "too slow"?
2. What are three questions you should always ask at the start of every HLD interview?
3. If you realize you made a mistake 20 minutes into the design, how do you handle it?
4. How do you balance the time between "Requirements" and "Drawing"?
5. What does "Think Out Loud" actually sound like in a real interview?

## Further Reading
- [[20 HLD Process]]
- [[24 Interview Questions]]

#system-design #placements #interview #strategy #soft-skills
