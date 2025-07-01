
URL = universal resource locator 
has 4 parts scheme(https)/domain(example.com)/path(product/eletctrc)/resource(phone)

<!-- WHAT HAPPENS URL ON BROWSER  -->

1. browser needs to knows how to reach the server , this is done with a process 
called DNS lookup , domain name system its translates domain names to IP addresses 

2. to make the lookup process fast , the DNS info is heavily cache - browsercache
   if not it will ask the operating system systemd/resolved on RAM

3. if not found in os 
    its make query outisde to dns server configured on resolv.conf(ISP dnsserver , 8.8.8.8, 1.1.1.1 ) 
    DNS server will do 
    Root DNS server (i know .com sends to tld)
      - TLD DNS (i know authoritative for url)
      - Authoritative DNS ( yes facebook url is 23.56.78.56)

4. broswer establishes TCP connection - three wayhandshake 
    
5. if HTTPS , it will do TLS/SSL hanshake , after the connection is established 
6. browser sends in a HTTP Request asking for the webpage
7. server sends back HTTP response 


<!-- WHAT IS TCP -->
TCP is connection oriented layer 4, reliable transport layer protocol used for communication over IP adddresses , ensures realiabilty ,connection oriented (3 way), ordered data , error checking , flow control, congestion control

<!-- WHAT IS IP -->
a layer3 network layer protocol routes packets between devcies accorss networks , uses IP address to identify 
connectionless and unrealible


<!-- WHAT IS 3 way TCP HANDSHAKE  -->
its a 3 step process to establish a connection between client and server before data is transferred 
SYN
Client -> server : hey i want to start a connection heres my SYN number x= 1000
SYN-ACK
server -> client: ok i got your SYN x , here is my SYN y= 5000 and I ACK your  x + 1= 1000+1
ACK
client -> server
i received you SYN 5000 , so im acking 5001 , MY sequence is ready from 1001 


<!-- WHAT IS HTTP  -->
its a application layer protocol used to transfer data (like html,images , json) between client and a server
stateless , Text based , Client - server, runs over TCP ( usually over port 80 serverport )

GET : fetch a resource
POST: submit data
PUT: update a resource
DELETE: delete a resource
HEAD: no body 

<!-- HTTP ERROR CODES -->

<!-- diff between HTTP 2 and 3 -->

HTTP1: one request at tine per one TCP connection 
HTTP 2; , multiplexing(over single TCP connection), Headline of block still exists because of TCP , uses TLS 1.2 or 1.3, reliable
HTTP 3: multiple streams over UDP , UDP default TLS 1.3 , QUIC , no head of line blocking 

<!-- what is line of headblocking  -->
Head-of-line blocking is when one delayed item blocks everything behind it.
In networking, it reduces performance.
HTTP/3 finally solves it completely by avoiding TCP and using UDP

<!-- WHAT IS HTTPS -->
HTTP + TLS , port 443
its just added the layer of security over http , it means text is encrypted  , requires SSL/TLS certificate issued by CA

<!-- explain TLS / SSL in https -->
Transport layer security 
if the data gets intercepted they will see jumbled words cause its encrypted 
TCP handshake
1. browser established TCP connection
2. this is where it begins 
   1. client -> server: client hello : to server ( tells what TLS version, cipher suite (encrypt algos))
   2. server -> clinet: server hello :server chooses the tls version and cipher suite 
   3. server - > client: Certificate TLS got from CA + public key = assysmetic encryption
   4. server hello done  total 2 round trips
3. client key exchange , RSA cipher suite , generate session key with server public key 
   server gets the session key and decrypts with private key 
   finished 
4. Data transmission = with symetric encryption with at session key(faster than assymetric= computationally heavy)

in TLS 1.3 - network round trips in one(where ?) , RSA is not suppported , Both sides agree on session key using prime number math


please Do Not Throw sauce Pizza away
<!-- OSI model (opensystems interconnect) -->
it splits the networking between 2 devices into 7 abstractions layers
PDNTSPA
7. application: HTTP 
6. Presentation: manage compression , encryption
5. Session layer: manage session
4. Transport Layer: TCP , UDP
3. Network Layer: routing between devices = IP protocol
2. Datalink layer : raws bits -> frames(MACheader|IP header|TCP header|HTTP header| Data) = ethernet, WIFI
1. phyical Layer: responsible for raw bits of data = cables, fiber optics

even though layers dont fit the real worl use case , widely used by networking vendors and cloud providers
for eg.: cloud load balancers are l4 tcp level vs l7 application layer https


<!-- LoadBalancers -->
In distrubuted systems, the idea is that each server where your app is hosted has limited memory , /computer resources so we scale it ( vertical scaling/out) by multiple servers .
load balancer is hardwar device or software component acts as traffic /distributes for incoming requests 
so never a single server becomes over whelmed , providing availabity

hardware :physical device high demand enterprices 
software load balancers: nginx can run on common servers  
cloud based balancers: 

