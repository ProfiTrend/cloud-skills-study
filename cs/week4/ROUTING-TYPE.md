# Routing Type

> 라우팅의 종류와 특징(rip, ospf, bgp, static 등)

## RIP

### About RIP

RIP(Routing Information Protocol) is a protocol of **Dynamic Routing Protocol**.

It is a **Distance Vector** routing protocol. It sends packets on the basis of distance(Hop) and direction.

It is an IGP protocol. It allows up to 15 hops.

### Strengths

It is efficient on small size network. It uses a little of resources like memory.

It is a standard routing protocol. All router support it.

### Weakness

It can be inefficient packets' path, because it is not considered speed and distance delay.

If you don't synchronize all routers, packets' path can be inappropriate.

## OSPF

### About OSPF

OSPF(Open Shortest Path First) is a protocol of **Dynamic Routing Protocol**.

It sends packets using **Dijkstra Algorithm**.

### Strengths

- Fast Reconvergence
- Partial Update

### Weakness

It is more complex than other routing protocol settings.

It uses a lot of resources like memory, CPU.

## BGP

### About BGP

BGP(Border Gateway Protocol) is an EGP protocol. It exchanges routing information among other routers.

It is made for huge network connection.

### Strengths

It ensures routing that does not fall into an infinity loop.

It supports CIDR.

### Weakness

It should pass many hops to connect species AS.

## STATIC

### About Static

Administrator set routing path.

### Strengths

- Reliability
- Security
- A few of resources

### Weakness

It is difficult to change settings. It is not good at scalability.
