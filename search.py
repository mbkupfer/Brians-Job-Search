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


def create_url(site: str, job_title: str, query_date_range: str, custom_query: str) -> str:
    base_url = "https://www.google.com/search?"
    query_string = urllib.parse.urlencode(
        {
            "q": f'"{job_title}" {custom_query}',
            "as_sitesearch": site,
            "tbs": f"qdr:{query_date_range}",
        },
        safe=":",
    )
    return base_url + query_string


def main(job_title: str, query_date_range: str, sites_fp=None, custom_query: str = None) -> None:
    if custom_query is None:
        custom_query = ''
    if not sites_fp:
        sites = SITES
    else:
        sites = [ln.strip() for ln in sites_fp.readlines()]
    for site in sites:
        webbrowser.open_new_tab(create_url(site, job_title, query_date_range, custom_query))


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
    parser.add_argument(
        "--sites",
        type=argparse.FileType("r"),
        help="Text file for customizing the sites that are used.",
    )
    parser.add_argument(
        "--custom-query",
        help="",
    )
    args = parser.parse_args()
    
    main(
        job_title=args.job_title,
        query_date_range=args.query_date_range,
        sites_fp=args.sites,
        custom_query=args.custom_query,
    )
