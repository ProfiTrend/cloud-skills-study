## [TCP 4 Handshake](TCP-4-HANDSHAKE.md)

> TCP 4 handshake에서 리눅스 소켓 close wait과 time wait의 차이점, 각 단계에서 나올 수 있는 문제

## CLOSE_WAIT vs TIME_WAIT

### Active Close vs Passive Close

**Active Close** : A target which request to disconnect TCP.

**Passive Close** : A target which response to disconnect TCP.

### CLOSE_WAIT

1. Passive Close is changed to CLOSE_WAIT.
2. Passive Close orders terminating to the process which use TCP port.
3. Passive Close waits until execute 'close'.

### TIME_WAIT

1. Active Close requests ACK to FIN packet.
2. Active Close disconnects after 240 seconds.

## TCP 4 Handshake Trouble

### SYN Flag

If the host send sequential sequence number(not a random number), other host can recognize previous connection's packet.

So, Hosts set random numbers to ISN.

### TIME_WAIt

ACK packet can be received after FIN packet because of routing delay or packet loss.

So, Active Close wait 240 seconds for ACK packet.
