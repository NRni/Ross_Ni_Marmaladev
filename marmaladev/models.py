from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional


DESIGNER_JOBS = [
    "System Designer",
    "Level Designer",
    "Narrative Designer / Writer",
    "Content Designer",
    "Combat Designer",
    "Economy Designer",
    "Quest/Mission Designer",
    "UX/UI Designer",
    "Technical Designer",
]

DEVELOPER_JOBS = [
    "Gameplay Programmer",
    "Graphics/Engine Programmer",
    "AI Programmer",
    "Network/Multiplayer Programmer",
    "Tools Programmer",
    "UI Programmer",
    "Physics Programmer",
    "Audio Programmer",
    "Build/DevOps Engineer",
]

ARTIST_JOBS = [
    "Concept Artist",
    "3D Modeller / Environment Artist",
    "3D Modeller / Character Artist",
    "Texture / Material Artist",
    "Animator",
    "Rigger",
    "UI Artist / Graphic Designer",
    "VFX Artist",
    "Lighting Artist",
    "Technical Artist",
    "Cinematic / Motion Graphics Artist",
    "Illustrator / Marketing Artist",
]

ALL_JOBS = {
    "Game Designer": DESIGNER_JOBS,
    "Game Developer": DEVELOPER_JOBS,
    "Game Artist": ARTIST_JOBS,
}

FLAT_JOBS = [j for group in ALL_JOBS.values() for j in group]


@dataclass
class Profile:
    name: str
    bio: str = ""
    skills: str = ""
    jobs: List[str] = field(default_factory=list)
    years: int = 0
    id: Optional[int] = None
    links: List[str] = field(default_factory=list)

    def validate(self) -> List[str]:
        errors = []
        if not self.name.strip():
            errors.append("Name is required.")
        if not self.jobs:
            errors.append("Select at least one job.")
        for url in self.links:
            if url.strip() and not url.strip().startswith(("http://", "https://")):
                errors.append(f"Invalid URL: {url}")
        return errors
