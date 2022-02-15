# Routing

> 라우터에서 설정 가능한 라우팅 방법의 종류와 대표적인 라우팅 프로토콜

## Static VS Dynamic

### Static Routing

Administrator set the routing information.

**Pros**

It is faster than dynamic routing.
The router is no pressure because it refers only routing information by the administrator.

**Cons**

Cannot change the routing information actively, and the administrator should learn about network operation.

### Dynamic Routing

Routers make exchanges about networks' information automatically.

**Pros**

Administrator just set only initial setting.
The router sends and receives routing information each other, and set routing tables automatically

**Cons**

Occupy router's memory more than static routing.

## IGP VS EGP

### IGP

> Internal Gateway Protocol

IGP is a routing protocol about the internal path of the domain.

### EGP

> Exterior Gatewau Protocol

EGP is a routing protocol about exchange path settings information between systems.
EGP us the purpose of SECURITY and CONTROL.