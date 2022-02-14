# Subnetting for 31 hosts

> 10.0.0.0/8 네트워크를 31대의 호스트가 사용 가능하도록 서브넷팅

We should need 31 hosts, and gateway IP.

## Status

| IP Address                          | Subnet Mask                         |
|-------------------------------------|-------------------------------------|
| 10.0.0.0                            | 255.0.0.0                           |
| 00001010.00000000.00000000.00000000 | 11111111.00000000.00000000.00000000 |

## Subnetting

| Subnetting  | IP Address           | Allocate Object   |
|-------------|----------------------|-------------------|
| 10.0.0.0/26 | 10.0.0.0             | Network Address   |
|             | 10.0.0.1 ~ 10.0.0.62 | Host IP           |
|             | 10.0.0.63            | Broadcase Address |