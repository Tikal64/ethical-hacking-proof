# ethical-hacking-proof



## Comandi Base Linux




1. **ls**: Questo comando viene utilizzato per elencare i file e le directory nel tuo attuale percorso di lavoro.

    Esempio: `ls`

2. **cd**: Usato per cambiare la directory attuale.

    Esempio: `cd /home/user/Documents`

3. **pwd**: Stampa il percorso della directory di lavoro attuale.

    Esempio: `pwd`

4. **cat**: Utilizzato per visualizzare il contenuto di un file.

    Esempio: `cat file.txt`

5. **echo**: Utilizzato per stampare un testo o una variabile.

    Esempio: `echo Ciao, mondo`

6. **touch**: Crea un nuovo file.

    Esempio: `touch nuovo_file.txt`

7. **rm**: Rimuove un file.

    Esempio: `rm vecchio_file.txt`

8. **mkdir**: Crea una nuova directory.

    Esempio: `mkdir nuova_directory`

9. **rmdir**: Rimuove una directory.

    Esempio: `rmdir vecchia_directory`

10. **cp**: Copia file o directory.

    Esempio: `cp /path/to/source/file.txt /path/to/destination/`

11. **mv**: Sposta o rinomina file o directory.

    Esempio: `mv /path/to/source/file.txt /path/to/destination/`

12. **grep**: Ricerca all'interno di file usando espressioni regolari.

    Esempio: `grep "testo_da_cercare" file.txt`

13. **find**: Ricerca file o directory.

    Esempio: `find / -name file.txt`

14. **man**: Visualizza il manuale dell'utente per un comando.

    Esempio: `man ls`

15. **chmod**: Cambia i permessi di un file o una directory.

    Esempio: `chmod 755 file.txt`

16. **chown**: Cambia il proprietario di un file o di una directory.

    Esempio: `chown utente:gruppo file.txt`








How to ping a host



```
ping hostName

```

_______________________________



## How to use ProxyChains and tor


Fonte : https://geekflare.com/anonymize-linux-traffic/


First, update the Linux system with the patches and the latest applications. For this we open a terminal and type:

```
sudo apt update && sudo apt upgrade
```
Then check whether Tor and Proxychains are pre-installed or not by simply typing these commands separately :

```
proxychains 

tor
```


If they were not installed, type the following command in the terminal:

```
sudo apt install proxychains tor -y
```

Please note that we’re not installing the Tor browser. We’re installing the tor service which is a service that runs locally on your virtual machine or on your operating system and is actually bound to a particular port on local-host. In our case, it’s going to be 9050 and that’s the default with the tor service.

To check the status of Tor :
```
┌──(root💀kali)-[/home/writer]
└─# service tor status                                                                 
● tor.service - Anonymizing overlay network for TCP (multi-instance-master)
     Loaded: loaded (/lib/systemd/system/tor.service; disabled; vendor preset: disabled)
     Active: inactive (dead)

```
To start the tor service :

```
service tor start
```

To stop the tor service :

```
service tor stop
```
Configuring ProxyChains

First, locate the directory of ProxyChains by using this command :
```
┌──(root💀kali)-[~]
└─# locate proxychains                       
/etc/proxychains4.conf
/etc/alternatives/proxychains
/etc/alternatives/proxychains.1.gz
/usr/bin/proxychains
/usr/bin/proxychains4
/usr/lib/x86_64-linux-gnu/libproxychains.so.4
/usr/share/applications/kali-proxychains.desktop
/usr/share/doc/libproxychains4
/usr/share/doc/proxychains4
```
This is our configuration file.


/etc/proxychains4.conf

Based on the above result, we can notice that the ProxyChain config file is located in /etc/.

We need to make some adjustments to ProxyChains configuration files. Open the config file in your favorite text editor like leafpad,  vim, or nano.

Here I am using nano editor.

nano /etc/proxychains.conf


The config file is opened. Now you need to comment and comment out some lines to set up the proxy chains.

You’ll notice “#” in the configuration, which stands for bash language comments. You may scroll down and make the adjustments using the arrow keys.

#1. Dynamic chain should be removed from the remark comment. All you have to do is to remove a # in front of dynamic_chain.

dynamic_chain


