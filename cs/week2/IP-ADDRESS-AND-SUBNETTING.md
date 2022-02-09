# IP Address And Subnetting

IP Address(Internet Protocol Address) is a special number between network equipments.

## IPv4

> 211.45.27.231

IPv4 address has a size of 32bits. The range of IPv4 is 4,294,967,296 address theoretically.

| Class   | Start Address | End Address   |
|---------|---------------|---------------|
| Class A | 0.0.0.0       | 127.255.255.0 |
| Class B | 128.0.0.0     | 191.255.255.0 |
| Class C | 192.0.0.0     | 223.255.255.0 |
| Class D | 224.0.0.0     | 239.255.255.0 |
| Class E | 240.0.0.0     | 255.255.255.0 |

Class D is multicast only, and Class E is research only.

## IPv6

> 2001:0db8:85a3:08d3:1319:8a2e:0370:7334

IPv6 is the next generation of internet protocol. IPv4 is already depleted, so they made a new standards.

It has as size of 128bits. The range og IPv6 is 340,282,366,920,938,463,463,374,607,431,768,211,456 address
theoretically.

## Subnetting

> A technology to divide a network as much as we need.

1. Efficiency : Divide ip addresses to prevent waste.
2. Performance : Reduce network broadcast size to improve performance.
3. Security : Improve security because we divide network.

### Example

IP address : 192.168.0.1

Subnet mask : 255.255.255.0(/24)

| Bit       | IP address range              |
|-----------|-------------------------------|
| 0 ~ 31    | 192.168.0.1 ~ 192.168.0.31    |
| 32 ~ 63   | 192.168.0.32 ~ 192.168.0.63   |
| 64 ~ 95   | 192.168.0.64 ~ 192.168.0.95   |
| 96 ~ 127  | 192.168.0.96 ~ 192.168.0.127  |
| 128 ~ 159 | 192.168.0.128 ~ 192.168.0.159 |
| 160 ~ 191 | 192.168.0.160 ~ 192.168.0.191 |
| 192 ~ 223 | 192.168.0.192 ~ 192.168.0.223 |
| 224 ~ 255 | 192.168.0.224 ~ 192.168.0.255 |

Network : 192.168.0.1


Broadcast : 192.168.0.255