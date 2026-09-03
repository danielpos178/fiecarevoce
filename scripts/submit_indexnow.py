#!/usr/bin/env python3
"""
IndexNow URL Submission Script for fiecarevoce.com

Submits URLs from the Hugo sitemap to IndexNow (Bing, Yandex, etc.).
IndexNow protocol documentation: https://www.indexnow.org/documentation
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

KEY = "4024a005e217c254e12a00ff47a26fd3"
HOST = "fiecarevoce.com"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SITEMAP_LOCAL = REPO_ROOT / "public" / "sitemap.xml"
DEFAULT_SITEMAP_REMOTE = f"https://{HOST}/sitemap.xml"

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://yandex.com/indexnow",
]

BATCH_SIZE = 10000


def check_key_online(host: str = HOST, key: str = KEY, key_location: str = KEY_LOCATION) -> bool:
    """Verifies that the IndexNow verification key is live and accessible."""
    print(f"Checking online key at {key_location}...")
    req = urllib.request.Request(
        key_location,
        headers={"User-Agent": "IndexNow-Checker/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode("utf-8").strip()
            if content == key:
                print(f"[OK] Verification key is live and valid on {host}.")
                return True
            else:
                print(f"[WARNING] Key file exists at {key_location} but content did not match expected key.")
                print(f"  Expected: {key}")
                print(f"  Received: {content[:100]}...")
                return False
    except urllib.error.HTTPError as e:
        print(f"[WARNING] Online key check failed: HTTP {e.code} ({e.reason}) at {key_location}")
        print("  IndexNow requires this file to verify domain ownership.")
        print(f"  Ensure 'static/{key}.txt' is committed and deployed to production.")
        return False
    except Exception as e:
        print(f"[WARNING] Could not check online key: {e}")
        return False


def extract_urls_from_xml(xml_content: str, host: str) -> list[str]:
    """Parses sitemap XML content and extracts page loc URLs."""
    urls = []
    try:
        root = ET.fromstring(xml_content)
        # Handle namespaces in sitemap XML (e.g. {http://www.sitemaps.org/schemas/sitemap/0.9}url)
        for elem in root.iter():
            if elem.tag.endswith("loc"):
                # Avoid <image:loc> inside <image:image>
                if "image" in elem.tag.lower():
                    continue
                url = (elem.text or "").strip()
                if url:
                    urls.append(url)
    except ET.ParseError:
        # Fallback to regex if XML parsing fails
        matches = re.findall(r"<loc>(.*?)</loc>", xml_content)
        for m in matches:
            url = m.strip()
            if url:
                urls.append(url)

    # Filter to ensure URLs belong to the host and remove duplicates
    host_prefix = f"https://{host}"
    seen = set()
    filtered_urls = []
    for u in urls:
        if u.startswith(host_prefix) and u not in seen:
            seen.add(u)
            filtered_urls.append(u)

    return filtered_urls


def get_urls_from_sitemap(sitemap_source: str | Path | None = None) -> list[str]:
    """Loads URLs from local sitemap file or remote fallback."""
    if sitemap_source:
        source_str = str(sitemap_source)
        if source_str.startswith("http://") or source_str.startswith("https://"):
            print(f"Fetching sitemap from remote URL: {source_str}")
            req = urllib.request.Request(source_str, headers={"User-Agent": "IndexNow-Submitter/1.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read().decode("utf-8")
            return extract_urls_from_xml(content, HOST)
        else:
            path = Path(source_str)
            if not path.is_absolute():
                path = (REPO_ROOT / path).resolve()
            if not path.exists():
                print(f"Error: Sitemap file not found at {path}")
                return []
            with open(path, "r", encoding="utf-8") as f:
                return extract_urls_from_xml(f.read(), HOST)

    # Default: check local public/sitemap.xml first
    if DEFAULT_SITEMAP_LOCAL.exists():
        print(f"Reading local sitemap: {DEFAULT_SITEMAP_LOCAL}")
        with open(DEFAULT_SITEMAP_LOCAL, "r", encoding="utf-8") as f:
            return extract_urls_from_xml(f.read(), HOST)

    # Fallback: fetch remote sitemap
    print(f"Local {DEFAULT_SITEMAP_LOCAL} not found. Attempting live sitemap: {DEFAULT_SITEMAP_REMOTE}")
    try:
        req = urllib.request.Request(DEFAULT_SITEMAP_REMOTE, headers={"User-Agent": "IndexNow-Submitter/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode("utf-8")
        print(f"Successfully fetched live sitemap from {DEFAULT_SITEMAP_REMOTE}")
        return extract_urls_from_xml(content, HOST)
    except Exception as e:
        print(f"Error: Could not retrieve live sitemap: {e}")
        print("Run 'hugo' to generate public/sitemap.xml locally, or check your internet connection.")
        return []


def submit_batch_to_endpoint(endpoint: str, urls: list[str], host: str = HOST, key: str = KEY, key_location: str = KEY_LOCATION) -> bool:
    """Submits a single batch of URLs to an IndexNow endpoint."""
    payload = {
        "host": host,
        "key": key,
        "keyLocation": key_location,
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
            if status == 200:
                print(f"  [{status} OK] Submitted {len(urls)} URLs to {endpoint}")
            elif status == 202:
                print(f"  [{status} Accepted] URLs received by {endpoint} (key validation in progress)")
            else:
                print(f"  [{status}] Submitted {len(urls)} URLs to {endpoint}")
            return True
    except urllib.error.HTTPError as e:
        error_body = ""
        try:
            error_body = e.read().decode("utf-8", errors="replace")
        except Exception:
            pass

        print(f"  [HTTP {e.code} {e.reason}] Failed submitting to {endpoint}")
        if error_body:
            try:
                err_json = json.loads(error_body)
                msg = err_json.get("message") or err_json.get("errorCode") or error_body
                print(f"    Reason: {msg}")
            except Exception:
                print(f"    Response: {error_body}")

        if e.code == 403:
            print("    -> 403 indicates domain ownership validation failed.")
            print(f"       Verify that {key_location} returns HTTP 200 with the key '{key}'.")
        return False
    except Exception as e:
        print(f"  Failed submitting to {endpoint}: {e}")
        return False


def submit_indexnow(urls: list[str], all_endpoints: bool = False, dry_run: bool = False):
    """Submits URLs in batches to IndexNow."""
    if not urls:
        print("No URLs found to submit.")
        return

    print(f"Preparing to submit {len(urls)} URL(s) to IndexNow...")

    if dry_run:
        print("\n[DRY RUN] Would submit the following URLs:")
        for u in urls[:10]:
            print(f"  - {u}")
        if len(urls) > 10:
            print(f"  ... and {len(urls) - 10} more.")
        return

    # Check key status first to provide actionable diagnostics
    key_ok = check_key_online()
    if not key_ok:
        print("\nNotice: Key verification failed online. Submission may be rejected with HTTP 403.\n")

    endpoints_to_use = ENDPOINTS if all_endpoints else [ENDPOINTS[0]]

    # Chunk URLs into batches of max 10,000
    for i in range(0, len(urls), BATCH_SIZE):
        batch = urls[i:i + BATCH_SIZE]
        batch_num = (i // BATCH_SIZE) + 1
        total_batches = (len(urls) + BATCH_SIZE - 1) // BATCH_SIZE

        if total_batches > 1:
            print(f"\nProcessing Batch {batch_num}/{total_batches} ({len(batch)} URLs)...")

        for ep in endpoints_to_use:
            success = submit_batch_to_endpoint(ep, batch)
            # If default mode (not all_endpoints) and primary endpoint failed due to network error, try fallback
            if not all_endpoints and not success and not key_ok:
                # Key error is permanent across all endpoints, but still try fallback if user wants
                pass


def parse_args():
    parser = argparse.ArgumentParser(description="Submit sitemap URLs to IndexNow (Bing, Yandex, etc.)")
    parser.add_argument(
        "--sitemap",
        help="Path to local sitemap.xml or remote sitemap URL (defaults to public/sitemap.xml or live sitemap)",
    )
    parser.add_argument(
        "--url",
        action="append",
        dest="custom_urls",
        help="Submit a specific URL (can be used multiple times). If omitted, sitemap URLs are used.",
    )
    parser.add_argument(
        "--all-endpoints",
        action="store_true",
        help="Submit to all participating search engine endpoints individually (api.indexnow.org, bing.com, yandex.com)",
    )
    parser.add_argument(
        "--check-key",
        action="store_true",
        help="Only check if the verification key is live online and exit",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Extract URLs and display payload without submitting",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.check_key:
        is_live = check_key_online()
        sys.exit(0 if is_live else 1)

    if args.custom_urls:
        urls = args.custom_urls
        print(f"Using {len(urls)} custom URL(s) provided via arguments.")
    else:
        urls = get_urls_from_sitemap(args.sitemap)
        print(f"Found {len(urls)} valid URLs.")

    submit_indexnow(urls, all_endpoints=args.all_endpoints, dry_run=args.dry_run)
