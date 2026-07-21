# 17 API Design & REST

## Why this topic matters
An API (Application Programming Interface) is the "Contract" between the frontend and the backend. If the contract is bad, the developers will fight, the app will be buggy, and the system will be hard to scale. In fresher interviews, you are often asked to "Design the API" for a feature.

## Learning Objectives
- Understand what an API is.
- Learn the principles of REST (Representational State Transfer).
- Know how to design clean, professional API endpoints.

## Intuition
Imagine a **Restaurant Menu**.
- The **Menu** is the **API**. It tells you what you can order and what you will get in return.
- You (the **Client**) don't go into the kitchen and start cooking. You just tell the waiter: *"I want Item #5."*
- The **Waiter** (the API Layer) takes your request to the kitchen (the **Backend**) and brings back the food.
As long as the menu stays the same, the kitchen can change the chef or the oven, and you won't even notice.

## Detailed Explanation

### What is REST?
REST is a set of architectural constraints that make an API "RESTful." It uses standard HTTP methods to perform actions on "Resources" (like Users, Orders, or Products).

### 1. HTTP Methods (The Verbs)
| Method | Action | Example | Success Code |
| :--- | :--- | :--- | :--- |
| **GET** | Retrieve data | `GET /users/123` | 200 OK |
| **POST** | Create data | `POST /users` | 201 Created |
| **PUT** | Update (Replace) | `PUT /users/123` | 200 OK |
| **PATCH** | Update (Partial) | `PATCH /users/123` | 200 OK |
| **DELETE** | Remove data | `DELETE /users/123` | 204 No Content |

### 2. API Design Best Practices
If an interviewer asks you to design an API for a "Blog App," follow these rules:

- **Use Nouns, not Verbs**: 
  - ❌ `/getAllUsers` $\rightarrow$ ✅ `GET /users`
  - ❌ `/createOrder` $\rightarrow$ ✅ `POST /orders`
- **Use Plural Nouns**: `GET /products` instead of `GET /product`.
- **Use Nesting for Relationships**: 
  - To get all comments for a specific post: `GET /posts/45/comments`.
- **Version your API**: Always use `/v1/` or `/v2/`. This prevents breaking the app for users when you make changes.
  - ✅ `/v1/users`

### 3. HTTP Status Codes
You must mention these in an interview to look professional:
- **2xx (Success)**: `200 OK`, `201 Created`.
- **4xx (Client Error)**: `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `429 Too Many Requests`.
- **5xx (Server Error)**: `500 Internal Server Error`, `503 Service Unavailable`.

## Real-world Example
**Spotify API**
- To get a playlist: `GET /v1/playlists/{playlist_id}`
- To add a song to a playlist: `POST /v1/playlists/{playlist_id}/tracks`
- To remove a song: `DELETE /v1/playlists/{playlist_id}/tracks/{track_id}`

## Advantages
- **Decoupling**: The frontend and backend can be developed independently.
- **Standardization**: Any client (Web, iOS, Android) can use the same REST API.
- **Scalability**: REST is stateless, meaning any server can handle any request.

## Disadvantages
- **Over-fetching**: `GET /user` might return 50 fields when you only needed the `username`.
- **Under-fetching**: You might need 3 API calls to get a user, their posts, and their followers.

## Common Interview Questions
- **What is REST and what makes an API "RESTful"?**
- **Difference between PUT and PATCH?**
- **What are the most common HTTP status codes?**
- **How do you version an API and why is it necessary?**

### Interview Answer Tips
- When designing an endpoint, **write it out clearly** on the whiteboard: `METHOD /path/to/resource`.
- Mention **JSON** as the standard data format for request and response bodies.

## Common Mistakes
- Using `GET` to delete or update data. (GET should be "Idempotent"—it should never change data on the server).
- Designing "RPC-style" endpoints (e.g., `/updateUserPassword`). Use `PATCH /users/123` instead.

## Summary
API Design is about creating a clean, predictable contract. REST is the industry standard, using HTTP verbs and nouns to manage resources in a stateless way.

## Practice Questions
1. Design the API endpoints for a "To-Do List" app.
2. If a user tries to access a private profile, which HTTP status code should you return?
3. Why is `POST` used for creating and not `PUT`?
4. What is the difference between a "Stateful" and "Stateless" API?
5. Design an endpoint to "Like" a post. Which method would you use?

## Further Reading
- [[15 Rate Limiting]]
- [[18 Authentication & Authorization]]
- [[19 Microservices vs Monolith]]

#system-design #placements #interview #api #rest