layer 4 loadboalaner in transport  = takes routing decisions based on , TCP UDP,ip addresses and ports, they dont inspect the content of traffic so faster , good for basic 

Layer 7 application: play at application layer like HTTP HTTPS , so content based server - ssl offloading 

Global server level balancers : over mutliple geographic locations - global avalaiabity , nearest region 
 uses different algorithms liek round robin , IP/URL hash cache

<!-- Proxy -->
Forwards client requests to external servers on the internet (e.g., browser → proxy → web).

<!-- Reverse Proxy: -->
Sits in front of backend servers and forwards client requests to them (e.g., NGINX → app servers).

<!-- API Gateway -->
Reverse proxy + API management (auth, rate-limiting, logging, etc)

<!-- Container --> 
is a lightweight and standalone package of an application with all its dependencies like libraries , frameworks and 
containerisation is considered to be lightweight version of virtulisation at OS level (not hardware)
uses a container engine like docker instead of hypervisor

<!-- Virtual machines -->
is an emulation of physical computer, running on top of baremetal using a hypervisor = abstracts hardware
and lets you run multiple vms on the same physical machine, each vm has its own guest OS
cheaper to run, easier to scale, shared resources

<!-- Random -->
The client uses a random high port (called ephemeral port), like 49235.


<!-- socket -->
A socket is an endpoint for sending or receiving data across a network.
Think of it as a software abstraction that connects two machines.
<IP address> + <Port number> + <Protocol (TCP/UDP)> = socket 

<!-- port -->
A port is a virtual number used to identify specific services or processes running on a device.

<!-- ssh -->
 SSH (Secure Shell) is a network protocol that allows you to securely access and control remote machines over an unsecured network (like the internet)

<!-- websocket -->
Enables full-duplex, real-time communication over a single TCP connection.
it starts like http, with TCP , TLS , keyexchange 
first HTTP get with upgrade header
server responds http 101 switiching protocols 
client-> serverr = websocket frames
WebSocket enables full-duplex, bidirectional communication over a single, long-lived TCP connection. Unlike HTTP, which is request-response and stateless, WebSocket allows both the client and server to send messages anytime without waiting for a request.
cons----
 but they introduce challenges in scaling, security, and debugging due to their persistent, stateful nature and lack of traditional HTTP safeguards."

It starts with an HTTP handshake, then upgrades the connection using the Upgrade header. Once established, messages can flow in both directions with very low overhead, making it ideal for real-time apps like chat systems, multiplayer games, stock tickers, or collaborative editors.

<!-- UDP(user datagramprotocol) -->
Fast, connectionless protocol with minimal overhead,unrealible suitable for streaming, games, VoIP, low latency
     

<!-- bandwidth -->
Max capacity of the system to transfer data (theoretical limit)

<!-- Throughput -->
Actual rate of successful data transfer (real-world performance)

<!-- IOPS -->
Number of read/write operations a storage system can handle per second

<!-- Latency -->
Time taken to complete a single I/O operation
or  Time taken for a data packet to travel from source to destination

<!-- IPv4 -->
32 bit Address Format , total 4.3, NAT head needed , dotted decimal ,NAT needed

<!-- IPv6 -->
128 bit Address Format , 340 undecilion, NAT head needed , cloud ISP , 5g


<!--  HTTP Status Code Categories -->
1xx	Informational	    Request received, continue processing
2xx	Success           	Request was successful
3xx	Redirection	       Further action needed (e.g., redirect)
4xx	Client Error      	Problem with request (e.g., bad input)
5xx	Server Error      	Problem on server side

🔹 1xx – Informational
Code	Meaning	Example Use Case
100	Continue	Client should keep sending request

🟢 2xx – Success
Code	Meaning	Example Use Case
200	OK	Successful GET or POST
201	Created	Resource created (e.g., POST /user)
204	No Content	Success, no response body

🔄 3xx – Redirection
Code	Meaning	Example Use Case
301	Moved Permanently	URL has changed forever
302	Found (Temporary)	Temporary redirect
304	Not Modified	Cached content still valid

❌ 4xx – Client Error
Code	Meaning	Example Use Case
400	Bad Request	Invalid syntax or missing data
401	Unauthorized	Missing or invalid authentication
403	Forbidden	Authenticated but not allowed
404	Not Found	Resource doesn't exist
429	Too Many Requests	Rate limit exceeded

💥 5xx – Server Error
Code	Meaning	Example Use Case
500	Internal Server Error	Generic server crash or bug
502	Bad Gateway	Server got invalid response upstream
503	Service Unavailable	Server overloaded or down for maintenance
504	Gateway Timeout	Upstream server didn’t respond


