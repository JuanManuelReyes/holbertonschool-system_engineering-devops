
# 0x04. Loops, conditions and parsing
## About  Bash  projects

Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

## Background Context

https://youtu.be/BC2neyc5GcI
## Resources

**Read or watch**:

 - [Loops sample](https://intranet.hbtn.io/rltoken/XnVjFM8a1W4RfRu4TCPY-g)
-   [Variable assignment and arithmetic](https://intranet.hbtn.io/rltoken/IM0Gv6VPzwAmqzlJxETZkw "Variable assignment and arithmetic")
-   [Comparison operators](https://intranet.hbtn.io/rltoken/K3E6xI9-goDM-93vsjCpPA "Comparison operators")
-   [File test operators](https://intranet.hbtn.io/rltoken/0OZLLDT28KrRZdid-l6hwg "File test operators")
-   [Make your scripts portable](https://intranet.hbtn.io/rltoken/Dyrnap2UC-LrzrmCOJRx8A "Make your scripts portable")

**man or help**:

-   `env`
-   `cut`
-   `for`
-   `while`
-   `until`
-   `if`

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/AVktLDpuzzD92vXnfuqeWg "explain to anyone"),  **without the help of Google**:

### General

-   How to create SSH keys
-   What is the advantage of using  `#!/usr/bin/env bash`  over  `#!/bin/bash`
-   How to use  `while`,  `until`  and  `for`  loops
-   How to use  `if`,  `else`,  `elif`  and  `case`  condition statements
-   How to use the  `cut`  command
-   What are files and other comparison operators, and how to use them

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Ubuntu 20.04 LTS
-   All your files should end with a new line
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   You are not allowed to use  `awk`
-   Your Bash script must pass  `Shellcheck`  (version  `0.7.0`) without any error
-   The first line of all your Bash scripts should be exactly  `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

## More Info

### Shellcheck

[Shellcheck](https://intranet.hbtn.io/rltoken/E7Pr2zeM3cdY5-C0HKwtbw "Shellcheck")  is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about.  `Shellcheck`  is your friend!  **All your Bash scripts must pass  `Shellcheck`  without any error or you will not get any points on the task**.

`Shellcheck`  is available on the school’s computers. If you want to use it on your own computer, here is how to  [install it](https://intranet.hbtn.io/rltoken/SOX0HZTMgzHbcxrvU1X4hw "install it").

Examples:

Not passing  `Shellcheck`:
![enter image description here](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png)
Passing `Shellcheck`:
![enter image description here](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png)
For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code `SC2034`, you can browse [https://github.com/koalaman/shellcheck/wiki/SC2034](https://intranet.hbtn.io/rltoken/1SeRQAUtYIpfXXIQeD1PFQ "https://github.com/koalaman/shellcheck/wiki/SC2034").
