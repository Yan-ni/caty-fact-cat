# 😺 Caty Fact Cat

An Instagram bot posting daily images of cats 🐈 with facts about them in the post caption caption.

You can check out the [instagram account](https://www.instagram.com/caty_fact_cat/) associated with the bot. Don't hesitate to follow 😉

## 🚀 Getting Started

### Prerequisites

To be able to run this script, you need:

* Python3
* Pip3

### Installation

Clone the repository:

```shell
git clone git@github.com:Yan-ni/caty-fact-cat.git
```

Change the working directory to the project directory:

```shell
cd caty-fact-cat
```

Create a virtual environement (venv):
> 💡 This step is optionnal but recommanded.

```shell
python3 -m venv .venv
source .venv/bin/activate
```

Installing the required python libraries to run the script:

```shell
pip3 install -r requirements.txt
```

Setup the cron job for executing the script reccurently:

```shell
crontab -e
```

Add the following tasks:

```shell
0 */6 * * * cd ~/caty-fact-cat/ && ./main.py > ./poster.log 2>&1
0 15 * * * cd ~/caty-fact-cat/ && ./main.py > ./poster.log 2>&1
0 21 * * * cd ~/caty-fact-cat/ && ./main.py > ./poster.log 2>&1
```
