import csv
import sys
from collections import defaultdict
from typing import Dict, List


def load_matches(path: str) -> List[Dict[str, str]]:
    """Load tennis matches from a CSV file."""
    matches = []
    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            matches.append(row)
    return matches


def compute_player_stats(matches: List[Dict[str, str]]) -> Dict[str, Dict[str, int]]:
    """Compute win and match counts for each player."""
    stats: Dict[str, Dict[str, int]] = defaultdict(lambda: {"wins": 0, "matches": 0})
    for match in matches:
        p1 = match["player1"]
        p2 = match["player2"]
        winner = match["winner"]
        stats[p1]["matches"] += 1
        stats[p2]["matches"] += 1
        stats[winner]["wins"] += 1
    return stats


def summarize(stats: Dict[str, Dict[str, int]]) -> None:
    """Print a summary of player statistics."""
    print("Player Summary")
    print("--------------")
    for player, info in sorted(stats.items(), key=lambda x: (-x[1]["wins"], x[0])):
        matches = info["matches"]
        wins = info["wins"]
        win_pct = wins / matches * 100 if matches else 0.0
        print(f"{player}: {wins} wins / {matches} matches ({win_pct:.1f}% win rate)")


def main(path: str) -> None:
    matches = load_matches(path)
    stats = compute_player_stats(matches)
    summarize(stats)


if __name__ == "__main__":
    dataset_path = sys.argv[1] if len(sys.argv) > 1 else "data/sample_tennis.csv"
    main(dataset_path)
