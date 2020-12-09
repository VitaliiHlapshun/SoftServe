import json
import random


class BookNote:
    notes_file = 'notes.json'

    def __init__(self):
        self.notes_data = dict()

    def add_note(self, note, author_name, author_rate=0.0):
        if not author_rate:
            author_rate = round(random.random(), 1)
        self.notes_data[note] = {'author': author_name, 'author_rate': author_rate}
        print(f'Note {note} of {author_name} author {self.notes_file} added.')
        self.write_file_with_content(self.notes_data)

    def write_file_with_content(self, content: dict):
        with open(self.notes_file, 'w') as f:
            json.dump(content, f, sort_keys=True, indent=4)
        print(f'Notes file {self.notes_file} has been updated with content of {content}.')

    def get_notes_from_file(self):
        with open(self.notes_file) as f:
            notes = json.load(f)
        print('Current notes read from notes.json file >> ', notes)
        return notes

    def get_author_with_highest_rate(self):
        highest_rate = max(data['author_rate'] for data in self.notes_data.values())
        best_rated_authors = [data['author'] for data in self.notes_data.values() if data['author_rate'] == highest_rate]
        # best_rated_authors = []
        # for author, data in self.notes_data.items():
        #     if data['rate'] == highest_rate:
        #         best_rated_authors.append(author)
        print(f'Authors list with highest rate of {highest_rate}: {best_rated_authors}')
        return best_rated_authors

    def get_author_with_lowest_rate(self):
        lowest_rate = min(data['author_rate'] for data in self.notes_data.values())
        worst_rated_authors = [data['author'] for data in self.notes_data.values() if data['author_rate'] == lowest_rate]
        print(f'Authors list with lowest rate of {lowest_rate}: {worst_rated_authors}')
        return worst_rated_authors

    def get_authors_average_rate(self):
        average_rate = sum(data['author_rate'] for data in self.notes_data.values()) / len(self.notes_data.values())
        average_rate = round(average_rate, 1)
        print(f'Average rate of all authors: {average_rate}')
        return average_rate


if __name__ == '__main__':
    note_obj = BookNote()
    note_obj.add_note('test_1', 'John', 0.8)  # likely to be the highest value
    note_obj.add_note('test_2', 'James')
    note_obj.add_note('test_3', 'Viktor')
    note_obj.add_note('test_4', 'Ivan')
    # print notes data from notes.json file
    note_obj.get_notes_from_file()
    # print author_with_highest_rate, author_with_lowest_rate, authors_average_rate
    note_obj.get_author_with_highest_rate()
    note_obj.get_author_with_lowest_rate()
    note_obj.get_authors_average_rate()
