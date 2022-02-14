# TCP 3 Step

> TCP의 연결 생성 단계는 왜 3단계로 구성되어 있는가?

## What is TCP Connection establishment 3 Step?

**A.K.A. 3-Way HandShake**

### SYN

Client sends a SYN packet to server.

### SYN-ACK

Server responses a SYN-ACK packet to client.

### ACK

Client sends a ACK packet to server.

## Why?

TCP is bi-directional protocol.

Client should prove that they can receive packet from server.

Linkwise, **server should prove that they can send packet to client, too.**

2-Way HandShake cannot be established.
