from supadata import Supadata

supadata = Supadata(
    api_key="sd_b395ac987341ccec2b930c33a513500f"
)

result = supadata.transcript(
    url="https://www.youtube.com/watch?v=HApMaNtwUTw"
)
with open(
    "Research/youtube-transcripts/justin-michael-cold-calling-ai-in-sales-and-the-future-of-outbound.md",

    "w",
    encoding="utf-8"
) as f:

    f.write("# Justin Michael Cold Calling, AI in Sales, and the Future of Outbound\n\n")

    for chunk in result.content:
        f.write(chunk.text + " ")

print("Transcript saved successfully!")