```
#
# Dynamic - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# at least one proxy must be online to play in chain
# (dead proxies are skipped)
# otherwise EINTR is returned to the app

#2. Put the comment in front of random_chain and strict_chain. Just add # in front of these.

#random_chain
#
# Random - Each connection will be done via random proxy
# (or proxy chain, see  chain_len) from the list.
# this option is good to test your IDS :)

#3. Max times it includes the proxy-DNS uncomment, double-check that it is uncommented. You will avoid any DNS leaks that may reveal your true IP address in this manner.

# Proxy DNS requests - no leak for DNS data
proxy_dns
 

#4. Add socks5 127.0.0.1 9050 in the proxy list the last line.

[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
socks4  127.0.0.1 9050 
socks5  127.0.0.1 9050 

```

Here socks4 proxy will be already given. You need to add the socks5 proxy as shown above. And finally, save the config file and exit the terminal.
Usage of ProxyChains

At first, you have to start the Tor service in order to use ProxyChains.

```
┌──(root💀kali)-[/home/writer]
└─# service tor start
```

After the tor service is started, you can use ProxyChains for browsing and for anonymous scanning and enumeration. You can also use Nmap or sqlmap tool with ProxyChain for scanning and searching exploits anonymously. It’s great, right?

To utilize ProxyChains, simply type the ProxyChains command in a terminal, followed by the name of the app you want to use. The format is as follows:

```
┌──(writer㉿kali)-[~]
└─$ proxychains firefox www.flippa.com
```


To use Nmap:
```
proxychains nmap -targetaddress
```


To use sqlmap:

```
proxychains python sqlmap -u target
```

You can also test for exploits anonymously like

```
proxychains python sqlmap -u http://www.targetaddress/products.php?product=3
```

Literally, Every TCP reconnaissance tool can be used with ProxyChains.

For the final confirmation of ProxyChains is working properly or not, just go to dnsleaktest.com and check your IP address and DNS leaks.

After running ProxyChains, you will notice that Firefox has been loaded with a different language. Now, let’s perform a DNS leak test by using a command :

```
proxychains firefox dnsleaktest.com
```

_______________________________


## How to use dmitry 

Dmitry is a powerful open-source intelligence (OSINT) tool included in Kali Linux, a popular penetration testing and ethical hacking distribution. Dmitry, also known as Deepmagic Information Gathering Tool, is designed to gather information about a target by performing various reconnaissance techniques.

Dmitry provides a range of functionalities for information gathering, including:

    DNS enumeration: Dmitry can perform DNS resolution to gather information about the target's domain names and associated IP addresses.

    Whois lookup: It can retrieve registration information about a domain name, such as the owner's name, organization, contact details, and domain registrar.

    Port scanning: Dmitry can scan a range of ports on a target system to identify open ports and services running on those ports.

    Network footprinting: It can gather information about the target's network infrastructure, such as netblocks, autonomous systems (AS), and routing information.

    Subdomain enumeration: Dmitry can perform subdomain brute-forcing to discover additional subdomains associated with a target domain.

    Email address gathering: It can search for email addresses associated with a domain name or perform a search for email addresses using specific keywords.

    TCP/IP fingerprinting: Dmitry can analyze the network packets to determine the operating system and other details about the target system.



The syntax for running Dmitry in Kali Linux is as follows:

```
dmitry [-winsepfb] [-t <seconds>] [-o <filename>] <target>
```

Here's an explanation of the available options:

- `-w`: Perform a whois lookup for the target domain.
- `-i`: Perform an IP address lookup for the target.
- `-n`: Perform a DNS lookup for the target domain.
- `-s`: Perform a subdomain search for the target domain.
- `-e`: Perform an email address search for the target domain.
- `-p`: Perform a TCP port scan on the target.
- `-f`: Perform a TCP fingerprinting scan on the target.
- `-b`: Perform a TCP banner grab on the target.
- `-t <seconds>`: Specify the timeout value for each operation in seconds.
- `-o <filename>`: Save the output to the specified filename.

The `<target>` can be an IP address or a domain name you want to gather information about.

Here are a few examples:

1. Perform a basic scan on a target domain:
   ```
   dmitry -winse <target>
   ```

