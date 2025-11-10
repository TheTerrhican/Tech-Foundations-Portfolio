# 🛡️ Project 2: Network Traffic Analysis Case Study

## 🎯 Focus Area
**Cybersecurity, Network Defense, and Incident Response**

## 💡 Overview
This case study documents the structured process of analyzing a suspicious network traffic capture (PCAP) file to identify the nature of a security incident. This project demonstrates proficiency in using network analysis tools to isolate threats and translate forensic findings into actionable mitigation strategies.

## ⚙️ Technologies Used
* **Wireshark:** Primary tool used for deep packet inspection and filtering.
* **Networking Fundamentals:** Application of knowledge regarding TCP/IP, common port numbers, and protocol behavior (HTTP, DNS, FTP, etc.).
* **Security Concepts:** Understanding of common attack patterns (e.g., clear-text communication, port scanning, malicious payloads).

## 📝 The Methodology (The Process)
To conduct the analysis, the following four-stage methodology is followed, regardless of the incident type:

### 1. Initial Triage and Baseline
* **Filtering:** Apply simple display filters (e.g., `http`, `tcp.port == 21`) to isolate traffic for specific protocols.
* **Statistics:** Review endpoint and conversation statistics to identify top talkers and unusual traffic volumes.

### 2. Identifying the Payload
* **Protocol Analysis:** Drill down into specific protocols to look for clear-text data (e.g., unencrypted passwords, sensitive information).
* **Alert Keywords:** Search packet payloads for known malicious indicators or suspicious keywords (e.g., "password," "exec," known malware domain names).

### 3. Incident Isolation
* **Source/Target Identification:** Pinpoint the exact **Source IP** and **Destination IP** involved in the suspicious conversation.
* **Timeline:** Use timestamps to determine the start and end time of the suspicious activity to aid in log correlation.

### 4. Recommendation and Reporting
* **Mitigation Strategy:** Document specific technical steps (firewall blocks, policy changes) to contain the threat and prevent recurrence.
* **Professional Reporting:** Summarize findings clearly and concisely for stakeholders and incident response teams.

## 📉 Example Mitigation Recommendations
* **Containment:** Isolate the identified source endpoint immediately via firewall or network access control.
* **Policy Change:** Disable all clear-text protocols (FTP, Telnet, HTTP) across the network to enforce the use of secure alternatives (SFTP, SSH, HTTPS).

---
