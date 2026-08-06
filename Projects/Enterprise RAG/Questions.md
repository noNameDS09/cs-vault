Based on your updated resume, here are likely mock interview questions:

**Resume walkthrough / general**
1. Walk me through your resume — what's the story connecting your projects?
2. Why AI/ML and Data Science as a specialization?
3. What are you looking for in this role, and why this company?

**Enterprise RAG Platform (will get the most scrutiny)**
4. Walk me through the architecture of your RAG pipeline end to end.
5. Why did you choose Qdrant over other vector databases like Pinecone or Weaviate?
6. Explain how your Hybrid Search (Dense + BM25) works — why combine both instead of just using dense embeddings?
7. How does Reciprocal Rank Fusion work mathematically?
8. What reranking model did you use, and why does reranking improve results after RRF already fuses ranked lists?
9. How did you chunk documents — what chunk size/overlap, and why?
10. How do you evaluate retrieval quality? What metrics did you use?
11. What was your generation quality evaluation approach — did you measure hallucination/faithfulness?
12. How do you handle a query where no relevant document exists in the corpus?
13. What's your system's latency at query time, and where are the bottlenecks?
14. How would this scale from your current dataset to 1M+ documents?
15. Why Ollama instead of a hosted LLM API? What are the tradeoffs?
16. Explain your query rewriting step — how does it help multi-turn conversations?
17. How did you implement SSE streaming, and why is that needed here?
18. What testing did you do (you mention Pytest, Ruff, MyPy) — walk me through your testing strategy.
19. What would you improve if you had another month on this project?
20. Have you implemented authentication/multi-tenancy? How would you add it?

**xLogia Tech internship (YOLOv8 wildlife detection)**
21. Walk me through your object detection pipeline.
22. Why YOLOv8 over other detection architectures?
23. How did you achieve 80% mAP50 — what did you tune to get there?
24. Explain how ByteTrack works and why it reduced duplicate counts by 70%.
25. How did you validate your model wasn't overfitting on the 10K image dataset?
26. What data preprocessing/augmentation techniques did you use?
27. How would you deploy this model to run in real-time in the field?

**FarmVichar**
28. How did you build the commodity price forecasting model — what algorithm, and why?
29. Why did you choose a mix of Firebase and SQL rather than one database?
30. How does the multilingual chat interface work?

**Cureify**
31. How does the AI diagnostic assistant handle sensitive medical data responsibly?
32. Walk me through the iterative follow-up questioning logic.
33. What are the risks of using Gemini API for medical image diagnosis, and how did you mitigate them?

**System design / conceptual (given RAG focus)**
34. How would you detect and reduce hallucinations in a RAG system?
35. What's the difference between semantic search and traditional keyword search?
36. How would you design this system to handle real-time document updates?
37. How do you decide what to retrieve vs. what to let the LLM answer from its own knowledge?

**Behavioral**
38. Tell me about a technical challenge you faced and how you resolved it.
39. Describe a time you had to learn a new technology quickly for a project.
40. How do you prioritize when working on multiple projects simultaneously?

Want me to also prep strong sample answers for any of these, especially the RAG deep-dive ones?