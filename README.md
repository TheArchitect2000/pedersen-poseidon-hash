# pedersen-poseidon-hash

### General Instructions:
- This is an individual exam. No collaboration, external help, or internet browsing (except for documentation) is allowed.
- You must write and submit functional code that adheres to the problem statement.
- Your submission must include:
The client code
The server code
A README file explaining how to run your program
- The server must run on TCP port 10,000 and implement a specific protocol (detailed below).
- Use Python for implementation. Your code must be well-structured and commented.
- Submission format: Upload a ZIP file containing all your code files and README.
- Late submissions will not be accepted.

### Problem Statement:
You need to implement a Client-Server application where:
- The client connects to a server running on TCP port 10,000.
- The protocol begins with the client sending “HELO” to the server. The server responds with “OK”.
- The client selects a hash function from the following:
SHA1
SHA256
Pedersen
Poseidon
- If the client sends an invalid hash function name, the server responds with “NOTSUPPORTED” and closes the connection.
- If the hash function is valid, the server responds with “OK”.
- The client then sends a string to the server.
- The server computes the hash using the selected function and returns:
The size of the hash value in bytes.
The actual hash value.
