import random

class AIWorkshopTopicBuilder:
    def __init__(self):
        self.topics = [
            "Introduction to Machine Learning",
            "Natural Language Processing Basics",
            "Deep Learning with TensorFlow",
            "AI Ethics and Responsible AI",
            "Building AI Chatbots",
            "Computer Vision and Image Recognition",
            "Reinforcement Learning",
            "AI in Healthcare",
            "AI for Finance and Trading",
            "AI for Social Good"
        ]
        self.tasks = []

    def generate_topics(self, audience, requirements):
        print("Generating topics based on audience and requirements...")
        # Custom logic to filter and generate topics can be added here
        return random.sample(self.topics, 5)

    def create_tasks(self, selected_topics):
        print("Creating tasks for the selected topics...")
        for topic in selected_topics:
            task = {
                "topic": topic,
                "description": f"Conduct a comprehensive workshop on {topic}.",
                "objectives": [
                    f"Understand the basics of {topic}",
                    f"Implement a simple project related to {topic}",
                    f"Discuss real-world applications of {topic}"
                ]
            }
            self.tasks.append(task)
        return self.tasks

    def review_and_select(self):
        print("Reviewing generated topics and tasks...")
        for idx, task in enumerate(self.tasks):
            print(f"{idx + 1}. Topic: {task['topic']}")
            print(f"   Description: {task['description']}")
            print(f"   Objectives: {', '.join(task['objectives'])}")
            print()

    def export_output(self, filename="workshop_topics.txt"):
        print("Exporting the final list of workshop topics and tasks to a file...")
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"Topic: {task['topic']}\n")
                file.write(f"Description: {task['description']}\n")
                file.write(f"Objectives: {', '.join(task['objectives'])}\n\n")

def main():
    builder = AIWorkshopTopicBuilder()
    audience = input("Enter the target audience: ")
    requirements = input("Enter any specific requirements: ")

    topics = builder.generate_topics(audience, requirements)
    tasks = builder.create_tasks(topics)
    builder.review_and_select()
    builder.export_output()

if __name__ == "__main__":
    main()
