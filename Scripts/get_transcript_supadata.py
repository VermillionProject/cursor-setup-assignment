from supadata import Supadata

supadata = Supadata(
    api_key="sd_b395ac987341ccec2b930c33a513500f"
)

result = supadata.transcript(
    url="https://www.youtube.com/watch?v=-yWiaoxvKQE"
)

with open(
    "Research/youtube-transcripts/josh-braun-sales-training-memoryblue.md",
    "w",
    encoding="utf-8"
) as f:

    f.write("# Sales Training With memeoryBlue\n\n")

    for chunk in result.content:
        f.write(chunk.text + " ")

print("Transcript saved successfully!")