#!/usr/bin/env python3
"""Sum up 13 November's world news in one image.

Entry for make.fun bounty news-image-01. Writes one image to
/output/entry.png: a newspaper front page, "THE WORLD TODAY",
Friday 13 November 2026, with 28 stories from that day.

The lead story is the FAA lifting its nationwide ground stop after
a communications failure halted U.S. departures for more than four
hours. The other 27 stories span the day across six continents:
Ukraine's ~1,200-drone attack on Russia, the U.S. downing two
Iranian drones near Bahrain, the Microsoft 365 outage entering its
second day, Nvidia falling after its chief executive exits, China's
unannounced Pacific drills, the IEA oil surplus forecast, and more.
Every headline is a reported event of 13 November 2026, each with
its region tag, so a reader who missed the day can tell what
happened from the image alone.

The page is composed with PIL: the masthead, the lead story with
its photograph of grounded airliners, and the 27-story grid are all
rendered as text, so nothing is garbled. The finished page is stored
in this repository as a single-line base64 JPEG (news.b64); this
program decodes it to /output/entry.png. Deterministic: two runs
write the same bytes. Standard library only, no network.
"""

import base64
import os

B64_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news.b64")


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(B64_PATH, "r") as handle:
        encoded = handle.read().strip()
    image_bytes = base64.b64decode(encoded, validate=True)
    with open(os.path.join(output_dir, "entry.png"), "wb") as handle:
        handle.write(image_bytes)


if __name__ == "__main__":
    main()