2. Perform a TCP port scan and save the output to a file:
   ```
   dmitry -p -o output.txt <target>
   ```

3. Perform a TCP fingerprinting scan on a target IP address:
   ```
   dmitry -f <target>
   ```

Remember to replace `<target>` with the actual IP address or domain name you want to target.




__________________________________


## nmap

Nmap è uno strumento di scansione di rete ampiamente utilizzato per rilevare host e servizi all'interno di una rete. Fornisce un'ampia gamma di funzionalità ed è disponibile per diverse piattaforme, inclusi Windows, macOS e Linux. 
1. Scansione di base:
   ```
   nmap <target>
   ```
   Esempio: `nmap 192.168.1.1`

   Questo eseguirà una scansione di base sull'host di destinazione e mostreràle porte aperte.

2. Scansione di tutti i porti TCP:
   ```
   nmap -p- <target>
   ```
   Esempio: `nmap -p- 192.168.1.1`

   Questo eseguirà una scansione di tutti i porti TCP sull'host di destinazione.

3. Scansione di un intervallo di porte specifico:
   ```
   nmap -p <port range> <target>
   ```
   Esempio: `nmap -p 1-1000 192.168.1.1`

   Questo eseguirà una scansione dei porti compresi nell'intervallo specificato sull'host di destinazione.

4. Scansione dei porti UDP:
   ```
   nmap -sU <target>
   ```
   Esempio: `nmap -sU 192.168.1.1`

   Questo eseguirà una scansione dei porti UDP sull'host di destinazione.

5. Scansione di più host:
   ```
   nmap <target1> <target2> ...
   ```
   Esempio: `nmap 192.168.1.1 192.168.1.2`

   Questo eseguirà una scansione su più host contemporaneamente.

6. Rilevamento del sistema operativo:
   ```
   nmap -O <target>
   ```
   Esempio: `nmap -O 192.168.1.1`

   Questo cercherà di rilevare il sistema operativo dell'host di destinazione.

7. Scansione con script:
   ```
   nmap -sC <target>
   ```
   Esempio: `nmap -sC 192.168.1.1`

   Questo eseguirà una scansione utilizzando gli script di default di Nmap per rilevare informazioni aggiuntive sui servizi.

8. Scansione "stealth" (scansione senza lasciare traccia):
   ```
   nmap -sS <target>
   ```
   Esempio: `nmap -sS 192.168.1.1`

   Questo eseguirà una scansione "stealth" utilizzando la tecnica di scansione SYN.

Questi sono solo alcuni esempi di utilizzo di Nmap. L'utility offre molte altre opzioni e funzionalità avanzate per adattarsi alle diverse esigenze di scansione di rete. 




https://github.com/giterlizzi/nmap-log4shell


_____________________________________________________________




Here are some examples of auxiliary modules in Metasploit:

1. Port Scanning:
   - `auxiliary/scanner/portscan/tcp`: Scans for open TCP ports on a target.
   - `auxiliary/scanner/portscan/udp`: Scans for open UDP ports on a target.

2. Banner Grabbing:
   - `auxiliary/scanner/http/http_title`: Grabs the HTTP title from web services.
   - `auxiliary/scanner/ftp/ftp_version`: Retrieves version information from FTP services.

3. Brute-Forcing:
   - `auxiliary/scanner/ssh/ssh_login`: Performs brute-force SSH login attempts.
   - `auxiliary/scanner/smb/smb_login`: Performs brute-force SMB login attempts.

4. Information Gathering:
   - `auxiliary/scanner/http/dir_scanner`: Scans for interesting directories on web servers.
   - `auxiliary/scanner/netbios/nbname`: Performs NetBIOS name resolution.

5. Denial of Service:
   - `auxiliary/dos/http/slowloris`: Performs a Slowloris DoS attack against an HTTP server.
   - `auxiliary/dos/udp/snarf`: Performs a UDP Snarf attack.

To use any of these modules, you can run Metasploit, load the appropriate module, set the required options, and then execute the module.

Please note that the list of modules and module names might change or get updated over time. Always ensure you have the latest version of Metasploit and use it responsibly and legally, with proper authorization and consent for penetration testing purposes. Unauthorized access or use of these tools is illegal and unethical.



_____________________________________________________________________________________________________







