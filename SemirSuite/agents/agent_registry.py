[agents]
PromptPort = {
    capabilities = ["parse_prompts"],
    status = "active",
    dependencies = []
}

IdeaForge = {
    capabilities = ["generate_ideas"],
    status = "active",
    dependencies = ["TrendSync"]
}

ClipSlicer = {
    capabilities = ["slice_video_clips"],
    status = "active",
    dependencies = []
}

AutoNarrate = {
    capabilities = ["add_voiceover", "add_subtitles"],
    status = "active",
    dependencies = ["ClipSlicer"]
}

TrendSync = {
    capabilities = ["analyze_trends"],
    status = "active",
    dependencies = []
}