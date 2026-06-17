from supadata import Supadata

supadata = Supadata(
    api_key="sd_b395ac987341ccec2b930c33a513500f"
)

result = supadata.transcript(
    url="https://www.youtube.com/watch?v=zGBVpE3DSqs"
)

with open(
    "Research/youtube-transcripts/Morgan-Ingram-The-Sales-Navigator-System-That-Built-$30M-in-B2B-Pipeline.md",

    "w",
    encoding="utf-8"
) as f:

    f.write("# Aaron Ross - Introducing the New Predictable Revenue Model\n\n")

    for chunk in result.content:
        f.write(chunk.text + " ")

print("Transcript saved successfully!")