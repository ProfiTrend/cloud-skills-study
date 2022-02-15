# Query Naver.com

> naver.com 쿼리 시 항상 .com 네임서버를 호출하는가?

**No! Because We Have Cache Data!**

Client request server's IP to DNS server.
If this DNS sever already have cache data about server's IP, DNS provide cache data to client.

But DNS has no cache data, it should request name servers.
