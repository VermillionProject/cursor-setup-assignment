from supadata import Supadata

supadata = Supadata(
    api_key="sd_b395ac987341ccec2b930c33a513500f"
)

result = supadata.transcript(
    url="https://www.youtube.com/watch?v=BJKAurmQ0zA"
)

with open(
    "Research/youtube-transcripts/josh-braun-cold-calling-reluctance.md",
    "w",
    encoding="utf-8"
) as f:

    f.write("# Josh Braun - The Cure for Cold Calling Reluctance\n\n")

    for chunk in result.content:
        f.write(chunk.text + " ")

print("Transcript saved successfully!")