---
tags:
  - System-Design
  - FAANG
  - Quick-Reference
  - Cheatsheet
  - Interview-Preparation
aliases:
  - System Design Cheatsheet
  - Quick Reference Card
---

# 📋 System Design — Quick Reference Card

> **Print this!** One-page cheatsheet for FAANG System Design interviews. Covers key patterns, formulas, trade-offs, and decision matrices.

---

## 🎯 The HLD Process (Follow in Order)

```
1. REQUIREMENTS          → Clarify functional + non-functional
         │
         ▼
2. ESTIMATION            → QPS, Storage, Bandwidth, Memory
         │
         ▼
3. API DESIGN            → REST/gRPC, contracts, versioning
         │
         ▼
4. HIGH-LEVEL DESIGN     → Boxes & arrows, data flow
         │
         ▼
5. DATA MODEL            → SQL/NoSQL, schema, partitioning
         │
         ▼
6. DETAILED DESIGN       → Deep dive into 2-3 critical components
         │
         ▼
7. BOTTLENECKS & SCALE   → Identify & mitigate
         │
         ▼
8. FAILURE & RECOVERY    → Graceful degradation, retries, DLQ
```

---

## 📐 Back-of-Envelope Estimation

### Traffic
| Metric | Formula | Example |
|--------|---------|---------|
| **QPS** | DAU × actions_per_day / 86400 | 100M DAU × 50 / 86400 ≈ 58K QPS |
| **Peak QPS** | QPS × peak_multiplier (2-10x) | 58K × 5 = 290K QPS |
| **Read/Write Ratio** | Typically 100:1 to 1000:1 | — |

### Storage
| Metric | Formula |
|--------|---------|
| **Data Size** | QPS × avg_object_size × retention_days × 86400 |
| **Index Size** | ~10-20% of data size |
| **Replication** | × 3 (typical) |

### Bandwidth
| Type | Formula |
|------|---------|
| **Ingress** | Write_QPS × avg_write_size |
| **Egress** | Read_QPS × avg_read_size × replication |

### Memory
| Component | Estimation |
|-----------|------------|
| **Cache** | Working_set_size × 1.5 |
| **Redis** | Keys × (key_size + value_size + overhead) |
| **Bloom Filter** | n × ln(1/ε) / ln(2)² bits |

---

## 🗄️ Database Selection Decision Matrix

| Requirement | Choose | Avoid |
|-------------|--------|-------|
| **ACID transactions** | PostgreSQL, MySQL, Spanner | Cassandra, DynamoDB |
| **Horizontal scaling** | Cassandra, DynamoDB, MongoDB | Single-node PostgreSQL |
| **Complex queries/joins** | PostgreSQL, MySQL | Cassandra, DynamoDB |
| **Time-series** | TimescaleDB, InfluxDB | MongoDB |
| **Graph/relationships** | Neo4j, JanusGraph | Relational DB |
| **Full-text search** | Elasticsearch, OpenSearch | PostgreSQL (basic) |
| **Vector search** | Pinecone, Milvus, Qdrant | — |
| **Key-value, low latency** | Redis, Memcached, DynamoDB | — |
| **Global distribution** | Spanner, Cosmos DB, DynamoDB Global Tables | — |

---

## 🔄 Cache Patterns Decision

| Pattern | Consistency | Write Latency | Complexity | Use When |
|---------|-------------|---------------|------------|----------|
| **Cache-Aside** | Eventual | Low | Low | General purpose |
| **Write-Through** | Strong | High | Medium | Write-heavy, strong consistency |
| **Write-Behind** | Eventual | Low | High | Write-heavy, can tolerate loss |
| **Refresh-Ahead** | Eventual | Background | Medium | Predictable access patterns |
| **Multi-Level (L1+L2)** | Eventual | Low | High | Ultra-low latency needed |

### Cache Invalidation

| Strategy | Consistency | Complexity | Best For |
|----------|-------------|------------|----------|
| **TTL** | Eventual | Low | Non-critical |
| **Explicit Delete** | Strong | Medium | Critical data |
| **Pub/Sub** | Strong | High | Multi-instance |
| **Version/Tag** | Strong | Medium | Complex deps |
| **Cache Version in Key** | Strong | Low | Simple |

---

## ⚖️ CAP / PACELC Decision

```
PACELC: If Partition (P) → Availability (A) or Consistency (C)
        Else (E) → Latency (L) or Consistency (C)
```

| System | Classification | Use Case |
|--------|----------------|----------|
| **CP** | MongoDB, HBase, Redis, etcd | Banking, inventory |
| **AP** | Cassandra, DynamoDB, CouchDB | Social feeds, catalogs |
| **CA** | Single-node MySQL/PostgreSQL | Non-distributed only |
| **PACELC** | Cosmos DB, FaunaDB | Global apps |

---

## 🔑 Consistent Hashing

```
Ring: 0 to 2^32-1 (or 2^160-1)
Virtual Nodes: 100-200 per physical node

Adding node: Only affects next node's keys (~1/N)
Removing node: Only affects removed node's keys
Hot keys: Add virtual nodes, or split key
```

---

## 📊 Load Balancer Algorithms

| Algorithm | Best For | Stateful? |
|-----------|----------|-----------|
| **Round Robin** | Homogeneous backends | No |
| **Weighted RR** | Heterogeneous capacity | No |
| **Least Connections** | Variable request duration | Yes |
| **Least Requests** | HTTP/grpc, similar duration | Yes |
| **Consistent Hash** | Session affinity, caching | Yes |
| **Maglev (Google)** | L4, high throughput | No |
| **Least Response Time** | Latency-sensitive | Yes |

---

## 🔐 Rate Limiting Algorithms

