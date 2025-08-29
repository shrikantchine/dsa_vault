#!/usr/bin/env python3
"""
DSA Revision Manager

This script helps manage spaced repetition for DSA topics by:
1. Calculating next review dates based on confidence and difficulty
2. Generating daily review lists
3. Updating revision statistics
4. Creating random topic suggestions for quick review
"""

import os
import re
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
import random

class DSARevisionManager:
    def __init__(self, tracker_file: str):
        self.tracker_file = tracker_file
        self.topics = []
        self.confidence_intervals = {
            1: 1,   # Poor - review tomorrow
            2: 2,   # Fair - review in 2 days
            3: 4,   # Good - review in 4 days
            4: 7,   # Very Good - review in 1 week
            5: 14   # Excellent - review in 2 weeks
        }
        
    def parse_tracker_file(self) -> List[Dict]:
        """Parse the revision tracker markdown file."""
        topics = []
        if not os.path.exists(self.tracker_file):
            return topics
            
        with open(self.tracker_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all table rows with topic data
        table_pattern = r'\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]*)\s*\|'
        matches = re.findall(table_pattern, content)
        
        for match in matches:
            topic, last_reviewed, next_review, difficulty, confidence, notes = match
            
            # Skip header rows
            if 'Topic' in topic or '---' in topic:
                continue
                
            topics.append({
                'name': topic.strip(),
                'last_reviewed': last_reviewed.strip(),
                'next_review': next_review.strip(),
                'difficulty': difficulty.strip(),
                'confidence': confidence.strip(),
                'notes': notes.strip()
            })
        
        return topics
    
    def calculate_next_review_date(self, confidence: int, difficulty: str, last_reviewed: str) -> str:
        """Calculate next review date based on confidence and difficulty."""
        if confidence not in self.confidence_intervals:
            return "Today"
            
        base_interval = self.confidence_intervals[confidence]
        
        # Adjust for difficulty
        if difficulty.lower() == 'hard':
            base_interval = max(1, base_interval - 1)
        
        try:
            last_date = datetime.strptime(last_reviewed, '%Y-%m-%d')
            next_date = last_date + timedelta(days=base_interval)
            return next_date.strftime('%Y-%m-%d')
        except ValueError:
            return "Today"
    
    def get_due_topics(self) -> List[str]:
        """Get list of topics due for review today or overdue."""
        topics = self.parse_tracker_file()
        due_topics = []
        today = datetime.now().strftime('%Y-%m-%d')
        
        for topic in topics:
            next_review = topic['next_review']
            if next_review == 'Today' or next_review == '-':
                due_topics.append(topic['name'])
            else:
                try:
                    review_date = datetime.strptime(next_review, '%Y-%m-%d')
                    today_date = datetime.strptime(today, '%Y-%m-%d')
                    if review_date <= today_date:
                        due_topics.append(topic['name'])
                except ValueError:
                    due_topics.append(topic['name'])
        
        return due_topics
    
    def get_random_topic(self, category: Optional[str] = None) -> str:
        """Get a random topic for quick review."""
        all_topics = [
            "Arrays (1-D)", "Arrays (2-D)", "Strings", "Linked Lists", 
            "Stacks & Queues", "Trees", "Graphs", "Heap", "Hashing",
            "Sorting", "Searching", "Greedy Algorithms", "Dynamic Programming",
            "Recursion", "Bit Manipulation", "Combinatorics", 
            "Modular Arithmetic & GCD", "Prime Numbers",
            "Prefix Sum & Sliding Window", "Two Pointers", "Interview Questions"
        ]
        
        data_structures = ["Arrays (1-D)", "Arrays (2-D)", "Strings", "Linked Lists", 
                          "Stacks & Queues", "Trees", "Graphs", "Heap", "Hashing"]
        algorithms = ["Sorting", "Searching", "Greedy Algorithms", "Dynamic Programming",
                     "Recursion", "Bit Manipulation"]
        math_concepts = ["Combinatorics", "Modular Arithmetic & GCD", "Prime Numbers"]
        techniques = ["Prefix Sum & Sliding Window", "Two Pointers", "Interview Questions"]
        
        if category == "data_structures":
            return random.choice(data_structures)
        elif category == "algorithms":
            return random.choice(algorithms)
        elif category == "math":
            return random.choice(math_concepts)
        elif category == "techniques":
            return random.choice(techniques)
        else:
            return random.choice(all_topics)
    
    def update_topic_review(self, topic_name: str, confidence: int, notes: str = "") -> bool:
        """Update a topic's review status."""
        if not os.path.exists(self.tracker_file):
            return False
            
        with open(self.tracker_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Find the topic's row and update it
        pattern = rf'(\|\s*{re.escape(topic_name)}\s*\|\s*)([^|]+)(\s*\|\s*)([^|]+)(\s*\|\s*)([^|]+)(\s*\|\s*)([^|]+)(\s*\|\s*)([^|]*)\s*\|'
        
        def replace_row(match):
            difficulty = match.group(6).strip()
            next_review = self.calculate_next_review_date(confidence, difficulty, today)
            
            return (f"{match.group(1)}{today}{match.group(3)}{next_review}"
                   f"{match.group(5)}{difficulty}{match.group(7)}{confidence}"
                   f"{match.group(9)}{notes} |")
        
        updated_content = re.sub(pattern, replace_row, content)
        
        if updated_content != content:
            with open(self.tracker_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
        
        return False
    
    def generate_daily_report(self) -> str:
        """Generate a daily review report."""
        due_topics = self.get_due_topics()
        random_topic = self.get_random_topic()
        
        report = f"""# Daily DSA Review - {datetime.now().strftime('%Y-%m-%d')}

## 📅 Due for Review Today ({len(due_topics)} topics)

"""
        
        for topic in due_topics:
            report += f"- [ ] {topic}\n"
        
        if not due_topics:
            report += "🎉 All caught up! No topics due for review today.\n"
        
        report += f"""
## 🎲 Random Quick Review Suggestion

**Topic**: {random_topic}

Spend 5-10 minutes reviewing key concepts, then mark as reviewed if confident.

## 📝 After Review

For each topic you review:
1. Rate your confidence (1-5)
2. Add any notes about areas that need work
3. Update the revision tracker using the Python script:

```bash
python revision_manager.py update "<topic_name>" <confidence> "<notes>"
```

## 🎯 Quick Commands

```bash
# Get today's due topics
python revision_manager.py due

# Get a random topic
python revision_manager.py random

# Update after reviewing
python revision_manager.py update "Sorting" 4 "Need more practice with merge sort"
```
"""
        
        return report
    
    def get_statistics(self) -> Dict:
        """Get revision statistics."""
        topics = self.parse_tracker_file()
        total_topics = len([t for t in topics if t['name'] and t['name'] != 'Topic'])
        reviewed_topics = len([t for t in topics if t['last_reviewed'] and t['last_reviewed'] != '-'])
        
        confidences = []
        for topic in topics:
            try:
                conf = int(topic['confidence'])
                confidences.append(conf)
            except (ValueError, TypeError):
                pass
        
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0
        
        return {
            'total_topics': total_topics,
            'reviewed_topics': reviewed_topics,
            'avg_confidence': round(avg_confidence, 2),
            'completion_rate': round((reviewed_topics / total_topics * 100), 1) if total_topics > 0 else 0
        }

def main():
    import sys
    
    tracker_file = "/home/runner/work/dsa_vault/dsa_vault/DSA/Revision/revision_tracker.md"
    manager = DSARevisionManager(tracker_file)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python revision_manager.py due                           # Show due topics")
        print("  python revision_manager.py random [category]             # Get random topic")
        print("  python revision_manager.py update <topic> <conf> [notes] # Update topic")
        print("  python revision_manager.py report                        # Generate daily report")
        print("  python revision_manager.py stats                         # Show statistics")
        return
    
    command = sys.argv[1]
    
    if command == "due":
        due_topics = manager.get_due_topics()
        print(f"📅 Topics due for review today ({len(due_topics)}):")
        for topic in due_topics:
            print(f"  - {topic}")
        if not due_topics:
            print("🎉 All caught up!")
    
    elif command == "random":
        category = sys.argv[2] if len(sys.argv) > 2 else None
        topic = manager.get_random_topic(category)
        print(f"🎲 Random topic: {topic}")
    
    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python revision_manager.py update <topic> <confidence> [notes]")
            return
        
        topic = sys.argv[2]
        try:
            confidence = int(sys.argv[3])
            if confidence < 1 or confidence > 5:
                print("Confidence must be between 1 and 5")
                return
        except ValueError:
            print("Confidence must be a number between 1 and 5")
            return
        
        notes = sys.argv[4] if len(sys.argv) > 4 else ""
        
        if manager.update_topic_review(topic, confidence, notes):
            print(f"✅ Updated {topic} with confidence {confidence}")
        else:
            print(f"❌ Failed to update {topic}")
    
    elif command == "report":
        report = manager.generate_daily_report()
        print(report)
    
    elif command == "stats":
        stats = manager.get_statistics()
        print(f"📊 Revision Statistics:")
        print(f"  Total Topics: {stats['total_topics']}")
        print(f"  Reviewed: {stats['reviewed_topics']}")
        print(f"  Completion: {stats['completion_rate']}%")
        print(f"  Avg Confidence: {stats['avg_confidence']}")
    
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()