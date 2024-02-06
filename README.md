# **Mission Statement - Network Architecture Objective:** 
### Design a Reliable, Redundant, and Secure Network to transport the data, video, telemetry, and voice from the moon's Smart Building to a Control Center(s) on Earth.
---
## Roles:
**Project Manager: Abel Semahegn @abelSemahegn [Digital Portfolio](https://codermerlin.academy/users/abel-semahegn/Digital%20Portfolio/index.html)** 


**Front End Developer: Vansh Bhatt @theogflamez [Digital Portfolio](https://codermerlin.academy/users/vansh-bhatt/Digital%20Portfolio/index.html)**


**QA: Richard Jang @Richard-Jang [Digital Portfolio](https://www.codermerlin.academy/users/ming-ruei-jang/Digital%20Portfolio/index.html)**


**UI/UX: Tanay Sreedharan @stuffysaturn [Digital Portfolio](https://codermerlin.academy/users/tanay-sreedharan/Digital%20Portfolio/index.html)**


**RM: Srujan Sannidhi @s-sannidhi [Digital Portfolio](https://codermerlin.academy/users/srujan-sannidhi/Digital%20Portfolio/index.html)**


**DBA: Andrew Lin (@Fangedan / @McAndrewJr) [Digital Portfolio](https://codermerlin.academy/users/andrewm-lin/Digital%20Portfolio/index.html)**


**Back End Developer: Aditya Sudharshan @ditya-beta [Digital Portfolio](https://codermerlin.academy/users/aditya-sudharshan/Digital%20Portfolio/CS-I/index.html)**


**Project Manager: Jacob Fesseha @Nigusi-Artabanus [Digital Portfolio](https://codermerlin.academy/users/jacob-fesseha/Digital%20Portfolio/index.html)**

---
# **Link to Project Presentation**
**[NASA CYBERSECURITY PROJECT PRESENTATION](https://docs.google.com/presentation/d/1yy5wZxm44n5CV3NfuLQcmYtim-0MNsef_eiQNs5aADA/edit?usp=sharing)**
---

# One time Pad encryption implementaion
This is the method of reading and encrypting the text


### 1. Git Cloning a Repo:

```bash
git clone <repository_url>
```

Replace `<repository_url>` with the actual URL of the repository you want to clone.

### 2. Make a New Branch:

```bash
git checkout -b <new_branch_name>
```

This command creates a new branch (`<new_branch_name>`) and switches to it.

### 3. Pushing Changes to Your Branch:

```bash
git add .
git commit -m "Your commit message"
git push origin <your_branch_name>
```


Replace `<your_branch_name>` with the name of your branch. The sequence of commands adds changes, commits them with a message, and then pushes the changes to the remote repository.

### 4. Go to github and make a pr(Pull Request)


### 5.Close branch on your machine
```bash
git branch -d <branch_name>
```
# Objective

**Mission Statement - Network Architecture Objective:** Design a Reliable, Redundant, and Secure Network to transport the data, video, telemetry, and voice from the moon's Smart Building to a Control Center(s) on Earth.

**Requirements:**
- At least 3 Network Designs
- A simulation/network model that demonstrates the networks
- A recommendation on the best network design and the rationale for each component.
- Take into account the loss of data due to the speed of light and radiation.

---

# Solution

## One Time Pad:

**OTP** refers to One-Time Password, a security feature designed to enhance authentication. OTPs are dynamic codes that expire after a short period, providing an additional layer of security beyond traditional static passwords. Users typically receive OTPs through various means, such as text messages, mobile apps, or hardware tokens. The uniqueness of each OTP ensures that even if the code is intercepted, it becomes useless after its expiration. This method significantly reduces the risk of unauthorized access, especially when compared to static passwords that are more susceptible to hacking or brute-force attacks. By implementing OTP in the program, it aims to fortify the security of user accounts and sensitive information.

## Quantum Computers:

If you re-use the key, it is not a one-time-pad. There is a reason the words "one-time" appear in the name. If you use it more than once it is literally not a one-time pad. Also, if you do not keep it completely secret, and if it's not completely random, it's not a one-time pad. Therefore, if any computational argument whatsoever even factors into the security of the encryption, it is not a one-time pad. The one-time pad is easily provably perfectly secure. When people say they might find a vulnerability in the one-time pad, what they mean is that they might find a vulnerability in the Vernam cipher. The one-time pad is inherently invulnerable, regardless of the computational method used; it is perfectly secure, not just computationally secure. The applications of alternative models of computation to cryptology are in attacking computationally secure ciphers. Clearly if a cipher is only computationally secure, then a nonstandard model of computation might break or undermine that security. But this has nothing to do with the one-time pad. Stories you might read online of supposedly broken one-time pad encryptions (e.g, the VENONA project) are *not* actually one-time pads. They have non-random keys, or reused keys, or non-secret keys, or other problems which make them by definition not one-time pads. They are other things, such as Vernam ciphers, and the only relevance they have to the one-time pad is that typically their authors do not realize their mistakes and therefore do not realize that they are not actually encrypting with a one-time pad. (Indeed, if people always noticed their mistakes, cryptology would be much harder.)

*Reference:*
von Hippel, Max. (2018). Re: Can one-time pad (OTP) cipher system be broken with quantum computers or techniques based on quantum theory?. Retrieved from: [ResearchGate](https://www.researchgate.net/post/Can-one-time-pad-OTP-cipher-system-be-broken-with-quantum-computers-or-techniques-based-on-quantum-theory/5a865c122018391be31c0540/citation/download).

## LoRa:

**LoRaWAN** (Long Range Wide Area Network) is a protocol built on top of the LoRa technology, defining the communication protocol and system architecture for network-wide communication. LoRaWAN allows for secure, bidirectional communication between IoT devices and a centralized network server, facilitating the deployment and management of large-scale IoT applications.

[Examples]

## Solution Summary:

Creating a Wide Area Network (WAN) in space with no existing infrastructure using LoRa, OTP (One-Time Pad), and quantum-resistant algorithms for peer-to-peer (P2P) encryption involves several considerations.

- LoRa, with its long-range and low-power capabilities, is suitable for space-based communication, especially when infrastructure is limited. It allows for efficient communication between devices in different parts of space.
- OTP, known for its theoretical security strength, could be implemented for secure communication between space-based nodes. Each communication session would require a unique, random key that is as long as the message itself, making it theoretically unbreakable if implemented correctly. However, managing and securely distributing these keys in a space environment would be a challenge.
- In the context of quantum-resistant algorithms, the use of cryptographic algorithms resistant to quantum attacks becomes crucial. Post-quantum cryptography algorithms, such as lattice-based cryptography or hash-based cryptography, would need to be employed to ensure the security of communications against potential future quantum threats.
- For P2P encryption, quantum-resistant algorithms could be integrated into the communication protocols, providing a secure layer for data exchange between devices. The decentralized nature of P2P communication aligns with the challenges of space communication, where traditional centralized infrastructure may be impractical.
- It's important to consider the harsh space environment, including radiation and temperature extremes, which could impact the performance of electronic components. Robust error correction and fault-tolerant mechanisms would be necessary to ensure reliable communication.

In summary, building a WAN in space with LoRa, OTP, and quantum-resistant algorithms involves careful consideration of the unique challenges posed by the space environment, including implementing secure key management and accounting for potential quantum threats in the future.

---

## One Time Pad Example:


20 35 49 44 06  04 04 02 23 14  33 26 23 41 16  11 33 17 07 25

46 31 41 48 14  33 02 19 16 24  33 26 23 41 16  10 00 48 19 49

10 04 28 38 21  33 02 19 16 24  22 20 18 17 33  47 34 42 06 13

03 21 38 12 41  11 28 46 25 42  46 21 03 17 34  32 40 23 35 44

---

---
# What we need to do to finish:

* OTP 2 way communication with quantum resistant p2p on top
* create 2 Meshtastatic nodes
* send an:
	* Image
	* document
	* media
* Create a presentation - [Slides link](https://docs.google.com/presentation/d/1AQqGboY-F6YAWDqTksTL0u90sNOWPKpcige1Z7kMyDA/edit?usp=sharing)
# Network Basics
These are the basic components of our network designs
## Switches
* They connect devices in a network together by sending each other packets
* They connect end devices with the same Subnet Mask (ex: all devices with mask 255.0.0.0 can communicate with each other but not with subnet mask 255.255.0.0)
* They do not have an IP and are just a pathway for packets
## Routers
* They connect small networks through switches for different subnet masks to communicate
* Their ports can be assigned different IP values which allows them to connect to many subnet masks
* Due to their ports they have several IP addresses which can all be pinged by end devices
## Central Office Server
* They are a special type of server that can wirelessly communicate with devices
* They can connect to radar towers which is useful for exploration communication and communication back to Earth
* They can also connect to end devices like PCs through routers and switches through their IP address
## Radar Tower
* They are similar to switches except for they're wireless
* They have an IP address to connect phones and COS but they can't be pinged as they are only  gateway
## End Devices
* These are the devices users will be using (For our designs Phones & PCs)
* These are configured with their own unique IP addresses and communicate with each other using the rest of the network
* In a well-set-up network all devices should be able to ping each other with no errors
## Connections
* Copper Straight Through: Ethernet cable connection between switches, routers, and PCs
* Copper Crossover: Ethernet cable for connection between the same type of devices (ie: PC to PC) or between routers/switches and network hubs like servers
* Coaxial: It's a cable type to connect radar devices like dishes and towers to COS
* 3/4G Wireless Connection: Broadband cellular network technology for wireless connection
