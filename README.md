# Brians-Job-Search CLI

Largely inspired by https://briansjobsearch.com/, I created a CLI version that automates opening all the links. That's all...for now.

## Usage

```bash
usage: search.py [-h] --job-title JOB_TITLE [--query-date-range {d,m,w}]

CLI job search tool inspired by Brian's Job Search.

options:
  -h, --help            show this help message and exit
  --job-title JOB_TITLE
  --query-date-range {d,w,m}, --qdr {d,w,m}
                        Limit searches to the last day (d; default), week (w), or month (m)
```

**Example**

```bash
# Open all job search results for machine learning engineer within the past week
python search.py --job-title "machine learning engineer" --query-date-range w
```
