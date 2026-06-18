from supadata import Supadata

supadata = Supadata(
    api_key="sd_b395ac987341ccec2b930c33a513500f"
)

result = supadata.transcript(
    url="https://www.youtube.com/watch?v=u-4R7Lt0qqM"
)
with open(
    "Research/youtube-transcripts/armand-farrokh-running-sales-teams-meetings-that-dont-suck.md",
    "w",
    encoding="utf-8"
) as f:

    f.write("# Armand Farrokh Running Sales Teams Meetings That Don't Suck\n\n")

    for chunk in result.content:
        f.write(chunk.text + " ")

print("Transcript saved successfully!")