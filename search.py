import urllib.parse
import webbrowser

SITES = [
    "ashbyhq.com",
    "lever.co",
    "greenhouse.io",
    "recruiting.paylocity.com",
    "jobs.workable.com",
    "breezy.hr",
    "oraclecloud.com",
    "myworkdayjobs.com",
    "recruitee.com",
    "rippling-ats.com",
    "careerpuck.com",
    "jobs.smartrecruiters.com",
    "homerun.co",
    "catsone.com",
    "applytojob.com",
    "glassdoor.com/job-listing",
]


def create_url(site: str, job_title: str, query_date_range: str) -> str:
    base_url = "https://www.google.com/search?"
    query_string = urllib.parse.urlencode(
        {
            "q": f'"{job_title}"',
            "as_sitesearch": site,
            "tbs": f"qdr:{query_date_range}",
        },
        safe=":",
    )
    return base_url + query_string


def main(job_title: str, query_date_range: str) -> None:
    for site in SITES:
        webbrowser.open_new_tab(create_url(site, job_title, query_date_range))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="CLI job search tool inspired by Brian's Job Search."
    )
    parser.add_argument("--job-title", required=True)
    parser.add_argument(
        "--query-date-range",
        "--qdr",
        choices=["d", "w", "m"],
        default="d",
        help="Limit searches to the last day (d; default), week (w), or month (m)",
    )
    args = parser.parse_args()
    main(job_title=args.job_title, query_date_range=args.query_date_range)
