# TCP 3 Handshake

> TCP 3 handshake에서 첫 연결 시도시 발생하는 문제들

## Timeout

Timeout is the time limit that receive ACK packet.

## SYN Flag

If the host send sequential sequence number(not a random number), other host can recognize previous connection's packet.

So, Hosts set random numbers to ISN.

## The other doesn't asnwer.

**FIREWALL**

We should use `netstat` to check network status.

## Server doesn't response, but status is ESTABLISHED.

We should check **Accept Code**.

Because we are success to connect server.
