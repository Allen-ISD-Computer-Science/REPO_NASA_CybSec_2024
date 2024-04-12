## What is it?:
>	Launched in 2021, it is the first optical relay station in space that communicates between a Optical Ground Station(OGS), and a Optical Space Station(OSS).
## Goals:
>	 prove that optical communication is practical and the next step for space communication

## Achievements:
>	One of these tests lasted over 17 hours and showed 63,356,162 data frames (4.1E12 data bits) were relayed error-free.

# Questions:
## Reliability:
## Pointing Problem:
>	Each Optical Ground Station (OGS) must provide three functions when communicating with one of the two optical communications terminals on the GEO spacecraft: 
>		(1) transmit an uplink beacon beam to support the GEO space terminal in pointing to the correct location on the Earth, 
>		(2) transmit a signal beam to the GEO space terminal, and 
>		(3) receive the communications signal from the GEO space terminal.
### Acquisition flow chart
![[Pasted image 20240401183524.png]]
>The LCRD Payload Optical Space Terminal states are:
- S1 - LCRD Optical Space Terminal initialized but not illuminated by the beacon or uplink beam
- S2 - LCRD Optical Space Terminal illuminated by the beacon
- S3 - LCRD Optical Space Terminal illuminated by the uplink beam
- S4 - LCRD Optical Space Terminal receiving data frames
The Ground Stations or User Platform states are:
- T1 - Ground Station or User Platform initialized but not illuminated by the downlink
- T2 - Ground Station or User Platform illuminated by the (optionally dithered) downlink beam
- T3 - Ground Station or User Platform synchronized clock to downlink beam stream
- T4 - Ground Station or User Platform receiving data frames
## Improvements over radio:
-  For approximately the same mass, power, and volume, an optical communications system will provide significantly higher data rates or data volume than a comparable radio frequency system
-  For the same data rate (e.g. 1 Gbps of output), an optical communications system will require less mass, power, and volume than a comparable radio frequency system
ead list
[Advanced Space Laser Communication....](https://www.zte.com.cn/content/dam/zte-site/res-www-zte-com-cn/mediares/magazine/publication/com_en/article/202004/202004007.pdf)
[NIST FINALIST](https://www.nist.gov/news-events/news/2022/07/nist-announces-first-four-quantum-resistant-cryptographic-algorithms)
[coms](https://www.jpl.nasa.gov/news/nasas-tech-demo-streams-first-video-from-deep-space-via-laser)
# LLCD
## Pointing Problem:
* What is it?:
	* How would you aim the laser?
## Speed:
* Laser Communications Relay Demonstration(LCRD)
>	Using optical communications, LCRD is sending data to Earth from geosynchronous orbit at *1.2 gigabits-per-second (Gbps).* At this speed and distance, you could download a movie in under a minute.[source](https://esc.gsfc.nasa.gov/projects/LCRD)
  
## Reliability:
* What to do in the event that cloud interference? 
>	Unlike radio frequency communications, optical signals cannot penetrate cloud coverage, so NASA must build a system flexible enough to avoid interruptions due to weather. LCRD will transmit data received from missions to two ground stations, located in Table Mountain, California, and Haleakalā, Hawaii. These locations were chosen for their minimal cloud coverage. LCRD will test different cloud coverage scenarios, gathering valuable information about the flexibility of optical communications.
* TLDR: Have multiple ground stations with preferable weather conditions to communicate effectively
## Security:
* How should we secure our systems / assets:
	>First, implement proper Authentication for who is supposed to login and use it.
	>Second, Chose a key based algo for sending messages.
	>Third, have secure sites and best practices