<!-- DNS records -->
A :	Address	Maps a domain to an IPv4 address	example.com → 93.184.216.34
AAAA :	IPv6 Address	Maps a domain to an IPv6 address	example.com → 2606:2800:220:1:248:1893::
CNAME:	Canonical Name	Alias one domain name to another domain name	www.example.com → example.com
MX	: Mail Exchange	Directs email traffic to mail servers for the domain	example.com → mail1.example.com
TXT:	Text	Stores arbitrary text — often used for verification or security	SPF, DKIM, Google site verification


<!-- TTL -->
TTL is the expiration time (in seconds) for how long a DNS record stays in cache.

DNS caching improves performance by avoiding repeated lookups, and TTL controls how long entries are cached. But stale records can lead to issues during troubleshooting or migrations if caches aren’t flushed."

<!-- NAT -->
NAT translates private IP addresses (used inside local networks) into public IP addresses when communicating with the internet

<!-- Fire wall -->
A firewall is a security system that monitors and controls incoming and outgoing network traffic based on predefined rules

<!-- slidingwindow tcp -->
"TCP uses a sliding window for flow control to match receiver speed, and congestion control algorithms like slow start and fast retransmit to detect and recover from packet loss. These mechanisms allow TCP to scale up efficiently and back off gracefully during network congestion

<!-- TROUBLESHOOT network -->
I use ping to check reachability,
traceroute to detect where the path slows down, and tools like dig or nslookup for DNS issues.
For deeper analysis, I capture packets using tcpdump or Wireshark to look for dropped packets, slow handshakes, or misconfigurations

<!-- TCP dump -->
"At a high level, tcpdump is a command-line packet analyzer. Its main purpose is to capture and display the packets that pass through a network interface on a system. This is extremely useful for network troubleshooting, security analysis, and understanding traffic patterns
"If I suspect suspicious traffic hitting my web server, I can run tcpdump -i eth0 port 80 to capture only HTTP traffic on the eth0 interface. This helps isolate potential attacks or unusual request patterns

<!-- ping -->
Sends ICMP echo requests, measures latency and packet loss, Check if a host is reachable

<!-- traceroute -->
Maps the path/hops packets take to destination, Diagnose where in the route delays occur


<!-- VPN -->
A VPN creates an encrypted tunnel between your device and another network over the internet. It hides your IP, secures your data, and makes it seem like you're part of another network

<!-- DDoS -->
DDoS (Distributed Denial of Service) is an attack where a bad actor overwhelms a server or network by flooding it with a massive number of fake or useless request

<!-- CDN -->
A CDN is a geographically distributed network of servers that caches and delivers web content closer to users.
like aws cloud front , 


<!-- MAC Address	 -->
	A unique hardware identifier assigned to each network interface (e.g., 00:1A:2B:3C:4D:5E

<!-- ARP (Address Resolution Protocol) -->
Resolves IP address → MAC address


<!-- DHCP -->
Dynamic Host Configuration Protocol
Automatically assigns IPs, subnet mask, DNS, gateway

<!-- Redundancy	 -->
Have multiple components (e.g., 2+ servers) in place

<!-- Failover -->
Automatically switch to a backup if one fails

<!-- Session Persistence	 -->
Keeps a user bound to the same server during a session (sticky sessions)


<!-- How is a network process terminated? -->
A network process is typically terminated through operating system signals or commands that stop the underlying program. This might involve sending a SIGTERM or SIGKILL in Unix-like systems, or using Task Manager on Windows. When terminated, the process closes its associated sockets, ending active connections
i use netstat to see find which process is using a specific port.
eg.: If you have a local web server on port 8080 and want to stop it, you might find its PID (e.g., ps aux | grep 8080) and use kill <PID> on Unix. This signals the server to shut down, closing the port.


<!-- Why wouldn’t you want a root DNS server to answer queries for you instead of delegating to an authoritative server? -->
Root DNS servers sit at the top of the DNS hierarchy. They only provide referrals to TLD (Top-Level Domain) servers instead of answering every DNS query directly. If they tried to respond to every single query, they’d be overwhelmed—leading to massive slowdowns and potentially destabilizing the DNS infrastructure. Delegation spreads out the workload among authoritative servers, keeping the entire system efficient and resilient


<!-- Why is TCP congestion control a problem? -->
TCP congestion control is essential to prevent network collapse by reducing send rates when congestion is detected. However, its very design can lead to problems—namely, underusing available bandwidth and unfairly distributing capacity among flows. This is especially problematic on networks with high latency or varied conditions


<!-- How does a router work? -->
"At a high level, a router is a device designed to forward data packets between different networks. It examines the destination IP address in each incoming packet, then uses its routing table to determine the best route (or next hop) for that packet to travel toward its final destination. Essentially, routers act as traffic directors on the internet, ensuring each packet takes an efficient pat


<!-- database Horizontal Partitioning (Sharding) -->
Horizontal partitioning (sharding) splits rows across multiple databases to distribute load and scale out


<!-- Vertical partitioning -->
Vertical partitioning splits columns into different tables to optimize access patterns and reduce table size


