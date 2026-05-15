from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional


ROLES = ("dev", "designer", "both")
EXPERIENCE_LEVELS = ("junior", "mid", "senior")


@dataclass
class Profile:
    name: str
    bio: str = ""
    skills: str = ""
    role: str = "dev"
    experience: str = "junior"
    id: Optional[int] = None
    links: List[str] = field(default_factory=list)

    def validate(self) -> list[str]:
        errors = []
        if not self.name.strip():
            errors.append("Name is required.")
        if self.role not in ROLES:
            errors.append(f"Role must be one of: {', '.join(ROLES)}")
        if self.experience not in EXPERIENCE_LEVELS:
            errors.append(f"Experience must be one of: {', '.join(EXPERIENCE_LEVELS)}")
        for url in self.links:
            if url.strip() and not url.strip().startswith(("http://", "https://")):
                errors.append(f"Invalid URL: {url}")
        return errors
