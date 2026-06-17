from pathlib import Path
from typing import Dict, List, Optional


from crewai.skills import Skill, discover_skills, activate_skill

def load_skills(skills_dir: Optional[str] = None) -> List:
    """
    Load and activate all CrewAI skills from the skills directory.

    Args:
        skills_dir: Path to the skills directory. Defaults to backend/app/skills

    Returns:
        List of activated Skill objects ready to be passed to CrewAI agents.
    """
    if skills_dir is None:
        # Default path relative to this file
        base_path = Path(__file__).parent
    else:
        base_path = Path(skills_dir)

    if not base_path.exists():
        raise FileNotFoundError(f"Skills directory not found: {base_path}")

    # Discover all skills
    discovered_skills = discover_skills(base_path)

    if not discovered_skills:
        print("No skills found in the skills directory.")
        return []

    # Activate (load full content of) all discovered skills
    activated_skills = [activate_skill(skill) for skill in discovered_skills]

    print(f"Loaded {len(activated_skills)} CrewAI skills:")
    for skill in activated_skills:
        print(f"  - {skill.name}: {skill.description}")

    return activated_skills


# Example usage
if __name__ == "__main__":
    skills = load_skills()
    print("\nSkills loaded successfully!")
    print(skills)