| Algorithm | Burst Handling | Memory | Precision |
|-----------|----------------|--------|-----------|
| **Token Bucket** | Smooth bursts | Low | Medium |
| **Leaky Bucket** | Fixed rate | Low | Medium |
| **Fixed Window** | Poor at boundaries | Low | Low |
| **Sliding Window Log** | Good | High | High |
| **Sliding Window Counter** | Good | Low | High |

---

## 🗃️ Sharding Strategies

| Strategy | Distribution | Range Queries | Resharding |
|----------|--------------|---------------|------------|
| **Hash** | Uniform | Poor | Hard (consistent hashing helps) |
| **Range** | Skewed possible | Excellent | Easy (split ranges) |
| **Geo** | By location | Good for local | Medium |
| **Directory** | Any | Any | Flexible |
| **Consistent Hash** | Uniform | Poor | Minimal |

---

## 📦 Message Queue Comparison

| Feature | Kafka | RabbitMQ | Pulsar | Redis Streams |
|---------|-------|----------|--------|---------------|
| **Throughput** | 10M+/sec | 100K/sec | 1M+/sec | 500K/sec |
| **Latency** | 2-5ms | <1ms | 2-5ms | <1ms |
| **Ordering** | Per-partition | Per-queue | Per-partition | Per-stream |
| **Replay** | Yes (retention) | Limited | Yes | Yes |
| **Exactly-once** | Yes (transactions) | No | Yes | No |
| **Multi-tenant** | Good | Limited | Excellent | Limited |
| **Protocol** | Custom | AMQP | Custom | RESP |

---

## 🔄 Distributed Consensus

| Algorithm | Leader | Throughput | Complexity | Use Case |
|-----------|--------|------------|------------|----------|
| **Raft** | Strong leader | High | Medium | etcd, Consul, TiKV |
| **Paxos** | Flexible | Medium | High | Chubby, Spanner |
| **Multi-Paxos** | Stable leader | High | High | Log replication |
| **ZAB (ZooKeeper)** | Leader | High | Medium | ZooKeeper |

---

## 🎯 Common Latency Numbers (Memorize)

| Operation | Time |
|-----------|------|
| L1 cache reference | 0.5 ns |
| L2 cache reference | 7 ns |
| Main memory reference | 100 ns |
| Compress 1KB with Zippy | 3 µs |
| Send 1KB over 1 Gbps network | 10 µs |
| Read 1MB sequentially from memory | 250 µs |
| Round trip within datacenter | 500 µs |
| Disk seek | 10 ms |
| Read 1MB sequentially from SSD | 1 ms |
| Read 1MB sequentially from HDD | 20 ms |
| Send packet CA → NY → CA | 70 ms |

---

## 🎯 System Design Interview Checklist

### Before Interview
- [ ] Review all 15 pattern categories
- [ ] Practice 3-5 full designs end-to-end
- [ ] Memorize estimation numbers
- [ ] Prepare 2-3 "deep dive" stories

### During Interview
- [ ] **Clarify requirements** (5-10 min)
- [ ] **Estimate scale** (back-of-envelope)
- [ ] **Draw architecture** (boxes + arrows + data flow)
- [ ] **Define APIs** (REST/gRPC, contracts)
- [ ] **Choose databases** (justify each)
- [ ] **Design data model** (schema, partitioning)
- [ ] **Deep dive** 2-3 components
- [ ] **Identify bottlenecks** + solutions
- [ ] **Discuss failures** + recovery
- [ ] **Mention monitoring** + alerting

### Red Flags to Avoid
- ❌ Jumping to solution without requirements
- ❌ Over-engineering (Kafka for 100 QPS)
- ❌ Ignoring trade-offs
- ❌ Not discussing failure modes
- ❌ Ignoring cost
- ❌ No monitoring/observability
- ❌ Single point of failure
- ❌ No capacity planning

---

## 🔗 Key System Design Patterns (One-Liners)

| Pattern | One-Liner |
|---------|-----------|
| **Cache-Aside** | Check cache → miss → fetch DB → populate cache |
| **Write-Through** | Write DB + cache together (strong consistency) |
| **Write-Behind** | Write cache → async flush to DB (high write throughput) |
| **CQRS** | Separate read/write models (optimize each) |
| **Event Sourcing** | Store events, not state (audit, replay) |
| **Saga** | Distributed transaction via choreography/orchestration |
| **Circuit Breaker** | Fail fast, prevent cascade failures |
| **Bulkhead** | Isolate resources, prevent cascade |
| **Retry + Backoff** | Exponential backoff + jitter |
| **Dead Letter Queue** | Capture failed messages for later |
| **Idempotency Keys** | Safe retries without duplication |
| **Leader Election** | Single active leader (etcd/ZooKeeper) |
| **Distributed Lock** | Redlock / etcd lease |
| **Rate Limiter** | Token bucket / sliding window in Redis |
| **Consistent Hashing** | Minimize reshuffle on scaling |
| **Sharding** | Hash / range / geo partitioning |
| **Read Replicas** | Scale reads, async replication |
| **Multi-Region** | Active-active or active-passive |
| **CDN** | Edge caching, geographic distribution |
| **Service Mesh** | mTLS, traffic mgmt, observability (Istio) |

---

## 🚀 Final Tips

> **"The best system design isn't the most complex—it's the one that solves the problem with the right trade-offs."**

- **Start simple**, scale incrementally
- **Explicit trade-offs** > implicit assumptions
- **Numbers speak louder** than adjectives
- **Draw as you talk** — diagram is your thinking tool
- **Admit uncertainty** — "I'd need to benchmark..." is a great answer

---

## 🏷️ Tags

```yaml
tags:
  - System-Design
  - FAANG
  - Quick-Reference
  - Cheatsheet
  - Interview-Preparation
```