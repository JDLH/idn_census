# IDN Census Tools
This repository contains tools for measuring the adoption of globally inclusive domain names, URLs, and email addresses in the World Wide Web at large, by measuring their occurrence in the Common Crawl data. 
By "globally inclusive" we mean that they are not limited to the basic letters and digits of the Latin script, sometimes called the "ASCII subset" of characters. 
Instead, they draw from a wide range of characters from many scripts and many languages: Chinese, Arabic, Thai, Cherokee, the accented Latin characters of Vietnamese, French, and German, and so on. 

Globally inclusive domain names are often referred to as "Internationalised Domain Names", or "IDNs". Globally inclusive email addresses are referred to as "EAI", which stands for "Email Address Internationalisation". 

Also in scope for the IDN Census are domain names, URLs, and email addresses which are registered under top-level domains beyond the original 2-character country code domain names (e.g. .ca for Canada), and 3-character domain names (e.g. .com, .net. .org). 
Thus, domain names under .tech, URLs at .museum domains, and email addresses at .mobi domains are all in scope for this project.  


## Resources

- The [**Common Crawl**](https://commoncrawl.org/) non-profit organisation "maintains a free, open repository of web crawl data that can be used by anyone." These tools search the Common Crawl data to find the globally inclusive material within them.
The common crawl data is hosted on AWS. You can search it from code running on AWS, or copy the data to another location and work on it there.
There is also a Common Crawl Index which can be searched using a simple REST API, sending URLs with parameters and getting lists URLs and domain names from the Common Crawl data in return.

- These tools are motivated by a desire to promote Universal Acceptance. This is the vision that all domain names and all email addresses work in all software applications. 
The [Universal Acceptance Steering Group](https://uasg.tech/) works to promote Universal Acceptance, through measurement, technology problem-solving, training, and awareness-raising.

## Tools

`count_domains.py` is a minimal tool, based on a program at the [Common Crawl "Get Started" page](https://commoncrawl.org/get-started) . It retrieves all URLs at a given top-level domain name (hard-coded) from an instance of the Common Crawl index (also hard-coded). It is in Python.  
There is no copyright statement in the original program. We do not assert copyright in our changes.

## Project team

Jim DeLaHunt ([Github/JDLH](https://github.com/JDLH)), project founder

